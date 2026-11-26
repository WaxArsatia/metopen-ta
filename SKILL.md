---
name: metopen-ta
description: "Aturan Metopen dan templat resmi FIF Telkom University untuk Tugas Akhir (TA, skripsi), bertag sumber. Pakai juga saat pengguna menulis \"ikuti aturan denis\". Pakai setiap kali menulis, merevisi, memformat, atau memeriksa proposal TA, buku TA, jurnal TA, atau slide sidang, atau menjawab soal syarat sidang, publikasi, kemiripan, dan pemakaian AI untuk TA, juga saat pengguna hanya menyebut bab, bagian, atau berkas .docx TA tanpa menyebut Metopen atau templat: format dan tata letak (margin, huruf, ukuran, spasi, heading, caption, nomor halaman), struktur bab, judul, abstrak, Pendahuluan (Latar Belakang, Perumusan Masalah, Tujuan, Batasan), Studi Terkait, evaluasi dan metrik, sitasi dan parafrase, penyuntingan akhir."
---

Pengetahuan metopen dan templat FIF, dipecah per topik di `references/`. Setiap aturan berakhir dengan tag sumber: `[W06 s15]` untuk slide (deck W06, slide 15), `[TP hlm. 6]`, `[TB hlm. 25]`, `[TJ hlm. 4]` untuk templat Proposal, Buku TA, dan Jurnal TA (halaman PDF hasil render), dan `[TB xml]` untuk fakta dari pengaturan di dalam docx. Dokumen resmi memakai `[PFIF20]`, `[PU027]`, `[PU026]`, `[KWR175]`, `[AI25]`, dan `[SONIA]`. Peta tag ke berkas dan cara memeriksanya ada di `SUMBER.md`.

## Urutan otoritas

Saat dua sumber bertentangan, yang lebih atas menang:

1. Aturan proyek pengguna (`CLAUDE.md`, `AGENTS.md`, atau catatan proyek lain yang memuat keputusan penulisan).
2. Templat resmi fakultas di `templates/` (aturan di `references/format-dokumen.md`). Di dalam templat Proposal dan Buku TA, pengaturan docx menang atas teks petunjuk; di templat Jurnal TA, teks petunjuk yang menang.
3. Slide kuliah.
4. Pola TA terbit (`references/pola-ta-terbit.md`): praktik teramati sebagai contoh, bukan aturan.

Aturan resmi (`references/aturan-resmi.md`) berperingkat menurut jenis butir: untuk integritas akademik, pemakaian AI, publikasi, dan syarat sidang atau kelulusan, aturan resmi berada di atas templat dan slide; untuk format dan struktur, templat tetap menang. Aturan proyek atau preset yang menyimpang dari butir integritas, AI, publikasi, atau kelulusan tetap keputusan pengguna dan dilaporkan beserta risikonya.

Dengan pemicu "ikuti aturan denis" (bagian berikut), satu penyesuaian berlaku: pada butir yang diatur preset dan berbeda dari praktik TA terbit bimbingan calon pembimbing, praktik TA terbit berada di atas preset (keputusan pengguna 2026-11-16). Butir lain tetap mengikuti urutan di atas. Tanpa pemicu, urutan di atas berlaku apa adanya.

Baca aturan proyek lebih dulu bila ada. Pertentangan antara slide, templat, dan aturan proyek dilaporkan ke pengguna beserta pilihan bawaan skill, juga saat pengguna meminta mengikuti slide sepenuhnya. Sarankan mencatat keputusan pengguna di aturan proyek.

## Aturan Denis (pemicu opsional)

Pengguna yang menulis "ikuti aturan denis" meminta preset keputusan proyek di `references/aturan-denis.md`. Preset ini menempati peringkat 1 di atas, kecuali pengguna sudah punya berkas aturan proyek yang bertentangan dengannya (berkas itu menang) dan kecuali butir yang berbeda dari praktik TA terbit (praktik itu menang, lihat "Prinsip otoritas" di preset).

