---
name: metopen-ta
description: "Aturan Metopen dan templat resmi FIF Telkom untuk Tugas Akhir (TA, skripsi), bertag sumber. Muat saat menulis, merevisi, memformat, atau memeriksa proposal, buku TA, jurnal TA, atau slide sidang: format dan tata letak (margin, huruf, ukuran, spasi, heading, caption, nomor halaman), struktur bab, judul, abstrak, Pendahuluan (Latar Belakang, Perumusan Masalah, Tujuan, Batasan), Studi Terkait, evaluasi dan metrik, sitasi dan parafrase, penyuntingan akhir, berkas .docx."
---

Pengetahuan metopen dan templat FIF, dipecah per topik di `references/`. Setiap aturan berakhir dengan tag sumber: `[W06 s15]` untuk slide (deck W06, slide 15), `[TP hlm. 6]`, `[TB hlm. 25]`, `[TJ hlm. 4]` untuk templat Proposal, Buku TA, dan Jurnal TA (halaman PDF hasil render), dan `[TB xml]` untuk fakta dari pengaturan di dalam docx. Peta tag ke berkas dan cara memeriksanya ada di `SUMBER.md`.

## Urutan otoritas

Saat dua sumber bertentangan, yang lebih atas menang:

1. Aturan proyek pengguna (`CLAUDE.md`, `AGENTS.md`, atau catatan proyek lain yang memuat keputusan penulisan).
2. Templat resmi fakultas di `templates/` (aturan di `references/format-dokumen.md`). Di dalam templat Proposal dan Buku TA, pengaturan docx menang atas teks petunjuk; di templat Jurnal TA, teks petunjuk yang menang.
3. Slide kuliah.
4. Pola TA terbit (`references/pola-ta-terbit.md`): praktik teramati sebagai contoh, bukan aturan.

Baca aturan proyek lebih dulu bila ada. Pertentangan antara slide, templat, dan aturan proyek dilaporkan ke pengguna beserta pilihan bawaan skill, juga saat pengguna meminta mengikuti slide sepenuhnya. Sarankan mencatat keputusan pengguna di aturan proyek.

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

Menulis atau merevisi satu bagian membaca berkas isinya ditambah bagian jenis dokumen yang sesuai di `format-dokumen.md`, karena templat juga mengatur isi tiap bab. Pemeriksaan akhir selalu menyertakan `checklist-editing.md` dan daftar "Pemeriksaan format sebelum selesai" di `format-dokumen.md`.

## Cara memakai aturan

- Terapkan setiap aturan di berkas yang dibaca pada bagian yang sedang dikerjakan, lalu sebutkan tag sumbernya saat menjelaskan alasan perubahan kepada pengguna.
- Sebut sesuatu "keputusan proyek" hanya setelah menemukan barisnya di aturan proyek. Aturan yang hanya ada di templat atau slide adalah bawaan skill. Hal yang tidak diatur di mana pun dilaporkan ke pengguna.
- Format dokumen mengikuti templat kecuali aturan proyek menyatakan lain. Gaya bahasa mengikuti templat dan slide, lalu aturan proyek.
- Sebelum finalisasi dokumen, ingatkan pengguna menjalankan pemeriksaan kemiripan kampus bila diwajibkan.
