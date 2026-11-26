#!/usr/bin/env bash
# Bangun PDF dari .docx lalu periksa: huruf pengganti, cek_format.py, baris awal dan akhir tiap halaman,
# dan lembar kontak halaman (6 halaman per gambar) untuk dilihat sekali, bukan halaman demi halaman.
#
# Pemakaian: scripts/bangun_pdf.sh BERKAS.docx [proposal|buku|jurnal] [FOLDER_KERJA]
#   PDF ditulis di folder yang sama dengan BERKAS.docx (nama sama, ekstensi .pdf).
#   FOLDER_KERJA menampung lembar kontak (bawaan: folder sementara baru).
# Kode keluar 0 bila PDF terbangun; temuan cek_format.py dan huruf pengganti hanya dilaporkan.
set -euo pipefail

[[ $# -ge 1 ]] || { sed -n '2,8p' "$0"; exit 2; }
docx=$(realpath "$1")
jenis=${2:-proposal}
work=${3:-$(mktemp -d)}
here=$(cd "$(dirname "$0")" && pwd)
dir=$(dirname "$docx")
pdf="$dir/$(basename "${docx%.docx}").pdf"
mkdir -p "$work"
shopt -s nullglob

soffice -env:UserInstallation="file://$work/lo-profil" --headless --convert-to pdf --outdir "$dir" "$docx" >/dev/null 2>&1
[[ -s "$pdf" ]] || { echo "GAGAL: PDF tidak terbentuk"; exit 1; }
pages=$(pdfinfo "$pdf" | awk '/^Pages:/{print $2}')
echo "PDF: $pdf ($pages halaman)"

echo; echo "== Huruf di PDF (Noto, DejaVu, Liberation = huruf pengganti; Carlito pengganti Calibri sudah setara metrik)"
pdffonts "$pdf" | awk 'NR>2{sub(/^[A-Z]+\+/, "", $1); print "  " $1}' | sort -u
for f in "Times New Roman" "Carlito"; do
  [[ $(fc-list | grep -ci "$f" || true) -gt 0 ]] || echo "  PERINGATAN: huruf $f tidak terpasang, pemenggalan halaman bisa beda dari Word"
done

echo; echo "== cek_format.py ($jenis)"
python3 -I "$here/cek_format.py" "$docx" --jenis "$jenis" || echo "(ada temuan: nilai dengan konteksnya)"

echo; echo "== Baris pertama dan terakhir tiap halaman (cari judul atau pengantar daftar yang tertinggal di dasar)"
for ((i = 1; i <= pages; i++)); do
  txt=$(pdftotext -f "$i" -l "$i" -layout "$pdf" - | sed 's/^[[:space:]]*//' | awk 'NF')
  printf 'hlm %-3s | %s\n        ... | %s\n' "$i" "$(head -n1 <<<"$txt" | cut -c1-90)" "$(tail -n2 <<<"$txt" | head -n1 | cut -c1-90)"
done

echo; echo "== Lembar kontak"
rm -f "$work"/hlm-*.png "$work"/lembar-*.png
pdftoppm -r 50 -png "$pdf" "$work/hlm"
files=("$work"/hlm-*.png)
n=0
for ((i = 0; i < ${#files[@]}; i += 6)); do
  n=$((n + 1))
  montage "${files[@]:i:6}" -tile 3x2 -geometry +4+4 "$work/lembar-$n.png"
  echo "  $work/lembar-$n.png (halaman $((i + 1)) sampai $((i + 6 > ${#files[@]} ? ${#files[@]} : i + 6)))"
done
echo; echo "Lihat lembar kontak sekali. Perbesar (pdftoppm -r 100 -f N -l N) hanya halaman yang meragukan."
