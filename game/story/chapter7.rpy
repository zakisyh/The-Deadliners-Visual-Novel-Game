# ============================================================
# THE DEADLINERS — CHAPTER 07: THE FINAL CHECKLIST
# Ren'Py 8.5.3 | H-12 sampai H-4
# 5 scene | 15 menu: 12 dialog biasa, 3 pilihan berpengaruh
# ============================================================
# Lanjutan langsung dari Chapter 6 (15 DAYS LEFT).
# Lima kesempatan bukti Secret Ending sudah ada di Chapter 2-6.
# Chapter ini TIDAK membuat bukti keenam dan TIDAK memilih ending.
# "Stay with me" tetap disimpan untuk fase H-3.

# MENU 04: menentukan integrasi yang didahulukan.
# "booking" = alur form, harga, ringkasan, dan data uji lokal.
# "admin"   = daftar pesanan dan status pada admin dengan data uji.
default prioritas_integrasi_ch7 = ""

# MENU 09: cara menanggapi belum adanya konten dari Adrian.
# "tenggat" = kirim permintaan terakhir yang jelas melalui grup.
# "demo"    = siapkan konten CONTOH dengan label, bukan koleksi asli.
default strategi_konten_ch7 = ""

# MENU 11: bagian yang diuji dan diperbaiki sebelum latihan demo.
# "pengunjung" = uji perjalanan pengunjung dan perbaiki penghambat.
# "pengelola"  = uji halaman admin / konfirmasi simulasi.
default fokus_pengujian_ch7 = ""


label chapter_7:
    $ hud_visible = False
    $ days_left = 12
    scene black with fade
    centered "{size=50}CHAPTER 07{/size}\n{size=42}THE FINAL CHECKLIST{/size}\n{size=34}12 DAYS LEFT{/size}"
    jump ch7_scene_01


# ============================================================
# SCENE 01 — TWELVE DAYS | H-12
# ============================================================
label ch7_scene_01:
    $ days_left = 12
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari setelah sesi evaluasi terakhir, Luuk dan Jane bertemu di area duduk kampus."
    "Di meja mereka ada laptop, catatan pengujian, dan daftar pekerjaan yang terus diperbarui."
    designer "Woy."
    coder "Woy."
    designer "Udah makan?"
    coder "Udah."
    designer "Bener?"
    coder "Beneran."
    designer "Oke. Gue nggak mau lo tiba-tiba bilang pusing pas ngetes."
    coder "Lo udah kayak pengawas praktikum."
    designer "Ada yang harus ngawasin."
    coder "Lah."
    "Jane duduk dan membuka kalender."
    designer "Dua belas hari."
    coder "Iya."
    designer "Angkanya makin nggak enak dilihat."
    coder "Kalendernya nggak salah, sih."
    designer "Gue tahu. Jangan dibela."
    coder "Kasihan kalendernya."
    designer "Kasihan kita dulu."

    # MENU 01 — hanya mengubah dialog.
    menu:
        "Gue belum pernah berantem sama kalender.":
            coder "Gue belum pernah berantem sama kalender."
            designer "Sekarang mulai?"
            coder "Nggak. Takut kalah."
            designer "Pilihan bijak."

        "Setidaknya hari ini kita tahu harus tes apa.":
            coder "Setidaknya hari ini kita tahu harus tes apa."
            designer "Iya. Nggak cuma buka website terus bilang lumayan."
            coder "Nah."
            designer "Harus ada hasil yang bisa dicek."

        "Kalau bisa, gue mau satu minggu tambahan.":
            coder "Kalau bisa, gue mau satu minggu tambahan."
            designer "Coba tanya kalender."
            coder "Tadi katanya jangan dibela."
            designer "Sekarang gue suruh negosiasi."
            coder "Susah juga."

    "Jane menampilkan daftar skenario demonstrasi Museum Arunika."
    designer "Oke. Gue mau coba jadi pengunjung dari awal."
    coder "Dari beranda?"
    designer "Iya. Lihat koleksi, buka booking, isi form, terus lihat hasil pesanan."
    coder "Oke."
    "Jane membuka beranda, lalu berpindah ke halaman galeri."
    "Beberapa kartu galeri masih berisi gambar dan teks contoh."
    designer "Yang ini belum bisa dibilang konten final."
    coder "Iya. Jangan sampai pas presentasi kita nyebutnya koleksi asli."
    designer "Pasti."
    "Jane membuka halaman booking dan mulai memasukkan data percobaan."

    if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking" or fokus_utama_ch5 == "booking":
        designer "Total harga tiket sudah bisa dihitung di jalur yang kita kerjain."
        coder "Iya. Sekarang kita perlu pastikan nilainya nggak hilang di langkah berikutnya."
    else:
        designer "Perhitungan harga asli masih belum kita tuntaskan."
        coder "Iya. Nilai contoh yang dipakai tes sebelumnya nggak boleh dikira hasil hitung final."

    if fokus_teknis_ch6 == "validasi_error" or prioritas_teknis_lanjutan == "validasi" or fokus_pengerjaan_ch4 == "form_booking":
        designer "Peringatan kalau input salah sudah lebih jelas."
        coder "Iya, walaupun belum semua kasus diuji."
    else:
        designer "Kalau input-nya salah, masih ada kondisi yang belum ketangani jelas."
        coder "Itu perlu masuk daftar perbaikan."

    if fokus_integrasi_ch6 == "admin":
        designer "Di admin kita sudah bisa baca beberapa data uji dari modul yang sama."
        coder "Betul. Tapi belum seluruh booking tersambung otomatis."
    else:
        designer "Bagian admin belum sepenuhnya terhubung ke alur pengunjung."
        coder "Iya. Masih ada data uji yang disiapkan terpisah."

    "Jane berhenti pada satu halaman."
    designer "Nah. Ini yang gue maksud."
    coder "Kenapa?"
    designer "Kalau tiap bagian dites sendiri kelihatan jalan. Tapi pas pindah, datanya belum selalu sesuai."
    coder "Iya. Ada perbedaan antara halaman yang jadi dan sistem yang nyambung."
    designer "Kita perlu satu daftar yang benar-benar dipakai buat tes."

    # MENU 02 — dialog biasa.
    menu:
        "Tandai yang berhasil, gagal, dan belum diuji.":
            coder "Tandai yang berhasil, gagal, dan belum diuji."
            designer "Jadi nggak asal centang selesai?"
            coder "Iya. Tiga status itu beda."
            designer "Oke, gue pakai."

        "Kita jangan tertipu tampilan yang udah rapi.":
            coder "Kita jangan tertipu tampilan yang udah rapi."
            designer "Hei, tampilan rapi juga penting."
            coder "Penting. Tapi tombolnya harus jalan."
            designer "Oke. Gue setuju."

    "Jane membandingkan daftar pekerjaan dengan hasil pengujian Chapter sebelumnya."
    if laporan_uji_ch6:
        designer "Laporan uji yang kemarin cukup ngebantu."
        coder "Iya. Ada langkah tes sama hasil sebenarnya."
        designer "Jadi kita tahu mana yang perlu diulang."
    else:
        designer "Catatan bug kemarin bisa kita pakai sebagai awal."
        coder "Iya. Sekarang kita bikin langkah uji yang lebih jelas."

    designer "Berarti hari ini kita bikin urutan."
    coder "Iya. Yang paling menghambat dulu."
    designer "Terus kita kerjain, bukan cuma dibahas."
    coder "Siap."

    # MENU 03 — dialog biasa.
    menu:
        "Kalau bisa didemokan tiga kali tanpa salah, baru gue tenang.":
            coder "Kalau bisa didemokan tiga kali tanpa salah, baru gue tenang."
            designer "Kenapa tiga kali?"
            coder "Sekali berhasil bisa aja kebetulan."
            designer "Oke, masuk akal."

        "Jangan tambahin fitur baru yang nggak wajib.":
            coder "Jangan tambahin fitur baru yang nggak wajib."
            designer "Gue tadi mau ngusulin transisi kartu."
            coder "Nanti kalau yang utama udah aman."
            designer "Iya, iya. Gue simpan dulu."

    "Mereka menetapkan urutan pengujian untuk beberapa hari berikutnya."
    "Sisa waktu sudah cukup pendek sehingga satu masalah kecil bisa mengganggu jadwal pekerjaan lain."
    $ stress_level = min(100, stress_level + 3)
    jump ch7_scene_02


