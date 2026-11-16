<!--
Preset "aturan Denis": keputusan proyek TA dari satu penulis, sebagai bawaan yang bisa diganti.
Cara pakai:
- Pemicu: pengguna menulis "ikuti aturan denis". Agen membaca berkas ini sebagai aturan proyek.
- Simpan permanen: salin ke berkas instruksi proyek yang dibaca agen Anda (AGENTS.md, CLAUDE.md, GEMINI.md, atau sejenisnya), isi setiap [ISI: ...], lalu hapus komentar ini.
- Hapus butir bertanda (OPSIONAL) bila tidak relevan. Ganti isi bawaan sesuai keputusan Anda dan pembimbing.
Berkas ini memuat keputusan proyek, termasuk beberapa keputusan format. Aturan format dasar, tata letak, dan struktur bab ada di berkas lain di skill.
-->

# Tugas Akhir dan Proposal TA

[ISI: nama], NIM [ISI: NIM], [ISI: program studi, fakultas, universitas]. Topik: *[ISI: judul]*. Calon pembimbing 1: [ISI: nama]. Calon pembimbing 2: [ISI: nama atau "belum ditetapkan"].

Keputusan di berkas ini menang atas templat dan slide. Konflik antara slide dan berkas ini dilaporkan ke pengguna, lalu keputusannya dicatat di sini.

## Alur kerja

1. Baca format, tata letak, struktur bab, dan cara mengedit docx dari berkas skill `metopen-ta` sesuai tabel penunjuknya, tidak diulang di sini.
2. Baca sumber: [ISI: folder paper, data, dan hasil eksperimen] dan [ISI: berkas catatan lanjutan, OPSIONAL]. Paper dan data yang saling bertentangan dilaporkan ke pengguna, bukan dipilih sendiri.
3. Tulis atau ubah pada salinan templat `[ISI: nama berkas proposal]`. Templat asli tetap utuh.
4. Jalankan skill `humanizer` pada prosa yang berubah. Bila tidak terpasang, sunting sendiri pola tulisan khas AI: kontras "bukan X melainkan Y", daftar tiga yang dipaksakan, dan kata klise. Fakta, angka, sitasi, dan format tetap.
5. Bangun ulang PDF dari docx (perintah di `references/menerapkan-format-docx.md`).
6. Periksa dengan daftar "Siap diserahkan" di bagian akhir.

## Gaya tulis

- Bahasa Indonesia baku (EYD edisi V). Istilah asing tanpa padanan dicetak miring. Desimal memakai koma.
- Subjek kalimat tak berpronomina (tanpa saya atau kami). Kalimat dari paper berbahasa Inggris ditulis ulang.
- Pemisah klausa memakai koma, titik, atau tanda kurung. Em dash dan en dash tidak muncul di badan teks.
- Setiap klaim dan angka bersumber dari paper, data, atau referensi. Keterbatasan penelitian dinyatakan.
- Bagian, tabel, dan gambar hanya yang diminta templat. [ISI: pengecualian, misalnya tabel kerangka hasil di Bab 3.]

## Bab 1

- Urutan: Latar Belakang, Perumusan Masalah, Tujuan, Batasan Masalah (Heading 2), Rencana Kegiatan, Jadwal Kegiatan. Hipotesis: [ISI: ya atau tidak]. Setiap butir Batasan menyebut alasannya.
- Latar Belakang berisi 4 paragraf, minimal 1 halaman, dengan 3 sampai 4 sitasi:
  1. Umum, dengan data atau fakta bersitasi.
  2. Penelitian mutakhir dan masalahnya.
  3. Penelitian lain dan celahnya, ditambah 1 kalimat tentang kesulitan membuat solusi.
  4. Usulan, 1 kalimat kontribusi utama, dan metode sekilas dalam 1 sampai 3 kalimat tanpa parameter (rincian di Bab 3), beserta alasan memilih metode dalam 1 sampai 2 kalimat.
