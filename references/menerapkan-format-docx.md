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

```bash
python3 -I scripts/cek_format.py "BERKAS.docx" --jenis proposal   # atau buku, jurnal
soffice --headless --convert-to pdf --outdir OUT "BERKAS.docx"
pdffonts OUT/BERKAS.pdf                      # huruf pengganti (Noto, DejaVu, Liberation) tanda huruf tidak terpasang
pdftoppm -r 60 -png OUT/BERKAS.pdf OUT/hlm   # lalu lihat setiap halaman
```

- Jalankan `cek_format.py` dari folder skill. Skrip hanya membaca berkas dan melaporkan kertas, margin, huruf, ukuran, spasi, heading, caption, sisa templat, dan kata ganti orang pertama. Sampul, lembar pengesahan, paragraf rata tengah, dan isi tabel tidak dinilai sebagai isi. Kode keluar 1 berarti ada temuan; nilai setiap temuan dengan konteksnya.
- Halaman PDF diperiksa satu per satu: judul atau kalimat pengantar tidak tertinggal di dasar halaman, tabel tidak terbelah, nomor halaman sesuai jenis dokumen, gambar terbaca.
- Pemeriksaan dianggap selesai bila setiap temuan skrip sudah diperbaiki atau dijelaskan, dan setiap halaman PDF sudah dilihat.

## Jebakan render LibreOffice

- Caption bermedan `STYLEREF 1 \s` + `SEQ` (gaya [TB]) tampil sebagai "Tabel PENDAHULUAN.1" di LibreOffice, padahal di Word tampil "Tabel 1.1". Bila PDF dibangun dengan LibreOffice, pakai nomor caption statis atau periksa hasilnya di Word.
- Times New Roman dan Aptos harus terpasang. Tanpa itu LibreOffice memakai huruf pengganti, sehingga pemenggalan baris dan halaman berbeda dari Word. Periksa dengan `fc-list | grep -i "times new roman"` dan `pdffonts`.
- Medan Daftar Isi, Daftar Gambar, dan Daftar Tabel tidak diperbarui otomatis saat konversi. Perbarui di Word, atau tulis ulang nomor halamannya dari PDF.
