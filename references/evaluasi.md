# Evaluasi
Aturan bagian Evaluasi (pengantar evaluasi, hasil pengujian, analisis hasil pengujian) dan rencana evaluasi untuk proposal TA.
Sumber: deck W09 slide 4-6, 8-9, 11-17, 19-20, 22-23 (slide 14, 16, 20, 22, 23 dibaca dari gambar).

## Posisi dan struktur bagian Evaluasi
- Pada artikel informatika, evaluasi atas sistem, gagasan, atau metode yang diusulkan (proposed method) umumnya berupa pengujian. [W09 s4]
- Inti bagian Evaluasi terdiri dari dua sub-bagian: Hasil Pengujian dan Analisis Hasil Pengujian. [W09 s4]
- Sampaikan juga dataset, detail implementasi (misalnya pengaturan parameter), metrik evaluasi, dan baseline (pembanding). [W09 s4]
- Informasi tersebut boleh ditulis sebagai sub-bagian tersendiri bernama Pengantar Evaluasi. [W09 s5]
- Pengujian dan analisis harus selaras dengan tujuan yang dinyatakan di Pendahuluan. [W09 s5]
- Tulis nama sub-bagian secara lengkap: "Analisis Hasil Pengujian", jangan disingkat "Analisis". Alasan: menghindari salah paham dengan analisis perancangan; terutama sebagai latihan penulisan hasil penelitian tingkat sarjana. [W09 s5]
- Pada artikel berbahasa Inggris, analisis hasil pengujian sering diberi nama "Discussion". [W09 s6]
- Contoh struktur artikel (Wang dkk., KDD 2020): bagian "Experiment Results" berisi sub-bagian Dataset, Implementation Details, Evaluation Metrics, Baselines, Results and Discussions. Empat sub-bagian pertama adalah pengantar evaluasi; "Results and Discussions" dibagi menjadi hasil pengujian dan analisis hasil pengujian. [W09 s22]
- Contoh pembagian "Results and Discussions": Performance Comparison (= hasil pengujian), lalu Impact of Multi-task Learning, Impact of Training Batch Size and Learning Rate, Parameter Sensitivity (= tiga poin analisis hasil pengujian, masing-masing pada kondisi yang dianggap penting untuk topik artikel). [W09 s23]

## Pengantar Evaluasi: data yang digunakan
- Sebutkan dari mana dan bagaimana data diambil atau dibangun. [W09 s8]
- Jika sumber data berupa tautan, cantumkan agar pembaca dapat mengakses data tersebut. [W09 s8]
- Sajikan statistika data (jumlah, distribusi) dan karakteristik lain. [W09 s8]

## Pengantar Evaluasi: detail implementasi
- Sebutkan perangkat keras dan perangkat lunak utama yang relevan dengan pengujian. [W09 s8]
- Sebutkan pengaturan parameter dan threshold yang digunakan. [W09 s8]

## Pengantar Evaluasi: metrik evaluasi
- Sebutkan metrik evaluasi apa saja yang dipakai. [W09 s9]
- Lebih baik disertai penjelasan singkat mengapa metrik tersebut dipilih. [W09 s9]
- Jika metrik lebih dari satu, jelaskan mana metrik utamanya. [W09 s9]

## Pengantar Evaluasi: baseline (pembanding)
- Jelaskan setiap pembanding dengan sangat singkat, termasuk pengaturan parameter yang dipakai. [W09 s9]
- Alasan perlunya pembanding: tinggi atau rendah, baik atau jeleknya hasil bersifat relatif, sehingga sangat dianjurkan membandingkan dengan sistem, model, metode, algoritma, atau pendekatan lain. [W09 s12]
- Perbandingan tetap dilakukan meskipun judul dan tujuan tulisan tidak menyatakan perbandingan secara eksplisit. [W09 s13]
- Pilih pembanding yang baik, misalnya yang populer atau state of the art. [W09 s13]
- Bandingkan pada lingkungan yang sama. Contoh: untuk mengukur efektivitas, pakai data yang sama. [W09 s13]