- Input dan output disebut eksplisit satu kali, di paragraf 1 atau 4. Istilah judul dijelaskan saat pertama muncul.
- Perumusan Masalah berupa kalimat pengantar singkat dan daftar bernomor berkalimat tanya, tanpa paragraf sesudahnya. Isinya hanya masalah, jadi nama metode, model, atau alat tidak masuk.
- Tujuan berupa daftar bernomor tanpa paragraf sesudahnya. Setiap butir diawali satu kata kerja Taksonomi Bloom revisi level [ISI: level, bawaan C4 sampai C5 untuk S1] (C4: menganalisis, membedakan; C5: mengevaluasi, memeriksa), dan menyebut metrik atau kriteria keberhasilan. Kata kerja diganti tanpa mengubah isi terukurnya. Level dan pilihan kata kerja dilaporkan di balasan, bukan di dokumen.
- Rumusan dan Tujuan dipasangkan satu lawan satu: nomor dan urutan sama. Mengubah salah satu berarti memeriksa pasangannya dan skenario pengujian bernomor sama di Bab 3.
- [ISI: bila pembimbing meminta Tujuan berbentuk narasi, ganti butir "Tujuan berupa daftar bernomor" di atas.]

## Sitasi dan Daftar Pustaka

- Gaya IEEE, bernomor menurut urutan kemunculan, satu penanda [n] per sumber, nomor tetap di seluruh dokumen. Di Latar Belakang tiap sumber disitasi satu kali.
- Nama penulis ditulis "Nama dkk. [n]" (tiga penulis atau lebih) atau "A dan B [n]" (dua penulis), tanpa tahun. Entri konferensi memakai "in Proc.".
- Setiap [n] punya entri, dan setiap entri dirujuk di teks.
- Minimal [ISI: bawaan 10] referensi, dengan minimal [ISI: bawaan 3] jurnal lima tahun terakhir yang terindeks Scopus/WoS atau SINTA 1 atau 2. Kuartil SCImago pada tahun terbit dicatat, status indeks diverifikasi lewat web dengan menyebut sumbernya, dan yang tidak ditemukan ditandai "belum terverifikasi".
- Klaim dikutip setelah PDF sumber diperiksa. Sumber kajian bertinjauan sejawat. Skripsi boleh dikutip, tetapi tidak dihitung ke syarat minimal.
- Paper sendiri disitasi: [ISI: ya atau tidak].

## Bab lain

- Abstrak proposal: tiga paragraf (apa, mengapa, bagaimana) tanpa sitasi dan tanpa paragraf hasil. Buku TA menambah paragraf hasil utama.
- Bab 2 memuat konsep dasar, metode yang ada, dataset, baseline, dan metrik. Bab 2 lebih panjang dari Bab 1 dilaporkan ke pengguna.
- Bab 3 memuat detail data dan eksperimen satu kali saja, sedangkan Rencana Kegiatan di Bab 1 hanya menyebut tahap. Setiap Tujuan punya satu skenario pengujian di Bab 3. Tautan repositori data ditulis di teks Bab 3, bukan di Daftar Pustaka.
- Metrik didefinisikan sekali dan dipakai konsisten: [ISI: definisi, misalnya F1 makro sebagai rerata F1 setiap kelas].

## Keputusan format dan laporan (konfirmasi dulu)

Keputusan pribadi dari proyek asal. Agen mengonfirmasinya ke pengguna satu kali di awal sesi, lalu mengikuti jawabannya.

- Paragraf isi: spasi sesudah 0 pt, tanpa inden baris pertama. Caption memakai gaya templat buku TA ("Tabel 1.1. Judul kalimat biasa."). Daftar Pustaka memakai format paragraf templat.
- Laporan akhir: buku TA ditambah artikel. [ISI: bentuk yang disetujui pembimbing.]
- Deklarasi pemakaian AI: [ISI: ya atau tidak]. Panduan AI Telkom 2025 (bagian 6.1) mewajibkannya dan menilai pemakaian tanpa deklarasi berisiko tinggi, jadi konfirmasi ke pembimbing.
- Placeholder Calon Pembimbing 2 di Lembar Persetujuan tetap sampai pembimbing 2 ditetapkan. (OPSIONAL)

## Siap diserahkan

Dokumen siap bila semua ini benar:

- `humanizer` sudah dijalankan pada setiap prosa yang berubah, dan PDF sama versinya dengan docx.
- `cek_format.py` bersih, atau setiap temuannya sudah dilaporkan.
- Setiap rumusan punya satu Tujuan dan satu skenario Bab 3 bernomor sama.
- Setiap [n] punya entri, setiap entri dirujuk, dan jumlah referensi memenuhi syarat.
- Pengguna sudah diingatkan menjalankan pemeriksaan kemiripan kampus bila diwajibkan.
