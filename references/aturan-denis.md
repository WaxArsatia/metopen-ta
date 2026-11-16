<!--
Preset "aturan Denis": keputusan proyek TA dari satu penulis, sebagai bawaan yang bisa diganti.
Cara pakai:
- Pemicu: pengguna menulis "ikuti aturan denis". Agen membaca berkas ini sebagai aturan proyek.
- Simpan permanen: salin ke berkas instruksi proyek yang dibaca agen Anda (AGENTS.md, CLAUDE.md, GEMINI.md, atau sejenisnya), isi setiap [ISI: ...], lalu hapus komentar ini.
- Hapus butir bertanda (OPSIONAL) bila tidak relevan. Ganti isi bawaan sesuai keputusan Anda dan pembimbing.
Berkas ini memuat aturan generik (berlaku untuk mahasiswa FIF mana pun) dan keputusan pribadi. Keputusan pribadi bertanda [ISI: ...] atau "konfirmasi dulu". Aturan format dasar, tata letak, dan struktur bab ada di berkas lain di skill.
-->

# Tugas Akhir dan Proposal TA

[ISI: nama], NIM [ISI: NIM], [ISI: program studi, fakultas, universitas]. Topik: *[ISI: judul]*. Calon pembimbing 1: [ISI: nama]. Calon pembimbing 2: [ISI: nama atau "belum ditetapkan"].

Keputusan di berkas ini menang atas templat dan slide. Konflik antara slide dan berkas ini dilaporkan ke pengguna, lalu keputusannya dicatat di sini. Satu pengecualian ada di bagian berikut.

## Prinsip otoritas (keputusan pengguna, 2026-11-16)

- Praktik TA terbit bimbingan calon pembimbing menang atas aturan di berkas ini pada butir yang berbeda. Praktik itu terbaca dari abstrak, Bab 1 sampai 3, dan artikel TA yang sama, dan tercatat di bagian "Pola TA satu pembimbing" di `references/pola-ta-terbit.md` [OL].
- Prinsip ini berlaku per butir. Butir yang tidak dibahas pola itu tetap mengikuti berkas ini, lalu templat, lalu slide.
- Menang tidak berarti otomatis mengubah. Bila penerapan pola membalik keputusan yang sudah tercatat di berkas ini, agen melaporkan daftar butirnya ke pengguna sebelum mengubah apa pun. Lima perbedaan sudah ditinjau pada 2026-11-16 dan preset tetap menang, jadi tidak perlu dilaporkan lagi: (1) Perumusan Masalah tanpa nama metode, (2) Latar Belakang 3 sampai 4 sitasi dengan satu penanda per sumber, (3) Bab 2 lebih panjang dari Bab 1, (4) alasan wajib pada setiap butir Batasan, dan (5) tanpa tabel keterkaitan Tujuan, Pengujian, dan Kesimpulan. Perbedaan lain yang belum ditinjau tetap dilaporkan dulu.
- Pola di `pola-ta-terbit.md` berasal dari TA bimbingan satu calon pembimbing. Bila calon pembimbing 1 pengguna berbeda, konfirmasi dulu apakah pola itu berlaku.
- Setiap butir di bawah yang berasal dari TA terbit menyebut sebarannya. Butir yang hanya mewakili minoritas sampel dicatat sebagai gaya satu TA, bukan sebagai kebiasaan umum.

## Alur kerja