## Hasil Pengujian: urutan dan isi
- Tampilkan lebih dulu hasil pengujian yang paling utama, lalu hasil yang lebih detail. Tujuannya memudahkan pembaca. [W09 s11]
- Hasil utama juga disampaikan di abstrak, boleh dengan cara berbeda (misalnya kualitatif). [W09 s11]
- Hasil utama umumnya adalah hasil terbaik dari pengujian yang dilakukan, dibandingkan dengan pembanding. [W09 s12]
- Tabel hasil utama menampilkan hasil terbaik; hasil lain dianalisis di Analisis Hasil Pengujian. [W09 s14]
- Tuliskan kondisi atau pengaturan (antara lain parameter) yang menghasilkan hasil terbaik dengan sistem yang diuji. [W09 s17]
- Setiap gambar dan tabel, termasuk hasil utama, diterangkan dalam teks. [W09 s17]

## Hasil Pengujian: format tabel
- Bentuk tabel utama: baris = sistem atau pembanding (termasuk penelitian sendiri), kolom = metrik (contoh: Precision, Recall, F1, E%; atau MAP, P, R, F1, Acc, satuan %). [W09 s14, s16]
- Beri format berbeda (misalnya tebal) pada angka terbaik di setiap metrik. [W09 s15]
- Angka desimal: digit di belakang koma sesedikit mungkin, asal masih cukup membedakan antar angka. [W09 s15]
- Beri catatan kaki tabel bila perlu (contoh: tanda * pada baris dengan keterangan fitur yang dipakai). [W09 s14]
- Baris penelitian sendiri boleh diberi label jelas (contoh: "This Work", "Penelitian yang dilakukan") dan tidak harus unggul di semua kolom; pada contoh slide, hasil sendiri tidak terbaik di setiap metrik. [W09 s14, s16]

## Analisis Hasil Pengujian
- Hasil utama membandingkan dengan pihak lain (eksternal). Analisis hasil pengujian umumnya menganalisis internal sistem yang dibangun pada beberapa kondisi berbeda. [W09 s19]
- Analisis adalah bagian penting untuk karya mahasiswa S1, termasuk TA. [W09 s19]
- TA S1 tidak dituntut memperoleh performa lebih baik daripada pembanding. Yang dituntut: implementasi yang benar serta analisis yang baik dan lengkap. [W09 s19]
- Analisis melihat pengaruh kondisi berbeda: parameter, jenis data, threshold, sub-sistem. [W09 s20]
- Lakukan analisis pada beberapa kondisi, tidak hanya satu. Contoh slide: selain pengaruh himpunan fitur, analisis juga pengaruh faktor lain. [W09 s20]
- Contoh tabel analisis (ablation fitur): baris = kondisi (semua fitur, fitur terbaik, lalu satu fitur dilepas satu per satu), kolom = metrik. Terangkan notasi tabel (tanda "(-)" berarti fitur tidak digunakan). [W09 s20]
- Terangkan setiap tabel dan gambar yang ditampilkan agar jelas bagi pembaca. [W09 s20]

## Yang direncanakan di proposal TA (belum ada eksperimen)
- Meski eksperimen belum dilakukan, rancang kerangka bagian Evaluasi di proposal. [W09 s6]
- Rencanakan kandidat metrik evaluasi dan sistem/model pembanding yang akan dipakai. [W09 s6]
- Rencanakan kerangka (baris dan kolom) tabel pengujian utama. [W09 s6]
- Rencanakan garis besar analisis hasil pengujian yang akan dilakukan. [W09 s6]
- Slide tidak menyebut letak rencana evaluasi di proposal. Ikuti templat program studi atau aturan proyek.

## Daftar periksa cepat
- Dataset: sumber, tautan, statistik, karakteristik tercantum. [W09 s8]
- Implementasi: perangkat keras/lunak relevan, parameter, threshold tercantum. [W09 s8]
- Metrik: daftar, alasan singkat, metrik utama ditunjuk. [W09 s9]
- Baseline: dijelaskan singkat, parameter tercantum, lingkungan sama. [W09 s9, s13]
- Tabel utama: hasil utama lebih dulu, angka terbaik ditebalkan, desimal minimal. [W09 s11, s15]
- Setiap tabel/gambar diterangkan di teks; kondisi hasil terbaik dituliskan. [W09 s17]
- Analisis: lebih dari satu kondisi, internal sistem, selaras dengan tujuan di Pendahuluan. [W09 s5, s20]
