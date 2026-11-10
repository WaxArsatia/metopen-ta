---
name: metopen-ta
description: "Aturan Metopen FIF Telkom untuk Tugas Akhir (TA, skripsi), bertag sumber per slide. Muat saat menulis, merevisi, atau memeriksa proposal, laporan, atau slide sidang TA: struktur bab, judul, abstrak, Pendahuluan (Latar Belakang, Perumusan Masalah, Tujuan, Batasan), Studi Terkait, evaluasi dan metrik, sitasi dan parafrase, penyuntingan akhir."
---

Pengetahuan metopen umum, dipecah per topik di `references/`. Setiap aturan berakhir dengan tag sumber, misalnya `[W06 s15]` (deck W06, slide 15). Saat sebuah tag perlu diperiksa ke slide asli, baca `SUMBER.md` (peta kode deck ke berkas di `slides/` dan perintah membukanya). Baris "Sumber" di kepala tiap berkas referensi mendaftar slide yang hanya terbaca dari gambar.

## Urutan otoritas

Saat dua sumber bertentangan, yang lebih atas menang:

1. Aturan proyek pengguna (`CLAUDE.md`, `AGENTS.md`, atau catatan proyek lain yang memuat keputusan penulisan).
2. Templat resmi program studi atau fakultas.
3. Slide kuliah (referensi ini).

Slide adalah dasar umum, bukan perintah yang menimpa keputusan proyek. Baca aturan proyek pengguna lebih dulu bila ada, lalu pakai referensi di bawah untuk bagian yang belum diatur. Konflik antara slide dan aturan proyek atau templat: laporkan ke pengguna dan minta keputusannya, juga saat pengguna meminta mengikuti slide sepenuhnya, lalu sarankan mencatat keputusannya di aturan proyek.

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
- Sebelum finalisasi dokumen, ingatkan pengguna menjalankan pemeriksaan kemiripan kampus bila diwajibkan.
- Gaya bahasa dan format dokumen mengikuti aturan proyek pengguna.
