# Format dokumen: proposal, buku TA, jurnal TA
Tata letak, huruf, ukuran, spasi, heading, caption, nomor halaman, daftar pustaka, dan struktur bab menurut tiga templat resmi FIF. Templat menang atas slide.
Sumber: `templates/Template Proposal FIF.docx` [TP], `templates/Template Buku TA FIF.docx` [TB], `templates/Template Jurnal TA FIF.docx` [TJ]. Tag `[TB hlm. 25]` menunjuk halaman ke-25 PDF hasil render templat (bukan nomor yang tercetak). Tag `[TB xml]` berarti fakta dibaca dari pengaturan di dalam docx (`document.xml`, `styles.xml`, `numbering.xml`, `theme1.xml`), bukan dari teks petunjuk. Cara memeriksa tag ada di `SUMBER.md`.

## Pilih templat lebih dulu

- Proposal TA memakai [TP]. Laporan akhir memakai [TB] (bentuk buku) atau [TJ] (bentuk jurnal). Tanyakan ke pengguna bentuk mana yang diminta prodi atau pembimbing bila belum tercatat di aturan proyek.
- Saat menulis ke berkas pengguna, kerjakan pada salinan templat. Templat asli tidak diubah.

## Aturan saat teks petunjuk dan format nyata bertentangan

Templat kadang memuat dua versi aturan: kalimat petunjuk di halaman, dan pengaturan yang benar-benar tertanam di docx (gaya, paragraf, bagian halaman).

- [TP] dan [TB]: **format nyata menang**. Ikuti pengaturan docx. Bila suatu elemen tidak punya contoh terformat di templat (misalnya caption di [TP]), ikuti teks petunjuk dan laporkan ke pengguna.
- [TJ]: **teks petunjuk menang**. Pengaturan docx [TJ] adalah sisa konversi PDF (margin kanan 0,25 cm, kiri 0,78 cm, indentasi paragraf menambal), jadi angka margin dan spasi diambil dari teks. [TJ xml]
- Setiap pertentangan yang ditemui dilaporkan ke pengguna beserta pilihan yang diambil. Daftar yang sudah diketahui ada di bagian "Pertentangan yang diketahui".

## Proposal TA [TP]

### Halaman dan huruf
- Kertas A4 tegak. Margin kiri 4 cm, atas 3 cm, kanan 3 cm, bawah 3 cm. Jarak header dan footer 1,27 cm. [TP xml; TP hlm. 6]
- Huruf Times New Roman di seluruh dokumen. [TP hlm. 6]
- Isi 12 pt, rata kiri-kanan, spasi baris 1,5 (`line=360`), spasi sebelum dan sesudah paragraf 0. Pengaturan ini ditaruh langsung di setiap paragraf. Gaya `Normal-TA` (TNR 12, rata kiri-kanan) mewarisi spasi 1,08 dari `Normal`, jadi paragraf baru harus menyalin `pPr` paragraf isi templat, bukan hanya memasang gaya. [TP xml]
- Cetak dengan tinta hitam. Gambar berwarna sesuai kebutuhan topik. [TP hlm. 6]

### Heading
- Judul bab (Heading 1): rata tengah, TNR 16 pt tebal, warna `auto`, huruf kapital, bernomor otomatis "1.", "2.", "3." (PENDAHULUAN, KAJIAN PUSTAKA, PERANCANGAN SISTEM). [TP xml; TP hlm. 6]
- Judul tanpa nomor yang memakai Heading 1 yang sama: Lembar Persetujuan, ABSTRAK, DAFTAR PUSTAKA, LAMPIRAN. [TP xml]
- Subbab (Heading 2): bernomor "1.1.", TNR 14 pt tebal, warna `auto`, indentasi kiri 1,27 cm gantung 1,27 cm. [TP xml; TP hlm. 6]
- Sub-subbab dan seterusnya: 12 pt. [TP hlm. 6] Templat tidak memberi contoh, jadi ikuti pola Heading 2 dengan ukuran 12 pt tebal.
- Gaya Heading 1-3 bawaan templat berhuruf Calibri Light berwarna biru. Tampilan TNR hitam berasal dari format langsung pada run. Heading baru menyalin run heading templat, bukan hanya memasang gaya. [TP xml]

