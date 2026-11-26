#!/usr/bin/env python3
"""Periksa format .docx proposal, buku TA, atau jurnal TA FIF terhadap spesifikasi templat.

Pemakaian:
    python3 -I scripts/cek_format.py BERKAS.docx --jenis proposal|buku|jurnal [--preset denis]

Hanya membaca berkas. Laporan berisi temuan per kelompok; kode keluar 1 bila ada temuan.
Kelompok "isi: ..." memeriksa aturan isi yang bisa dihitung. Tanpa preset (templat dan slide): sitasi dan
Daftar Pustaka, panjang abstrak, paling banyak enam kata kunci, rujukan tabel dan gambar.
Dengan --preset denis (references/aturan-denis.md): ditambah tanda pisah, rumusan diawali Bagaimana dan berkalimat tanya,
rumusan-tujuan satu lawan satu, kata kerja Bloom, 3 sampai 6 Batasan, paragraf kosong antarsubbab, dan
tepat lima kata kunci tanpa singkatan.
Spesifikasi berasal dari references/format-dokumen.md. Skrip memeriksa hal yang terbaca dari XML;
pemenggalan halaman, baris yatim, dan tampilan gambar tetap diperiksa dari render PDF.
"""
import argparse
import re
import sys
import zipfile
from collections import Counter
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
CM = 567.0  # twip per cm (dibulatkan)

SPEC = {
    "proposal": dict(margin=(3, 3, 4, 3), fonts={"Times New Roman"}, body=12, line=1.5,
                     h1=16, h2=14, h3=12, caption=None),
    "buku": dict(margin=(3, 3, 4, 3), fonts={"Times New Roman", "Calibri", "Aptos"}, body=12, line=1.5,
                 h1=14, h2=12, h3=12, caption=9),
    "jurnal": dict(margin=(2.5, 2.5, 2.5, 2.5), fonts={"Times New Roman"}, body=10, line=1.0,
                   h1=10, h2=10, h3=10, caption=10),
}
PLACEHOLDER = re.compile(r"<[^<>]{2,40}>|113x+|x{5,}|…{3,}|\.{6,}|Nama Prodi|nama_prodi|Lorem ipsum", re.I)
PRONOUN = re.compile(r"\b(saya|kami|kita)\b", re.I)
CAPTION = re.compile(r"^(Tabel|Gambar|Algoritma)\s+\d+(\.\d+)*\.?\s")
CAPNUM = re.compile(r"^((?:Tabel|Gambar|Algoritma)\s+\d+(?:\.\d+)*)[.:]\s")  # caption sungguhan: nomor diikuti titik
EQNUM = re.compile(r"^\(\d+(\.\d+)?\)$")
# --preset denis: kata kerja Bloom revisi pada Tujuan (C4 sampai C5); ubah di sini bila keputusan berubah.
BLOOM = {"menganalisis", "membedakan", "mengevaluasi", "memeriksa"}
DASH = re.compile("[–—]")
CITE = re.compile(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]")


def wa(el, name):
    return None if el is None else el.get(W + name)


class Styles:
    def __init__(self, z):
        self.st = ET.fromstring(z.read("word/styles.xml"))
        self.by_id = {wa(s, "styleId"): s for s in self.st.iter(W + "style")}
        self.default_p = next((wa(s, "styleId") for s in self.st.iter(W + "style")
                               if wa(s, "type") == "paragraph" and wa(s, "default") == "1"), None)
        self.theme = {}
        try:
            th = z.read("word/theme/theme1.xml").decode("utf8")
            for kind in ("major", "minor"):
                m = re.search(r"<a:%sFont><a:latin typeface=\"([^\"]*)\"" % kind, th)
                if m:
                    self.theme[kind] = m.group(1)
        except KeyError:
            pass
        dd = self.st.find(W + "docDefaults")
        self.dd_r = dd.find(f"{W}rPrDefault/{W}rPr") if dd is not None else None
        self.dd_p = dd.find(f"{W}pPrDefault/{W}pPr") if dd is not None else None

    def chain(self, sid):
        out, seen = [], set()
        while sid and sid not in seen and sid in self.by_id:
            seen.add(sid)
            s = self.by_id[sid]
            out.append(s)
            sid = wa(s.find(W + "basedOn"), "val")
        return out

    def name(self, sid):
        s = self.by_id.get(sid)
        return wa(s.find(W + "name"), "val") if s is not None else sid

    def font_of(self, rfonts):
        if rfonts is None:
            return None
        if wa(rfonts, "ascii"):
            return wa(rfonts, "ascii")
        t = wa(rfonts, "asciiTheme")
        if t:
            return self.theme.get("major" if t.startswith("major") else "minor", t)
        return None