1. Baca format, tata letak, struktur bab, dan cara mengedit docx dari berkas skill `metopen-ta` sesuai tabel penunjuknya, tidak diulang di sini.
2. Baca sumber: [ISI: folder paper, data, dan hasil eksperimen] dan [ISI: berkas catatan lanjutan, OPSIONAL]. Paper dan data yang saling bertentangan dilaporkan ke pengguna, bukan dipilih sendiri.
3. Tulis atau ubah pada salinan templat `[ISI: nama berkas proposal]`. Templat asli tetap utuh.
4. Jalankan skill `humanizer` pada prosa yang berubah. Bila tidak terpasang, sunting sendiri pola tulisan khas AI: kontras "bukan X melainkan Y", daftar tiga yang dipaksakan, dan kata klise. Fakta, angka, sitasi, dan format tetap.
5. Setelah isi berubah, periksa relevansi dan konsistensi seluruh dokumen: rumusan, tujuan, skenario Bab 3, abstrak, sitasi, dan istilah.
6. Bangun ulang PDF dari docx (perintah di `references/menerapkan-format-docx.md`) setiap docx berubah, supaya kedua versi sama.
7. Periksa dengan daftar "Siap diserahkan" di bagian akhir.

## Gaya tulis

- Bahasa Indonesia baku (EYD edisi V). Pakai padanan Indonesia bila ada. Istilah asing tanpa padanan dicetak miring. Desimal memakai koma.
- Kalimat aktif, singkat, dan jelas. Subjek tak berpronomina (tanpa saya atau kami). Kalimat dari paper berbahasa Inggris ditulis ulang.
- Pemisah klausa memakai koma, titik, atau tanda kurung. Em dash dan en dash tidak muncul di badan teks.
- Setiap klaim dan angka bersumber dari paper, data, atau referensi. Keterbatasan penelitian dinyatakan.
- Bagian, tabel, dan gambar hanya yang diminta templat, ditambah pengecualian di bagian Bab 2 dan Bab 3 di bawah. Teks petunjuk templat diganti isi, bukan ditambah. Subbab petunjuk untuk penulis dihapus saat bab diisi.

## Format dan tata letak

Angka dan cara pengaturannya ada di `format-dokumen.md` dan `menerapkan-format-docx.md`. Preset hanya menambah keputusan berikut.

- Caption tabel di atas tabel, caption gambar di bawah gambar. Setiap tabel dan gambar dirujuk di teks.
- Tabel dan caption tidak terbelah antarhalaman: baris tidak terbelah, `keepNext` pada caption dan semua baris.
- Pemenggalan halaman rapi: tidak ada judul atau kalimat pengantar daftar sendirian di dasar halaman, dan tidak ada baris yatim atau janda.
- Heading baru menyalin run heading templat, bukan membuat run baru.

## Bab 1

- Urutan: Latar Belakang, Perumusan Masalah, Tujuan, Batasan Masalah (Heading 2), Rencana Kegiatan, Jadwal Kegiatan. Hipotesis: [ISI: ya atau tidak].
- Latar Belakang berisi 4 paragraf, minimal 1 halaman, dengan 3 sampai 4 sitasi:
  1. Umum, dengan data atau fakta bersitasi.
  2. Penelitian mutakhir dan masalahnya.
  3. Penelitian lain dan celahnya, ditambah 1 kalimat tentang kesulitan membuat solusi.
  4. Usulan, 1 kalimat kontribusi utama, dan metode sekilas dalam 1 sampai 3 kalimat tanpa parameter (rincian di Bab 3), beserta alasan memilih metode dalam 1 sampai 2 kalimat.