### Halaman awal dan penomoran
- Sampul: judul TNR 16 pt tebal; "Proposal Tugas Akhir", kelas mata kuliah, NIM, dan nama 12 pt tebal; prodi, fakultas, universitas, kota, dan tahun 16 pt tebal; semua rata tengah. [TP xml; TP hlm. 1]
- Lembar Persetujuan: judul Indonesia, judul Inggris, NIM, dan nama 14 pt tebal; kalimat pengajuan dan blok tanda tangan calon pembimbing 1 dan 2 (nama lengkap bergelar, NIP) 12 pt. [TP xml; TP hlm. 2]
- Sampul berada di bagian halaman sendiri tanpa nomor. Nomor Arab dimulai dari 1 pada Lembar Persetujuan, di footer kanan bawah. Nomor halaman memakai gaya Footer tanpa format langsung, jadi tampil dengan huruf bawaan dokumen (Calibri 11 pt). [TP xml]
- Setiap bagian utama (Lembar Persetujuan, Abstrak, tiap bab, Daftar Pustaka, Lampiran) dimulai di halaman baru dengan pemisah halaman. [TP xml]

### Struktur isi
- Abstrak: resume keseluruhan TA yang akan dikerjakan, memuat permasalahan, metodologi, dan hipotesa awal. Kata kunci huruf kecil, maksimal enam. [TP hlm. 3]
- Bab 1 Pendahuluan: 1.1 Latar Belakang (minimal satu halaman; alasan masalah diangkat, konsep baru bila ada, gap kondisi kini dan harapan, proses identifikasi masalah), 1.2 Perumusan Masalah (mengacu ke latar belakang dan penelitian terdahulu; boleh memuat definisi, asumsi, lingkup; tidak harus berbentuk pertanyaan), 1.3 Tujuan (spesifik, jelas, terukur, berupa kondisi baru setelah TA selesai), 1.4 Hipotesis (opsional), 1.5 Rencana Kegiatan (kajian pustaka, cara pengumpulan data, rancangan penelitian, cara menguji hasil), 1.6 Jadwal Kegiatan (bar chart per bulan atau per minggu, *shading* abu-abu). [TP hlm. 4-5]
- Bab 2 Kajian Pustaka: diawali ringkasan kajian pustaka terkait *research question* atau *problem statement*, boleh ditambah teori pendukung dari buku teks, jurnal, tesis, atau TA lain dengan teknik acuan yang jujur. [TP hlm. 6]
- Bab 3: pilih judul "Perancangan Sistem" (diagram blok atau *flowchart* beserta penjelasan, rencana kebutuhan data, praproses, skenario pengujian) atau "Alur Pemodelan" (alur pembuatan model, tahapan menurut metode, metode dan skenario pengujian). [TP hlm. 8]
- Daftar Pustaka: minimal 10 referensi, semuanya diacu di teks; minimal 3 referensi yang menjadi dasar gap berasal dari 5 tahun terakhir dan terbit di jurnal terindeks Scopus/WoS dan/atau SINTA 1 atau 2; bernomor menurut urutan kemunculan di teks. [TP hlm. 9]
- Lampiran: data pendukung, CV pembimbing dari luar Telkom University. [TP hlm. 10]
- Subbab petunjuk "Percetakan Proposal Tugas Akhir" dan "Kaidah Penulisan" di Bab 2 templat adalah panduan bagi penulis. Ganti dengan isi kajian pustaka, jangan dipertahankan.

### Kaidah bahasa [TP hlm. 6-7]
- Bahasa Indonesia baku dengan kalimat utuh, singkat, dan jelas, mengikuti kelaziman disiplin ilmu.
- Tanpa kata ganti orang, terutama orang pertama (saya, kami), kecuali di kutipan. Susun kalimat tanpa perlu kata ganti.
- Kata terakhir di dasar halaman tidak dipenggal. Pemenggalan kata asing mengikuti kamus bahasa itu.
- Acuan bahasa: pedoman ejaan resmi (kini EYD edisi V), Pedoman Umum Pembentukan Istilah, KBBI.

## Buku TA [TB]

### Halaman dan huruf
- Kertas A4 HVS putih 80 g, dicetak satu sisi. Margin kiri 4 cm (termasuk 1 cm jilid), kanan, atas, dan bawah 3 cm. Jarak header dan footer 1,25 cm. [TB hlm. 25; TB xml]
- Huruf Times New Roman, Calibri, atau Aptos 12 pt, rata kiri-kanan, spasi 1,5, tinta hitam pekat dan seragam. [TB hlm. 25] Isi templat memakai huruf tema Aptos (tanpa huruf langsung pada run), spasi 1,5, dan spasi sesudah paragraf 6 pt. [TB xml] Pilih satu huruf dan pakai konsisten.
- Abstrak dan *abstract*: 11 pt, maksimal 200 kata. [TB hlm. 6, 8; TB xml]