# ============================================================
# SCENE 02 — THE LAST CONNECTION | H-10
# MENU 04: pilihan penting; MENU 05, 06: dialog biasa.
# ============================================================
label ch7_scene_02:
    $ days_left = 10
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Jane datang ke kontrakan Luuk."
    "Keduanya sudah sepakat untuk mengerjakan satu hambatan utama sebelum mencoba demonstrasi penuh lagi."
    designer "Hari ini jangan nyasar ke hal lain dulu, ya."
    coder "Iya."
    designer "Biasanya lo bilang begitu, terus nemu bug lain."
    coder "Bug-nya yang nyamperin gue."
    designer "Alasan."
    coder "Kadang beneran."
    "Luuk membuka editor kode dan catatan bagian yang belum terhubung."
    coder "Kita punya dua pekerjaan yang sama-sama penting."
    designer "Booking sama admin?"
    coder "Iya. Yang satu alur pengunjung, yang satu pembacaan pesanan buat pengelola."
    designer "Kalau waktunya nggak cukup buat dua-duanya hari ini, pilih dulu."
    coder "Setuju."

    # MENU 04 — pilihan penting pertama.
    menu:
        "Utamakan alur booking sampai ringkasan dan data uji tersimpan.":
            $ prioritas_integrasi_ch7 = "booking"
            coder "Utamakan alur booking sampai ringkasan dan data uji tersimpan."
            designer "Oke. Gue tes dari form, bukan buka ringkasannya langsung."
            coder "Bagus. Kita perlu tahu input-nya sampai."

            if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking" or fokus_utama_ch5 == "booking":
                coder "Perhitungan harga sebelumnya kita pakai lagi."
                designer "Kita cek dengan jumlah tiket yang berbeda."
                "Jane menguji beberapa jumlah tiket dan mencocokkan totalnya."
            else:
                coder "Pertama, total harga yang tertunda harus kita beresin."
                designer "Biar nggak pakai angka contoh terus?"
                coder "Iya."
                "Luuk melengkapi perhitungan total harga sesuai jumlah tiket pada form."
                "Jane memeriksa hasilnya dengan beberapa data percobaan."
                designer "Nah, totalnya sekarang berubah sesuai jumlah."
                coder "Iya. Kita lanjut ke ringkasan."

            if fokus_teknis_ch6 == "validasi_error" or prioritas_teknis_lanjutan == "validasi" or fokus_pengerjaan_ch4 == "form_booking":
                designer "Validasi dasar yang kemarin juga kita cek lagi."
                coder "Iya. Jangan sampai data kosong masuk ke penyimpanan."
            else:
                coder "Gue tambah pemeriksaan wajib paling dasar sebelum data dikirim."
                designer "Nama sama jumlah tiket?"
                coder "Iya. Yang lain tetap perlu tes lanjutan."
                "Beberapa input kosong kini ditolak sebelum melanjutkan."

            if fokus_pengerjaan_ch4 == "data_pemesanan" or fokus_utama_ch5 == "booking" or fokus_teknis_ch6 == "alur_pesanan":
                coder "Struktur data uji lama bisa kita lanjut."
                designer "Berarti nggak perlu nyusun semuanya dari nol."
                coder "Iya. Tapi tetap harus dicek setelah disambung."
            else:
                coder "Kita belum punya jalur data uji yang rapi dari form. Gue buat satu alur lokal yang sederhana."
                designer "Bukan database permanen dulu?"
                coder "Belum. Targetnya alur tes yang konsisten."

            "Luuk menghubungkan hasil form ke ringkasan, lalu ke penyimpanan data uji lokal."
            "Jane memasukkan dua pesanan percobaan yang berbeda dan mengulangi langkahnya."
            designer "Sekarang datanya nggak hilang setelah pindah ke ringkasan."
            coder "Iya, buat alur uji ini."
            designer "Berarti booking udah selesai?"
            coder "Belum. Belum semua kasus gagal, penyimpanan permanen, dan halaman admin kita pastikan."
            designer "Oke. Tulis: alur booking lokal lebih siap diuji."
            "Mereka menyimpan hasil tes tanpa menganggap seluruh sistem telah selesai."
            $ website_progress = min(100, website_progress + 6)
            $ stress_level = max(0, stress_level - 2)

        "Utamakan daftar admin, detail pesanan, dan status data uji.":
            $ prioritas_integrasi_ch7 = "admin"
            coder "Utamakan daftar admin, detail pesanan, dan status data uji."
            designer "Biar waktu demo pengelolanya nggak cuma lihat tabel kosong?"
            coder "Iya. Kita rapihin yang bisa dibaca dari data percobaan."

            if fokus_integrasi_ch6 == "admin":
                coder "Pembacaan data uji dari modul yang sama udah kita mulai."
                designer "Berarti kita lanjut detail sama statusnya."
                coder "Betul."
            elif fokus_lanjutan_ch4 == "admin" or fokus_utama_ch5 == "admin":
                coder "Tabelnya udah ada. Tapi sambungan datanya masih terbatas."
                designer "Oke. Kita tes dengan beberapa data berbeda."
            else:
                coder "Kita masih perlu kerangka admin yang bisa diuji."
                designer "Gue bantu buat kolomnya sederhana."
                "Jane menyiapkan tabel nama pengunjung, jumlah tiket, tanggal, dan status."

            if fokus_pengerjaan_ch4 == "data_pemesanan" or fokus_utama_ch5 == "booking" or fokus_teknis_ch6 == "alur_pesanan":
                designer "Kita bisa coba pakai data dari modul tes pemesanan yang pernah dibuat."
                coder "Iya. Kalau belum nyambung pada satu jalur, kita catat jelas batasnya."
            else:
                designer "Data form asli masih belum punya alur penyimpanan lengkap."
                coder "Iya. Jadi admin kita uji dengan dataset contoh terstruktur dulu."

            "Luuk memperbaiki cara tabel admin membaca data percobaan."
            "Jane memeriksa detail beberapa baris dan mencoba mengubah status simulasi."
            designer "Sekarang nomor dan detail pesanan lebih gampang dicocokkan."
            coder "Iya. Statusnya juga bisa ditampilkan dalam uji lokal."
            designer "Tapi belum berarti semua booking otomatis masuk?"
            coder "Betul. Yang belum terhubung tetap masuk daftar."
            "Halaman admin menjadi lebih bisa didemonstrasikan, tanpa mengklaim integrasi penuh."
            $ website_progress = min(100, website_progress + 5)
            $ stress_level = max(0, stress_level - 2)

    "Jane memeriksa pekerjaan yang baru disimpan."
    designer "Oke, ada hasilnya."
    coder "Iya."
    designer "Tapi bagian yang tadi nggak dipilih masih perlu."
    coder "Jelas. Kita nggak boleh pura-pura dia hilang."
    designer "Setuju."

    # MENU 05 — dialog biasa.
    menu:
        "Satu masalah selesai, yang lain langsung antre.":
            coder "Satu masalah selesai, yang lain langsung antre."
            designer "Kayak antrean kantin?"
            coder "Bedanya ini nggak ngasih makan."
            designer "Pantes lo kesel."

        "Lebih baik ada satu bagian yang jelas daripada semuanya setengah.":
            coder "Lebih baik ada satu bagian yang jelas daripada semuanya setengah."
            designer "Iya. Tapi nanti tetap harus disatukan."
            coder "Betul."

        "Gue mulai hafal bunyi keyboard sendiri.":
            coder "Gue mulai hafal bunyi keyboard sendiri."
            designer "Itu karena lo ngetik terus."
            coder "Kalau bunyinya berhenti, gue curiga."
            designer "Jangan sampai keyboard-nya juga ikut stres."

    "Jane membuka kembali daftar tes dan menandai fitur yang baru diperiksa."
    designer "Nanti kita ulang pakai data yang beda lagi."
    coder "Iya. Satu contoh berhasil belum cukup."
    designer "Terus kalau gagal?"
    coder "Catat langkahnya, baru perbaiki."
    designer "Oke."

    # MENU 06 — dialog biasa.
    menu:
        "Kita simpan versi yang jalan dulu sebelum ngubah lagi.":
            coder "Kita simpan versi yang jalan dulu sebelum ngubah lagi."
            designer "Biar bisa balik kalau rusak?"
            coder "Iya."
            designer "Nah, itu penting."

        "Istirahat sebentar, habis itu cek tugas kuliah.":
            coder "Istirahat sebentar, habis itu cek tugas kuliah."
            designer "Masih ada tugas lain, ya."
            coder "Sayangnya."
            designer "Oke, jangan lupa makan dulu."

    "Mereka menyimpan revisi hari itu dan mencatat bagian yang belum terintegrasi."
    "Pekerjaan bergerak maju, tetapi tidak ada waktu untuk menganggap semua masalah sudah selesai."
    jump ch7_scene_03