def first(*vals):
    return next((v for v in vals if v is not None), None)


def para_props(p, sty):
    """Format efektif paragraf: gaya, spasi baris, nomor outline, keepNext, perataan, bernomor."""
    pp = p.find(W + "pPr")
    sid = wa(pp.find(W + "pStyle"), "val") if pp is not None else None
    sid = sid or sty.default_p
    layers = ([pp] if pp is not None else []) + [s.find(W + "pPr") for s in sty.chain(sid)] + [sty.dd_p]
    layers = [x for x in layers if x is not None]
    line = rule = outline = jc = None
    keep = numbered = False
    for lay in layers:
        if jc is None and lay.find(W + "jc") is not None:
            jc = wa(lay.find(W + "jc"), "val")
        if lay.find(W + "numPr") is not None:
            numbered = True
        sp = lay.find(W + "spacing")
        if line is None and sp is not None and wa(sp, "line"):
            line, rule = int(wa(sp, "line")), wa(sp, "lineRule") or "auto"
        ol = lay.find(W + "outlineLvl")
        if outline is None and ol is not None:
            outline = int(wa(ol, "val"))
        if lay.find(W + "keepNext") is not None:
            keep = True
    spacing = None if line is None else (round(line / 240, 2) if rule == "auto" else f"{line / 20:g}pt {rule}")
    return sid, spacing if spacing is not None else 1.0, outline, keep, jc, numbered


def run_props(r, p_sid, sty):
    rp = r.find(W + "rPr")
    layers = ([rp] if rp is not None else []) + [s.find(W + "rPr") for s in sty.chain(p_sid)] + [sty.dd_r]
    layers = [x for x in layers if x is not None]
    font = size = color = None
    bold = None
    for lay in layers:
        font = first(font, sty.font_of(lay.find(W + "rFonts")))
        sz = lay.find(W + "sz")
        size = first(size, int(wa(sz, "val")) / 2 if sz is not None else None)
        c = lay.find(W + "color")
        color = first(color, wa(c, "val") if c is not None else None)
        b = lay.find(W + "b")
        if bold is None and b is not None:
            bold = wa(b, "val") not in ("0", "false")
    return font or "?", size or 10.0, color or "auto", bool(bold)


def text_of(el):
    return "".join(t.text or "" for t in el.iter(W + "t")).strip()


def norm(txt):
    return re.sub(r"^[\d.\s]+", "", txt).strip().lower()


def cite_numbers(txt):
    out = []
    for m in CITE.finditer(txt):
        for part in re.split(r"\s*,\s*", m.group(1)):
            rng = re.split(r"\s*[–-]\s*", part)
            out += list(range(int(rng[0]), int(rng[-1]) + 1)) if len(rng) == 2 else [int(rng[0])]
    return out