### Heading
- Judul bab (Heading 1): "BAB n" lalu judul berhuruf kapital, 14 pt tebal, hitam, rata tengah, huruf tema judul (Aptos Display). Nomor "BAB %1" otomatis dari daftar bernomor. [TB xml]
- Judul halaman awal dan akhir (LEMBAR PENGESAHAN, LEMBAR ORISINALITAS, ABSTRAK, ABSTRACT, KATA PENGANTAR, UCAPAN TERIMA KASIH, DAFTAR ISI, DAFTAR GAMBAR, DAFTAR TABEL, DAFTAR PUSTAKA, LAMPIRAN) memakai Heading 1 tanpa nomor. [TB xml]
- Subbab ("1.1.") dan sub-subbab ("2.2.1."): paragraf `List Paragraph` bernomor, tebal, 12 pt, indentasi kiri 1 cm gantung 1 cm, spasi 1,5. Templat tidak memakai Heading 2 atau 3; gaya itu terdefinisi biru dan tidak dipakai. [TB xml]
- Karena subbab bukan Heading 2/3, Daftar Isi otomatis tidak menangkapnya. Bila Daftar Isi dibuat otomatis, ubah gaya Heading 2/3 agar tampil sama (12 pt tebal hitam bernomor) lalu pakai gaya itu. Laporkan pilihan ini ke pengguna.

### Halaman awal dan penomoran
- Urutan halaman awal: Sampul, Lembar Pengesahan (pembimbing I dan II, Ketua Program Studi), Lembar Orisinalitas, Abstrak, Abstract, Kata Pengantar, Ucapan Terima Kasih, Daftar Isi, Daftar Gambar, Daftar Tabel. [TB hlm. 1-15]
- Sampul simetris rata tengah. Judul tanpa singkatan kecuali yang lazim di bidangnya (contoh MIMO, WLAN), tidak berbentuk kalimat tanya, dan tanpa tanda baca penutup. [TB hlm. 26] Judul sampul 16 pt tebal berhuruf kapital; prodi, fakultas, universitas, kota, dan tahun 16 pt tebal. [TB xml]
- Lembar Orisinalitas menyatakan TA adalah karya sendiri dan produknya bukan hasil *Generative AI*. [TB hlm. 5; TJ hlm. 3] Lihat "Pertentangan yang diketahui".
- Kata Pengantar: syukur, penjelasan singkat topik, terima kasih, harapan manfaat, permohonan maaf. [TB hlm. 9]
- Nomor halaman: angka Romawi kecil untuk halaman awal (sampul dihitung, tidak dicetak), angka Arab mulai 1 pada BAB 1 sampai Daftar Pustaka, tanpa imbuhan. Dalam templat, keduanya berada di footer kanan bawah, 1,25 cm dari tepi bawah. [TB xml; TB hlm. 25-26]

