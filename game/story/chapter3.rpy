
# ============================================================
# THE DEADLINERS — CHAPTER 03: JUST A FEW MORE THINGS
# 68 DAYS LEFT -> 60 DAYS LEFT
# Ren'Py 8.5.3
# ============================================================

# MENU 02:
# True = tes booking dahulu.
# False = mengerjakan kerangka galeri dahulu.
default uji_booking_dulu = False

# MENU 09:
# True = menyimpan chat pembagian tugas sebagai dokumentasi.
default arsip_chat_kelompok_tersimpan = False

# MENU 11:
# "validasi" = memperbaiki validasi form.
# "pembayaran" = membuat simulasi pembayaran.
default prioritas_teknis_lanjutan = ""

# Variabel dari Chapter 2 yang kita gunakan:
# form_tiket_dikerjakan_dulu
# prioritas_pengerjaan_website
# catatan_progres_dibuat
# jumlah_bukti_rahasia
#
# Jangan membuat default kedua untuk variabel di atas.


# ============================================================
# PEMBUKA CHAPTER 3
# ============================================================

label chapter_3:

    $ hud_visible = False
    $ days_left = 68

    scene black with fade

    centered "{size=50}CHAPTER 03{/size}\n{size=42}JUST A FEW MORE THINGS{/size}\n{size=34}68 DAYS LEFT{/size}"

    jump ch3_scene_01


# ============================================================
# SCENE 01 — BACK TO THE LIST
# 68 DAYS LEFT
#
# MENU 01: Candaan kuliah.
# MENU 02: Pilihan penting, booking atau galeri.
# MENU 03: Candaan pengingat Jane.
# ============================================================

label ch3_scene_01:

    $ days_left = 68

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Seminggu berlalu sejak terakhir kali Luuk dan Jane membahas daftar fitur Museum Arunika secara lengkap."

    "Mereka masih mengerjakan proyek itu sesekali, tetapi tugas kuliah lain mulai menyita perhatian."

    "Siang itu, Luuk duduk di dekat tempat fotokopi kampus."

    "Di depannya ada laptop, sebotol air mineral, dan beberapa lembar tugas yang belum selesai."

    "Jane datang membawa map dan minuman dingin."

    designer "Woy."

    coder "Woy."

    designer "Udah lama?"

    coder "Baru sepuluh menit."

    designer "Tumben nggak telat."

    coder "Kenapa tiap gue tepat waktu selalu jadi pembahasan?"

    designer "Karena biasanya ada yang bisa dibahas."

    coder "Reputasi gue buruk banget, ya."

    designer "Lumayan."

    "Jane meletakkan tasnya dan duduk."

    designer "Eh, yang tugas Kecerdasan Buatan udah lo kumpulin?"

    coder "Udah."

    designer "Serius?"

    coder "Iya."

    designer "Wah."

    coder "Kenapa lagi?"

    designer "Nggak, gue lagi mengapresiasi perkembangan karakter lo."

    coder "Gue bukan karakter game."

    designer "Iya, iya."


    # ========================================================
    # MENU 01 — CANDAAN KULIAH
    # Tiga opsi, hanya mengubah dialog.
    # ========================================================

    menu:

        "Perkembangan karakter gue mahal, tahu.":

            coder "Perkembangan karakter gue mahal, tahu."

            designer "Dibayar pakai apa?"

            coder "Nilai bagus."

            designer "Berarti belum cair."

            coder "Jahat banget."


        "Lo sendiri udah kumpulin?":

            coder "Lo sendiri udah kumpulin?"

            designer "Udah dong."

            coder "Kapan?"

            designer "Lima menit sebelum deadline."

            coder "Berarti kita sama aja."

            designer "Beda. Gue empat menit lebih awal dari bencana."


        "Kita bahas museum aja sebelum gue dihina lagi.":

            coder "Kita bahas museum aja sebelum gue dihina lagi."

            designer "Lah, gue belum mulai."

            coder "Justru itu yang gue takutkan."

            designer "Yaudah, buka proyeknya."


    # ========================================================
    # LANJUTAN SCENE 01
    # ========================================================

    "Luuk membuka folder Museum Arunika."

    "Jane mengeluarkan laptopnya dan membuka rancangan terbaru."

    designer "Oke. Sekarang kita cek satu-satu."

    coder "Beranda dulu?"

    designer "Boleh."

    coder "Beranda udah ada. Walaupun belum persis desain lo."

    designer "Iya, nanti gue bantu rapihin."

    coder "Halaman informasi museum juga udah mulai."

    designer "Jam buka sama harga tiket udah dimasukin?"

    coder "Baru data sementara. Belum final."

    designer "Oke. Nanti kita tentuin yang konsisten."

    coder "Terus galeri..."

    "Luuk membuka halaman koleksi."

    "Beberapa kotak gambar kosong muncul di layar."

    designer "Masih begini?"

    coder "Iya. Bahan dari Adrian belum masuk."

    designer "Dia belum kirim apa-apa juga?"

    coder "Belum ada di folder."

    designer "Hmm. Nanti gue tanyain lagi."

    coder "Oke."


    # ========================================================
    # PENGARUH PILIHAN CHAPTER 2 — MENU 04
    #
    # Kalau coding dulu:
    # Perhitungan harga sudah bekerja.
    #
    # Kalau Marvel dulu:
    # Perhitungan harga belum selesai.
    # ========================================================

    if form_tiket_dikerjakan_dulu:

        coder "Kalau form tiket, perhitungan totalnya udah jalan."

        designer "Yang jumlah tiket dikali harga itu?"

        coder "Iya. Tapi jangan dites aneh-aneh dulu."

        designer "Aneh gimana?"

        coder "Masukin jumlah negatif, misalnya."

        designer "Lah, emangnya bisa?"

        coder "Nah. Itu yang belum gue cegah."

        designer "Oh, berarti masih harus dites."

    else:

        coder "Kalau form tiket, perhitungan totalnya belum selesai."

        designer "Yang kemarin mau lo lanjutin?"

        coder "Iya."

        designer "Oh, oke. Berarti masih masuk daftar."

        coder "Iya. Kemarin keburu ngerjain tugas lain."

        designer "Nggak apa-apa. Nanti lanjut."


    designer "Terus halaman booking-nya gimana sekarang?"


    # ========================================================
    # PENGARUH PILIHAN CHAPTER 2 — MENU 08
    #
    # "fungsi" = fungsi booking lebih berkembang.
    # "desain" = tampilan lebih rapi.
    # ========================================================

    if prioritas_pengerjaan_website == "fungsi":

        coder "Alurnya udah lebih kebentuk. Pilihan tanggal sama data pengunjung mulai nyambung."

        designer "Tapi tampilannya masih agak polos."

        coder "Iya. Lo pasti mau ngomong itu."

        designer "Nggak, gue cuma menyampaikan fakta."

        coder "Fakta yang menyakitkan."

        designer "Nanti gue rapihin lagi."

    else:

        designer "Tampilannya udah lumayan mirip prototype gue."

        coder "Iya. Versi mobile juga lebih rapi."

        designer "Nah, kan."

        coder "Tapi beberapa tombolnya masih belum ngapa-ngapain."

        designer "Oh, iya."

        coder "Jadi jangan cuma dilihat."

        designer "Iya, harus dipencet juga."


    "Jane membuka daftar pekerjaan yang mereka rencanakan."


    # ========================================================
    # PENGARUH PILIHAN CHAPTER 2 — MENU 12
    #
    # Pemain memilih catatan progres atau merapikan folder.
    # ========================================================

    if catatan_progres_dibuat:

        designer "Untung kemarin kita bikin catatan progres."

        coder "Iya. Jadi kelihatan mana yang udah."

        designer "Gue update bagian desain, ya."

        coder "Sip. Gue update form tiket."

        "Jane mengisi tanggal dan bagian pekerjaan terakhir."

        "Kolom milik Adrian masih belum memiliki hasil yang bisa dicatat."

    else:

        designer "Untung folder kemarin udah kita rapihin."

        coder "Iya. Setidaknya sekarang file booking nggak ada tiga versi."

        designer "Yang 'baru_banget' udah dihapus?"

        coder "Udah."

        designer "Syukurlah."

        "Mereka melihat beberapa file pekerjaan yang tersusun lebih teratur, meskipun belum mempunyai catatan progres mingguan khusus."


    designer "Oke, sekarang kita mau ngerjain yang mana?"

    coder "Ada beberapa pilihan."

    designer "Yang paling gampang dulu?"

    coder "Atau yang paling perlu."

    designer "Hmm, dua-duanya masuk akal."

    coder "Nah, itu."


    # ========================================================
    # MENU 02 — PILIHAN PENTING
    #
    # A. Tes booking dahulu.
    #    uji_booking_dulu = True
    #
    # B. Kerjakan galeri dahulu.
    #    uji_booking_dulu = False
    #
    # Pilihan ini memengaruhi Scene 02 dan Scene 05.
    # ========================================================

    menu:

        "Kita uji alur booking dulu.":

            $ uji_booking_dulu = True

            coder "Kita uji alur booking dulu."

            designer "Oke. Jadi nanti kita pura-pura pesan tiket?"

            coder "Iya. Dari pilih tanggal sampai konfirmasi."

            designer "Boleh. Gue jadi pengunjung."

            coder "Emang itu yang mau dites."

            designer "Siap. Pelanggan pertama Museum Arunika."

            coder "Museumnya aja fiktif."

            designer "Pelanggannya juga."

            "Mereka memutuskan akan menguji alur booking saat bertemu di kontrakan Luuk."


        "Kita isi kerangka halaman koleksi dulu.":

            $ uji_booking_dulu = False

            coder "Kita isi kerangka halaman koleksi dulu."

            designer "Oh, yang kotak-kotak kosong itu?"

            coder "Iya. Bikin komponen kartunya dulu. Nanti gambar sama deskripsi tinggal dimasukin."

            designer "Boleh. Gue bikin template yang konsisten."

            coder "Jadi nggak harus bongkar layout nanti."

            designer "Oke. Berarti pakai konten sementara dulu."

            "Mereka memutuskan akan memperbaiki kerangka galeri sebelum melanjutkan pengujian alur booking."


    designer "Besok gue bisa ke kontrakan lo."

    coder "Jam berapa?"

    designer "Siang aja."

    coder "Oke."

    designer "Eh, jangan lupa tugas Pancasila."

    coder "Kenapa lo selalu mengingatkan tugas lain pas kita baru semangat ngerjain satu tugas?"

    designer "Biar seimbang."

    coder "Seimbang apanya?"

    designer "Penderitaannya."


    # ========================================================
    # MENU 03 — CANDAAN PENGINGAT JANE
    # Dua opsi, hanya dialog.
    # ========================================================

    menu:

        "Gue mau unsubscribe dari pengingat lo.":

            coder "Gue mau unsubscribe dari pengingat lo."

            designer "Nggak bisa."

            coder "Kenapa?"

            designer "Paketnya permanen."

            coder "Waduh."


        "Tolong ingetin yang menyenangkan juga.":

            coder "Tolong ingetin yang menyenangkan juga."

            designer "Oke. Nanti malam Marvel?"

            coder "Itu baru pengingat yang bagus."

            designer "Tapi setelah tugas."

            coder "Yah."


    # ========================================================
    # PENUTUP SCENE 01
    # ========================================================

    "Luuk menutup daftar pekerjaan."

    "Beberapa bagian Museum Arunika memang mulai terbentuk."

    "Namun, semakin sering mereka memeriksanya, semakin banyak hal kecil yang harus ditambahkan ke daftar."

    designer "Yaudah. Besok kita lanjut."

    coder "Sip."

    designer "Pelan-pelan aja. Masih ada waktu."

    coder "Iya."

    "Mereka membereskan laptop masing-masing."

    "Tidak ada yang terlalu mengkhawatirkan bagi mereka hari itu."

    "Masih 68 hari tersisa."

    $ website_progress = min(100, website_progress + 2)

    jump ch3_scene_02