- Input dan output disebut eksplisit satu kali, di paragraf 1 atau 4. Istilah judul dijelaskan saat pertama muncul.
- Perumusan Masalah berupa kalimat pengantar singkat dan daftar bernomor berkalimat tanya, tanpa paragraf sesudahnya. Isinya hanya masalah, jadi nama metode, model, atau alat tidak masuk. Kata kerja Bloom tidak dipakai di sini.
- Tujuan berupa daftar bernomor tanpa paragraf sesudahnya. Setiap butir diawali satu kata kerja Taksonomi Bloom revisi level [ISI: level, bawaan C4 sampai C5 untuk S1] (C4: menganalisis, membedakan; C5: mengevaluasi, memeriksa), dan menyebut metrik atau kriteria keberhasilan. Kata kerja di luar proses kognitif Bloom (misalnya "mengukur") dan kata kerja berlevel berbeda (misalnya "menentukan", "membandingkan") tidak menjadi kata kerja utama; keduanya boleh muncul sebagai maksud. Kata kerja diganti tanpa mengubah isi terukurnya. Level dan pilihan kata kerja dilaporkan di balasan, bukan di dokumen. Kata kerja Bloom tidak diterapkan pada label tabel Jadwal Kegiatan.
- Rumusan dan Tujuan dipasangkan satu lawan satu: nomor dan urutan sama. Mengubah salah satu berarti memeriksa pasangannya dan skenario pengujian bernomor sama di Bab 3.
- Batasan Masalah menjadi subbab sendiri (Heading 2) setelah Tujuan dan sebelum Rencana Kegiatan, tidak digabung ke Perumusan Masalah.
  - Jumlah butir 3 sampai 6, mengikuti TA terbit (3 sampai 6 butir pada seluruh sampel, tidak ada yang 8) [OL]. Jumlah tidak dipaksa.
  - Tiap butir menyebut apa yang dikerjakan dan dibatasi, lalu alasannya: keterbatasan waktu, data, atau kemampuan [W06 s13-15]. Alasan ini tidak lazim di TA terbit, jadi preset menjaganya sebagai keputusan sendiri.
  - Tiap butir lolos uji *future work* dan tidak mengulang judul [W06 s16-18].
  - Butir baru ditambahkan di akhir supaya rujukan "butir n" di Bab 3 tidak bergeser.
- [ISI: bila pembimbing meminta Tujuan berbentuk narasi, ganti butir "Tujuan berupa daftar bernomor" di atas.]

## Sitasi dan Daftar Pustaka

- Gaya IEEE, bernomor menurut urutan kemunculan, satu penanda [n] per sumber, nomor tetap di seluruh dokumen. Di Latar Belakang tiap sumber disitasi satu kali.
- Nama penulis ditulis "Nama dkk. [n]" (tiga penulis atau lebih) atau "A dan B [n]" (dua penulis), tanpa tahun. Entri konferensi memakai gaya IEEE baku ("in Proc.").
- Setiap [n] punya entri, dan setiap entri dirujuk di teks.
- Minimal [ISI: bawaan 10] referensi, dengan minimal [ISI: bawaan 3] jurnal lima tahun terakhir yang terindeks Scopus/WoS atau SINTA 1 atau 2. Kuartil SCImago dicatat pada tahun terbit artikel (Q1 sampai Q4). Status indeks diverifikasi lewat web dengan menyebut sumbernya, dan yang tidak ditemukan ditandai "belum terverifikasi".
- Klaim dikutip setelah PDF sumber diperiksa. Sumber kajian bertinjauan sejawat, bukan prapublikasi.
- Skripsi boleh dikutip di proposal dan buku TA, tetapi tidak dihitung ke syarat minimal dan tidak dimasukkan ke artikel jurnal TA.
- Paper sendiri disitasi: [ISI: ya atau tidak].

## Abstrak dan kata kunci

Ketentuan ini menggantikan butir lama "tiga paragraf".

- Abstrak proposal berupa satu paragraf tanpa judul subbagian, maksimal 200 kata, tanpa sitasi, tanpa hipotesa awal (walaupun templat menyebutnya), dengan lima unsur berurutan:
  1. Latar belakang, 1 kalimat.
  2. Masalah, 1 kalimat yang diawali "Namun,".
  3. Tujuan, 1 kalimat yang diawali "Tugas Akhir ini mengusulkan".
  4. Metode, beberapa kalimat, dengan masukan dan keluaran disebut.
  5. Harapan hasil, tanpa klaim hasil.