### Struktur bab
- BAB 1 Pendahuluan: 1.1 Latar Belakang, 1.2 Rumusan Masalah, 1.3 Tujuan dan Manfaat, 1.4 Batasan Masalah, 1.5 Metode Penelitian, 1.6 Jadwal Pelaksanaan. [TB hlm. 11, 16-21]
- Latar Belakang wajib memuat: kondisi umum yang mendukung, kondisi bidang spesifik, masalah di bidang itu, penyebab, perilaku, dan dampak masalah, solusi yang mungkin, solusi pilihan beserta alasannya, deskripsi singkat solusi usulan, dan keunggulan solusi dibanding solusi lain. Lengkapi dengan survei, berita, atau laporan ilmiah. [TB hlm. 16-17]
- Rumusan Masalah: masalah dirumuskan menjadi satu atau beberapa pernyataan ringkas. Setiap masalah punya jawaban di model sistem, lampiran, analisis, atau kesimpulan. Bukan kendala teknis pengerjaan. Bentuknya kalimat tanya atau kalimat positif berkonotasi negatif; pilih satu dan konsisten. [TB hlm. 17-18]
- Tujuan: kondisi yang hendak dicapai, terukur dengan metrik evaluasi, ditulis naratif. Tujuan menentukan skenario eksperimen, dan kesimpulan selaras dengan tujuan. Tabel 1.1 templat (No, Tujuan, Pengujian, Kesimpulan) memperlihatkan pemetaan satu lawan satu. [TB hlm. 18-19]
- Batasan Masalah: penyederhanaan karena keterbatasan waktu satu semester, data, atau kemampuan; tiap batasan diberi alasan; batasan yang sah bisa dilonggarkan di Saran; batasan yang sudah tercermin di judul tidak perlu. [TB hlm. 19-20]
- Metode Penelitian: pendekatan studi literatur, pengukuran empirik, analisis statistik, simulasi, perancangan, implementasi. Jadwal Pelaksanaan memuat *milestone* (Tabel 1.2). [TB hlm. 20-21]
- BAB 2 Tinjauan Pustaka: uraian pemahaman penulis atas teori (bukan salin-tempel), berisi sistem, cara kerja, metode, algoritme, pendekatan, dan kasus penerapan. Bukan spesifikasi alat (board, komponen, sensor, aktuator). Dibagi menurut 3 sampai 5 bidang ilmu. Tiap topik: teori, asal dan pengembangannya, komponen, diagram, cara kerja, tempat biasa dipakai, dan konfigurasi yang cocok untuk penelitian ini. [TB hlm. 22-23]
- BAB 3 Perancangan Sistem: desain perancangan, diagram blok, fungsi dan fitur, desain perangkat keras dan lunak. [TB hlm. 42]
- BAB 4 Hasil Percobaan dan Analisis: skenario percobaan, hasil percobaan, analisis, masing-masing per skenario. [TB hlm. 43]
- BAB 5 Kesimpulan dan Saran: kesimpulan naratif satu sampai dua paragraf yang menyatakan ketercapaian Tujuan Bab 1 dan menjadi bahan abstrak; saran untuk pengembangan berikutnya. [TB hlm. 44]
- Lampiran: kode sumber dan tabel pendukung yang kurang relevan untuk badan bab. [TB hlm. 46]

### Abstrak [TB hlm. 6-7]
- Memuat permasalahan, tujuan, metode, hasil, dan kesimpulan; empat sub-bagian apa, mengapa, bagaimana, hasil utama (judul sub-bagian boleh digarisbawahi).
- Bagaimana biasanya bagian terpanjang. Hasil utama dua sampai tiga kalimat. Kontribusi boleh ditulis di antara solusi dan hasil.
- Abstrak laporan tidak menyalin abstrak proposal dan tidak memakai kata "akan".
- Tanpa sitasi, tanpa simbol atau istilah teknis berkode. Kata kunci maksimal enam, huruf kecil kecuali singkatan, diambil dari judul dan abstrak.

### Gambar, tabel, persamaan [TB hlm. 26-28; TB xml]
- Caption gambar di bawah gambar, caption tabel di atas tabel. Nomor "Bab.urutan" (Gambar 2.1, Tabel 2.1).
- Caption memakai gaya `Caption`: 9 pt tebal hitam rata tengah, bentuk "Tabel 1.1. Judul kalimat biasa." dengan medan `STYLEREF 1 \s` dan `SEQ`. Teks petunjuk menyebut nomenklatur tebal diikuti dua spasi; templat memakai titik dan satu spasi (format nyata menang).
- Setiap gambar dan tabel dirujuk di kalimat sebelum atau sesudahnya, lalu dijelaskan maksud dan tujuannya setelah disisipkan.
- Isi tabel contoh 10 pt.
- Persamaan memakai Equation Word, nomor "(2.1)" rata kanan, lalu setiap simbol dijelaskan dan maksud persamaan diuraikan.

### Kutipan dan referensi [TB hlm. 28-30, 39-41, 45]
- Kutipan langsung: apa adanya, bertanda kutip, nomor referensi [n] di awal atau akhir, bahasa asing dimiringkan, bagian yang dihilangkan diganti tiga titik (empat di akhir kalimat). Utamakan kutipan tidak langsung (parafrase + [n]).
- Minimal 5 referensi ber-ISSN atau ber-ISBN.
- Daftar Pustaka format IEEE, gaya paragraf `references`: nomor otomatis "[n]" dengan indentasi gantung, rata kiri-kanan, Times New Roman. Penulis sampai enam disebut semua; lebih dari enam boleh "et al." setelah penulis pertama.
- Templat juga memuat aturan catatan kaki (ibid, op. cit., loc. cit.). Lihat "Pertentangan yang diketahui".

