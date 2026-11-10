# metopen-ta

Skill agen AI yang memuat aturan metodologi penelitian dan tata tulis ilmiah dari materi kuliah Metopen FIF Telkom University. Dipakai untuk menulis, merevisi, dan memeriksa proposal serta laporan Tugas Akhir (TA). Setiap aturan membawa tag sumber (misalnya `[W06 s15]`, deck W06 slide 15) yang menunjuk ke slide asli, jadi setiap saran bisa diperiksa.

*English: an agent skill that distills a university thesis-writing course (Telkom University, Informatics) into on-demand reference files with per-rule slide citations. Content is in Indonesian.*

## Pasang

```bash
npx skills add WaxArsatia/metopen-ta
```

Perintah itu memasang skill ke proyek yang sedang dibuka. Untuk semua proyek di Claude Code, tanpa pertanyaan:

```bash
npx skills add WaxArsatia/metopen-ta -g -a claude-code -y
```

Opsi yang berguna:

| Opsi | Fungsi |
|---|---|
| `-g`, `--global` | Pasang ke folder pengguna, bukan ke proyek |
| `-a`, `--agent <agen>` | Pilih agen tujuan, misalnya `claude-code` atau `codex` |
| `-l`, `--list` | Tampilkan skill di repo tanpa memasang |
| `--copy` | Salin berkas, bukan symlink |
| `-y`, `--yes` | Lewati semua konfirmasi |

Kelola setelah terpasang:

```bash
npx skills list              # daftar skill terpasang
npx skills update metopen-ta # perbarui
npx skills remove metopen-ta # hapus
```

