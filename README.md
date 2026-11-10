# metopen-ta

Skill agen AI berisi aturan metodologi penelitian dan tata tulis ilmiah dari materi kuliah Metopen FIF Telkom University, untuk menulis, merevisi, dan memeriksa proposal serta laporan Tugas Akhir. Setiap aturan membawa tag sumber (misalnya `[W06 s15]`) yang menunjuk ke slide asli.

*English: an agent skill that distills a university thesis-writing course (Telkom University, Informatics) into on-demand reference files with per-rule slide citations. Content is in Indonesian.*

## Status dan hak cipta

Isi `references/` berupa ringkasan parafrase dari slide dosen. Salinan slide aslinya disertakan di `slides/` agar tag sumber bisa diperiksa di mesin mana pun tanpa memindahkan berkas terpisah. Slide itu milik pengampu kelas dan Universitas Telkom, dan penyusun repo telah memperoleh izin untuk membagikannya. Repo ini belum memakai lisensi terbuka, jadi hak cipta atas konten buatan penyusun tetap pada penyusun. Lihat `NOTICE.md`.

## Isi

```
metopen-ta/
├── SKILL.md              pintu masuk: urutan otoritas dan tabel "kerjakan X, baca Y"
├── SUMBER.md             pemetaan kode deck (W01 sampai W13) ke berkas, topik, dan cara memeriksa tag
├── slides/               salinan slide asli (12 berkas, sekitar 31 MB)
├── references/           8 berkas topik, dimuat sesuai kebutuhan
│   ├── struktur-isi.md
│   ├── judul-abstrak.md
│   ├── pendahuluan.md
│   ├── studi-terkait.md
│   ├── evaluasi.md
│   ├── sitasi-parafrase.md
│   ├── checklist-editing.md
│   └── presentasi-sidang.md
├── NOTICE.md
└── README.md             berkas ini (tidak dimuat agen)
```

Agen hanya membaca `SKILL.md` lebih dulu, lalu satu atau dua berkas `references/` sesuai bagian yang dikerjakan. Folder `slides/` hanya dibuka saat sebuah tag perlu diperiksa.

## Pasang

Claude Code, per pengguna (berlaku di semua proyek):

```bash
git clone https://github.com/WaxArsatia/metopen-ta.git ~/.claude/skills/metopen-ta
```

Claude Code, per proyek:

```bash
git clone https://github.com/WaxArsatia/metopen-ta.git <proyek-anda>/.claude/skills/metopen-ta
```

Perbarui dengan `git pull` di folder itu.

Harness agen lain: salin folder ini, lalu arahkan berkas instruksi proyek (misalnya `AGENTS.md`) ke `SKILL.md` dengan kalimat seperti: "Sebelum menulis atau memeriksa proposal atau TA, baca `metopen-ta/SKILL.md` dan ikuti penunjuknya." Berkas `references/` dibuka sesuai tabel di `SKILL.md`.

## Menyimpan keputusan proyek sendiri

Skill ini sengaja umum. Keputusan khusus Anda (struktur bab dari templat prodi, bagian yang dibuang, batas referensi, gaya sitasi) jangan diubah di sini. Catat di `CLAUDE.md` atau `AGENTS.md` proyek Anda. `SKILL.md` menetapkan bahwa aturan proyek menang atas slide, dan konflik dilaporkan ke Anda dulu.

Contoh catatan di `CLAUDE.md` proyek:

```markdown
## Skill metopen-ta
Sebelum menulis atau memeriksa isi proposal atau TA, muat skill `metopen-ta`.
Keputusan proyek (menang atas slide):
- Bab 1 hanya memuat Latar Belakang, Perumusan Masalah, Tujuan, Batasan Masalah.
- Tanpa bagian Hipotesis.
- Sitasi IEEE bernomor.
```

## Batasan yang perlu diketahui

- Ringkasan bergantung pada ekstraksi teks dan pembacaan visual slide bergambar. Cocokkan dengan slide asli sebelum menjadikan aturan sebagai dasar keputusan penting.
- Slide mengacu ke Template Laporan TA untuk laporan akhir. Untuk proposal, templat proposal fakultas dan aturan proyek Anda lebih tinggi derajatnya.
- Skill tidak menjalankan pemeriksaan kemiripan (plagiarisme) dan tidak mengecek indeks jurnal.
- Clone pertama mengunduh sekitar 31 MB karena memuat slide. Memeriksa slide bergambar butuh LibreOffice dan `pdftoppm` (lihat `SUMBER.md`).
