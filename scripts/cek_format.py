#!/usr/bin/env python3
"""Periksa format .docx proposal, buku TA, atau jurnal TA FIF terhadap spesifikasi templat.

Pemakaian:
    python3 -I scripts/cek_format.py BERKAS.docx --jenis proposal|buku|jurnal

Hanya membaca berkas. Laporan berisi temuan per kelompok; kode keluar 1 bila ada temuan.
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
CAPTION = re.compile(r"^(Tabel|Gambar)\s+\d+(\.\d+)*\.?\s")


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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--jenis", required=True, choices=SPEC)
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
            if not cap.startswith("Tabel"):
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
        if spacing != spec["line"]:
            add("spasi", f"spasi {spacing}, templat {spec['line']}: {txt[:60]!r}")

    print(f"Berkas: {args.docx}\nJenis : {args.jenis} (spesifikasi references/format-dokumen.md)\n")
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