### Kaidah bahasa [TB hlm. 23-24]
- Kalimat sederhana dan lengkap (SPOK), maksimal tiga baris. Hindari kalimat majemuk panjang dengan "yang" berulang.
- Kalimat efektif tanpa bahasa berbunga; kalimat tanpa subjek adalah frasa, bukan kalimat.
- Tanda baca menempel pada kata (titik atau koma tidak tertinggal sendirian di awal baris).
- Pakai padanan Indonesia yang benar (bukan "eksisting" untuk *existing*; periksa KBBI). Padanan yang terasa asing (tunak, mangkus, sangkil) boleh diganti istilah aslinya. Istilah asing yang tidak diterjemahkan dicetak miring.

## Jurnal TA [TJ]

### Halaman dan huruf (teks petunjuk menang)
- A4, empat sampai delapan halaman, satu spasi, satu baris kosong antarbagian (judul-penulis, penulis-abstrak, abstrak-kata kunci, subbab-isi). Margin 25 mm semua sisi, header dan footer 15 mm, naskah tanpa header dan footer. [TJ hlm. 4]
- Huruf Times New Roman. [TJ xml] Judul 12 pt tebal; nama penulis 10 pt; abstrak maksimal 200 kata 10 pt; judul bagian 10 pt tebal bernomor "1.", "2."; isi 10 pt. [TJ hlm. 4]
- Caption tabel "Tabel 1." di atas tabel dan "Gambar 1" di bawah gambar, bernomor urut tanpa nomor bab, 10 pt tebal rata tengah. [TJ hlm. 6; TJ xml]

### Penulis
- Nama lengkap. Mahasiswa penulis pertama, pembimbing penulis kedua dan ketiga, maksimal empat penulis. Afiliasi "Fakultas Informatika, Universitas Telkom" (bukan nama prodi). Email institusi. Pembimbing luar memakai afiliasi dan email institusinya. Gelar pembimbing ditulis benar. [TJ hlm. 5]