# ============================================================
# SCENE 02 — THE TEST BOOKING
# 66 DAYS LEFT
#
# MENU 04: Nama pengunjung.
# MENU 05: Candaan debugging.
# MENU 06: Candaan pembayaran.
# ============================================================

label ch3_scene_02:

    $ days_left = 66

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Jane kembali datang ke kontrakan Luuk."

    "Ia membawa laptop, minuman, dan sebuah bungkus makanan."

    designer "Permisi."

    coder "Masuk aja."

    designer "Gue bawa makanan."

    coder "Tumben baik."

    designer "Emang biasanya gue jahat?"

    coder "Nggak. Cuma mencurigakan."

    designer "Yaudah, gue makan sendiri."

    coder "Bercanda."

    "Jane duduk dan mengeluarkan laptop."

    designer "Oke. Hari ini ngapain dulu?"

    coder "Sesuai rencana kemarin."


    # ========================================================
    # PENGARUH MENU 02 CHAPTER 3
    #
    # True = menguji booking.
    # False = mengerjakan galeri.
    # ========================================================

    if uji_booking_dulu:

        coder "Kita tes booking."

        designer "Siap. Gue jadi pelanggan."

        coder "Tunggu. Gue jalanin server lokalnya dulu."

        "Luuk membuka website Museum Arunika."

        "Jane memperhatikan halaman booking."

        designer "Oke. Jadi gue pilih tanggal dulu?"

        coder "Iya."

        designer "Tanggal berapa?"

        coder "Bebas. Ini buat tes."

        designer "Kalau tanggal kemarin?"

        coder "Nah, itu yang harus dicegah."

        designer "Oh, jadi jangan dulu?"

        coder "Boleh dicoba nanti."


        # Jika coding sudah dikerjakan pada Chapter 2.
        if form_tiket_dikerjakan_dulu:

            "Jane memilih jumlah tiket."

            "Angka total harga di bagian ringkasan ikut berubah."

            designer "Nah, yang ini udah jalan."

            coder "Iya. Kemarin gue beresin."

            designer "Kalau jumlahnya nol?"

            coder "Coba."

            "Jane memasukkan angka nol."

            "Total harga menjadi nol, tetapi formulir masih mengizinkan proses dilanjutkan."

            designer "Lah, bisa beli nol tiket."

            coder "Nah. Validasi."

            designer "Catat."

        else:

            "Jane memilih beberapa tiket."

            "Bagian total harga masih belum menampilkan perhitungan yang benar."

            designer "Oh, yang ini belum."

            coder "Iya. Gue beresin sekarang."

            "Luuk kembali membuka kode."

            "Ia menambahkan perhitungan harga berdasarkan jumlah tiket yang dipilih."

            "Percobaan pertama belum berhasil."

            coder "Lah, kok malah jadi teks?"

            designer "Hah?"

            coder "Nilai input-nya belum diubah jadi angka."

            designer "Oh."

            coder "Bentar."

            "Setelah beberapa kali mencoba, total harga akhirnya ikut berubah ketika jumlah tiket diganti."

            designer "Nah, sekarang jalan."

            coder "Iya. Tinggal validasi sama konfirmasinya."

    else:

        coder "Kita lanjut halaman koleksi dulu."

        designer "Oke. Gue buka desainnya."

        "Jane membuka rancangan galeri yang pernah ia buat."

        "Ia sudah menyiapkan beberapa variasi kartu koleksi."

        coder "Yang ini kalau layarnya kecil gimana?"

        designer "Gue mau bikin jadi satu kolom."

        coder "Oke. Jadi gambar di atas, teks di bawah."

        designer "Iya."

        "Luuk mulai menulis struktur kartu koleksi."

        "Jane memperbaiki ukuran gambar dan jarak antar elemen."

        "Beberapa kartu dengan gambar sementara muncul di halaman galeri."

        designer "Nah, sekarang udah lebih kebentuk."

        coder "Iya. Tinggal isi sebenarnya."

        designer "Yang masih nunggu Adrian."

        coder "Iya."


        # Kondisi form tiket dari Chapter 2.
        if form_tiket_dikerjakan_dulu:

            designer "Untung bagian total harga udah selesai kemarin."

            coder "Iya. Nanti tinggal kita tes lebih lengkap."

        else:

            designer "Berarti bagian total harga masih belum selesai, ya?"

            coder "Iya. Sekarang gue fokus ke galeri dulu."

            designer "Oke. Kita masukin ke daftar pekerjaan berikutnya."


    # ========================================================
    # LANJUTAN SCENE 02
    # ========================================================

    "Setelah beberapa waktu, Jane kembali membuka halaman booking untuk memeriksa tampilannya."

    designer "Eh, boleh gue coba isi data pengunjung?"

    coder "Boleh."

    designer "Nama siapa?"

    coder "Bebas."

    designer "Oke."


    # ========================================================
    # MENU 04 — CANDAAN NAMA PENGUNJUNG
    # Tiga opsi, hanya dialog.
    # ========================================================

    menu:

        "Pakai nama lo aja.":

            coder "Pakai nama lo aja."

            designer "Gue jadi pengunjung pertama?"

            coder "Iya."

            designer "Dapet diskon?"

            coder "Nggak."

            designer "Pelayanan yang buruk."


        "Tulis 'Pengunjung Misterius'.":

            coder "Tulis 'Pengunjung Misterius'."

            designer "Ini museum atau film detektif?"

            coder "Kan cuma tes."

            designer "Nanti kalau datanya muncul di admin, gue takut sendiri."


        "Nama gue aja, biar kelihatan profesional.":

            coder "Nama gue aja, biar kelihatan profesional."

            designer "Profesional dari mana?"

            coder "Dari nama pemesannya."

            designer "Oke, Pak Luuk."

            coder "Jangan gitu juga."


    "Jane mencoba mengisi kolom nama, nomor telepon, dan jumlah tiket."

    "Beberapa saat kemudian, ia menghapus isi kolom nama."

    designer "Eh, kalau gue kosongin ini gimana?"

    coder "Coba."

    "Jane menekan tombol konfirmasi."

    "Halaman belum memberikan peringatan yang jelas."

    designer "Oh."

    coder "Nah, itu salah satunya."

    designer "Harusnya ada tulisan wajib diisi, kan?"

    coder "Iya."

    designer "Yang tanggal juga."

    coder "Betul."

    designer "Yang jumlah tiket juga."

    coder "Iya."

    designer "Banyak juga."

    coder "Makanya perlu dites."

    designer "Gue kira tinggal bikin form, selesai."

    coder "Kalau cuma ditampilin, iya."

    designer "Kalau dipakai orang?"

    coder "Baru ketahuan masalahnya."

    "Luuk membuat daftar beberapa masalah yang baru ditemukan."

    "Data pengunjung kosong belum dicegah."

    "Tanggal yang sudah lewat belum ditolak."

    "Jumlah tiket masih perlu diperiksa."

    "Halaman konfirmasi belum lengkap."

    designer "Ini baru satu halaman?"

    coder "Iya."

    designer "Hmm."

    coder "Kenapa?"

    designer "Berarti website kita punya banyak kesempatan buat menemukan error."

    coder "Cara berpikir yang positif."


    # ========================================================
    # MENU 05 — CANDAAN DEBUGGING
    # Dua opsi, hanya dialog.
    # ========================================================

    menu:

        "Kita sebut aja fitur yang belum ditemukan.":

            coder "Kita sebut aja fitur yang belum ditemukan."

            designer "Itu bukan fitur."

            coder "Belum tentu."

            designer "Luuk."

            coder "Oke, error."


        "Bagus, ketahuannya sekarang.":

            coder "Bagus, ketahuannya sekarang."

            designer "Iya juga, sih."

            coder "Daripada pas presentasi."

            designer "Jangan sampai."

            coder "Makanya kita catat dulu."


    designer "Eh, nanti pembayaran tiketnya gimana?"

    coder "Simulasi."

    designer "Iya, tapi tampilannya?"

    coder "Ada pilihan metode, terus halaman konfirmasi, habis itu status pembayaran."

    designer "Kayak checkout?"

    coder "Kurang lebih. Tapi nggak ada transaksi beneran."

    designer "Oke, berarti jangan sampai ada orang yang beneran transfer."

    coder "Jelas."

    designer "Bagian statusnya nanti apa?"

    coder "Misalnya 'Menunggu Pembayaran' sama 'Pembayaran Berhasil' buat simulasi."

    designer "Kalau gagal?"

    coder "Bisa dibuat juga."

    designer "Wah, nanti gue desain."

    coder "Iya. Tapi jangan terlalu rumit dulu."

    designer "Gue tahu, gue tahu."

    "Jane melihat layar laptopnya."

    designer "Eh, bentar. Gue mau ambil minum."

    coder "Ambil aja."

    designer "Lo mau?"

    coder "Boleh."

    designer "Bayar."

    coder "Lah."

    designer "Simulasi pembayaran."

    coder "Oh, jadi gini rasanya."


    # ========================================================
    # MENU 06 — CANDAAN PEMBAYARAN
    # Tiga opsi, hanya dialog.
    # ========================================================

    menu:

        "Metodenya transfer senyuman.":

            coder "Metodenya transfer senyuman."

            designer "Nggak diterima."

            coder "QRIS?"

            designer "Nggak."

            coder "Tunai?"

            designer "Ambil sendiri minumnya."


        "Masukin ke database utang.":

            coder "Masukin ke database utang."

            designer "Emang udah ada databasenya?"

            coder "Belum."

            designer "Berarti aman."

            coder "Kok malah seneng?"


        "Nanti statusnya 'Pembayaran Gagal'.":

            coder "Nanti statusnya 'Pembayaran Gagal'."

            designer "Berarti minumnya nggak jadi dikasih."

            coder "Kejam amat sistemnya."

            designer "Sistem yang lo bikin sendiri."

            coder "Oh, iya."


    # ========================================================
    # PENUTUP SCENE 02
    # ========================================================

    "Menjelang sore, mereka menyimpan hasil pekerjaan."

    if uji_booking_dulu:

        "Alur booking telah mereka uji lebih jauh."

        "Perhitungan total harga kini bekerja, tetapi validasi data dan konfirmasi pemesanan masih perlu diperbaiki."

        # Progres website bertambah 4.
        $ website_progress = min(100, website_progress + 4)

    else:

        "Kerangka galeri sudah lebih rapi dan mudah diisi."

        "Namun data koleksi sebenarnya belum tersedia."

        "Alur booking juga masih menunggu pengujian lebih lanjut."

        # Progres website bertambah 3.
        $ website_progress = min(100, website_progress + 3)


    designer "Lumayan hari ini."

    coder "Iya."

    designer "Besok kita lanjut?"

    coder "Lihat tugas kuliah dulu."

    designer "Oh, iya. Besok ada PBO."

    coder "Jangan bilang."

    designer "Kenapa?"

    coder "Baru mau merasa produktif."

    designer "Yaudah, hari ini produktif dulu."

    "Mereka tertawa dan mulai membereskan meja."

    "Meskipun satu bagian sudah lebih baik, daftar pekerjaan mereka belum menjadi lebih pendek."

    jump ch3_scene_03