# ============================================================
# SCENE 03 — AN ANSWER WE STILL DON'T HAVE | H-8
# MENU 07, 08: dialog biasa; MENU 09: pilihan berpengaruh.
# Bukan bukti Secret Ending keenam.
# ============================================================
label ch7_scene_03:
    $ days_left = 8
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Luuk dan Jane kembali bertemu di kampus setelah kelas."
    "Jane membuka folder bahan koleksi Museum Arunika sambil menunggu Luuk mengeluarkan laptop."
    designer "Luuk."
    coder "Ya?"
    designer "Folder koleksinya masih belum ada kiriman Adrian."
    coder "Masih?"
    designer "Iya."
    coder "Padahal tinggal delapan hari."
    designer "Gue tahu."
    "Jane menunjukkan daftar kebutuhan konten yang sejak awal menjadi tugas Adrian."
    designer "Sepuluh gambar koleksi sama lima deskripsi itu belum kita terima."
    coder "Kalau ada sebagian aja, kita setidaknya bisa cek ukuran dan teks aslinya."
    designer "Iya. Tapi sampai sekarang belum ada."
    "Luuk membaca pesan terakhir di grup."
    if konfirmasi_target_adrian:
        coder "Dulu dia sudah menyetujui tenggat tertulis."
        designer "Iya, tapi file-nya tetap belum masuk."
    else:
        coder "Kita sudah berkali-kali minta kabar."
        designer "Iya. Jawabannya belum bikin kita bisa lanjut konten asli."

    if rekap_pengumpulan_ch5:
        designer "Di rekap berkas juga belum ada kiriman baru."
        coder "Oke. Catat sesuai keadaan folder sekarang."
    else:
        designer "Gue cek langsung folder dan grup. Belum ada file yang bisa dipakai."
        coder "Oke. Jangan asumsi lebih dari itu."

    # MENU 07 — dialog biasa.
    menu:
        "Kita perlu keputusan tentang demo, bukan cuma harapan.":
            coder "Kita perlu keputusan tentang demo, bukan cuma harapan."
            designer "Iya. Kalau bahan belum ada, kita harus tahu apa yang bisa ditampilkan."
            coder "Dan harus jujur soal statusnya."

        "Gue lebih suka jawaban jelas meski belum selesai.":
            coder "Gue lebih suka jawaban jelas meski belum selesai."
            designer "Sama. Kalau ada kendala, kita bisa pikirin jalan lain."
            coder "Iya. Yang bikin susah justru nggak tahu."

        "Kata 'nanti' udah hampir jadi menu utama website.":
            coder "Kata 'nanti' udah hampir jadi menu utama website."
            designer "Jangan sampai lo beneran bikin tombol itu."
            coder "Kalau diklik, muncul tulisan 'belum'."
            designer "Anjir. Jangan kasih ide."

    "Jane menutup folder dan menatap prototipe galeri."
    designer "Gue nggak mau ngisi galeri dengan gambar yang kita nggak tahu boleh dipakai atau nggak."
    coder "Setuju."
    designer "Dan kalau cuma placeholder, harus kelihatan kalau itu contoh."
    coder "Iya. Biar nggak menyesatkan waktu demo."
    designer "Berarti kita punya dua pilihan sementara."
    coder "Apa?"
    designer "Minta kepastian terakhir dari Adrian, atau siapin tampilan demo yang jelas diberi label contoh."
    coder "Dua-duanya masuk akal. Tinggal prioritas kita sekarang."

    # MENU 08 — dialog biasa.
    menu:
        "Jangan masukkan gambar yang asal ketemu di internet.":
            coder "Jangan masukkan gambar yang asal ketemu di internet."
            designer "Iya. Kita harus tahu sumber dan izin pakainya."
            coder "Kalau nggak, lebih aman pakai placeholder yang jelas."

        "Yang penting kita nggak bilang konten contoh sebagai konten final.":
            coder "Yang penting kita nggak bilang konten contoh sebagai konten final."
            designer "Setuju."
            coder "Nanti kalau bahan asli datang, baru dites ulang."

    # MENU 09 — pilihan penting kedua; BUKAN bukti baru.
    menu:
        "Kirim permintaan terakhir yang jelas lewat grup.":
            $ strategi_konten_ch7 = "tenggat"
            coder "Kirim permintaan terakhir yang jelas lewat grup."
            designer "Oke. Kita minta bagian yang sudah ada, bukan cuma jawaban nanti."
            "Jane mengetik pesan di grup dengan kebutuhan berkas dan batas waktu yang jelas."
            "Jane (grup): Adrian, kami butuh kiriman gambar dan deskripsi koleksi untuk finalisasi. Tolong kirim bagian yang sudah ada paling lambat besok sore, atau jelaskan kendalanya sekarang supaya kami bisa menyiapkan demo yang sesuai kondisi sebenarnya."
            "Pesan terkirim, tetapi tidak langsung dibalas."
            designer "Udah."
            coder "Oke. Sambil nunggu, kita tetap kerjain bagian lain."
            designer "Iya. Tapi kali ini kita harus tindak lanjuti."
            "Mereka mencatat bahwa permintaan terakhir sudah disampaikan, tanpa menambah penghitung bukti rahasia."
            $ stress_level = min(100, stress_level + 2)

        "Siapkan galeri demo dengan placeholder yang diberi label jelas.":
            $ strategi_konten_ch7 = "demo"
            coder "Siapkan galeri demo dengan placeholder yang diberi label jelas."
            designer "Oke. Jadi penguji tahu ini contoh tampilan, bukan koleksi asli."
            coder "Iya. Jangan menulis deskripsi seolah-olah itu data museum yang sudah diverifikasi."
            "Jane menambahkan label 'Konten contoh untuk demonstrasi' pada bagian galeri yang belum memiliki bahan asli."
            "Luuk membantu memastikan kartu contoh tidak mengganggu navigasi pada ukuran layar berbeda."
            designer "Nah, sekarang setidaknya galeri bisa dijelaskan dengan jujur."
            coder "Iya. Tapi bahan asli tetap belum tersedia."
            designer "Masuk daftar kendala yang harus kita sampaikan."
            "Tampilan galeri demo menjadi lebih jelas, meskipun ini tidak menggantikan pekerjaan Adrian."
            $ website_progress = min(100, website_progress + 2)
            $ stress_level = max(0, stress_level - 1)

    "Luuk kembali melihat daftar fitur yang harus diperiksa sebelum latihan demo."
    coder "Jangan sampai masalah konten bikin kita berhenti ngetes booking."
    designer "Iya. Dua-duanya perlu ditangani, tapi kerjaan kita tetap lanjut."
    "Delapan hari tersisa, dan urusan galeri belum dapat dianggap selesai."
    $ stress_level = min(100, stress_level + 4)
    jump ch7_scene_04