- Buku TA menambah satu kalimat hasil utama di akhir paragraf, bukan paragraf baru.
- Dasar dari TA terbit [OL]: satu paragraf pada 5 dari 7 abstrak; "Namun" memisahkan latar belakang dan masalah pada 3 dari 7; pembuka "Penelitian ini mengusulkan" pada 6 dari 7, dan "Tugas Akhir ini" adalah adaptasi dari pembuka itu; panjang 132 sampai 239 kata, dengan 3 dari 7 melampaui 200, sehingga batas 200 kata mengikuti slide [W05 s4].
- Kata kunci tepat 5, semua huruf kecil, memakai kepanjangan tanpa singkatan, nama diri tetap berkapital, istilah asing dicetak miring, dan memuat istilah penting judul. Lima butir dipakai pada 4 dari 7 TA terbit; gaya huruf kecil dan kepanjangan mengikuti satu TA (gaya hampir sama pada TA kedua), sedangkan TA lain memakai singkatan atau kapital awal [OL].
- Preset ini berbeda dari slide pada dua hal: paragraf tunggal (slide: empat paragraf atau subbagian untuk TA FIF [W05 s4]) dan kata kunci tanpa singkatan (slide: huruf kecil kecuali singkatan [W05 s17]). Keduanya mengikuti prinsip otoritas di atas.

## Bab 2

- Bab 2 mengikuti materi W07 penuh: konsep dasar, metode yang ada, dataset, baseline, dan metrik pada pustaka. Bab 2 lebih panjang dari Bab 1 dilaporkan ke pengguna. Batas sekitar 15% halaman [W07 s6] berlaku untuk Studi Terkait artikel, jadi Bab 2 diringkas saat menyusun jurnal TA, bukan di proposal.
- Subbab konsep dasar memuat [ISI: data atau sinyal yang diolah dan daftar arsitektur atau metode dasar] dari sumber yang PDF-nya sudah diperiksa. Tiap ulasan bersumber dari referensi yang PDF-nya sudah diperiksa, dan sumbernya bertinjauan sejawat.
- Subbab kajian literatur memuat tabel kajian literatur beserta pembahasan sintesisnya. Tabel dibagi dua supaya tiap tabel muat satu halaman: Tabel 2.1 artikel jurnal, Tabel 2.2 skripsi.
  - Enam kolom isi tetap: Pustaka Utama, Rumusan Masalah, Tujuan atau Ide Pokok, Metode atau Algoritme, Kelebihan dan Kekurangan, Relasi dengan Topik TA. Tanpa label "Bobot" dan tanpa kolom pemisah.
  - Huruf tabel 10 pt, pengecualian dari 12 pt karena enam kolom pada lebar teks.
  - Sel tanpa kata ganti orang pertama dan memakai nomor sitasi dokumen. Kolom Kekurangan hanya menilai terhadap tujuan penelitian aslinya. Kebutuhan TA ini masuk kolom Relasi.
  - Ulasan skripsi bersumber dari teks lengkap (Bab 1 sampai 5 dan daftar pustaka). [ISI: tempat berkas skripsi dan tabel kajian literatur dari kelas, bila ada.]
- Subbab metrik di Bab 2 bersifat deskriptif tanpa rumus. Rumus ada di Bab 3.

## Bab 3

- Bab 3 berjudul Perancangan Sistem. Isinya diagram alur atau blok, rencana perangkat keras dan lunak, metode secara ringkas, dataset beserta alasan pemilihan, baseline atau pembanding beserta alasannya (atau pernyataan bahwa tidak ada), rencana data, skenario pengujian, metrik beserta alasan, dan rencana analisis.
- Detail data dan eksperimen hanya ditulis di Bab 3, sedangkan Rencana Kegiatan di Bab 1 hanya menyebut tahap. Setiap Tujuan punya satu skenario pengujian di Bab 3 dengan nomor sama. Saat Tujuan berubah, skenarionya diperiksa.
- Tautan repositori data ditulis di teks Bab 3, bukan di Daftar Pustaka [W09 s8].
- Teks tidak menyiratkan model berjalan di mikrokontroler bila mikrokontroler hanya dipakai untuk akuisisi data.
- Gambar dan tabel di Bab 3 (pengecualian dari "hanya yang diminta templat"):
  - Gambar 3.1 berupa diagram alur tahapan (flowchart), Gambar 3.2 berupa arsitektur sistem.
  - Satu algoritma (*pseudocode*) bernomor "Algoritma 1" tanpa nomor bab, dengan caption di atas. Isinya Input dan Output (atau Require dan Ensure), lalu langkah bernomor, sekitar 10 sampai 20 baris.
  - Tabel kerangka hasil utama [W09 s6]: baris tiap model atau arsitektur, kolom metrik utama pada validasi dan uji, sel berisi "… ± …".
  - Persamaan bernomor "(3.n)" rata kanan di subbab metrik dan praproses, dengan penjelasan setiap simbol.
