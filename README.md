# metopen-ta

Skill agen AI yang memuat aturan metodologi penelitian dan tata tulis ilmiah dari materi kuliah Metopen FIF Telkom University, ditambah aturan format dari templat resmi FIF (Proposal, Buku TA, Jurnal TA). Dipakai untuk menulis, merevisi, memformat, dan memeriksa proposal serta laporan Tugas Akhir (TA). Setiap aturan membawa tag sumber (misalnya `[W06 s15]` untuk deck W06 slide 15, atau `[TB hlm. 25]` untuk halaman 25 templat Buku TA) yang menunjuk ke berkas asli, jadi setiap saran bisa diperiksa.

*English: an agent skill that distills a university thesis-writing course and the faculty's official proposal and thesis templates (Telkom University, Informatics) into on-demand reference files with per-rule source citations, plus a read-only .docx format checker. Content is in Indonesian.*

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
- Pemasangan menyalin seluruh folder skill, termasuk `slides/` (sekitar 31 MB) dan `templates/` (sekitar 0,5 MB).
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

Memformat:
- "Atur margin, huruf, dan spasi proposal saya sesuai templat FIF, lalu cek dengan skrip pemeriksa."
- "Nomor halaman buku TA FIF diletakkan di mana? Templatnya membingungkan."

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
- Skripnya tidak mengecek indeks atau kuartil jurnal; pemeriksaan itu hanya dilakukan agen lewat web bila diminta aturan proyek atau preset.
- Tidak menetapkan keputusan proyek Anda. Konflik antara slide dan templat atau aturan proyek dilaporkan, bukan dipilih sendiri.

## Isi repo

```
metopen-ta/
├── SKILL.md       pintu masuk: urutan otoritas dan tabel "kerjakan X, baca Y"
├── SUMBER.md      kode deck (W01 sampai W13) dan templat (TP, TB, TJ) ke berkas, serta cara memeriksa tag
├── references/    berkas topik, dimuat sesuai kebutuhan
├── scripts/       cek_format.py (pemeriksa format dan isi .docx, hanya membaca), bangun_pdf.sh (docx ke PDF, cek, lembar kontak), docx_peta.py (peta elemen docx), docx_kemas.sh (kemas docx dengan cadangan dan uji zip)
├── slides/        salinan slide asli (12 berkas, sekitar 31 MB)
├── templates/     salinan templat resmi FIF: Proposal, Buku TA, Jurnal TA
└── README.md      berkas ini (untuk manusia, tidak dimuat agen)
```

| Berkas di `references/` | Topik |
|---|---|
| `format-dokumen.md` | Format per templat (proposal, buku TA, jurnal TA), struktur bab, pertentangan templat |
| `menerapkan-format-docx.md` | Cara menulis ke salinan templat .docx, skrip pemeriksa, render PDF |
| `pola-ta-terbit.md` | Pola dari TA FIF yang sudah terbit (contoh, bukan aturan), termasuk pola TA bimbingan satu pembimbing |
| `struktur-isi.md` | Isi dan urutan proposal atau laporan, jenis metode penelitian |
| `judul-abstrak.md` | Judul, identitas penulis, abstrak, kata kunci |
| `pendahuluan.md` | Latar Belakang, Perumusan Masalah, Batasan, Tujuan |
| `studi-terkait.md` | Studi terkait, penelusuran pustaka, kualitas jurnal |
| `evaluasi.md` | Rencana dan hasil pengujian, metrik, analisis |
| `sitasi-parafrase.md` | Sitasi IEEE dan APA, jenis publikasi, parafrase |
| `checklist-editing.md` | Penyuntingan dan pemeriksaan akhir |
| `aturan-resmi.md` | Syarat sidang, publikasi, integritas akademik, dan AI dari dokumen resmi FIF dan Telkom University |
| `presentasi-sidang.md` | Slide dan persiapan sidang |
| `aturan-denis.md` | Preset aturan generik dan keputusan proyek TA (opsional), dipicu dengan "ikuti aturan denis" |

## Cara kerja

