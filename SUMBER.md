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

Slide yang isinya berupa gambar (tabel, checklist, diagram) didaftar di baris "Sumber" pada kepala tiap berkas referensi, karena hanya terbaca dari render slide dan tidak muncul pada ekstraksi teks.

## Memeriksa sebuah tag

Jalankan dari akar repo. Nama berkas mengandung spasi, jadi selalu diberi tanda kutip.

Teks slide dari `.pptx` (contoh W06 slide 15):

```bash
unzip -p "slides/W06 - Pendahuluan.pptx" ppt/slides/slide15.xml | grep -o '<a:t>[^<]*</a:t>' | sed 's/<[^>]*>//g' | paste -sd' '
```

Gambar slide (contoh W12 slide 7, untuk slide bergambar). Butuh LibreOffice dan `pdftoppm` (paket poppler):

```bash
mkdir -p /tmp/metopen
soffice --headless --convert-to pdf --outdir /tmp/metopen "slides/W12 - Poin-poin Isi Tulisan dan Checklist.pptx"
pdftoppm -r 70 -png -f 7 -l 7 "/tmp/metopen/W12 - Poin-poin Isi Tulisan dan Checklist.pdf" /tmp/metopen/w12
```

W01 sudah berupa PDF, jadi cukup `pdftoppm -r 70 -png -f 51 -l 51 "slides/Week 01 - Pengantar Metodologi Penelitian dan Tata Tulis Ilmiah.pdf" /tmp/metopen/w01`. Tanpa LibreOffice, buka `.pptx` langsung di PowerPoint atau aplikasi presentasi lain.

## Templat resmi (tag TP, TB, TJ)

Salinan templat FIF ada di `templates/`, diperoleh penyusun dari program studi pada 2024-2025 dan disertakan agar tag bisa diperiksa. Versi docx proposal dan buku TA tidak ditemukan di situs publik fakultas; portal SONIA memuat templat gaya jurnal TA. Hak cipta templat pada Fakultas Informatika Universitas Telkom.

| Kode | Berkas di `templates/` | Dipakai untuk | Dirangkum di |
|---|---|---|---|
| TP | `Template Proposal FIF.docx` | Proposal TA (MK Penulisan Proposal) | `references/format-dokumen.md` |
| TB | `Template Buku TA FIF.docx` | Laporan TA bentuk buku | `references/format-dokumen.md` |
| TJ | `Template Jurnal TA FIF.docx` | Laporan TA bentuk jurnal (gaya selingkung versi November 2017) | `references/format-dokumen.md` |

`[TB hlm. 25]` berarti halaman ke-25 PDF hasil render LibreOffice (nomor urut halaman PDF, bukan nomor yang tercetak di halaman). Render ulang dan baca halamannya:

```bash
mkdir -p /tmp/metopen
soffice --headless --convert-to pdf --outdir /tmp/metopen "templates/Template Buku TA FIF.docx"
pdftotext -f 25 -l 25 -layout "/tmp/metopen/Template Buku TA FIF.pdf" -
```

`[TB xml]` berarti fakta dibaca dari pengaturan docx, bukan dari teks petunjuk. Periksa dengan membuka XML-nya, misalnya margin dan gaya:

```bash
unzip -p "templates/Template Buku TA FIF.docx" word/document.xml | grep -o '<w:pgMar [^>]*>'
unzip -p "templates/Template Buku TA FIF.docx" word/styles.xml | grep -o '<w:style [^>]*w:styleId="Caption".*</w:style>' | head -c 800
```

`scripts/cek_format.py` membaca hal yang sama (format efektif dari paragraf, gaya, bawaan dokumen, dan huruf tema), jadi menjalankannya pada templat juga cara cepat memeriksa tag `xml`.

## Dokumen resmi (tag PFIF20, PU027, PU026, KWR175, AI25, SONIA)

Diperiksa 26 November 2026 dari alamat publik di bawah. Berkasnya tidak disalin ke repo. `hlm.` = halaman PDF. Dirangkum di `references/aturan-resmi.md`.

| Kode | Dokumen | Alamat |
|---|---|---|
| PFIF20 | Panduan TA Berbasis Riset Program Studi Sarjana FIF, 1 September 2020 (tersimpan di situs staf, bukan situs fakultas) | https://donnir.staff.telkomuniversity.ac.id/files/2020/10/panduan-ta-2020.pdf |
| PU027 | PU.027/AKD11/AKD-BPA/2024, Persyaratan Kelulusan Studi dan Standar Luaran TA | https://bpa.telkomuniversity.ac.id/wp-content/uploads/2024/11/PU_PERSYARATAN_KELULUSAN_STUDI_DAN_STANDAR_LUARAN_TUGAS_AKHIR.pdf |
| PU026 | PU.026/AKD13/PPM/2022, Pedoman Penegakan Integritas Akademik Karya Ilmiah | https://ppm.telkomuniversity.ac.id/wp-content/uploads/2026/08/PU.026-PEDOMAN-PENEGAKAN-INTEGRITAS-AKADEMIK-KARYA-ILMIAH-1.pdf |
| KWR175 | KWR1.175/AKD26/AKD-PUS/2022, Aturan Umum TA sebagai Penelitian dan Publikasi | https://seb.telkomuniversity.ac.id/wp-content/uploads/2022/09/Regulasi_Aturan_Umum_Tugas_Akhir.pdf |
| AI25 | Panduan Penggunaan AI untuk Pembelajaran dan Pengajaran 2025, versi 1.0 | https://bpa.telkomuniversity.ac.id/wp-content/uploads/2025/08/Panduan-Penggunaan-Artificial-Intelligence-AI-Untuk-Pembelajaran-dan-Pengajaran-2025-Versi-1.0.pdf |
| SONIA | Templat TA di portal resmi FIF (isinya gaya selingkung jurnal) | https://sonia.soc.telkomuniversity.ac.id/cdn/docs_academic/dokpenunjang/Template_Buku_Tugas_Akhir_Program_Sarjana_Fakutas_Informatika.pdf |

Memeriksa tag: unduh berkasnya, lalu baca halaman yang dirujuk, misalnya `pdftotext -f 14 -l 14 -layout panduan-ta-2020.pdf -`.

## Pola TA terbit (tag OL)

`[OL]` di `references/pola-ta-terbit.md` menunjuk pembacaan TA S1 FIF 2025-2026 di Open Library Telkom University (openlibrary.telkomuniversity.ac.id), November 2026. Berkas itu memuat pola agregat. Bagian "Pola TA satu pembimbing" memuat sampel kedua (16 November 2026): abstrak, Bab 1-3, dan artikel tujuh TA bimbingan satu calon pembimbing, dengan kode katalog TA pada temuan tertentu. Untuk memeriksa, buka katalog Open Library, saring jenis "Skripsi" dan program studi FIF, lalu baca abstrak dan Bab 1-3 beberapa TA terbaru.

Catatan penggunaan: slide mengacu ke Template Laporan TA FIF untuk laporan akhir, sedangkan proposal memakai templat proposal fakultas. Templat menang atas slide; aturan proyek pengguna menang atas keduanya.
