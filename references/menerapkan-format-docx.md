# Menerapkan format di berkas .docx
Cara menulis ke salinan templat FIF tanpa merusak gaya, penomoran, dan *shading*, lalu memeriksa hasilnya. Angka format ada di `references/format-dokumen.md`; berkas ini hanya memuat caranya.
Sumber: pengamatan langsung pada `templates/*.docx` (2026-11), kecuali yang diberi tag.

## Langkah

1. **Salin templat.** Kerjakan pada salinan berkas pengguna, bukan templat di `templates/`.
2. **Edit `word/document.xml` langsung.** Bongkar docx (`unzip`), ubah XML, lalu kemas ulang dari dalam folder: `zip -X -r ../hasil.docx '[Content_Types].xml' _rels docProps word` (ikut sertakan folder lain yang ada, misalnya `customXml`). Konversi bolak-balik lewat pandoc atau pengolah lain merusak gaya, penomoran otomatis, dan *shading* templat.
3. **Kloning paragraf sejenis.** Paragraf baru menyalin `w:pPr` dan `w:rPr` dari paragraf templat yang jenisnya sama: isi, heading per tingkat, butir daftar, caption, entri daftar pustaka. Memasang nama gaya saja tidak cukup:
   - [TP] spasi 1,5 ada di format langsung tiap paragraf; gaya `Normal-TA` mewarisi spasi 1,08.
   - Gaya Heading templat berhuruf Calibri Light/Aptos Display dan sebagian biru. Tampilan TNR hitam di [TP] berasal dari run heading, jadi heading baru menyalin run itu (huruf, ukuran, tebal, `w:color w:val="auto"`).
   - [TB] subbab memakai `List Paragraph` bernomor, bukan Heading 2.
4. **Pakai penomoran templat.** Nomor bab dan subbab memakai `w:numPr` (numId dan ilvl) yang sama dengan heading templat. Nomor "1.1" tidak diketik manual, kecuali templat memang begitu.
5. **Jaga tabel dan gambar utuh.**
   - Caption tabel di atas tabel, dengan `w:keepNext`. Untuk tabel yang muat satu halaman, beri `w:cantSplit` pada setiap baris dan `w:keepNext` pada paragraf di semua baris kecuali baris terakhir, agar caption dan tabel tidak terpisah halaman.
   - Tabel yang lebih dari satu halaman memakai `w:tblHeader` pada baris judul. [Tips s9]
   - Paragraf gambar diberi `w:keepNext` agar caption di bawahnya ikut.
6. **Rapikan pemenggalan halaman.** Bab baru dimulai dengan pemisah halaman. Heading dan kalimat pengantar daftar diberi `w:keepNext` supaya tidak tertinggal di dasar halaman. `w:widowControl` aktif untuk mencegah baris yatim dan janda. [Tips s9]
7. **Bersihkan sisa templat.** Ganti teks petunjuk dan *placeholder* (`<Nama Prodi>`, `113xxxxxx`, deretan titik) dengan isi. Normalkan huruf run sisa templat ("Times", "MS Mincho") menjadi huruf templat (TNR untuk [TP]).
8. **Bangun PDF dan periksa** (bagian berikut). Bila proyek menyimpan PDF berdampingan dengan docx, bangun ulang setiap kali docx berubah.

## Pemeriksaan

Satu perintah dari folder skill membangun PDF di samping docx, lalu menjalankan semua pemeriksaan berikut:

```bash
scripts/bangun_pdf.sh "BERKAS.docx" proposal [FOLDER_KERJA]   # jenis: proposal, buku, jurnal
```

Keluarannya berurutan: huruf yang dipakai PDF (`pdffonts`; Noto, DejaVu, atau Liberation berarti huruf pengganti), laporan `cek_format.py`, baris pertama dan terakhir tiap halaman, lalu lembar kontak (6 halaman per gambar, 50 dpi) di FOLDER_KERJA.

- `cek_format.py` membaca berkas dan melaporkan kertas, margin, huruf, ukuran, spasi, heading, caption, sisa templat, kata ganti orang pertama, dan kelompok `isi: ...` (tanda pisah, sitasi dan Daftar Pustaka, jumlah rumusan dan Tujuan, kata kerja Bloom, jumlah Batasan, abstrak dan kata kunci, rujukan tabel dan gambar). Sampul, lembar pengesahan, paragraf rata tengah, dan isi tabel tidak dinilai sebagai isi. Kode keluar 1 berarti ada temuan; nilai setiap temuan dengan konteksnya.
- Pemenggalan halaman dibaca dari daftar baris pertama dan terakhir: judul atau kalimat pengantar yang tertinggal di dasar halaman tampak di sana tanpa membuka gambar.
- Lembar kontak dilihat sekali untuk tabel, gambar, dan nomor halaman. Halaman yang meragukan diperbesar satu per satu (`pdftoppm -r 100 -f N -l N`); membaca ulang seluruh gambar setelah tiap perubahan kecil memboroskan konteks.
- Pemeriksaan dianggap selesai bila setiap temuan skrip sudah diperbaiki atau dijelaskan, dan lembar kontak sudah dilihat.

Shell di mesin ini zsh: pola glob yang tidak cocok menggagalkan perintah (`no matches found`), jadi uji dengan `ls` atau `find` lebih dulu. Perintah berspasi tidak disimpan di variabel, dan nama fungsi `g` bentrok dengan alias.

## Jebakan render LibreOffice

- Caption bermedan `STYLEREF 1 \s` + `SEQ` (gaya [TB]) tampil sebagai "Tabel PENDAHULUAN.1" di LibreOffice, padahal di Word tampil "Tabel 1.1". Bila PDF dibangun dengan LibreOffice, pakai nomor caption statis atau periksa hasilnya di Word.
- Times New Roman, Aptos, dan Calibri (huruf bawaan dokumen [TP], dipakai nomor halaman) harus terpasang. Tanpa itu LibreOffice memakai huruf pengganti, sehingga pemenggalan baris dan halaman berbeda dari Word. Periksa dengan `fc-list | grep -i "times new roman"` dan `pdffonts`.
- Medan Daftar Isi, Daftar Gambar, dan Daftar Tabel tidak diperbarui otomatis saat konversi. Perbarui di Word, atau tulis ulang nomor halamannya dari PDF.