def cek_isi(body, sty, add, preset):
    """Aturan isi yang bisa dihitung. Hanya berjalan pada bagian yang ditemukan di dokumen."""
    tables = {p for t in body.iter(W + "tbl") for p in t.iter(W + "p")}
    rows = []  # (teks, judul?, butir bernomor?, di tabel?)
    for p in body.iter(W + "p"):
        txt = text_of(p)
        if not txt:
            continue
        sid, _, outline, _, _, numbered = para_props(p, sty)
        sname = (sty.name(sid) or "").lower()
        if sname.startswith("toc") or sname == "table of figures":
            continue
        head = (outline is not None and outline <= 2) or sname.startswith("heading")
        rows.append((txt, head, numbered and not head, p in tables))

    denis = preset == "denis"
    for txt, _, _, intbl in rows if denis else []:
        if DASH.search(txt) and not intbl and not re.match(r"^\[\d+\]", txt):  # entri pustaka: rentang halaman sah
            add("isi: tanda pisah", f"em/en dash: {txt[:70]!r}")

    start = next((i for i, r in enumerate(rows) if r[1] and norm(r[0]) == "daftar pustaka"), None)
    if start is not None:
        entries = {}
        for r in rows[start + 1:]:
            m = re.match(r"^\[(\d+)\]", r[0])
            if m:
                entries[int(m.group(1))] = r[0]
        order, cited = [], set()
        for r in rows[:start]:
            for n in cite_numbers(r[0]):
                cited.add(n)
                if n not in order:
                    order.append(n)
        for n in sorted(cited - set(entries)):
            add("isi: sitasi", f"[{n}] dikutip di teks tetapi tidak ada entri Daftar Pustaka")
        for n in sorted(set(entries) - cited):
            add("isi: sitasi", f"entri [{n}] tidak dirujuk di teks")
        if order != list(range(1, len(order) + 1)):
            add("isi: sitasi", f"urutan kemunculan pertama bukan 1,2,3,...: {order[:20]}")

    def block(name, stop):
        i = next((k for k, r in enumerate(rows) if r[1] and norm(r[0]).startswith(name)), None)
        if i is None:
            return None
        out = []
        for r in rows[i + 1:]:
            if r[1] and norm(r[0]).startswith(stop):
                break
            if r[2]:
                out.append(r[0])
        return out

    rum, tuj, bat = None, None, None
    if denis:
        rum, tuj = block("perumusan masalah", "tujuan"), block("tujuan", "batasan")
        bat = block("batasan masalah", "rencana kegiatan")
    if rum is not None and tuj is not None and len(rum) != len(tuj):
        add("isi: rumusan-tujuan", f"{len(rum)} rumusan dan {len(tuj)} tujuan (harus satu lawan satu)")
    for k, t in enumerate(tuj or [], 1):
        w = re.split(r"\W+", t.strip().lower())[0]
        if w not in BLOOM:
            add("isi: Bloom", f"Tujuan {k} diawali {w!r}, bukan salah satu dari {sorted(BLOOM)}")
    if bat is not None and not 3 <= len(bat) <= 6:
        add("isi: batasan", f"{len(bat)} butir Batasan Masalah (aturan 3 sampai 6)")
    for k, t in enumerate(rum or [], 1):
        if not t.rstrip().endswith("?") or not t.lstrip().lower().startswith("bagaimana"):
            add("isi: rumusan", f"Rumusan {k} tidak diawali 'Bagaimana' dan diakhiri '?': {t[:60]!r}")

    if denis:  # jarak antarsubbab templat: paragraf kosong sesudah judul bab bernomor dan sebelum tiap Heading 2
        kids = list(body)

        def kosong(el):
            return (el.tag == W + "p" and not text_of(el)
                    and not any(x.tag in (W + "drawing", W + "sectPr", W + "pict") for x in el.iter())
                    and not any(b.get(W + "type") == "page" for b in el.iter(W + "br")))

        for i, el in enumerate(kids):
            if el.tag != W + "p" or not text_of(el):
                continue
            sid, _, outline, _, _, numbered = para_props(el, sty)
            sname = (sty.name(sid) or "").lower()
            if sname == "heading 2" or (outline == 1 and sname.startswith("heading")):
                if i == 0 or not kosong(kids[i - 1]):
                    add("isi: jarak subbab", f"tidak ada paragraf kosong sebelum subbab {text_of(el)[:40]!r}")
            elif numbered and (sname == "heading 1" or outline == 0):
                if i + 1 >= len(kids) or not kosong(kids[i + 1]):
                    add("isi: jarak subbab", f"tidak ada paragraf kosong sesudah judul bab {text_of(el)[:40]!r}")

    i = next((k for k, r in enumerate(rows) if norm(r[0]) == "abstrak"), None)
    if i is not None:
        words, kw = 0, None
        for txt, head, _, _ in rows[i + 1:]:
            if re.match(r"^kata kunci", txt, re.I):
                kw = re.sub(r"^kata kunci\s*[:.]?\s*", "", txt, flags=re.I)
                break
            if head:
                break
            words += len(txt.split())
        msg = f"Abstrak: {words} kata"
        if words > 200:
            add("isi: abstrak", f"{words} kata (maksimal 200)")
        if kw is not None:
            ks = [k.strip() for k in re.split(r"[,;]", kw) if k.strip()]
            msg += f", {len(ks)} kata kunci"
            if denis and len(ks) != 5:
                add("isi: kata kunci", f"{len(ks)} kata kunci (preset: tepat 5): {ks}")
            if not denis and len(ks) > 6:
                add("isi: kata kunci", f"{len(ks)} kata kunci (maksimal 6): {ks}")
            for k in ks if denis else []:
                if re.search(r"\b[A-Z]{2,}\b", k):
                    add("isi: kata kunci", f"{k!r}: singkatan (preset: pakai kepanjangan)")
        print(msg)

    for r in rows:
        m = CAPNUM.match(r[0])
        if not m:
            continue
        label = m.group(1)
        pat = re.compile(re.escape(label) + r"(?!\.?\d)")
        if not any(pat.search(o[0]) for o in rows if not CAPNUM.match(o[0])):
            add("isi: rujukan", f"{label} tidak dirujuk di teks")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--jenis", required=True, choices=SPEC)
    ap.add_argument("--preset", choices=["denis"], help="tambahkan pemeriksaan preset aturan Denis")
    ap.add_argument("--maks", type=int, default=8, help="contoh temuan per kelompok (bawaan 8)")
    args = ap.parse_args()
    spec = SPEC[args.jenis]
    z = zipfile.ZipFile(args.docx)
    sty = Styles(z)
    body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    findings = {}

    def add(group, msg):
        findings.setdefault(group, []).append(msg)

    # 1. Halaman
    for i, s in enumerate(body.iter(W + "sectPr"), 1):
        pg, m = s.find(W + "pgSz"), s.find(W + "pgMar")
        w, h = int(wa(pg, "w") or 0), int(wa(pg, "h") or 0)
        if wa(pg, "orient") == "landscape" or w > h:
            w, h = h, w
        if abs(w - 11906) > 40 or abs(h - 16838) > 40:
            add("halaman", f"bagian {i}: kertas {w}x{h} twip, bukan A4 (11906x16838)")
        got = tuple(round(int(wa(m, k) or 0) / CM, 2) for k in ("top", "bottom", "left", "right"))
        if any(abs(g - e) > 0.05 for g, e in zip(got, spec["margin"])):
            add("halaman", f"bagian {i}: margin atas/bawah/kiri/kanan {got} cm, templat {spec['margin']} cm")

    # 2. Paragraf
    body_combo, ref_spacing, tables = Counter(), Counter(), set()
    for tbl in body.iter(W + "tbl"):
        for p in tbl.iter(W + "p"):
            tables.add(p)
    children = list(body)
    prev_text = ""
    in_isi = False  # halaman sampul dan pengesahan tidak diperiksa sebagai isi
    heading_fonts = spec["fonts"] | ({sty.theme.get("major")} if args.jenis == "buku" else set())
    for idx, el in enumerate(children):
        if el.tag == W + "tbl" and not in_isi:
            continue
        if el.tag == W + "tbl":
            cap = prev_text
            if not cap.startswith(("Tabel", "Algoritma")):
                add("caption", f"tabel ke-{idx}: paragraf tepat di atasnya bukan caption 'Tabel ...' ({cap[:50]!r})")
            continue
        if el.tag != W + "p":
            continue
        txt = text_of(el)
        sid, spacing, outline, keep, jc, numbered = para_props(el, sty)
        sname = (sty.name(sid) or "").lower()
        if not in_isi:
            starts = (outline == 0 or sname == "heading 1") and (numbered or txt.upper() in ("ABSTRAK", "ABSTRACT"))
            if starts or (args.jenis == "jurnal" and txt == "Abstrak"):
                in_isi = True
            elif txt and PLACEHOLDER.search(txt):
                add("sisa templat", f"{txt[:80]!r}")
            if not in_isi:
                continue
        if sname.startswith("toc") or sname == "table of figures":
            continue
        runs = [r for r in el.iter(W + "r") if text_of(r)]
        props = [run_props(r, sid, sty) for r in runs]
        has_draw = el.find(f".//{W}drawing") is not None or el.find(".//{urn:schemas-microsoft-com:vml}shape") is not None
        if has_draw:
            nxt = next((text_of(c) for c in children[idx + 1:idx + 3] if c.tag == W + "p" and text_of(c)), "")
            if not nxt.startswith("Gambar"):
                add("caption", f"gambar di paragraf {idx}: tidak diikuti caption 'Gambar ...' ({nxt[:50]!r})")
        if not txt:
            continue
        prev_text = txt
        if PLACEHOLDER.search(txt):
            add("sisa templat", f"{txt[:80]!r}")
        if PRONOUN.search(txt) and not re.search(r"orisinalitas|pernyataan|menyatakan", txt, re.I):
            add("kata ganti orang pertama", f"{txt[:80]!r}")
        fonts = {f for f, *_ in props}
        sizes = {s for _, s, *_ in props}
        colors = {c for *_, c, _ in props}
        is_h1 = outline == 0 or sname == "heading 1"
        is_h2 = outline == 1 or sname == "heading 2"
        is_h3 = outline == 2 or sname == "heading 3"
        if is_h1 or is_h2 or is_h3:
            want = spec["h1"] if is_h1 else spec["h2"] if is_h2 else spec["h3"]
            lvl = 1 if is_h1 else 2 if is_h2 else 3
            if sizes - {want}:
                add("heading", f"H{lvl} {txt[:50]!r}: ukuran {sorted(sizes)} pt, templat {want} pt")
            if fonts - heading_fonts:
                add("heading", f"H{lvl} {txt[:50]!r}: huruf {sorted(fonts)}")
            if colors - {"auto", "000000"}:
                add("heading", f"H{lvl} {txt[:50]!r}: warna {sorted(colors)}, templat hitam/auto")
            if not all(b for *_, b in props):
                add("heading", f"H{lvl} {txt[:50]!r}: tidak seluruhnya tebal")
            continue
        if CAPTION.match(txt) or sname == "caption":
            if spec["caption"] and sizes - {spec["caption"]}:
                add("caption", f"{txt[:60]!r}: ukuran {sorted(sizes)} pt, templat {spec['caption']} pt")
            if txt.startswith("Tabel") and not keep:
                add("caption", f"{txt[:60]!r}: caption tabel tanpa keepNext (bisa terpisah dari tabelnya)")
            continue
        if el in tables or jc == "center":
            continue
        if re.match(r"^\[\d+\]", txt) or sname == "references":
            ref_spacing[spacing] += 1  # daftar pustaka: lihat pertentangan No. 4
            continue
        body_combo[(tuple(sorted(fonts)), tuple(sorted(sizes)), spacing)] += 1
        if fonts - spec["fonts"] or sizes - {spec["body"], 11.0 if args.jenis == "buku" else spec["body"]}:
            add("isi", f"huruf {sorted(fonts)} {sorted(sizes)} pt: {txt[:60]!r}")
        if spacing != spec["line"] and not EQNUM.match(txt):
            add("spasi", f"spasi {spacing}, templat {spec['line']}: {txt[:60]!r}")

    print(f"Berkas: {args.docx}\nJenis : {args.jenis} (spesifikasi references/format-dokumen.md)\nPreset: {args.preset or 'tidak dipakai'}\n")
    cek_isi(body, sty, add, args.preset)
    print("Kombinasi isi (huruf, ukuran pt, spasi) -> jumlah paragraf:")
    for k, n in body_combo.most_common(6):
        print(f"  {k}: {n}")
    if ref_spacing:
        print("Spasi entri daftar pustaka -> jumlah:", dict(ref_spacing))
        if len(ref_spacing) > 1:
            add("daftar pustaka", f"spasi entri tidak seragam: {dict(ref_spacing)}")
    if not findings:
        print("\nTidak ada temuan dari XML. Lanjutkan cek render PDF (pemenggalan, nomor halaman, gambar).")
        return 0
    for g, items in findings.items():
        print(f"\n[{g}] {len(items)} temuan")
        for it in items[:args.maks]:
            print("  -", it)
        if len(items) > args.maks:
            print(f"  ... {len(items) - args.maks} lagi (pakai --maks)")
    print("\nCatatan: abstrak buku TA 11 pt, isi tabel, sampul, dan halaman pengesahan sah berbeda dari isi; "
          "nilai temuan dengan konteksnya.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
