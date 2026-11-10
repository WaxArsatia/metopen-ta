---
name: metopen-ta
description: Aturan metodologi penelitian dan tata tulis ilmiah dari materi kuliah Metopen FIF Telkom untuk menulis, merevisi, atau memeriksa proposal dan laporan TA. Muat sebelum menyentuh judul, abstrak, Latar Belakang, Perumusan Masalah, Tujuan, Batasan, Studi Terkait, Evaluasi, sitasi, parafrase, checklist penyuntingan, atau slide sidang.
---

Pengetahuan metopen umum, dipecah per topik di `references/`. Setiap aturan berakhir dengan tag sumber, misalnya `[W06 s15]` (deck W06, slide 15), supaya klaim bisa diperiksa ke slide asli kelas. `SUMBER.md` memetakan kode deck ke topiknya. Tag `(gambar)` berarti isinya hanya terbaca dari render slide.

## Urutan otoritas

Saat dua sumber bertentangan, yang lebih atas menang:

1. Aturan proyek pengguna (`CLAUDE.md`, `AGENTS.md`, atau catatan proyek lain yang memuat keputusan penulisan).
2. Templat resmi program studi atau fakultas.
3. Slide kuliah (referensi ini).

Slide adalah dasar umum, bukan perintah yang menimpa keputusan proyek. Baca aturan proyek pengguna lebih dulu bila ada, lalu pakai referensi di bawah untuk bagian yang belum diatur. Konflik antara slide dan aturan proyek atau templat: laporkan ke pengguna, jangan pilih sendiri, lalu sarankan mencatat keputusannya di aturan proyek.

## Penunjuk: kerjakan X, baca Y

Baca hanya berkas yang cabangnya sedang dikerjakan.

| Sedang mengerjakan | Baca |
|---|---|
| Isi dan urutan proposal atau laporan, apa yang sudah final di proposal, jenis metode penelitian | `references/struktur-isi.md` |
| Judul, identitas penulis, abstrak, kata kunci | `references/judul-abstrak.md` |
| Latar Belakang, Perumusan Masalah (topik), Batasan, Tujuan | `references/pendahuluan.md` |
| Studi terkait, penelusuran pustaka, kualitas jurnal | `references/studi-terkait.md` |
| Rencana atau hasil pengujian, metrik, analisis | `references/evaluasi.md` |
| Sitasi, format IEEE atau APA, jenis publikasi, parafrase, plagiarisme | `references/sitasi-parafrase.md` |
| Menyunting naskah, pemeriksaan akhir sebelum selesai | `references/checklist-editing.md` |
| Slide atau persiapan sidang | `references/presentasi-sidang.md` |

Naskah yang menyentuh beberapa bagian membaca beberapa berkas. Pemeriksaan akhir selalu menyertakan `checklist-editing.md`.

## Cara memakai aturan

- Terapkan setiap aturan di berkas yang dibaca pada bagian yang sedang dikerjakan, lalu sebutkan tag sumbernya saat menjelaskan alasan perubahan kepada pengguna.
- Sebut sesuatu "keputusan proyek" hanya setelah menemukan barisnya di aturan proyek atau templat. Bila tidak ada, itu belum diputuskan: laporkan ke pengguna.
- Bila pengguna memilih mengikuti slide secara penuh di suatu bagian, tetap laporkan setiap konflik dengan aturan proyek atau templat.
- Sebelum finalisasi dokumen, ingatkan pengguna menjalankan pemeriksaan kemiripan kampus bila diwajibkan. Agen tidak menjalankannya.
- Aturan gaya bahasa dan format dokumen milik proyek pengguna, bukan skill ini.
