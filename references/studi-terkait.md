# Studi Terkait (Tinjauan Pustaka) dan Literature Review (pemilihan, penelusuran, cek kualitas pustaka)
Sumber: deck W07 (slide 4-6, 8-10, 12-18, 20) dan W10 (slide 2-10). W07 s13 dan W10 s7-10 dibaca dari gambar.

## Fungsi dan penamaan
- Bagian ini berisi teori/studi/literatur yang mendukung dan terkait erat dengan topik tulisan. [W07 s4]
- Pada proposal TA biasanya bernama Tinjauan Pustaka atau Landasan Teori; Inggris: *Related Work* atau *Literature Review*. [W07 s4]
- Materi yang dibahas harus benar-benar terkait erat dengan topik, walau tidak dipakai pada sistem yang dibuat. [W07 s4]
- Letak umum: setelah Pendahuluan; kadang di akhir tulisan sebelum Kesimpulan. [W07 s4]
- Biasanya tidak dibagi sub-bagian, tetapi boleh dibagi menurut bidang studi terkait. [W07 s5]
- Panjang sekitar 15% dari total halaman; untuk tulisan 8 halaman (laporan TA FIF saat itu) sekitar 1-1,5 halaman. [W07 s6]
- Definisi *Literature Review*: kegiatan menganalisis penelitian pada bidang keilmuan yang berkaitan melalui media seperti buku, artikel, jurnal ilmiah. [W10 s2]

## Sitasi dan referensi
- Semua studi/teori yang dipaparkan mengacu ke daftar pustaka (referensi) tulisan. [W07 s5]
- Semua sitasi dalam tulisan harus ada di referensi, dan sebaliknya semua pustaka di referensi harus disitasi di tulisan. [W07 s5]
- Bedakan bibliografi (semua sumber yang dipakai selama pengerjaan, diacu atau tidak) dari referensi (daftar sumber yang diacu dalam tulisan). [W07 s9]

## Pemilihan pustaka
- Gunakan sumber kredibel. Saat mengerjakan TA, kredibilitas sumber dapat dikonsultasikan dengan pembimbing. [W07 s8]
- Pustaka biasanya dari jurnal dan konferensi bereputasi baik; tambahan boleh buku teks. [W07 s8]
- Hindari sebisa mungkin sumber yang tidak di-*review* ketat (Wikipedia, blog, materi kuliah), walau boleh membantu memahami topik (sebagai bibliografi). [W07 s9]
- Hindari TA mahasiswa sebagai referensi, kecuali yang spesifik (misalnya basis data yang dibangun TA yang telah selesai). [W07 s10]
- Untuk subbab yang menjadi inti topik, kaji beberapa pustaka, jangan hanya satu. Contoh: topik kesamaan semantik dengan *monolingual alignment*, maka bagian *monolingual alignment* mengkaji beberapa pustaka dan memberi contoh kasus. [W07 s10]

## Isi Studi Terkait (komponen)
### 1. Konsep dasar
- Tulis konsep dasar lebih detail daripada di Pendahuluan, termasuk klasifikasi topik, disertai contoh. [W07 s12]
- Contoh pada topik deteksi plagiat: definisi menurut berbagai pustaka; contoh input dan output proses; jenis-jenis proses (*source retrieval*, *text alignment*) seperti pada diagram alur deteksi plagiat (*suspicious document* ke *source retrieval* ke *candidate documents* ke *text alignment* ke *knowledge-based post-processing* ke *suspicious passages*, dengan *document collection*). [W07 s12-13] (gambar)

### 2. Sistem/metode/algoritma yang ada
- Terangkan sistem/metode/algoritma yang ada untuk bagian topik yang dikerjakan, bukan hanya yang akan dipakai di TA. Contoh: TA mengerjakan *text alignment*, maka terangkan semua metode *text alignment*. [W07 s14]
- Tulis juga perbandingan hasilnya, misalnya dari hasil kompetisi (contoh: PAN) dan dari tulisan survei. [W07 s14]

### 3. Evaluasi topik
- Bahas tiga hal dari pustaka: dataset yang biasa dipakai, *baseline*/pembanding, dan metrik evaluasi yang biasa dipakai. [W07 s15]
- *Baseline* adalah pembanding solusi/metode untuk menilai seberapa baik sistem TA dibanding sistem lain. [W07 s15]

#### Dataset
- Uraikan semua dataset yang dipakai pustaka, walau tidak dipakai TA; bandingkan dan klasifikasikan. [W07 s16]
- Dataset yang dipakai TA diterangkan lebih detail di bagian sistem, lengkap dengan alasan pemilihan. [W07 s16]

#### Baseline
- Sebutkan pembanding yang ada di pustaka (sebagian besar sudah dijelaskan di subbab metode) dan jelaskan alasan pemilihan *baseline*. [W07 s16]
- *Baseline* yang dipakai TA cukup dijelaskan singkat di bagian Evaluasi, dengan alasan pemilihannya. [W07 s16]