# ============================================================
# SCENE 03 — NOTHING IN THE FOLDER
# 64 DAYS LEFT
#
# MENU 07: Candaan Adrian.
# MENU 08: Candaan fitur tambahan.
# MENU 09: Bukti rahasia kedua.
# ============================================================

label ch3_scene_03:

    $ days_left = 64

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Luuk dan Jane bertemu setelah menyelesaikan kelas."

    "Keduanya duduk di salah satu bangku koridor kampus."

    "Luuk sedang melihat ponselnya ketika Jane mengeluarkan laptop dari tas."

    designer "Luuk."

    coder "Hm?"

    designer "Adrian ada masuk kelas tadi?"

    coder "Kayaknya nggak."

    designer "Oh."

    coder "Kenapa?"

    designer "Nggak. Gue mau nanya langsung soal gambar museum."

    coder "Chat aja dulu."

    designer "Udah, kemarin."

    coder "Dibales?"

    designer "Belum."

    "Jane membuka grup Museum Arunika."

    "Di sana masih terlihat permintaan bahan koleksi yang sebelumnya sudah mereka kirim."

    designer "Ini yang gue kirim dua hari lalu."

    coder "Hmm."

    designer "Udah dibaca."

    coder "Coba tanya lagi."

    designer "Oke."

    "Jane mengetik sebuah pesan baru."

    "Jane (grup): Adrian, yang 10 gambar referensi sama 5 deskripsi koleksi udah ada belum?"

    "Jane (grup): Kalau ada yang udah jadi, kirim dulu aja."

    "Pesan terkirim."

    "Luuk mengalihkan perhatian ke laptop Jane."

    coder "Galeri yang kemarin gimana?"

    designer "Layout-nya udah lumayan."

    coder "Tinggal konten."

    designer "Iya."

    coder "Kalau bahannya lama, kita tetap bisa ngerjain bagian lain dulu."

    designer "Bener juga."

    "Beberapa menit kemudian, ponsel Jane bergetar."

    designer "Oh, dibales."

    "Adrian (grup): Belum."

    designer "..."

    coder "Cuma itu?"

    designer "Iya."

    coder "Hmm."

    designer "Gue coba tanya kapan bisa dikirim."

    "Jane (grup): Kira-kira kapan bisa dikirim? Biar bagian galeri bisa kita lanjut."

    "Adrian (grup): Nanti saya cari."

    "Tidak ada penjelasan tambahan."

    "Tidak ada file yang dikirim."

    designer "Nanti itu kapan, ya?"

    coder "Nggak tahu."

    designer "Gue kira udah ada beberapa."

    coder "Sama."

    designer "Padahal yang kita minta gambar referensi sama deskripsi singkat."

    coder "Iya."

    designer "Bukan bikin museum beneran."

    coder "Untung."

    designer "Kenapa?"

    coder "Kalau disuruh bangun museum, kita butuh semen."

    designer "Anjir."


    # ========================================================
    # MENU 07 — CANDAAN SOAL ADRIAN
    # Dua opsi, hanya dialog.
    # ========================================================

    menu:

        "Jangan-jangan dia masih cari museumnya.":

            coder "Jangan-jangan dia masih cari museumnya."

            designer "Museum Arunika kan fiktif."

            coder "Nah, mungkin itu masalahnya."

            designer "Masa nyari museum yang nggak ada?"

            coder "Perjalanan yang panjang."

            designer "Tolong jangan bikin gue ketawa."


        "Mungkin dia belum sempat.":

            coder "Mungkin dia belum sempat."

            designer "Bisa jadi."

            coder "Tapi udah beberapa minggu."

            designer "Iya, sih."

            coder "Nanti kita ingetin lagi."

            designer "Oke."


    # ========================================================
    # LANJUTAN SCENE 03
    # ========================================================

    "Jane menyimpan ponselnya."

    "Ia kemudian membuka halaman galeri yang sedang dikerjakan."

    designer "Kalau kita nunggu terus, nanti gue nggak bisa lihat hasil desainnya."

    coder "Ya pakai placeholder dulu."

    designer "Udah. Tapi gue pengin lihat kalau ada gambar benerannya."

    coder "Coba sementara pakai gambar uji yang bebas dipakai."

    designer "Buat ngetes layout?"

    coder "Iya. Bukan konten final."

    designer "Oke. Nanti dibedain jelas, ya."

    coder "Iya. Jangan sampai gambar uji ikut masuk presentasi."

    designer "Nah, itu."

    "Jane memperlihatkan beberapa kartu koleksi yang sudah memiliki kerangka gambar, judul, dan deskripsi."

    designer "Yang ini nanti buat deskripsi pendek."

    coder "Oke."

    designer "Kalau teksnya kepanjangan, kartunya jadi beda tinggi."

    coder "Bisa dibatasi."

    designer "Tapi kalau deskripsinya penting?"

    coder "Bisa ada tombol lihat detail."

    designer "Oh, bagus juga."

    coder "Cuma berarti nambah satu pekerjaan."

    designer "..."

    coder "Kenapa?"

    designer "Kita baru aja nambah fitur lagi, ya?"

    coder "Iya."

    designer "Hmm."

    coder "Mau dibatalin?"

    designer "Nggak. Bagus kok idenya."

    coder "Oke. Masuk daftar."

    designer "Daftarnya makin panjang."

    coder "Tapi masih bisa dikerjain."

    designer "Iya."


    # ========================================================
    # MENU 08 — CANDAAN FITUR TAMBAHAN
    # Tiga opsi, hanya dialog.
    # ========================================================

    menu:

        "Setiap ngobrol, lahir fitur baru.":

            coder "Setiap ngobrol, lahir fitur baru."

            designer "Berarti kita kreatif."

            coder "Kreatif bikin kerjaan."

            designer "Setidaknya bukan kehabisan ide."

            coder "Iya, ide kita kebanyakan."


        "Jangan sampai websitenya jadi aplikasi segala.":

            coder "Jangan sampai websitenya jadi aplikasi segala."

            designer "Kenapa?"

            coder "Nanti ada fitur login, profil, notifikasi..."

            designer "Eh, notifikasi booking bagus juga."

            coder "JANE."

            designer "Bercanda!"


        "Yang penting fitur yang wajib dulu.":

            coder "Yang penting fitur yang wajib dulu."

            designer "Iya. Yang tambahan nanti aja."

            coder "Beranda, koleksi, booking, pembayaran simulasi, sama admin."

            designer "Oke, itu dulu."

            coder "Jangan tiba-tiba nambah fitur lain."

            designer "Nggak janji."


    # ========================================================
    # LANJUTAN SCENE 03
    # ========================================================

    "Luuk membuka kembali grup Museum Arunika."

    "Belum ada pesan tambahan dari Adrian."

    coder "Eh, chat pembagian tugas yang dulu masih ada, kan?"

    designer "Ada. Kenapa?"

    coder "Gue mau lihat yang tugas masing-masing."

    designer "Tunggu, gue scroll."

    "Jane menemukan pesan lama yang berisi pembagian pekerjaan pada awal proyek."

    "Tertulis bahwa Luuk mengurus struktur website dan sistem pemesanan tiket."

    "Jane bertanggung jawab terhadap UI/UX dan prototype."

    "Adrian mendapat tugas mengumpulkan sepuluh gambar referensi serta lima deskripsi koleksi singkat."

    designer "Nah, ini."

    coder "Oh, iya."

    designer "Kita nentuin tugasnya waktu itu."

    coder "Iya. Biar nggak ketuker."

    designer "Eh, sekalian kita perlu nyimpen informasi yang penting nggak, sih?"

    coder "Boleh juga."

    designer "Mau gimana?"


    # ========================================================
    # MENU 09 — BUKTI RAHASIA KEDUA
    #
    # Pilihan A:
    # Simpan arsip chat pembagian tugas.
    # +1 jumlah_bukti_rahasia.
    #
    # Pilihan B:
    # Membuat pengingat HP.
    # Tidak menambah bukti.
    #
    # Poin tidak ditampilkan kepada pemain.
    # Bukti pertama dari Chapter 2 tetap tersimpan.
    # ========================================================

    menu:

        "Simpan salinan chat pembagian tugas ke folder proyek.":

            # Tambah bukti hanya jika belum dimiliki.
            if not arsip_chat_kelompok_tersimpan:
                $ jumlah_bukti_rahasia += 1

            $ arsip_chat_kelompok_tersimpan = True

            coder "Simpan salinan chat pembagian tugas ke folder proyek aja."

            designer "Screenshot?"

            coder "Iya. Yang pembagian tugas sama update pekerjaan terakhir."

            designer "Boleh. Biar nggak perlu scroll jauh."

            coder "Simpan tanggalnya juga, ya."

            designer "Oke."

            "Jane menyimpan tangkapan layar pembagian tugas awal, permintaan pembaruan bahan koleksi, serta balasan Adrian yang menyatakan pekerjaannya belum selesai."

            "Ia menyimpannya di folder dokumentasi proyek dengan nama yang mudah dikenali."

            designer "Udah."

            coder "Sip."

            designer "Kalau nanti butuh lihat pembagian awal, tinggal buka folder ini."

            coder "Iya. Lebih praktis."

            if catatan_progres_dibuat:

                designer "Sekalian gue cocokkin sama catatan progres kemarin."

                coder "Oke."

                designer "Bagian yang belum ada hasilnya tetap gue kosongin dulu."

                coder "Iya. Nanti diisi kalau ada file masuk."

            else:

                designer "Untung folder proyek kemarin udah rapi."

                coder "Iya. Tinggal bikin folder dokumentasinya."

                designer "Udah, gue taruh di situ."

                coder "Sip."


        "Cukup bikin pengingat tenggat di catatan HP.":

            $ arsip_chat_kelompok_tersimpan = False

            # Tidak menambahkan jumlah_bukti_rahasia.

            coder "Cukup bikin pengingat tenggat di catatan HP aja."

            designer "Boleh. Biar nggak kelupaan."

            coder "Tulis yang masih kurang."

            designer "Oke. Gambar koleksi, deskripsi, terus kita perlu cek form tiket lagi."

            coder "Iya."

            "Jane membuat pengingat baru berisi pekerjaan yang belum selesai dan perkiraan waktu pengerjaan."

            designer "Udah. Nanti gue cek lagi."

            coder "Sip."

            if catatan_progres_dibuat:

                designer "Nanti kalau ada hasil baru, catatan progres kita update juga."

                coder "Iya."

            else:

                designer "Paling nggak sekarang ada pengingatnya."

                coder "Iya. Biar nggak kelewat."


    # ========================================================
    # PENUTUP SCENE 03
    # ========================================================

    "Tidak ada perubahan besar pada sore itu."

    "Adrian tetap belum mengirim bahan museum."

    "Luuk dan Jane masih menggunakan konten sementara untuk halaman koleksi."

    designer "Yaudah, kita kerjain yang bisa dulu."

    coder "Iya."

    designer "Kalau dia udah kirim, nanti gue masukin."

    coder "Sip."

    "Jane menutup laptopnya."

    "Luuk memeriksa daftar pekerjaan mereka sekali lagi."

    "Beberapa pekerjaan sudah bergerak."

    "Beberapa lainnya masih berada di tempat yang sama."

    "Tidak ada alasan bagi mereka untuk berhenti, tetapi mereka juga belum merasa perlu terburu-buru."

    "Masih 64 hari tersisa."

    $ website_progress = min(100, website_progress + 1)

    jump ch3_scene_04