Skill memakai pemuatan bertahap (*progressive disclosure*) sesuai [spesifikasi Agent Skills](https://agentskills.io/specification):

1. Nama dan deskripsi selalu ada di konteks agen, sebagai penentu kapan skill dipakai.
2. `SKILL.md` dimuat saat skill aktif. Isinya urutan otoritas dan tabel penunjuk ke berkas topik.
3. Agen membuka satu atau dua berkas `references/` sesuai bagian yang dikerjakan.
4. `slides/` hanya dibuka saat sebuah tag perlu diperiksa. Cara memeriksanya ada di `SUMBER.md`.

Urutan otoritas saat aturan bertentangan: aturan proyek Anda, lalu templat resmi fakultas, lalu slide kuliah, lalu pola TA terbit. Untuk integritas akademik, AI, publikasi, dan syarat sidang, aturan resmi di `aturan-resmi.md` berada di atas templat dan slide. Pemicu "ikuti aturan denis" menambah satu penyesuaian: pada butir yang diatur preset dan berbeda dari praktik TA terbit, praktik TA terbit menang atas preset. Di dalam templat Proposal dan Buku TA, pengaturan yang tertanam di docx menang atas kalimat petunjuknya (contoh: teks menyebut "1 spasi", paragraf diatur 1,5). Templat Jurnal TA dikecualikan karena docx-nya sisa konversi PDF; di sana teks petunjuk yang menang.

## Pemeriksa format

```bash
scripts/bangun_pdf.sh "Proposal.docx" proposal                      # PDF, cek, lembar kontak; jenis: proposal, buku, jurnal
scripts/bangun_pdf.sh "Proposal.docx" proposal --preset denis       # ditambah pemeriksaan preset
python3 -I scripts/cek_format.py "Proposal.docx" --jenis proposal   # hanya pemeriksa
```

`cek_format.py` hanya membaca berkas; daftar pemeriksaannya ada di `python3 -I scripts/cek_format.py -h`. Pemenggalan halaman dibaca dari daftar baris pertama dan terakhir tiap halaman serta lembar kontak (lihat `references/menerapkan-format-docx.md`).

## Menyimpan keputusan proyek sendiri

Skill ini sengaja umum, dan satu-satunya bagian berisi keputusan proyek adalah preset opsional di bawah. Keputusan khusus Anda (struktur bab dari templat prodi, bagian yang dibuang, batas referensi, gaya sitasi) jangan diubah di sini. Catat di `CLAUDE.md` atau `AGENTS.md` proyek Anda, karena aturan proyek menang atas slide.

Contoh catatan di `CLAUDE.md` proyek:

```markdown
## Skill metopen-ta
Sebelum menulis atau memeriksa isi proposal atau TA, muat skill `metopen-ta`.
Keputusan proyek (menang atas slide):
- Bab 1 hanya memuat Latar Belakang, Perumusan Masalah, Tujuan, Batasan Masalah.
- Tanpa bagian Hipotesis.
- Sitasi IEEE bernomor.
```

## Preset "aturan Denis" (opsional)

Selain keputusan sendiri, skill menyertakan satu preset keputusan proyek TA dari penyusun: `references/aturan-denis.md`. Isinya prinsip otoritas, format dan tata letak, struktur Latar Belakang, pasangan Rumusan Masalah dan Tujuan (kata kerja Bloom), Batasan Masalah, aturan sitasi, abstrak dan kata kunci, isi Bab 2 dan Bab 3, metrik, gaya tulis, dan daftar "Siap diserahkan". Data pribadi diganti kolom `[ISI: ...]`.

Dua cara memakainya, berlaku untuk agen apa pun yang mendukung Agent Skills:

1. **Sekali pakai.** Tulis di percakapan: `ikuti aturan denis`. Agen membaca preset, menanyakan kolom yang kosong, lalu menerapkannya selama sesi.
2. **Permanen.** Tempel instruksi berikut ke berkas instruksi proyek yang dibaca agen Anda (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, atau pengaturan instruksi kustom):

```markdown
## Aturan TA
Untuk pekerjaan proposal atau TA, ikuti aturan Denis: baca `references/aturan-denis.md`
di skill `metopen-ta`, terapkan sebagai aturan proyek, dan tanyakan kolom [ISI: ...] yang kosong.
```

Preset bersifat pilihan. Aturan proyek tertulis milik Anda menang atas preset, dan preset menang atas templat dan slide. Pengecualiannya butir yang berbeda dari praktik TA terbit di `references/pola-ta-terbit.md`: praktik itu menang, dan agen melaporkan daftar butirnya sebelum membalik keputusan yang tercatat di preset.

## Batasan

- Ringkasan bergantung pada ekstraksi teks dan pembacaan visual slide bergambar. Cocokkan dengan slide asli sebelum menjadikan aturan sebagai dasar keputusan penting.
- Slide mengacu ke Template Laporan TA untuk laporan akhir. Untuk proposal, templat proposal fakultas dan aturan proyek Anda lebih tinggi derajatnya.
- Templat di `templates/` adalah versi yang diperoleh penyusun pada 2024-2025. Bila prodi menerbitkan versi baru, ganti berkasnya dan periksa ulang `references/format-dokumen.md`.
- Pemeriksa format membaca XML, bukan tampilan. Huruf yang tidak terpasang dan medan caption bisa tampil berbeda di LibreOffice dan Word.
- Memeriksa slide bergambar butuh LibreOffice dan `pdftoppm` (lihat `SUMBER.md`).

## Hak cipta dan lisensi

- Templat di `templates/` adalah salinan yang diperoleh penyusun dari program studi pada 2024-2025, bukan unduhan dari situs resmi. Portal resmi fakultas (SONIA) memuat templat gaya jurnal TA; versi docx proposal dan buku TA ini tidak ditemukan di situs publik. Struktur templat buku sejalan dengan TA S1 FIF yang terbit 2025-2026. Hak cipta templat tetap pada Fakultas Informatika Universitas Telkom.
- Slide di `slides/` milik pengampu kelas dan Universitas Telkom. Penyusun repo memperoleh izin untuk membagikannya agar tag sumber bisa diperiksa tanpa berkas terpisah. Izin itu tidak mengalihkan hak cipta slide kepada penyusun repo atau pemakai repo.
- Dokumen resmi yang dirujuk `aturan-resmi.md` tidak disalin ke repo; hanya ringkasan dan alamatnya.
- Isi `references/` adalah ringkasan parafrase dari slide, templat, dan dokumen tersebut. Contoh judul, kutipan referensi, dan nama penulis di dalamnya berasal dari contoh di slide.
- Repo ini bukan materi resmi universitas dan tidak mewakili pandangan universitas.
- Repo belum memakai lisensi terbuka, jadi hak cipta atas konten buatan penyusun tetap pada penyusun. Bila lisensi ditambahkan nanti, lisensi itu harus mengecualikan `slides/` dan `templates/`.