### Struktur dan panjang
- Halaman awal: sampul, Lembar Pengesahan, Lembar Pernyataan (orisinalitas, bukan produk *Generative AI*). [TJ hlm. 1-3]
- Isi: Abstrak, Pendahuluan, Studi Terkait, Sistem yang Dibangun, Evaluasi, Kesimpulan, Daftar Pustaka, Lampiran. [TJ hlm. 5]
- Pendahuluan 1,5 sampai 2 halaman (untuk naskah 8 halaman): Latar Belakang, Topik dan Batasannya, Tujuan, Organisasi Tulisan. Bukan salinan abstrak; tanpa penjelasan "bagaimana" solusi. Berbeda dari proposal: lebih pendek, Rencana Kegiatan diganti metodologi, ada Organisasi Tulisan, tanpa jadwal. [TJ hlm. 5-6]
- Studi Terkait sekitar setengah halaman, maksimal 1,5 halaman: sumber kredibel (jurnal dan konferensi bereputasi, buku teks). Hindari Wikipedia, blog, materi kuliah, dan TA mahasiswa kecuali untuk hal spesifik seperti basis data yang dibangun TA terdahulu. [TJ hlm. 6-7]
- Sistem yang Dibangun: judul bagian spesifik sesuai topik, bukan generik. Uraikan data beserta sampelnya, metrik evaluasi beserta alasan memilihnya. [TJ hlm. 7]
- Evaluasi: Hasil Pengujian (hasil utama dulu, pembanding/*baseline* di lingkungan dan dataset yang sama) dan Analisis Hasil Pengujian (pengaruh parameter, jenis data, ambang, subsistem). TA S1 tidak dituntut mengalahkan *baseline*, tetapi dituntut analisis lengkap. [TJ hlm. 7]
- Kesimpulan dan Saran: hanya dari hasil pengujian dan analisis, selaras dengan seluruh tujuan. [TJ hlm. 7]
- Sitasi "[1]" atau "[2,3]"; semua sitasi ada di Daftar Pustaka dan sebaliknya. [TJ hlm. 7]

## Pertentangan yang diketahui

Laporkan butir yang relevan ke pengguna saat mengerjakan bagian terkait. Pilihan pengguna dicatat di aturan proyek.

| No | Pertentangan | Pilihan bawaan skill |
|---|---|---|
| 1 | [TP] teks: isi "1 spasi" [TP hlm. 6]; paragraf templat: spasi 1,5 [TP xml] | Spasi 1,5 (format nyata) |
| 2 | [TP] teks: "batas atas, kiri dan bawah 3 cm" [TP hlm. 6]; maksudnya kanan, sesuai margin docx | Atas, kanan, bawah 3 cm |
| 3 | [TP] teks: semua isi 12 pt [TP hlm. 6]; gaya `Caption` 9 pt tetapi tidak dipakai di templat [TP xml] | Tidak ada contoh terformat: tanyakan ke pengguna |
| 4 | [TP] daftar pustaka: teks "1 spasi dalam satu pustaka, 1,5 spasi antarpustaka" [TP hlm. 9]; contoh pustaka di templat berspasi 1,5 seperti isi [TP xml] | Laporkan; ikuti pilihan pengguna |
| 5 | [TP] contoh pustaka "Ludeman, L. C., 1987, ..." bergaya penulis-tahun [TP hlm. 9]; [TB] mewajibkan IEEE [TB hlm. 39]; slide menganjurkan IEEE [W05 s67] | IEEE bernomor menurut kemunculan |
| 6 | [TP] abstrak memuat "hipotesa awal" [TP hlm. 3]; Hipotesis di Bab 1 opsional [TP hlm. 5] | Ikuti keputusan proyek; bila tidak ada, tanyakan |
| 7 | [TB] teks: Romawi di tengah bawah 2,5 cm, Arab di kanan atas 1,5 cm, halaman pertama bab di tengah bawah [TB hlm. 25-26]; templat: semua nomor di footer kanan bawah 1,25 cm, tanpa header [TB xml] | Footer kanan bawah (format nyata) |
| 8 | [TB] teks: nomenklatur tabel tebal + dua spasi [TB hlm. 27]; templat: "Tabel 1.1." + satu spasi, seluruh caption tebal [TB xml] | Format templat |
| 9 | [TB] aturan catatan kaki (ibid, op. cit., loc. cit.) [TB hlm. 30-39] berdampingan dengan sitasi IEEE bernomor [TB hlm. 28-29] | Sitasi IEEE; catatan kaki hanya untuk keterangan tambahan |
| 10 | [TJ] Daftar Pustaka: unsur "nama akhir, nama awal. tahun. judul. tempat. penerbit." dan urutan boleh menurut abjad [TJ hlm. 7, 9]; [TB] dan slide: IEEE urut kemunculan | Tanyakan ke pembimbing atau pengguna; bawaan IEEE |
| 11 | Lembar Orisinalitas [TB hlm. 5; TJ hlm. 3] menyatakan produk TA bukan hasil *Generative AI*; slide Tips membolehkan bantuan gen-AI asal dibaca ulang [Tips s9] | Templat menang. Ingatkan pengguna bahwa pernyataan yang ditandatangani itu mengikat, dan sarankan memeriksa kebijakan AI prodi atau pembimbing |
| 12 | [TB] huruf "TNR/Calibri/Aptos" [TB hlm. 25]; [TP] hanya TNR [TP hlm. 6] | Proposal TNR; buku TA satu huruf konsisten (TNR bila proposal TNR) |
| 13 | [TB] referensi minimal 5 ber-ISSN/ISBN [TB hlm. 30]; [TP] minimal 10 dengan 3 terindeks [TP hlm. 9] | Proposal ikut [TP]; laporan memenuhi keduanya |

## Pemeriksaan format sebelum selesai

Jalankan `scripts/cek_format.py` (lihat `references/menerapkan-format-docx.md`) lalu render PDF dan lihat halamannya. Format dianggap selesai bila setiap butir di bawah ini terpenuhi atau dilaporkan sebagai pertentangan:

- [ ] Ukuran kertas dan margin setiap bagian halaman sesuai templat.
- [ ] Huruf dan ukuran isi, heading, caption, abstrak, dan tabel sesuai templat; heading berwarna `auto`, bukan biru.
- [ ] Spasi baris dan spasi antarparagraf sama di seluruh isi.
- [ ] Nomor halaman sesuai jenis dokumen (Romawi/Arab, letak, sampul tanpa nomor).
- [ ] Caption tabel di atas, caption gambar di bawah, bernomor urut, dan dirujuk di teks.
- [ ] Teks petunjuk templat sudah diganti isi; tidak ada sisa "<Nama Prodi>", "113xxxxxx", atau kalimat petunjuk.
- [ ] Daftar pustaka bernomor, urut kemunculan, semua diacu, dan jumlahnya memenuhi syarat templat.