# ============================================================
# SCENE 04 — ONE PROBLEM AT A TIME
# 62 DAYS LEFT
#
# MENU 10: Candaan website.
# MENU 11: Pilihan penting teknis.
# MENU 12: Candaan programmer.
# ============================================================

label ch3_scene_04:

    $ days_left = 62

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari berikutnya, Luuk kembali mengerjakan Museum Arunika dari kontrakannya."

    "Namun, pagi hingga siang dihabiskan untuk menyelesaikan tugas mata kuliah lain."

    "Baru menjelang sore ia membuka folder proyek museum."

    "Beberapa menit kemudian, Jane menghubunginya."

    "Jane (chat): Luuk."

    "Luuk (chat): Apa?"

    "Jane (chat): Lagi coding?"

    "Luuk (chat): Baru mau."

    "Jane (chat): Gue ke sana, ya?"

    "Luuk (chat): Boleh."

    "Jane (chat): Oke, otw."

    "Tidak lama kemudian, Jane tiba membawa laptop."

    designer "Halo."

    coder "Halo."

    designer "Lo udah mulai?"

    coder "Baru buka proyek."

    designer "Sama. Gue tadi masih ngerjain tugas lain."

    coder "Yang mana?"

    designer "Pancasila."

    coder "Oh."

    designer "Kenapa?"

    coder "Gue belum."

    designer "Lah."

    coder "Nanti malam."

    designer "Yakin?"

    coder "Semoga."

    "Jane duduk di samping Luuk dan membuka desain halaman pemesanan tiket."

    designer "Oke, sekarang kita cek apa lagi."

    coder "Form tiket masih butuh validasi."

    designer "Terus pembayaran simulasi."

    coder "Sama halaman admin."

    designer "Oh, iya. Admin."

    coder "Belum ada bagian buat lihat data pemesanan."

    designer "Berarti kita masih punya lumayan banyak."

    coder "Iya."

    designer "Tapi setidaknya bentuk website-nya udah kelihatan."

    coder "Nah, itu."

    "Luuk mencoba menjalankan proyek."

    "Pada layar muncul beberapa halaman yang mereka kerjakan selama beberapa minggu terakhir."

    designer "Eh, tampilannya lumayan sekarang."

    coder "Iya, lebih bagus daripada awal."

    designer "Yang awal cuma tulisan sama tombol."

    coder "Jangan dihina."

    designer "Sekarang udah punya warna."

    coder "Kemajuan besar."

    designer "Sangat besar."


    # ========================================================
    # MENU 10 — CANDAAN TAMPILAN WEBSITE
    # Tiga opsi, hanya dialog.
    # ========================================================

    menu:

        "Dulu website kita masih zaman batu.":

            coder "Dulu website kita masih zaman batu."

            designer "Sekarang?"

            coder "Zaman perunggu."

            designer "Berarti masih panjang evolusinya."

            coder "Pelan-pelan."


        "Sekarang minimalisnya udah disengaja.":

            coder "Sekarang minimalisnya udah disengaja."

            designer "Sebelumnya?"

            coder "Minimalis karena belum ada CSS."

            designer "Nah, sekarang gue percaya."

            coder "Makasih."


        "Setidaknya tombolnya udah punya rumah.":

            coder "Setidaknya tombolnya udah punya rumah."

            designer "Maksud lo?"

            coder "Udah nggak nyasar ke pojok layar."

            designer "Itu karena gue bantu rapihin."

            coder "Iya. Jasa lo besar."

            designer "Akhirnya diakui."


    # ========================================================
    # LANJUTAN SCENE 04
    # ========================================================

    "Luuk membuka halaman booking."

    designer "Kalau buat simulasi pembayaran nanti, data pesanan harus dikirim ke halaman berikutnya, kan?"

    coder "Iya. Harus ada ringkasan pesanan."

    designer "Terus metode pembayaran."

    coder "Iya."

    designer "Terus status."

    coder "Betul."

    designer "Kalau datanya kosong?"

    coder "Nah, berarti harus dicek dulu."

    designer "Oh."

    "Mereka melihat daftar pekerjaan yang berkaitan dengan halaman booking."


    # Pengaruh pilihan tes booking atau galeri pada Scene 01.
    if uji_booking_dulu:

        designer "Untung kemarin kita udah coba booking."

        coder "Iya. Ketahuan beberapa masalahnya."

        designer "Jadi sekarang tinggal pilih mau memperbaiki yang mana dulu."

    else:

        designer "Kita belum ngetes alur booking sampai akhir, ya."

        coder "Belum. Kemarin fokus galeri."

        designer "Iya. Tapi yang sekarang tetap bisa mulai kita siapkan."

        coder "Bisa. Asal fitur yang belum nyambung jangan dianggap udah selesai."


    designer "Jadi sekarang mau fokus ke bagian apa?"

    coder "Ada dua yang bisa kita kerjain."

    designer "Apa aja?"

    coder "Validasi data pemesanan atau kerangka simulasi pembayaran."

    designer "Hmm. Dua-duanya penting."


    # ========================================================
    # MENU 11 — PILIHAN PENTING TEKNIS
    #
    # A. Validasi form pemesanan.
    #    prioritas_teknis_lanjutan = "validasi"
    #
    # B. Pembayaran simulasi.
    #    prioritas_teknis_lanjutan = "pembayaran"
    #
    # Pilihan ini memengaruhi Scene 05.
    # ========================================================

    menu:

        "Perbaiki validasi data pemesanan dulu.":

            $ prioritas_teknis_lanjutan = "validasi"

            coder "Perbaiki validasi data pemesanan dulu."

            designer "Berarti kalau ada data kosong, pengunjung nggak bisa lanjut?"

            coder "Iya."

            designer "Terus tanggal yang udah lewat?"

            coder "Harus ditolak juga."

            designer "Oke. Gue bantu tes."

            "Luuk mulai menambahkan pemeriksaan terhadap data pemesanan."

            "Jane mencoba beberapa input yang tidak sesuai."

            designer "Coba nama kosong."

            coder "Oke."

            designer "Nah, sekarang ada peringatan."

            coder "Bagus."

            designer "Kalau jumlah tiket nol?"

            coder "Coba."

            "Pesan kesalahan kini muncul."

            designer "Nah."

            coder "Tinggal beberapa kondisi lagi."

            designer "Setidaknya pengunjung nggak bisa pesan nol tiket sekarang."

            coder "Kemajuan yang penting."

            designer "Iya."

            "Validasi dasar mulai bekerja."

            "Namun, koneksi database, alur pembayaran, dan halaman admin masih belum selesai."

            # Progress bertambah 4.
            $ website_progress = min(100, website_progress + 4)


        "Bikin kerangka pembayaran simulasi dulu.":

            $ prioritas_teknis_lanjutan = "pembayaran"

            coder "Bikin kerangka pembayaran simulasi dulu."

            designer "Jadi gue bisa bikin tampilannya?"

            coder "Iya. Kita siapkan halaman terpisah dulu."

            designer "Kenapa terpisah?"

            coder "Karena alur booking belum semuanya nyambung. Jadi sementara pakai data contoh."

            designer "Oh, oke."

            "Jane mulai merancang halaman pembayaran sederhana."

            "Terdapat ringkasan pesanan, pilihan metode pembayaran, dan tempat menampilkan status pembayaran."

            designer "Metodenya apa aja?"

            coder "Bisa transfer bank simulasi sama pembayaran digital simulasi."

            designer "Nggak ada transaksi asli, kan?"

            coder "Nggak ada. Semuanya dummy."

            designer "Oke."

            "Luuk membuat halaman percobaan menggunakan data pemesanan contoh."

            "Ketika tombol simulasi ditekan, status pada halaman berubah."

            designer "Oh, muncul 'Pembayaran Berhasil'."

            coder "Iya. Tapi ini baru demo terpisah."

            designer "Belum tersambung ke booking?"

            coder "Belum."

            designer "Oke. Nanti kita sambungin."

            "Kerangka pembayaran simulasi sudah terlihat."

            "Namun, validasi pemesanan, database, dan hubungan antarhalaman masih perlu dibuat."

            # Progress bertambah 3.
            $ website_progress = min(100, website_progress + 3)


    # ========================================================
    # LANJUTAN SCENE 04
    # ========================================================

    "Matahari mulai terbenam ketika keduanya berhenti sebentar."

    "Jane meregangkan tubuh."

    designer "Capek juga."

    coder "Lumayan."

    designer "Tapi kalau udah ada yang jalan, rasanya enak."

    coder "Iya."

    designer "Kalau semuanya jalan, lebih enak lagi."

    coder "Itu namanya selesai."

    designer "Oh, iya."

    "Jane memandangi laptop Luuk."

    designer "Eh, lo nggak takut salah hapus kode?"

    coder "Takut."

    designer "Serius?"

    coder "Ya iyalah."

    designer "Gue kira programmer kebal."

    coder "Kebal dari apa?"

    designer "Error."

    coder "Justru kita tiap hari ketemu error."


    # ========================================================
    # MENU 12 — CANDAAN PROGRAMMER
    # Dua opsi, hanya dialog.
    # ========================================================

    menu:

        "Error itu teman lama.":

            coder "Error itu teman lama."

            designer "Teman yang nyusahin?"

            coder "Iya. Datang tanpa diundang."

            designer "Terus susah disuruh pulang."

            coder "Nah, tepat."


        "Kalau nggak ada error, gue malah curiga.":

            coder "Kalau nggak ada error, gue malah curiga."

            designer "Kenapa?"

            coder "Biasanya ada yang belum dites."

            designer "Wah, pengalaman hidup."

            coder "Pengalaman menyakitkan."


    # ========================================================
    # PENUTUP SCENE 04
    # ========================================================

    "Menjelang malam, Jane menyimpan pekerjaan desainnya."

    "Luuk juga menyimpan perubahan kode terakhir."

    designer "Oke, hari ini lumayan."

    coder "Iya."

    designer "Besok gue nggak bisa ke sini."

    coder "Kenapa?"

    designer "Ada tugas lain yang harus gue selesaiin."

    coder "Oke. Gue juga ada tugas PBO."

    designer "Nah, tuh. Jangan lupa."

    coder "Lo nggak pernah lupa ngingetin, ya?"

    designer "Keahlian khusus."

    "Mereka membereskan laptop dan catatan."

    "Beberapa fitur baru mulai mengambil bentuk."

    "Tetapi sebuah halaman yang tampak selesai belum tentu sudah siap digunakan."

    "Luuk mengetahui hal itu."

    "Jane juga mulai memahami bahwa setiap desain masih membutuhkan pengujian."

    "Namun, keduanya masih merasa pekerjaan dapat diselesaikan sedikit demi sedikit."

    "Masih 62 hari tersisa."

    jump ch3_scene_05