# ============================================================
# SCENE 04 — A DEMO WITHOUT SHORTCUTS | H-6
# MENU 10, 12: dialog biasa; MENU 11: pilihan penting.
# ============================================================
label ch7_scene_04:
    $ days_left = 6
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Luuk dan Jane memulai latihan demonstrasi di kontrakan Luuk."
    "Mereka menyiapkan data percobaan, daftar pengujian, dan versi website yang terakhir disimpan."
    designer "Oke, hari ini jangan buka halaman langsung dari alamatnya."
    coder "Maksud lo?"
    designer "Ikutin tombol yang beneran bakal diklik pengunjung."
    coder "Setuju."
    "Jane membuka beranda dan mencoba masuk ke alur pemesanan."

    if prioritas_integrasi_ch7 == "booking":
        designer "Alur booking lokal yang kita rapihin kemarin bisa kita coba ulang."
        coder "Iya. Tapi jangan anggap semua kasus langsung aman."
    else:
        designer "Kemarin kita lebih fokus admin. Booking dari awal masih punya bagian yang harus dites."
        coder "Iya. Kalau ada yang belum nyambung, kita tandai apa adanya."

    "Pada salah satu percobaan, tombol kembali menyebabkan data yang ditampilkan tidak sesuai dengan isian sebelumnya."
    designer "Eh, tunggu. Ini datanya beda."
    coder "Yang mana?"
    designer "Jumlah tiket yang tadi gue pilih."
    coder "Oh. Berarti ada keadaan yang belum kita tangani."
    "Luuk mencatat langkah yang membuat masalah itu muncul."
    designer "Kalau kita tadi cuma tes satu arah, ini nggak ketahuan."
    coder "Betul."
    "Mereka mencoba variasi lain dan menemukan satu masalah tampilan status pada halaman lanjutan."
    designer "Jadi bukan cuma satu bug."
    coder "Iya."
    "Luuk memeriksa waktu dan menatap daftar perbaikan."
    $ stress_level = min(100, stress_level + 3)

    # MENU 10 — dialog biasa.
    menu:
        "Bug-nya baru muncul kalau kita benar-benar pakai websitenya.":
            coder "Bug-nya baru muncul kalau kita benar-benar pakai websitenya."
            designer "Berarti tes asal klik tadi belum cukup."
            coder "Iya. Harus ikutin alur."

        "Lebih baik ketahuan sekarang daripada di depan dosen.":
            coder "Lebih baik ketahuan sekarang daripada di depan dosen."
            designer "Jangan bikin gue ngebayangin itu."
            coder "Makanya kita perbaiki."
            designer "Iya."

        "Website ini punya cara sendiri buat ngajarin kesabaran.":
            coder "Website ini punya cara sendiri buat ngajarin kesabaran."
            designer "Ujiannya tiap dua menit."
            coder "Dan nggak ada kisi-kisi."
            designer "Anjir."

    designer "Kita nggak bakal sempat ngerapihin semua hal sekaligus hari ini."
    coder "Iya. Pilih pengujian yang paling perlu dulu."
    designer "Alur pengunjung atau alur pengelola?"
    coder "Itu dua bagian yang paling harus bisa kita jelaskan."

    # MENU 11 — pilihan penting ketiga.
    menu:
        "Uji perjalanan pengunjung dan perbaiki bug penghambat booking.":
            $ fokus_pengujian_ch7 = "pengunjung"
            coder "Uji perjalanan pengunjung dan perbaiki bug penghambat booking."
            designer "Oke. Kita ulang dari beranda, form, sampai ringkasan."
            coder "Pakai dua set data berbeda."
            "Jane mengisi data percobaan, kembali satu langkah, lalu mengubah jumlah tiket."
            if prioritas_integrasi_ch7 == "booking":
                coder "Jalur data uji yang kemarin sudah kita sambungkan bisa dipakai buat perbaikan ini."
                "Luuk memperbaiki cara ringkasan mengambil nilai terbaru dari form."
                designer "Nah, sekarang setelah balik lalu ubah jumlah, ringkasannya ikut berubah."
                coder "Iya. Itu satu kasus yang sudah lolos tes ulang."
            else:
                coder "Karena sambungan booking belum lengkap, kita mulai dari jalur uji yang masih bisa dijalankan."
                "Luuk membetulkan perpindahan tombol dan penyegaran nilai pada ringkasan data contoh."
                designer "Sekarang bagian ini nggak loncat ke halaman yang salah."
                coder "Iya. Tapi penyimpanan pesanan penuh tetap belum selesai."
            if fokus_teknis_ch6 == "validasi_error" or prioritas_teknis_lanjutan == "validasi":
                designer "Pesan validasinya juga gue coba ulang."
                coder "Oke. Catat kalau ada kondisi yang belum ditangani."
            else:
                designer "Masih ada beberapa input salah yang perlu pesan lebih jelas."
                coder "Iya. Kita catat sebagai pekerjaan berikutnya, jangan dianggap sudah aman."
            "Mereka mengulangi rangkaian yang sama dan menyimpan hasil tes yang berhasil serta yang belum."
            "Satu bug penghambat pada jalur pengunjung berkurang, tetapi alur produksi lengkap belum dijamin stabil."
            $ website_progress = min(100, website_progress + 4)
            $ stress_level = max(0, stress_level - 2)

        "Uji pengelolaan pesanan dan halaman konfirmasi simulasi.":
            $ fokus_pengujian_ch7 = "pengelola"
            coder "Uji pengelolaan pesanan dan halaman konfirmasi simulasi."
            designer "Oke. Kita pakai data yang sama di tiap langkah kalau bisa."
            coder "Iya. Dan tandai yang masih pakai data contoh."
            if prioritas_integrasi_ch7 == "admin" or fokus_integrasi_ch6 == "admin":
                designer "Daftar admin yang pernah kita kerjain bisa dites lagi."
                coder "Iya. Gue perbaiki satu masalah pembacaan status yang tadi muncul."
                "Jane mencoba beberapa baris data uji dan melihat detail pesanan."
                designer "Sekarang statusnya lebih konsisten pada data percobaan itu."
            else:
                designer "Bagian admin belum nyambung penuh dari form."
                coder "Iya. Kita tes tabelnya dengan data yang tersedia, tanpa mengklaim semuanya otomatis."
                "Luuk memperbaiki tampilan satu detail data dan alur kembali ke daftar."
                designer "Setidaknya detailnya sekarang nggak ketuker."
            if fokus_integrasi_ch6 == "pembayaran" or fokus_lanjutan_ch5 == "pembayaran" or prioritas_teknis_lanjutan == "pembayaran":
                designer "Halaman pembayaran simulasi yang udah ada bisa kita coba lagi."
                coder "Iya. Pastikan label statusnya nggak bikin orang mengira ada transaksi asli."
            else:
                designer "Bagian pembayaran masih belum punya alur simulasi yang lengkap."
                coder "Iya. Jadi hari ini kita nggak menganggapnya siap diuji. Kita fokus pada data admin contoh."
            "Mereka memperbaiki satu masalah pada halaman lanjutan dan menyimpan hasil uji dengan status yang jelas."
            "Alur pengelolaan pada data contoh menjadi lebih mudah didemonstrasikan, tanpa menjadikannya sistem produksi lengkap."
            $ website_progress = min(100, website_progress + 3)
            $ stress_level = max(0, stress_level - 2)

    designer "Hari ini ada yang berhasil kita beresin."
    coder "Iya."
    designer "Tapi setiap langkah tetap harus dicoba ulang."
    coder "Betul. Jangan sampai perbaikan baru ngerusak halaman lain."

    # MENU 12 — dialog biasa.
    menu:
        "Gue mau menyimpan versi yang sekarang sebelum lanjut.":
            coder "Gue mau menyimpan versi yang sekarang sebelum lanjut."
            designer "Bagus."
            coder "Kalau nanti ada error baru, kita punya pembanding."
            designer "Iya."

        "Kita tulis bagian yang masih gagal, jangan ditutup-tutupin.":
            coder "Kita tulis bagian yang masih gagal, jangan ditutup-tutupin."
            designer "Setuju."
            coder "Lebih enak memperbaiki masalah yang kelihatan."
            designer "Daripada pura-pura nggak ada."

        "Gue minta istirahat lima menit dari kata 'error'.":
            coder "Gue minta istirahat lima menit dari kata 'error'."
            designer "Oke. Kita sebut 'kejutan teknis'."
            coder "Itu malah lebih serem."
            designer "Yaudah, istirahat beneran."

    "Luuk menyimpan perubahan kode dan catatan pengujian."
    "Jane menyimpan rancangan serta status tiap langkah yang berhasil dan belum berhasil."
    "Enam hari tersisa. Mereka mulai menyiapkan demonstrasi yang bisa dijalankan berdasarkan kondisi website yang sebenarnya."
    jump ch7_scene_05


