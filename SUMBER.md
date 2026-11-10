# Sumber materi

Skill ini merangkum (parafrase, bukan salinan) slide kuliah Metodologi Penelitian dan Tata Tulis Ilmiah, Fakultas Informatika Universitas Telkom, disusun oleh pengampu kelas (nama tertera pada slide). Salinan slide aslinya ada di folder `slides/` supaya setiap tag bisa diperiksa tanpa memindahkan berkas dari luar repo.

Tag seperti `[W06 s15]` berarti deck W06, slide 15. Nomor slide sama dengan nomor halaman pada PDF hasil konversi dan sama dengan `ppt/slides/slide15.xml` di dalam berkas `.pptx`.

| Kode | Berkas di `slides/` | Dirangkum di |
|---|---|---|
| W01 | `Week 01 - Pengantar Metodologi Penelitian dan Tata Tulis Ilmiah.pdf` | `references/struktur-isi.md` |
| W02 | `W02 - Struktur dan Isi Proposal  Laporan TA.pptx` | `references/struktur-isi.md` |
| W04 | `W04 - Judul, Identitas Penulis, dan Pengantar Abstrak.pptx` | `references/judul-abstrak.md` |
| W05 | `W05 - Abstrak dan Jenis-jenis Publikasi Ilmiah.pptx` | `references/judul-abstrak.md` (abstrak), `references/sitasi-parafrase.md` (publikasi, sitasi) |
| W06 | `W06 - Pendahuluan.pptx` | `references/pendahuluan.md` |
| W07 | `W07 - Studi Terkait.pptx` | `references/studi-terkait.md` |
| W09 | `W09 - Evaluasi.pptx` | `references/evaluasi.md` |
| W10 | `W10 - Literature Review.pptx` | `references/studi-terkait.md` |
| W11 | `W11 - Pengeditan dan Parafrase.pptx` | `references/sitasi-parafrase.md` |
| W12 | `W12 - Poin-poin Isi Tulisan dan Checklist.pptx` | `references/checklist-editing.md` |
| W13 | `W13 - Slide dan Presentasi.pptx` | `references/presentasi-sidang.md` |
| Tips | `Tips Mengerjakan Tugas Akhir - by KIF.pptx` | `references/checklist-editing.md` |

Slide yang isinya berupa gambar (tabel, checklist, diagram) ditandai `(gambar)` di referensi, karena hanya terbaca dari render slide dan tidak muncul pada ekstraksi teks.

## Memeriksa sebuah tag

Jalankan dari akar repo. Nama berkas mengandung spasi, jadi selalu diberi tanda kutip.

Teks slide dari `.pptx` (contoh W06 slide 15):

```bash
unzip -p "slides/W06 - Pendahuluan.pptx" ppt/slides/slide15.xml | grep -o '<a:t>[^<]*</a:t>' | sed 's/<[^>]*>//g' | paste -sd' '
```

Gambar slide (contoh W12 slide 7, untuk tag `(gambar)`). Butuh LibreOffice dan `pdftoppm` (paket poppler):

```bash
mkdir -p /tmp/metopen
soffice --headless --convert-to pdf --outdir /tmp/metopen "slides/W12 - Poin-poin Isi Tulisan dan Checklist.pptx"
pdftoppm -r 70 -png -f 7 -l 7 "/tmp/metopen/W12 - Poin-poin Isi Tulisan dan Checklist.pdf" /tmp/metopen/w12
```

W01 sudah berupa PDF, jadi cukup `pdftoppm -r 70 -png -f 51 -l 51 "slides/Week 01 - Pengantar Metodologi Penelitian dan Tata Tulis Ilmiah.pdf" /tmp/metopen/w01`. Tanpa LibreOffice, buka `.pptx` langsung di PowerPoint atau aplikasi presentasi lain.

Catatan penggunaan: slide mengacu ke Template Laporan TA FIF untuk laporan akhir, sedangkan proposal memakai templat proposal fakultas. Bila keduanya berbeda, templat proposal dan aturan proyek menang.