# ============================================================
# SCENE 05 — STILL TWO MONTHS
# 60 DAYS LEFT
#
# MENU 13: Hasil website.
# MENU 14: Ajakan Marvel.
# MENU 15: Rencana pekerjaan selanjutnya.
#
# Semua menu hanya memengaruhi dialog.
# ============================================================

label ch3_scene_05:

    $ days_left = 60

    scene black with dissolve

    $ hud_visible = True

    show coder at char_center

    "Dua hari berlalu."

    "Luuk dan Jane mengerjakan Museum Arunika secara terpisah."

    "Jane menyelesaikan beberapa rancangan halaman."

    "Luuk memperbaiki bagian kode yang menurutnya masih membutuhkan perhatian."

    "Namun, sebagian waktu mereka tetap digunakan untuk kuliah, tugas mata kuliah lain, dan bermain."

    "Malam ini, Luuk sedang duduk di depan laptopnya."

    "Ia baru saja mengumpulkan salah satu tugas kuliah."

    coder "Akhirnya."

    "Sebuah notifikasi muncul di ponselnya."

    "Jane (chat): Luukkk."

    "Luuk (chat): Apa?"

    "Jane (chat): Udah selesai tugas?"

    "Luuk (chat): Baru satu."

    "Jane (chat): Sama."

    "Luuk (chat): Yang lain?"

    "Jane (chat): Jangan ditanya."

    "Luuk (chat): Oke."

    "Jane (chat): Museum gimana?"

    "Luuk (chat): Lagi gue cek."

    "Jane (chat): Call?"

    "Luuk (chat): Boleh."

    "Tidak lama kemudian, mereka masuk ke voice call."

    designer "Halo."

    coder "Halo."

    designer "Coba share screen."

    coder "Bentar."

    "Luuk membagikan layar laptopnya."

    "Website Museum Arunika muncul di browser."

    designer "Wih."

    coder "Apa?"

    designer "Udah lumayan kelihatan kayak website beneran."

    coder "Emangnya sebelumnya apa?"

    designer "Percobaan ilmiah."

    coder "Jahat."

    designer "Bercanda."

    "Luuk membuka halaman utama."

    "Bagian informasi museum, tombol pemesanan tiket, serta beberapa kartu koleksi mulai terlihat."

    designer "Berandanya udah enak."

    coder "Iya. Desain lo juga membantu."

    designer "Tentu saja."

    coder "Jangan langsung sombong."

    designer "Biar seimbang sama lo."

    coder "Gue nggak sombong."

    designer "Iya, iya."


    # ========================================================
    # MENU 13 — CANDAAN HASIL WEBSITE
    # Tiga opsi, hanya dialog.
    # ========================================================

    menu:

        "Ini kerja sama dua manusia berbakat.":

            coder "Ini kerja sama dua manusia berbakat."

            designer "Wih."

            coder "Apa?"

            designer "Baru kali ini lo muji diri sendiri sekaligus orang lain."

            coder "Efisien."

            designer "Boleh juga."


        "Kalau nggak ada lo, CSS gue masih polos.":

            coder "Kalau nggak ada lo, CSS gue masih polos."

            designer "Nah, akhirnya sadar."

            coder "Iya."

            designer "Coba bilang lagi."

            coder "Nggak."

            designer "Yah."


        "Kalau nggak ada gue, tombolnya cuma pajangan.":

            coder "Kalau nggak ada gue, tombolnya cuma pajangan."

            designer "Kalau nggak ada gue, tombolnya jelek."

            coder "Berarti sama-sama butuh."

            designer "Nah, itu."

            coder "Setuju."


    # ========================================================
    # LANJUTAN SCENE 05
    # ========================================================

    "Luuk membuka halaman booking."

    designer "Eh, yang ini sekarang gimana?"


    # ========================================================
    # PENGARUH CODING CHAPTER 2 DAN UJI BOOKING CHAPTER 3
    #
    # Kalau pernah coding dahulu ATAU memilih tes booking,
    # perhitungan total harga sudah berjalan.
    # ========================================================

    if form_tiket_dikerjakan_dulu or uji_booking_dulu:

        coder "Perhitungan total harga udah jalan."

        designer "Oh, iya. Yang kemarin kita tes."

        coder "Iya."

        designer "Tinggal bagian yang belum lengkap, kan?"

        coder "Iya. Konfirmasi sama penyimpanan data masih harus diberesin."

    else:

        coder "Perhitungan total harga masih masuk daftar."

        designer "Oh, iya. Kita kemarin fokus bagian lain."

        coder "Iya. Nanti itu harus diberesin sebelum seluruh booking disambungin."

        designer "Oke. Kita kerjain pas lanjut form."


    # ========================================================
    # PENGARUH MENU 11 CHAPTER 3
    # Validasi atau pembayaran simulasi.
    # ========================================================

    if prioritas_teknis_lanjutan == "validasi":

        designer "Validasi yang kemarin gimana?"

        coder "Udah bisa nolak beberapa input yang salah."

        designer "Nama kosong?"

        coder "Udah ada peringatan."

        designer "Jumlah tiket nol?"

        coder "Udah dicegah."

        designer "Oke."

        coder "Tapi belum semua kondisi dites."

        designer "Nanti kita coba lagi."

    else:

        designer "Halaman pembayaran simulasi yang kemarin coba buka."

        coder "Bentar."

        "Luuk membuka halaman percobaan terpisah."

        designer "Oh, udah kelihatan."

        coder "Iya. Tapi ini baru pakai data contoh."

        designer "Belum nyambung sama booking?"

        coder "Belum."

        designer "Oke. Nanti kita sambungin."

        coder "Iya. Jangan dianggap transaksi asli juga."

        designer "Jelas. Gue juga nggak mau tiba-tiba ada tagihan beneran."


    "Luuk berpindah ke halaman koleksi."


    # ========================================================
    # PENGARUH PILIHAN BOOKING ATAU GALERI
    # ========================================================

    if not uji_booking_dulu:

        designer "Yang galeri kemarin udah lebih rapi."

        coder "Iya. Kartunya juga udah bisa menyesuaikan ukuran layar."

        designer "Tinggal konten aslinya."

    else:

        designer "Galeri masih banyak placeholder, ya."

        coder "Iya. Kita kemarin fokus tes booking."

        designer "Oke. Nanti layout-nya gue lanjut."


    designer "Ngomong-ngomong, Adrian belum kirim, ya?"

    coder "Belum ada file baru."

    designer "Hmm."

    coder "Gue udah cek folder."

    designer "Oke. Nanti kita ingetin lagi."

    coder "Iya."

    "Percakapan kembali beralih ke bagian website lain."

    designer "Halaman admin belum kita kerjain, kan?"

    coder "Belum banyak."

    designer "Yang buat lihat data pemesanan itu."

    coder "Iya. Nanti perlu tabel atau daftar pesanan."

    designer "Gue bisa buat desainnya."

    coder "Boleh."

    designer "Terus database?"

    coder "Masih harus disambungin."

    designer "Oh, oke."

    coder "Banyak bagian yang saling berhubungan."

    designer "Iya, sih."

    "Jane diam sebentar."

    designer "Tapi kelihatannya udah lumayan, ya?"

    coder "Secara tampilan, iya."

    designer "Kalau secara fungsi?"

    coder "Masih ada yang harus dikerjain."

    designer "Yaudah. Nanti kita lanjut satu-satu."

    coder "Iya."

    "Luuk menutup browser dan membuka daftar pekerjaan."


    # ========================================================
    # PENGARUH BUKTI PERTAMA CHAPTER 2
    # ========================================================

    if catatan_progres_dibuat:

        designer "Eh, coba buka catatan progres kita."

        coder "Bentar."

        "Luuk membuka dokumen yang mereka buat pada minggu sebelumnya."

        "Beberapa pekerjaan sudah diberi tanggal pembaruan."

        designer "Yang bagian gue nanti gue update lagi."

        coder "Oke."

        designer "Yang belum selesai jangan dicentang dulu, ya."

        coder "Iya."

    else:

        designer "File proyek sekarang udah gampang dicari, kan?"

        coder "Iya. Foldernya lebih rapi."

        designer "Bagus."

        coder "Tinggal daftar pekerjaan yang kadang masih ada di beberapa tempat."

        designer "Nanti kita rapihin juga."


    # ========================================================
    # PENGARUH BUKTI KEDUA CHAPTER 3
    # ========================================================

    if arsip_chat_kelompok_tersimpan:

        designer "Eh, dokumentasi chat yang kemarin udah gue simpan juga."

        coder "Oke."

        designer "Jadi kalau mau cek pembagian tugas awal, tinggal buka folder proyek."

        coder "Sip."

    else:

        designer "Pengingat yang kemarin gue buat masih ada."

        coder "Bagus."

        designer "Nanti gue cek lagi pas kita lanjut kerja."

        coder "Oke."


    # ========================================================
    # LANJUTAN SCENE 05
    # ========================================================

    "Setelah beberapa saat membahas website, Jane mengganti topik pembicaraan."

    designer "Eh, Luuk."

    coder "Hm?"

    designer "Lo masih mau lanjut coding malam ini?"

    coder "Kayaknya nggak lama lagi."

    designer "Oh."

    coder "Kenapa?"

    designer "Marvel?"

    coder "Lo nggak capek?"

    designer "Dikit."

    coder "Terus masih mau main?"

    designer "Biar istirahat."

    coder "Logika yang menarik."

    designer "Jadi?"

    coder "Hmm."


    # ========================================================
    # MENU 14 — CANDAAN AJAKAN MARVEL RIVALS
    # Tiga opsi, hanya dialog.
    # ========================================================

    menu:

        "Satu match beneran, ya.":

            coder "Satu match beneran, ya."

            designer "Iya."

            coder "Jangan kayak kemarin."

            designer "Kemarin kenapa?"

            coder "Satu match berubah jadi beberapa."

            designer "Itu karena kita belum puas."

            coder "Nah, alasan lagi."


        "Gue curiga kata 'satu' punya arti lain buat lo.":

            coder "Gue curiga kata 'satu' punya arti lain buat lo."

            designer "Maksudnya?"

            coder "Satu match menurut lo bisa berlangsung satu malam."

            designer "Nggak juga."

            coder "Yakin?"

            designer "Tergantung."

            coder "Tuh, kan."


        "Boleh, tapi abis itu tidur.":

            coder "Boleh, tapi abis itu tidur."

            designer "Siap."

            coder "Serius?"

            designer "Serius."

            coder "Jangan tiba-tiba ngajak lagi."

            designer "Kalau menang duluan, nggak."

            coder "Jawaban lo nggak meyakinkan."


    # ========================================================
    # LANJUTAN SCENE 05
    # ========================================================

    "Keduanya membuka Marvel Rivals."

    "Beberapa menit kemudian, mereka sudah berada di dalam pertandingan."

    designer "Luuk, belakang!"

    coder "Gue lihat!"

    designer "Jangan maju sendiri!"

    coder "GUE NGGAK MAJU SENDIRI!"

    designer "Terus itu siapa?"

    coder "..."

    designer "Luuk?"

    coder "Oke, tadi gue maju sendiri."

    designer "Nah!"

    "Pertandingan berlangsung cukup ramai."

    "Sesekali mereka tertawa, berteriak, dan menyalahkan situasi yang sebenarnya bisa mereka hindari."

    "Beberapa waktu kemudian, pertandingan selesai."

    coder "Akhirnya."

    designer "Lumayan."

    coder "Iya."

    designer "Satu lagi?"

    coder "..."

    designer "Kenapa diem?"

    coder "Gue lagi mengingat percakapan sebelumnya."

    designer "Oh."

    coder "Katanya satu."

    designer "Iya."

    coder "Terus?"

    designer "Yang tadi udah selesai."

    coder "Ya emang."

    designer "Berarti bisa mulai satu yang baru."

    coder "Itu bukan cara kerja janji."

    designer "Bercanda, bercanda."

    "Jane tertawa."

    "Akhirnya mereka memutuskan berhenti bermain."

    "Luuk menutup game, sementara Jane kembali melihat catatan pekerjaannya."

    designer "Eh, besok lo sibuk?"

    coder "Ada kelas."

    designer "Gue juga."

    coder "Kenapa?"

    designer "Nggak. Gue mau nyusun jadwal buat lanjut museum minggu depan."

    coder "Oh, boleh."

    designer "Kita kerjain beberapa bagian lagi."

    coder "Iya."

    designer "Yang penting ada kemajuan terus."

    coder "Setuju."

    "Jane melihat tanggal pada kalender."

    designer "Eh, berarti sekarang sisa berapa hari, ya?"

    coder "Sekitar enam puluh."

    designer "Oh, dua bulan lagi."

    coder "Iya."

    designer "Masih lumayan."

    coder "Hmm."

    designer "Kenapa?"

    coder "Nggak. Lagi mikir bagian admin."

    designer "Oh, nanti kita bikin."

    coder "Iya."


    # ========================================================
    # MENU 15 — RENCANA PEKERJAAN SELANJUTNYA
    # Dua opsi, hanya dialog.
    # ========================================================

    menu:

        "Minggu depan kita lanjut bagian yang belum selesai.":

            coder "Minggu depan kita lanjut bagian yang belum selesai."

            designer "Oke."

            coder "Admin, database, sama booking."

            designer "Iya. Gue juga lanjutin desainnya."

            coder "Sip."

            designer "Pelan-pelan, yang penting jadi."


        "Kita harus mulai nyicil lebih rutin.":

            coder "Kita harus mulai nyicil lebih rutin."

            designer "Boleh. Mau jadwal tetap?"

            coder "Nggak harus tiap hari, tapi lebih teratur."

            designer "Oke. Nanti gue lihat jadwal kuliah dulu."

            coder "Iya."

            designer "Kalau sempat, gue ke kontrakan lagi."


    # ========================================================
    # PENUTUP SCENE 05
    # ========================================================

    "Tidak lama kemudian, keduanya mengakhiri voice call."

    "Luuk kembali membuka folder Museum Arunika."

    "Ia melihat halaman utama, kode booking, serta beberapa file yang baru diperbarui."

    "Website itu memang sudah jauh berbeda dibandingkan hari pertama mereka memulainya."

    "Sekarang halaman beranda sudah memiliki struktur."

    "Desain booking mulai menyatu dengan kode."

    "Galeri sudah mempunyai kerangka yang lebih rapi."

    "Beberapa bagian form sudah dapat digunakan."

    "Namun masih ada hal-hal penting yang belum selesai."

    "Database belum terhubung sepenuhnya."

    "Halaman admin masih memerlukan pekerjaan."

    "Alur pemesanan dan pembayaran simulasi belum menjadi satu sistem yang utuh."

    "Konten koleksi dari Adrian belum tersedia."

    "Dan masih ada sejumlah masalah kecil yang hanya akan terlihat ketika website diuji."

    "Luuk menatap layar beberapa saat."

    coder "Masih ada yang harus dikerjain."

    "Ia menutup laptop."

    "Di tempat lain, Jane juga sedang membereskan pekerjaannya."

    "Ia merasa cukup puas melihat desain Museum Arunika yang perlahan menjadi lebih jelas."

    "Bagi keduanya, proyek ini memang belum selesai."

    "Tetapi mereka merasa masih mempunyai waktu yang cukup untuk menyelesaikannya."

    "Hari-hari berikutnya akan dipenuhi tugas lain, perbaikan kecil, percakapan panjang, dan pekerjaan yang terus bertambah."

    "Tidak semuanya terasa penting pada saat itu."

    "Namun, banyak hal kecil yang ditunda akan tetap menunggu sampai seseorang mengerjakannya."

    "60 DAYS LEFT."

    $ website_progress = min(100, website_progress + 1)

    $ hud_visible = False

    scene black with fade

    centered "{size=50}CHAPTER 03 COMPLETE{/size}\n{size=36}60 DAYS LEFT{/size}\n{size=28}Just a Few More Things."

    # Chapter 4 belum dibuat.
    # Jangan jump ke Chapter 4 sampai filenya tersedia.
    return