#### Metrik evaluasi
- Tulis jenis-jenis metrik yang dipakai pustaka sebanyak mungkin, walau tidak dipakai TA. [W07 s17]
- Jika lebih dari satu metrik, sebutkan mana yang utama. [W07 s17]
- Metrik yang dipakai TA disebut di Bab Perancangan Sistem, dengan alasan dan boleh disertai contoh. [W07 s17]

### Cakupan untuk TA dibanding artikel konferensi/jurnal
- Studi terkait di tulisan konferensi/jurnal kredibel terutama membahas aspek "bagaimana" (metode, teknik riset terkait), tanpa dataset, metrik, pembanding, dan apa yang dianalisis. [W07 s18]
- Untuk laporan TA, aspek-aspek itu (dataset, metrik evaluasi, pembanding, apa yang dianalisis) disarankan juga diulas, karena TA adalah sarana belajar awal penelitian. [W07 s18]

## Contoh studi terkait yang disebut dosen
- Lima contoh tulisan (KDD 2020 Wang et al.; IEEE TKDE Giasemidis et al.; ACL 2020 Xu et al.; IEEE Trans. Cybernetics Liu et al.; ACM TOG Karacan et al.) dipakai sebagai contoh gaya studi terkait. Slide hanya memuat daftar rujukan, tanpa kriteria baik/buruk. [W07 s20]

## Manfaat literature review
- Mengetahui tren terkini (*recent trend*) bidang atau area riset. [W10 s3]
- Mengetahui metode yang tepat untuk menyelesaikan suatu masalah. [W10 s3]
- Mengetahui hasil penelitian terdahulu yang berkaitan dengan bidang. [W10 s3]
- Menambah ilmu pengetahuan. [W10 s3]
- Menentukan pokok permasalahan yang akan diteliti. [W10 s3]

## Tahap literature review
### Tahap 1: tentukan kriteria inklusi/eksklusi rujukan
- Contoh kriteria pada slide: [W10 s4]
  - tipe berkas: .pdf, .epub;
  - sumber: Google Scholar;
  - jenis: buku, jurnal bereputasi (Q1/Q2/Q3/Q4/SINTA 1/SINTA 2), prosiding;
  - tahun: 2019-2023;
  - bahasa: Inggris;
  - jurnal akses terbuka (*Open Access*).
- Rentang tahun contoh 2019-2023 tampaknya ilustrasi untuk kuliah tahun itu. Slide tidak menyatakan akses terbuka atau bahasa Inggris sebagai syarat. Ikuti aturan proyek atau pembimbing untuk rentang tahun dan jumlah referensi. [W10 s4]

### Tahap 2: cari dan seleksi lewat abstrak
- Cari pustaka sesuai topik penelitian. [W10 s5]
- Baca dan pahami abstrak. Abstrak yang baik memuat latar belakang, permasalahan, tujuan, metode, dan hasil penelitian. [W10 s5]

### Tahap 3: identifikasi mendalam
- Baca bagian kesimpulan, metode penelitian, dan hasil penelitian. [W10 s5]
- Catat hasil penelusuran pustaka dalam bentuk tabel. [W10 s5]

## Praktik penelusuran (Google Scholar)
- Empat kegiatan praktik: penelusuran dengan Google Scholar; pengecekan kualitas karya ilmiah; identifikasi karya ilmiah secara mendalam; pakai *reference manager* (Mendeley). [W10 s6]
- Contoh penelusuran (kueri "data imputation"): [W10 s7] (gambar)
  - filter tahun lewat menu kiri ("Sejak 2019");
  - lihat jumlah "Dirujuk N kali" (jumlah sitasi) tiap hasil;
  - lihat tautan akses penuh di kanan (HTML/PDF) untuk memeriksa ketersediaan teks lengkap.
- Lingkaran merah pada tangkapan layar menyorot filter tahun, jumlah sitasi, dan tautan teks lengkap. [W10 s7] (gambar)

## Cek kualitas jurnal (SCImago, SJR)
- Buka scimagojr.com (*Scimago Journal & Country Rank*). [W10 s8] (gambar)
- Cari nama jurnal (contoh: "Applied Artificial Intelligence") di kotak pencarian. [W10 s8-9] (gambar)
- Pilih hasil yang dilingkari: jurnal yang dicari beserta negara dan penerbitnya (contoh: United Kingdom, Taylor and Francis Ltd.); hasil lain di daftar berupa prosiding konferensi. [W10 s9] (gambar)
- Buka halaman jurnal dan baca grafik *Quartiles* per tahun (warna per kuartil); slide menyorot kuartil tahun terakhir pada grafik (contoh: Q3 untuk 2022). [W10 s10] (gambar)
- Slide menyorot kuartil tahun terakhir pada grafik SCImago tanpa menyatakan apakah yang dipakai kuartil tahun terbit artikel atau tahun terbaru. Tetapkan satu pilihan dan catat di aturan proyek. [W10 s10]
- Slide hanya menunjukkan cek lewat SCImago. Cara cek SINTA tidak dibahas, jadi verifikasi status indeks lewat situs resmi masing-masing dan sebut sumbernya. [W10 s8-10]