- Dasar dari TA terbit [OL]: Gambar 3.1 berupa alur dan Gambar 3.2 berupa arsitektur sistem pada 6 dari 7 TA; satu algoritma bernomor tanpa nomor bab pada 3 dari 7; persamaan bernomor (3.n) hanya di Bab 3, tidak pernah di Bab 2.

## Slide proposal

- Slide proposal mengikuti isi proposal tanpa hasil dan kesimpulan, dengan aturan tampilan W13 (`references/presentasi-sidang.md`).
- Daftar 10 slide TA di W13 hanya panduan. Contoh rumusan dan tujuan di slide tidak ditiru. Diagram metodologi di slide hanya untuk slide, sedangkan diagram alur dan arsitektur di Bab 3 tetap ada sebagai pengecualian yang tercatat di bagian Bab 3.

## Metrik

- Metrik didefinisikan sekali dan dipakai konsisten: [ISI: definisi, misalnya F1 makro sebagai rerata F1 setiap kelas dan akurasi seimbang sebagai rerata *recall* setiap kelas].
- Definisi ditulis deskriptif di Bab 2 dan dengan rumus di Bab 3.

## Keputusan format dan laporan (konfirmasi dulu)

Keputusan pribadi dari proyek asal. Agen mengonfirmasinya ke pengguna satu kali di awal sesi, lalu mengikuti jawabannya.

- Paragraf isi: spasi sesudah 0 pt, tanpa inden baris pertama. Caption memakai gaya templat buku TA (lihat `format-dokumen.md`, bagian Gambar, tabel, persamaan). Daftar Pustaka memakai format paragraf templat.
- Laporan akhir: buku TA ditambah artikel. [ISI: bentuk yang disetujui pembimbing.]
- Tujuan berupa butir bernomor berkata kerja Bloom di proposal dan buku TA, walaupun templat buku meminta narasi. Dasar: separuh TA terbit memakai butir [OL].
- Deklarasi pemakaian AI: [ISI: ya atau tidak]. Panduan AI Telkom 2025 (bagian 6.1) mewajibkannya dan menilai pemakaian tanpa deklarasi berisiko tinggi, jadi konfirmasi ke pembimbing.
- Placeholder Calon Pembimbing 2 di Lembar Persetujuan tetap sampai pembimbing 2 ditetapkan. (OPSIONAL)

## Siap diserahkan

Dokumen siap bila semua ini benar:

- `humanizer` sudah dijalankan pada setiap prosa yang berubah, dan PDF sama versinya dengan docx.
- `cek_format.py` bersih, atau setiap temuannya sudah dilaporkan.
- Setiap rumusan punya satu Tujuan dan satu skenario Bab 3 bernomor sama.
- Setiap [n] punya entri, setiap entri dirujuk, dan jumlah referensi memenuhi syarat.
- Setiap tabel dan gambar dirujuk di teks, caption di posisi yang benar, dan pemenggalan halaman sudah dilihat di PDF.
- Abstrak maksimal 200 kata dengan 5 kata kunci, dan Batasan Masalah 3 sampai 6 butir beralasan.
- Perbedaan antara preset dan TA terbit yang belum ditinjau (di luar lima yang tercatat di "Prinsip otoritas") sudah dilaporkan ke pengguna.
- Pengguna sudah diingatkan menjalankan pemeriksaan kemiripan kampus bila diwajibkan.
