# Pola TA FIF yang sudah terbit
Praktik teramati pada TA S1 FIF (Teknologi Informasi dan Informatika) yang terbit di Open Library Telkom University, sebagai contoh cara templat dipakai. Derajatnya paling bawah: templat dan slide menang. Pola yang bertentangan dengan templat dicatat sebagai pelanggaran yang perlu diperiksa, bukan sebagai izin. Satu pengecualian: bagian "Pola TA satu pembimbing" menang atas preset `aturan-denis.md` pada butir yang berbeda, hanya bila pengguna memicu preset itu (lihat `SKILL.md`, Urutan otoritas).
Sumber: `[OL]` = pembacaan abstrak dan Bab 1-3 delapan buku TA serta sepuluh artikel TA tahun 2025-2026, topik IoT, sensor, dan kompresi model (November 2026). Bab 4, Bab 5, dan daftar pustaka buku tidak dapat diunduh dengan akun mahasiswa, jadi tidak tercakup. Angka berupa sebaran pada sampel itu, bukan aturan. Sampel kedua (16 November 2026) dibahas di bagian "Pola TA satu pembimbing".

## Bentuk laporan

- Hampir semua TA mengunggah buku TA (Bab 1-5 dan daftar pustaka) beserta hasil pemeriksaan kemiripan. Sebagian juga mengunggah artikel: naskah gaya jurnal TA FIF atau makalah konferensi IEEE dua kolom berbahasa Inggris. [OL]
- Label "pengganti sidang" di katalog menandai jalur kelulusan, bukan format tulisan; TA berlabel itu tetap mengunggah buku. [OL]

## Struktur buku

- Bab 1 hampir selalu persis mengikuti templat buku: 1.1 Latar Belakang, 1.2 Rumusan Masalah, 1.3 Tujuan dan Manfaat, 1.4 Batasan Masalah, 1.5 Metode Penelitian, 1.6 Jadwal Pelaksanaan. Bab 2 Tinjauan Pustaka, Bab 3 Perancangan Sistem. [OL]
- Satu TA membawa susunan proposal (Perumusan Masalah, Hipotesis, Rencana Kegiatan) ke buku. Itu menyimpang dari templat buku; saat menyusun buku dari proposal, ganti susunannya. [OL]
- Sistematika Penulisan tidak muncul di Bab 1 buku. Naskah gaya jurnal TA memuat Organisasi Tulisan. [OL]
- Bab 2 lazim dibuka dengan tabel ringkasan studi terkait (Tabel 2.1: metode, hasil, relevansi, celah), lalu teori dan metode yang dipakai. [OL]
- Bab 3 lazim memuat diagram alur atau diagram blok (Gambar 3.1), arsitektur sistem atau perangkat, dataset dan praproses, rancangan model, dan metrik evaluasi dengan rumus bernomor. [OL]
- Bagian hasil di artikel berjudul "Evaluasi", "Hasil Pengujian dan Evaluasi", atau "Hasil dan Pembahasan", lalu "Kesimpulan". [OL]

## Pendahuluan

- Rumusan Masalah: kalimat tanya pada semua sampel, umumnya "Bagaimana ...", didahului kalimat pengantar, tiga butir bernomor. [OL]
- Banyak rumusan memuat nama metode. Itu berbenturan dengan aturan Pendahuluan di slide (bagaimana-nya tidak di Pendahuluan, [W06 s4]) dan dengan aturan proyek bila proyek melarang solusi di rumusan; ikuti aturan yang lebih tinggi derajatnya.
- Tujuan: separuh sampel berupa daftar bernomor berkata kerja (menganalisis, mengevaluasi, membandingkan), separuh narasi. Templat buku dan gaya jurnal TA meminta narasi. Tujuan yang baik menyebut metriknya (akurasi, F1, MAE, RMSE, waktu inferensi). [OL]
- Tabel keterkaitan Tujuan, Pengujian, Kesimpulan dipakai sebagian TA; kolom Kesimpulan yang paling informatif berisi hasil angka. [OL]
- Manfaat ditulis sebagai paragraf narasi. [OL]
- Batasan Masalah ada di semua sampel (tiga sampai enam butir), tetapi alasan per butir jarang ditulis dan banyak butir mengulang judul ("model yang digunakan adalah ..."). Periksa aktif: setiap butir punya alasan dan tidak mengulang judul [W06 s15-18]. [OL]
- Hipotesis hampir tidak pernah muncul di buku. [OL]
- Metode Penelitian berupa narasi tahapan: studi literatur, pengumpulan data, praproses, pemodelan, evaluasi. Jadwal berupa tabel tahapan per bulan (enam bulan). [OL]

## Abstrak dan kata kunci

- Abstrak memuat masalah, alasan, dan solusi; sebagian besar memuat hasil angka; tidak ada sitasi. Kebanyakan satu paragraf; sebagian memakai empat sub-bagian berlabel (permasalahan, pentingnya penelitian, solusi, hasil utama). [OL]
- Pelanggaran yang sering: lebih dari 200 kata dan lebih dari enam kata kunci, kata kunci berhuruf kapital. Hitung kata dan kata kunci sebelum selesai. [OL]

## Tata letak (hasil pengukuran PDF)