# ============================================================
# SCENE 05 — FOUR DAYS | H-4
# MENU 13, 14, 15: dialog biasa; penutup sebelum H-3.
# ============================================================
label ch7_scene_05:
    $ days_left = 4
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Luuk dan Jane bertemu lagi di area kampus."
    "Mereka tidak membuka fitur baru. Hari itu dipakai untuk melihat apa yang benar-benar sudah bisa didemonstrasikan."
    designer "Woy."
    coder "Woy."
    designer "Gue bawa daftar pengujian terbaru."
    coder "Oke. Gue bawa hasil kode terakhir."
    designer "Berarti kita cocokkan satu-satu."
    coder "Iya."
    "Jane membaca bagian yang sudah diberi tanda."

    if prioritas_integrasi_ch7 == "booking":
        designer "Booking dari form sampai ringkasan data uji sudah lebih nyambung."
        coder "Iya. Tapi penyimpanan permanen dan seluruh kasus gagal masih belum kita tuntaskan."
        designer "Oke, jangan tulis selesai total."
    else:
        designer "Daftar admin dan status data uji sudah lebih jelas."
        coder "Iya. Tapi alur booking pengunjung masih ada sambungan yang belum beres."
        designer "Oke."

    if fokus_pengujian_ch7 == "pengunjung":
        designer "Bug penghambat di jalur pengunjung yang kemarin kita tes sudah berkurang."
        coder "Iya. Itu hasil pada data tes kita, bukan jaminan semua kondisi aman."
    else:
        designer "Data contoh pada admin dan halaman konfirmasi sudah lebih mudah dicek."
        coder "Iya. Tapi beberapa sambungan masih butuh pengujian lanjutan."

    if strategi_konten_ch7 == "demo":
        designer "Galeri demo kita sudah dilabeli sebagai konten contoh."
        coder "Bagus. Jangan sampai orang mengira itu koleksi asli Museum Arunika."
        designer "Bahan aslinya tetap belum ada."
    else:
        designer "Permintaan terakhir ke Adrian sudah kita kirim."
        coder "Ada file yang masuk?"
        designer "Belum ada di folder."
        coder "Oke. Kita harus siap jelasin kondisi kontennya sesuai fakta."

    "Jane melihat kembali daftar pekerjaan Adrian."
    designer "Sampai sekarang kita masih belum punya gambar dan deskripsi yang bisa dipakai dari dia."
    coder "Iya."
    designer "Gue udah capek nanya hal yang sama terus."
    coder "Gue ngerti."
    designer "Tapi gue juga nggak mau kita ngaku itu kerjaan kita kalau memang tugasnya dia."
    coder "Setuju. Kita cukup jelaskan hasil yang benar-benar ada dan siapa yang mengerjakannya."
    "Mereka tidak membahas kemungkinan nilai atau keputusan dosen. Belum ada yang tahu bagaimana presentasi nanti akan berjalan."

    # Bukti Secret Ending tidak bertambah di sini.
    # Kelima pilihan bukti hanya berada pada Chapter 2-6.
    if jumlah_bukti_rahasia >= 3:
        "Jane memeriksa dokumentasi pekerjaan yang mereka simpan selama proyek."
        designer "Setidaknya catatan yang kita simpan cukup membantu buat menjelaskan alur kerja kita."
        coder "Iya. Simpan baik-baik dan jangan ubah isi bukti lama."
        designer "Oke."
    else:
        "Jane membuka daftar tugas dan beberapa catatan yang masih tersedia."
        designer "Nanti kalau ditanya proses kerja, kita jelaskan berdasarkan file dan hasil tes yang ada."
        coder "Iya. Jangan membuat klaim yang nggak bisa kita tunjukkan."
        designer "Setuju."

    designer "Sekarang tinggal empat hari."
    coder "Iya."
    "Luuk menatap tanggal di pojok layar laptopnya."
    "Jumlah hari yang dulu terasa panjang sekarang hampir habis."
    "Ia sadar mereka masih punya pekerjaan penting dan hanya sedikit waktu untuk mengulang pengujian."
    $ stress_level = min(100, stress_level + 5)

    # MENU 13 — dialog biasa.
    menu:
        "Gue mau fokus ke fungsi yang wajib jalan dulu.":
            coder "Gue mau fokus ke fungsi yang wajib jalan dulu."
            designer "Setuju. Yang tambahan bisa ditunda."
            coder "Iya. Jangan mengambil risiko baru."

        "Kalau kita panik, tesnya malah berantakan.":
            coder "Kalau kita panik, tesnya malah berantakan."
            designer "Iya. Makanya satu langkah setiap kali."
            coder "Oke."

        "Empat hari. Kayaknya gue baru kedip kemarin.":
            coder "Empat hari. Kayaknya gue baru kedip kemarin."
            designer "Kalau kedipnya empat puluh hari, itu tidur."
            coder "Gue nggak tidur selama itu."
            designer "Bagus. Kalau iya, tugas lo nggak bakal selesai."

    "Jane menggeser daftar latihan presentasi ke depan Luuk."
    designer "Sebelum presentasi, kita perlu tahu siapa jelasin bagian apa."
    coder "Gue jelasin coding, data, dan fungsi yang gue kerjain."
    designer "Gue jelasin UI/UX, alur pengunjung, dan hasil uji tampilan."
    coder "Bagian Adrian?"
    designer "Kita masih perlu kepastian, tapi jangan bikin-bikin hasil yang belum dia kasih."
    coder "Oke."
    "Keduanya menyusun urutan demonstrasi sesuai fitur yang betul-betul tersedia."

    # MENU 14 — dialog biasa.
    menu:
        "Kita siapkan urutan demo yang bisa diulang.":
            coder "Kita siapkan urutan demo yang bisa diulang."
            designer "Oke. Mulai dari beranda, lalu yang benar-benar bisa kita tes."
            coder "Kalau ada batasan, kita sebutkan jelas."

        "Jangan sampai ada yang mengaku fitur selesai padahal belum.":
            coder "Jangan sampai ada yang mengaku fitur selesai padahal belum."
            designer "Setuju."
            coder "Kalau perlu, tunjukin versi uji dan jelasin keterbatasannya."
            designer "Iya."

        "Gue ingin bisa tidur setelah satu sesi demo yang bersih.":
            coder "Gue ingin bisa tidur setelah satu sesi demo yang bersih."
            designer "Mau gue kasih sertifikat tidur?"
            coder "Kalau bisa beserta libur kuliah."
            designer "Itu gue juga mau."

    "Menjelang sore, Luuk mencoba kembali membuka halaman utama."
    "Website Museum Arunika tampil seperti biasa."
    "Namun, Luuk tahu satu tampilan yang muncul dengan benar belum cukup untuk menjamin seluruh alur aman."
    designer "Besok kita ulang tes terakhir."
    coder "Iya."
    designer "Jangan ngerjain semua sendirian malam ini."
    coder "Gue bakal kabarin kalau nemu masalah."
    designer "Oke. Gue juga cek bagian desain dari rumah."
    "Mereka membereskan laptop dan catatan."

    # MENU 15 — dialog penutup biasa.
    menu:
        "Besok kita tes bersama, pakai data yang sama.":
            coder "Besok kita tes bersama, pakai data yang sama."
            designer "Oke. Biar hasilnya bisa dibandingin."
            coder "Sip."

        "Gue simpan cadangan, terus berhenti dulu malam ini.":
            coder "Gue simpan cadangan, terus berhenti dulu malam ini."
            designer "Bagus."
            coder "Besok baru kita lanjut."
            designer "Setuju."

    "Di jalan pulang, Luuk beberapa kali memikirkan bagian yang belum selesai."
    "Jane masih berjalan dengan ritme biasanya, sesekali mengomentari tugas kuliah yang belum mereka kumpulkan."
    "Mereka tetap bisa bercanda, tetapi keduanya tahu minggu terakhir ini tidak akan mudah."
    "Empat hari lagi, mereka harus membawa hasil pekerjaan yang sebenarnya."
    "Bukan daftar rencana. Bukan tampilan contoh yang disebut final. Bukan janji bahwa bahan akan segera datang."
    "Dan besok, mereka harus menguji semuanya sekali lagi."
    "4 DAYS LEFT."

    $ hud_visible = False
    scene black with fade
    centered "{size=50}CHAPTER 07 COMPLETE{/size}\n{size=36}4 DAYS LEFT{/size}\n{size=28}The Final Checklist."

    jump chapter_8