1. Baca `references/aturan-denis.md` penuh dan bagian "Pola TA satu pembimbing" di `references/pola-ta-terbit.md`, lalu terapkan isinya selama sesi. Bila menerapkan pola itu membalik keputusan yang tercatat di preset, daftar butirnya dilaporkan ke pengguna sebelum mengubah apa pun.
2. Kolom `[ISI: ...]` kosong yang dibutuhkan tugas saat ini ditanyakan ke pengguna sekaligus, sebelum menulis. Kolom bertulisan "bawaan" memakai nilai bawaan bila pengguna tidak menjawab. Bagian "Keputusan format dan laporan" dikonfirmasi satu kali di awal sesi.
3. Setelah kolom terisi, tawarkan menyimpannya ke berkas instruksi proyek yang dibaca agen ini (AGENTS.md, CLAUDE.md, atau sejenisnya), supaya pemicu tidak perlu diulang.
4. Pemeriksa dijalankan dengan `--preset denis`. Tanpa pemicu atau aturan proyek yang memakai preset, opsi itu tidak dipakai.
5. Daftar "Siap diserahkan" di akhir preset ditambahkan pada pemeriksaan akhir skill (`checklist-editing.md` dan "Pemeriksaan format sebelum selesai"). Keduanya dijalankan saat naskah dinyatakan selesai.

## Penunjuk: kerjakan X, baca Y

Baca hanya berkas yang cabangnya sedang dikerjakan.

| Sedang mengerjakan | Baca |
|---|---|
| Format dan tata letak: margin, huruf, ukuran, spasi, heading, caption, nomor halaman, halaman awal, struktur bab per jenis dokumen, pertentangan templat | `references/format-dokumen.md` |
| Menulis ke atau memeriksa berkas `.docx`, membangun PDF | `references/menerapkan-format-docx.md` |
| Isi dan urutan proposal atau laporan, apa yang sudah final di proposal, jenis metode penelitian | `references/struktur-isi.md` |
| Judul, identitas penulis, abstrak, kata kunci | `references/judul-abstrak.md` |
| Latar Belakang, Perumusan Masalah (topik), Batasan, Tujuan | `references/pendahuluan.md` |
| Studi terkait, penelusuran pustaka, kualitas jurnal | `references/studi-terkait.md` |
| Rencana atau hasil pengujian, metrik, analisis | `references/evaluasi.md` |
| Sitasi, format IEEE atau APA, jenis publikasi, parafrase, plagiarisme | `references/sitasi-parafrase.md` |
| Contoh nyata dari TA FIF yang sudah terbit | `references/pola-ta-terbit.md` |
| Menyunting naskah, pemeriksaan akhir sebelum selesai | `references/checklist-editing.md` |
| Slide atau persiapan sidang | `references/presentasi-sidang.md` |
| Syarat sidang dan revisi, bimbingan, jalur publikasi, kemiripan dan plagiarisme, pemakaian AI | `references/aturan-resmi.md` |

Menulis atau merevisi satu bagian membaca berkas isinya ditambah bagian jenis dokumen yang sesuai di `format-dokumen.md`, karena templat juga mengatur isi tiap bab. Pemeriksaan akhir selalu menyertakan `checklist-editing.md` dan daftar "Pemeriksaan format sebelum selesai" di `format-dokumen.md`.

## Alur kerja

1. Baca aturan proyek pengguna bila ada, lalu tentukan jenis dokumen (proposal, buku TA, jurnal TA, slide).
2. Buka berkas referensi sesuai tabel di atas: berkas isi untuk bagian yang dikerjakan dan bagian jenis dokumen di `format-dokumen.md`.
3. Tulis atau periksa naskah. Untuk berkas `.docx`, ikuti `menerapkan-format-docx.md` dan jalankan `scripts/bangun_pdf.sh` (membangun PDF, menjalankan `cek_format.py`, dan membuat lembar kontak).
4. Laporkan ke pengguna: perubahan atau temuan beserta tag sumbernya, pertentangan yang ditemui beserta pilihan bawaan skill, dan hal yang belum diatur di mana pun.

Pekerjaan selesai bila setiap aturan di berkas yang dibaca sudah diterapkan atau dilaporkan sebagai pertentangan, dan pemeriksaan akhir (`checklist-editing.md` serta "Pemeriksaan format sebelum selesai") sudah dijalankan untuk naskah yang akan diserahkan.

## Cara memakai aturan

- Sebut sesuatu "keputusan proyek" hanya setelah menemukan barisnya di aturan proyek. Aturan yang hanya ada di templat atau slide adalah bawaan skill. Hal yang tidak diatur di mana pun dilaporkan ke pengguna.
- Format dan gaya bahasa mengikuti templat lalu slide, kecuali aturan proyek menyatakan lain.
- Sebelum finalisasi dokumen, ingatkan pengguna menjalankan pemeriksaan kemiripan kampus bila diwajibkan.
