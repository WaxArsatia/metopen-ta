#!/usr/bin/env python3
"""Peta isi word/document.xml: satu baris per elemen badan, supaya indeks elemen bisa dipakai untuk menyunting.

Pemakaian:
    python3 -I scripts/docx_peta.py BERKAS.docx [--xml N [N ...]] [--cari TEKS]

Tanpa opsi: tiap elemen badan dicetak sebagai `indeks jenis gaya [penanda] teks`. Penanda: keepNext, keepLines,
pageBreakBefore, sectPr, numPr, drawing. `--xml N`: XML mentah elemen ke-N (tanpa deklarasi namespace).
`--cari TEKS`: hanya elemen yang teksnya memuat TEKS. Hanya membaca berkas.
"""
import argparse
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ET.register_namespace("w", W[1:-1])
FLAGS = ("keepNext", "keepLines", "pageBreakBefore", "sectPr", "numPr")


def teks(el):
    return "".join(x.text or "" for x in el.iter() if x.tag in (W + "t", W + "instrText"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("--xml", type=int, nargs="+", metavar="N")
    ap.add_argument("--cari")
    a = ap.parse_args()
    with zipfile.ZipFile(a.docx) as z:
        body = ET.fromstring(z.read("word/document.xml")).find(W + "body")
    kids = list(body)
    if a.xml:
        for n in a.xml:
            s = ET.tostring(kids[n], encoding="unicode")
            print(f"== {n}\n{re.sub(r' xmlns:\w+=\"[^\"]+\"', '', s)}")
        return 0
    for i, el in enumerate(kids):
        jenis = el.tag.replace(W, "")
        t = teks(el)
        if a.cari and a.cari not in t:
            continue
        gaya, tanda = "", []
        pp = el.find(W + "pPr") if jenis == "p" else None
        if pp is not None:
            s = pp.find(W + "pStyle")
            gaya = s.get(W + "val") if s is not None else ""
            tanda = [f for f in FLAGS if pp.find(W + f) is not None]
        if any(x.tag == W + "drawing" for x in el.iter()):
            tanda.append("drawing")
        print(f"{i:4} {jenis:5} {gaya:14} {','.join(tanda):22} {t[:90]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