- Isi 12 pt dengan jarak baris setara spasi 1,5, margin kiri sekitar 4 cm dan kanan sekitar 3 cm, sesuai templat. [OL]
- Huruf isi: Times New Roman paling sering, lalu Aptos. Ada yang memakai Arial dan ada yang berukuran kertas Letter; keduanya di luar templat. [OL]
- Nomor halaman isi di kanan bawah pada hampir semua sampel, termasuk halaman pertama bab; tidak ada yang di kanan atas. Ini sejalan dengan pengaturan docx templat buku. [OL]
- Judul bab: "BAB n" dan judul bab, tebal, rata tengah, satu baris atau dua baris. [OL]
- Artikel gaya jurnal TA: Times New Roman 10 pt, spasi 1. [OL]

## Caption, persamaan, sitasi

- Caption tabel di atas, gambar di bawah, tebal, rata tengah, caption tabel lebih kecil dari isi. Pemisah setelah nomor beragam (spasi, titik, titik dua) antar-TA; dalam satu naskah harus seragam. [OL]
- Persamaan bernomor "(3.1)" rata kanan. [OL]
- Sitasi angka "[n]" di semua sampel, gaya IEEE urut kemunculan, termasuk di artikel gaya jurnal TA (bukan gaya nama-tahun pada contoh lama). Nama penulis ditulis "Nama et al. [n]" atau "Nama dkk. [n]". [OL]
- Jumlah referensi artikel 14 sampai 29; porsi artikel jurnal 30-67%, sisanya prosiding, prapublikasi, dan web. [OL]

## Metrik dan pembanding

- Klasifikasi: akurasi, presisi, *recall*, F1, *confusion matrix*, AUC. Regresi atau peramalan: MAE, RMSE, R². [OL]
- TA kompresi atau model ringan melaporkan efisiensi di samping kinerja: ukuran model, jumlah parameter, waktu inferensi, rasio kompresi, memori. Pembanding utamanya model sebelum kompresi atau model dasar. [OL]
- Waktu inferensi kadang diukur di komputer awan atau hos, bukan perangkat tepi, dan dinyatakan sebagai batasan. [OL]

## Pola TA satu pembimbing (pembacaan 16 November 2026)

Sampel kedua `[OL]`: abstrak, Bab 1, 2, 3, dan artikel tujuh TA S1 FIF bimbingan satu calon pembimbing yang sama (nama tidak dicantumkan). Delapan TA diperiksa, berkode 25.04.7062, 26.04.1885, 26.04.307, 26.04.3085, 26.04.3314, 26.04.3319, 26.04.3321, dan 26.04.3329. TA 26.04.3329 berupa gambar sehingga tidak terbaca otomatis. Semua angka di bagian ini dari tujuh TA yang terbaca.

### Abstrak dan kata kunci

- Bentuk: 5 dari 7 satu paragraf, 2 dari 7 empat subbagian berlabel. [OL]
- Panjang 132 sampai 239 kata, dengan 3 dari 7 melampaui 200 kata. [OL]
- Kata "Namun" memisahkan latar belakang dan masalah pada 3 dari 7 (26.04.3085 memakai "Meskipun"). [OL]
- Pembuka kalimat tujuan: "Tujuan dari" pada 0 dari 7, "Penelitian ini mengusulkan" pada 6 dari 7. [OL]
- Semua abstrak memuat hasil angka. [OL]
- Kata kunci: 5 butir pada 4 dari 7, 6 butir pada 1, 7 butir pada 2. Gaya huruf kecil dan kepanjangan semua persis pada 26.04.3085, hampir pada 26.04.1885 (hanya "sensor IMU"). TA lain memakai singkatan atau kapital awal. [OL]

### Bab 2 dan Bab 3

- Bab 2 tidak memuat persamaan bernomor pada ketujuh TA. [OL]
- Bab 3 panjang 4 sampai 11 halaman (median 8). [OL]
- Gambar 3.1 berupa alur atau flowchart dan Gambar 3.2 berupa arsitektur sistem pada 6 dari 7 TA. Satu TA tidak punya caption gambar yang terdeteksi. [OL]
- Pseudocode pada 3 dari 7 (26.04.307, 26.04.3085, 26.04.3314), selalu tepat satu, bernomor "Algoritma 1" atau "Algorithm 1" tanpa nomor bab. Isinya Input dan Output (atau Require dan Ensure), lalu langkah bernomor, sekitar 10 sampai 20 baris. Pseudocode 26.04.3085 jauh lebih panjang dan bergaya kode. [OL]
- Persamaan bernomor (3.n) hanya di Bab 3: 11 pada 26.04.3321, 6 pada 26.04.3319, 3 pada 26.04.1885, dan sebagian tak bernomor pada 26.04.307 dan 26.04.3085. [OL]
- Subbab "Metrik Evaluasi" berisi rumus (akurasi, presisi, *recall*, F1, latensi) pada beberapa TA. [OL]

### Batasan Masalah

- Jumlah butir: 3 (26.04.7062), 4 (26.04.307, 26.04.3314), 5 (26.04.1885), 6 (26.04.3085, 26.04.3321). Tidak ada yang 8. [OL]
- Alasan per butir jarang tertulis. [OL]

## Cara memakai pola ini

- Pakai sebagai contoh bentuk saat templat dan slide tidak mengatur (misalnya kolom tabel studi terkait atau isi Bab 3).
- Saat sebuah pola menyimpang dari templat (Arial, kertas Letter, Hipotesis di buku, batasan tanpa alasan), ikuti templat dan sebut penyimpangan itu bila pengguna mencontoh TA terbit.
- Pola khusus pembimbing tertentu disimpan di bagian "Pola TA satu pembimbing" tanpa nama pembimbing. Pola yang lebih rinci, bila ada, disimpan di aturan proyek pengguna.