Catatan:
- Pakai `WaxArsatia/metopen-ta` atau URL repo GitHub. Tautan langsung ke `SKILL.md` mentah hanya memasang `SKILL.md`, sehingga `references/` tidak ikut.
- Pemasangan menyalin seluruh folder skill, termasuk `slides/` (sekitar 31 MB).
- CLI mengirim data penggunaan anonim. Matikan dengan `DISABLE_TELEMETRY=1` atau `DO_NOT_TRACK=1`.
- Opsi lengkap ada di [dokumentasi `skills add`](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

<details>
<summary>Pasang manual dengan <code>git clone</code></summary>

Claude Code, per pengguna (berlaku di semua proyek):

```bash
git clone https://github.com/WaxArsatia/metopen-ta.git ~/.claude/skills/metopen-ta
```

Claude Code, per proyek:

```bash
git clone https://github.com/WaxArsatia/metopen-ta.git <proyek-anda>/.claude/skills/metopen-ta
```

Perbarui dengan `git pull` di folder itu.

Agen lain: salin folder ini, lalu tambahkan ke `AGENTS.md` proyek kalimat seperti "Sebelum menulis atau memeriksa proposal atau TA, baca `metopen-ta/SKILL.md` dan ikuti penunjuknya."

</details>

## Kapan skill ini dipakai

Agen memuat skill ini sendiri saat tugasnya menyangkut penulisan atau pemeriksaan proposal, laporan, atau slide sidang TA. Nama skill tidak perlu disebut. Menyebut `metopen-ta` secara eksplisit tetap memastikan skill termuat.

### Contoh prompt

Menulis:
- "Susun draf Latar Belakang proposal TA saya tentang klasifikasi gestur dengan sensor IMU. Ikuti aturan Metopen."
- "Buat kerangka Bab 1 proposal TA: bagian apa saja yang harus ada dan urutannya?"
- "Tulis Perumusan Masalah dan Tujuan dari topik ini, lalu cek apakah keduanya saling memetakan."
- "Bantu tulis abstrak dari draf proposal ini, lengkap dengan kata kunci."

Memeriksa dan merevisi:
- "Periksa Latar Belakang saya terhadap aturan Metopen. Tunjukkan bagian yang menyimpang beserta tag slidenya."
- "Apakah Batasan Masalah saya sudah benar? Rasanya ada yang mengulang judul."
- "Cek apakah daftar pustaka dan sitasi di bab ini sudah konsisten dengan gaya IEEE."
- "Parafrase paragraf ini supaya tidak terkena plagiarisme, tanpa mengubah maknanya."

Merencanakan pengujian dan studi terkait:
- "Rencana evaluasi saya sudah memuat dataset, baseline, dan metrik? Apa yang masih kurang?"
- "Bagaimana cara menyusun Studi Terkait dan memeriksa kualitas jurnal yang saya kutip?"

Sidang dan penyelesaian:
- "Buatkan outline slide presentasi proposal TA 15 menit sesuai aturan tampilan Metopen."
- "Jalankan checklist penyuntingan akhir sebelum proposal ini saya kirim ke calon pembimbing."

### Yang tidak dilakukan

- Tidak menjalankan pemeriksaan kemiripan (plagiarisme) kampus. Agen hanya mengingatkan.
- Tidak mengecek indeks atau kuartil jurnal.
- Tidak menetapkan keputusan proyek Anda. Konflik antara slide dan templat atau aturan proyek dilaporkan, bukan dipilih sendiri.

## Isi repo

```
metopen-ta/
├── SKILL.md       pintu masuk: urutan otoritas dan tabel "kerjakan X, baca Y"
├── SUMBER.md      kode deck (W01 sampai W13) ke berkas slide, topik, dan cara memeriksa tag
├── references/    8 berkas topik, dimuat sesuai kebutuhan
├── slides/        salinan slide asli (12 berkas, sekitar 31 MB)
└── README.md      berkas ini (untuk manusia, tidak dimuat agen)
```

| Berkas di `references/` | Topik |
|---|---|
| `struktur-isi.md` | Isi dan urutan proposal atau laporan, jenis metode penelitian |
| `judul-abstrak.md` | Judul, identitas penulis, abstrak, kata kunci |
| `pendahuluan.md` | Latar Belakang, Perumusan Masalah, Batasan, Tujuan |
| `studi-terkait.md` | Studi terkait, penelusuran pustaka, kualitas jurnal |
| `evaluasi.md` | Rencana dan hasil pengujian, metrik, analisis |
| `sitasi-parafrase.md` | Sitasi IEEE dan APA, jenis publikasi, parafrase |
| `checklist-editing.md` | Penyuntingan dan pemeriksaan akhir |
| `presentasi-sidang.md` | Slide dan persiapan sidang |

## Cara kerja

Skill memakai pemuatan bertahap (*progressive disclosure*) sesuai [spesifikasi Agent Skills](https://agentskills.io/specification):

1. Nama dan deskripsi selalu ada di konteks agen, sebagai penentu kapan skill dipakai.
2. `SKILL.md` dimuat saat skill aktif. Isinya urutan otoritas dan tabel penunjuk ke berkas topik.
3. Agen membuka satu atau dua berkas `references/` sesuai bagian yang dikerjakan.
4. `slides/` hanya dibuka saat sebuah tag perlu diperiksa. Cara memeriksanya ada di `SUMBER.md`.

Urutan otoritas saat aturan bertentangan: aturan proyek Anda, lalu templat resmi prodi atau fakultas, lalu slide kuliah.

## Menyimpan keputusan proyek sendiri

Skill ini sengaja umum. Keputusan khusus Anda (struktur bab dari templat prodi, bagian yang dibuang, batas referensi, gaya sitasi) jangan diubah di sini. Catat di `CLAUDE.md` atau `AGENTS.md` proyek Anda, karena aturan proyek menang atas slide.

Contoh catatan di `CLAUDE.md` proyek:

```markdown
## Skill metopen-ta
Sebelum menulis atau memeriksa isi proposal atau TA, muat skill `metopen-ta`.
Keputusan proyek (menang atas slide):
- Bab 1 hanya memuat Latar Belakang, Perumusan Masalah, Tujuan, Batasan Masalah.
- Tanpa bagian Hipotesis.
- Sitasi IEEE bernomor.
```

## Batasan

- Ringkasan bergantung pada ekstraksi teks dan pembacaan visual slide bergambar. Cocokkan dengan slide asli sebelum menjadikan aturan sebagai dasar keputusan penting.
- Slide mengacu ke Template Laporan TA untuk laporan akhir. Untuk proposal, templat proposal fakultas dan aturan proyek Anda lebih tinggi derajatnya.
- Memeriksa slide bergambar butuh LibreOffice dan `pdftoppm` (lihat `SUMBER.md`).

## Hak cipta dan lisensi

- Slide di `slides/` milik pengampu kelas dan Universitas Telkom. Penyusun repo memperoleh izin untuk membagikannya agar tag sumber bisa diperiksa tanpa berkas terpisah. Izin itu tidak mengalihkan hak cipta slide kepada penyusun repo atau pemakai repo.
- Isi `references/` adalah ringkasan parafrase dari slide tersebut. Contoh judul, kutipan referensi, dan nama penulis di dalamnya berasal dari contoh di slide.
- Repo ini bukan materi resmi universitas dan tidak mewakili pandangan universitas.
- Repo belum memakai lisensi terbuka, jadi hak cipta atas konten buatan penyusun tetap pada penyusun. Bila lisensi ditambahkan nanti, lisensi itu harus mengecualikan `slides/`.
