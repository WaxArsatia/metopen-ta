#!/usr/bin/env bash
# Kemas folder hasil unzip menjadi .docx baru, lalu uji zipnya sebelum menimpa berkas pengguna.
#
# Pemakaian: scripts/docx_kemas.sh FOLDER_XML BERKAS.docx [FOLDER_CADANGAN]
#   FOLDER_XML       hasil `unzip` docx, sudah disunting (berisi [Content_Types].xml, _rels, word, ...).
#   BERKAS.docx      berkas pengguna yang akan ditimpa; kemas dibuat dulu di sebelahnya sebagai .baru.docx.
#   FOLDER_CADANGAN  bawaan: .cadangan di folder BERKAS.docx. Docx lama disalin ke sini sebagai
#                    <nama>_<stempel waktu>.docx sebelum ditimpa.
# Urutan: zip, `unzip -tq` pada kemas, cadangkan docx lama, timpa. Gagal di langkah mana pun menghentikan
# skrip dan membiarkan BERKAS.docx utuh. Zip rusak tetap bisa dibangun LibreOffice menjadi PDF, jadi uji ini
# tidak digantikan oleh PDF yang jadi.
set -euo pipefail
[[ $# -ge 2 ]] || { sed -n '2,11p' "$0"; exit 2; }
src=$(realpath "$1")
docx=$(realpath "$2")
[[ -f $src/[Content_Types].xml ]] || { echo "GAGAL: $src bukan hasil unzip docx"; exit 1; }
dir=$(dirname "$docx")
cad=${3:-$dir/.cadangan}
baru="${docx%.docx}.baru.docx"
rm -f "$baru"
(cd "$src" && zip -X -q -r "$baru" '[Content_Types].xml' && zip -X -q -r "$baru" . -x '[Content_Types].xml')
unzip -tq "$baru" >/dev/null || { rm -f "$baru"; echo "GAGAL: zip kemas rusak"; exit 1; }
mkdir -p "$cad"
cp "$docx" "$cad/$(basename "${docx%.docx}")_$(date +%Y%m%d-%H%M%S).docx"
mv "$baru" "$docx"
echo "OK: $docx ditimpa (zip utuh); cadangan di $cad"
