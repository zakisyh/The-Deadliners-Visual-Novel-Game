
# ============================================================
# THE DEADLINERS — CHAPTER 02: WE STILL HAVE TIME
# ============================================================


# ============================================================
# VARIABEL PILIHAN PEMAIN
# ============================================================

# MENU 04:
# True = Luuk memilih menyelesaikan form tiket sebelum main.
# False = Luuk memilih main Marvel Rivals terlebih dahulu.
default form_tiket_dikerjakan_dulu = False

# MENU 08:
# "fungsi" = mengutamakan fungsi booking website.
# "desain" = mengutamakan tampilan website.
default prioritas_pengerjaan_website = "fungsi"

# MENU 12:
# True = Luuk dan Jane membuat catatan progres mingguan.
# False = mereka memilih merapikan folder proyek.
default catatan_progres_dibuat = False

# SECRET ENDING:
# Menghitung bukti tersembunyi yang dikumpulkan pemain.
# Chapter 2 menyediakan kesempatan mendapatkan bukti pertama.
# Total kesempatan pengumpulan bukti sepanjang game = 5.
# Untuk Secret Ending nanti diperlukan minimal 3 bukti,
# serta kondisi website yang cukup siap dan stabil.
default jumlah_bukti_rahasia = 0


# ============================================================
# CHAPTER 02 — OPENING
# ============================================================

label chapter_2:

    $ hud_visible = False
    $ days_left = 81

    scene black with fade

    play music "audio/BGM/insomniac.mp3" loop volume 0.5 

    centered "{size=50}CHAPTER 02{/size}\n{size=42}WE STILL HAVE TIME{/size}\n{size=34}81 DAYS LEFT{/size}"

    jump ch2_scene_01


# ============================================================
# SCENE 01 — ONE WEEK LATER
# 81 DAYS LEFT
#
# Jumlah menu: 3
# Menu 01, 02, dan 03 hanya memengaruhi dialog.
# ============================================================

label ch2_scene_01:

    $ days_left = 81

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    # Lokasi: Area duduk dekat perpustakaan kampus.

    "Seminggu telah berlalu sejak kelompok Museum Arunika menyepakati pembagian tugas."

    "Dalam tujuh hari itu, Luuk mulai menyusun struktur website. Jane membuat beberapa rancangan halaman. Namun, keduanya juga disibukkan dengan kuliah, tugas mata kuliah lain, dan aktivitas yang jauh lebih menyenangkan daripada mengerjakan tugas akhir."

    "Hari ini, mereka berencana memperlihatkan hasil awal pekerjaan masing-masing."

    "Luuk berjalan menuju area duduk dekat perpustakaan. Dari kejauhan, ia melihat Jane sedang menatap layar laptopnya."

    coder "Pagi."

    designer "Pagi. Sini."

    coder "Udah lama?"

    designer "Nggak. Baru buka laptop."

    coder "Kirain gue telat."

    designer "Jam berapa sekarang?"

    "Luuk memeriksa ponselnya."

    coder "Masih sesuai jadwal."

    designer "Wih."

    coder "Kenapa?"

    designer "Nggak apa-apa. Jarang aja."


    # ========================================================
    # MENU 01 — CANDAAN SOAL KETEPATAN WAKTU LUUK
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # Tidak mengubah statistik atau Secret Ending.
    # ========================================================

    menu:

        "Emangnya gue sering telat?":

            coder "Emangnya gue sering telat?"

            designer "Lo nanya serius?"

            coder "Iya."

            designer "Mau gue jawab jujur?"

            coder "Nggak jadi."

            designer "Nah."


        "Gue juga heran bisa tepat waktu.":

            coder "Gue juga heran bisa tepat waktu."

            designer "Setidaknya lo sadar."

            coder "Harusnya lo bangga."

            designer "Iya, selamat. Prestasi pertama semester ini."

            coder "Makasih, sangat memotivasi."


        "Fokus ke tugas aja, jangan bahas reputasi gue.":

            coder "Fokus ke tugas aja, jangan bahas reputasi gue."

            designer "Waduh. Profesional banget hari ini."

            coder "Tentu saja."

            designer "Bentar, gue foto dulu. Takutnya besok hilang."

            coder "Apanya?"

            designer "Jiwa profesional lo."


    # ========================================================
    # LANJUTAN SCENE 01
    # ========================================================

    "Jane menggeser laptopnya ke arah Luuk."

    designer "Udah, nih. Gue mau nunjukin wireframe."

    coder "Oh, udah ada?"

    designer "Ada. Nggak semuanya, ya."

    coder "Iya, coba."

    "Pada layar terlihat rancangan sederhana halaman utama Museum Arunika. Terdapat bagian informasi museum, beberapa kotak gambar, dan tombol menuju halaman pemesanan tiket."

    designer "Ini berandanya."

    coder "Hmm."

    designer "Jangan hmm doang."

    coder "Gue lagi lihat."

    designer "Terus?"

    coder "Bagus."

    designer "Nah, kan bisa ngomong."

    coder "Tombol pesan tiketnya mau ditaruh di sini?"

    designer "Iya. Biar pengunjung langsung lihat."

    coder "Masuk akal."

    designer "Terus ini kalau discroll ada penjelasan singkat museum."

    coder "Oh, oke."

    designer "Bagian koleksinya masih kotak kosong. Gue belum punya gambar."

    coder "Placeholder dulu?"

    designer "Iya. Nanti kalau bahan dari Adrian udah ada, tinggal diganti."

    "Jane berpindah ke rancangan halaman lain."

    designer "Ini halaman booking."

    coder "Oh."

    designer "Ada pilihan tanggal, jumlah tiket, sama data pengunjung."

    coder "Kalau jumlah tiketnya berubah, totalnya juga harus ikut berubah."

    designer "Iya. Bisa, kan?"

    coder "Bisa dibuat. Cuma belum gue kerjain."

    designer "Oke."

    coder "Yang bagian konfirmasi juga belum?"

    designer "Belum. Gue mau lihat dulu form-nya bakal kayak gimana."

    coder "Sip."

    designer "Lo sendiri udah ada hasil?"

    coder "Ada. Tapi jangan berharap banyak."

    designer "Waduh."

    "Luuk mengeluarkan laptop dan membuka folder proyek."

    coder "Gue udah bikin struktur folder sama file awal."

    designer "Terus?"

    coder "Halaman berandanya masih polos. Gue juga mulai bikin bagian form tiket."

    designer "Udah bisa dipakai?"

    coder "Belum. Masih nyusun."

    designer "Coba buka."

    "Luuk membuka website versi lokal."

    "Halaman yang muncul jauh lebih sederhana dibandingkan desain Jane."

    designer "..."

    coder "Apa?"

    designer "Nggak, gue lagi membayangkan hasil akhirnya."

    coder "Sekarang masih versi mentah."

    designer "Iya, gue tahu."

    coder "CSS-nya juga belum banyak."

    designer "Nanti kita samain sama desain."

    coder "Nah."


    # ========================================================
    # MENU 02 — CANDAAN TAMPILAN WEBSITE LUUK
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Ini gaya minimalis.":

            coder "Ini gaya minimalis."

            designer "Minimalis atau belum dikerjain?"

            coder "Dua-duanya bisa benar."

            designer "Oke, jawaban aman."


        "Makanya gue butuh desainer.":

            coder "Makanya gue butuh desainer."

            designer "Untung ada gue."

            coder "Iya, iya."

            designer "Coba bilang sekali lagi."

            coder "Nggak."


        "Jangan dihina dulu, masih bayi.":

            coder "Jangan dihina dulu. Websitenya masih bayi."

            designer "Gue belum menghina."

            coder "Tatapan lo udah."

            designer "Perasaan lo aja."


    # ========================================================
    # LANJUTAN SCENE 01
    # ========================================================

    "Setelah bercanda, keduanya kembali melihat catatan pembagian kerja yang sudah dikirim Jane pada pertemuan pertama."

    designer "Berarti buat minggu ini kita udah ada beberapa hasil."

    coder "Iya. Walaupun masih awal."

    designer "Nanti tinggal kita gabungin."

    coder "Jangan langsung semuanya. Yang form harus dites dulu."

    designer "Oke."

    designer "Eh, Adrian mana?"

    "Luuk melihat sekeliling."

    coder "Belum datang."

    designer "Gue kemarin udah ingetin di grup, kan?"

    coder "Iya."

    designer "Coba cek."

    "Luuk membuka grup Museum Arunika."

    "Pesan pengingat pertemuan terlihat di antara percakapan sebelumnya. Belum ada pembaruan pekerjaan dari Adrian."

    coder "Belum ada kabar baru."

    designer "Hmm."

    coder "Coba tanya progresnya aja."

    designer "Oke."

    "Jane mengirim pesan."

    "Jane (grup): Guys, gimana progress minggu ini?"

    "Jane (grup): Adrian, gambar sama deskripsinya udah ada?"

    "Beberapa saat berlalu."

    "Tidak ada balasan."

    coder "Mungkin belum lihat."

    designer "Iya. Nanti juga dibales."

    coder "Yang penting kita udah ada bahan buat lanjut."

    designer "Iya. Gue mau lanjut wireframe galeri dulu."

    coder "Gue form tiket."

    designer "Oke."

    "Jane menutup beberapa tab di laptopnya."

    coder "Banyak amat tab lo."

    designer "Yang ini buat museum. Yang itu buat tugas lain."

    coder "PBO?"

    designer "Bukan. Yang Kecerdasan Buatan."

    coder "Oh, iya. Gue juga belum selesai."

    designer "Terus masih ada Pancasila."

    coder "Jangan diingetin."

    designer "Kenapa?"

    coder "Baru inget."

    designer "Lah."

    "Jane tertawa."


    # ========================================================
    # MENU 03 — CANDAAN TUGAS KULIAH
    #
    # Dua opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Tugasnya bisa antre nggak, sih?":

            coder "Tugasnya bisa antre nggak, sih?"

            designer "Maksud lo?"

            coder "Satu selesai dulu, baru yang lain muncul."

            designer "Coba lo bilang ke semua dosen."

            coder "Nggak jadi."

            designer "Nah."


        "Kayaknya semester ini isinya tugas semua.":

            coder "Kayaknya semester ini isinya tugas semua."

            designer "Emang ada semester yang nggak begitu?"

            coder "Gue masih berharap."

            designer "Semangat berharapnya."

            coder "Makasih."


    # ========================================================
    # PENUTUP SCENE 01
    # ========================================================

    designer "Yaudah. Nanti bagi waktu aja."

    coder "Iya. Yang penting hari ini udah ada yang bisa kita lihat."

    "Mereka menyimpan hasil pekerjaan masing-masing sebelum meninggalkan tempat itu."

    "Belum banyak yang selesai."

    "Namun, keduanya merasa proyek mereka sudah mulai bergerak."

    # Website Progress bertambah 3 setelah Scene 01.
    $ website_progress = min(100, website_progress + 3)

    jump ch2_scene_02


# ============================================================
# SCENE 02 — JUST ONE MATCH
# 80 DAYS LEFT
#
# Jumlah menu: 3
# Menu 04 adalah pilihan penting.
# Menu 05 dan 06 hanya memengaruhi dialog.
# ============================================================

label ch2_scene_02:

    $ days_left = 80

    scene black with dissolve

    $ hud_visible = True

    show coder at char_center

    # Lokasi: Kontrakan Luuk, malam hari.

    "Malam berikutnya, Luuk duduk di depan laptopnya."

    "Di layar terdapat beberapa file proyek Museum Arunika. Salah satunya berisi form pemesanan tiket yang mulai ia buat."

    "Ia mencoba menjalankan halaman tersebut melalui browser."

    coder "Oke..."

    "Form sederhana muncul."

    coder "Tanggal. Jumlah tiket. Nama pengunjung."

    "Luuk mengisi beberapa data percobaan."

    "Ia menekan tombol konfirmasi."

    "Tidak terjadi apa-apa."

    coder "Lah."

    "Luuk kembali ke editor dan memeriksa kode."

    coder "Kenapa nggak kepanggil?"

    "Ia mengecek bagian yang menangani tombol tersebut."

    coder "Oh."

    "Ada kesalahan kecil pada nama elemen yang dirujuk oleh kode."

    coder "Pantes."

    "Luuk memperbaikinya, lalu mencoba lagi."

    "Kali ini sebuah pesan percobaan berhasil muncul."

    coder "Nah."

    "Ia memeriksa kembali apa saja yang masih kurang."

    coder "Total harga belum."

    coder "Validasi input juga belum semua."

    coder "Database belakangan."

    "Luuk menyesap minumannya, lalu kembali mengetik."

    "Beberapa menit kemudian, ponselnya bergetar."

    "Jane (chat): Luukkk"

    "Jane (chat): Lagi apa?"

    "Luuk (chat): Coding."

    "Jane (chat): Rajin amat."

    "Luuk (chat): Sekali-sekali."

    "Jane (chat): Marvel?"

    "Jane (chat): Satu match doang."

    "Luuk menatap pesan itu."

    "Lalu menatap form yang masih terbuka."


    # ========================================================
    # MENU 04 — PILIHAN PENTING
    #
    # Pemain memilih:
    #
    # A. Selesaikan form tiket terlebih dahulu.
    #    form_tiket_dikerjakan_dulu = True
    #
    # B. Main Marvel Rivals terlebih dahulu.
    #    form_tiket_dikerjakan_dulu = False
    #
    # Pilihan ini memengaruhi dialog di Scene 03.
    # ========================================================

    menu:

        "Bentar, gue beresin form ini dulu.":

            # Luuk memilih bekerja dahulu.
            $ form_tiket_dikerjakan_dulu = True

            # Kemajuan website bertambah 3.
            $ website_progress = min(100, website_progress + 3)

            # Sedikit menambah stres.
            $ stress_level = min(100, stress_level + 2)

            "Luuk (chat): Bentar, gue beresin form ini dulu."

            "Jane (chat): Oke."

            "Jane (chat): Gue sambil lanjutin desain."

            "Luuk menutup notifikasi dan kembali bekerja."

            coder "Tinggal jumlah tiket."

            "Ia menambahkan perhitungan sederhana untuk menampilkan total harga berdasarkan jumlah tiket yang dipilih."

            "Percobaan pertama menghasilkan nilai yang salah."

            coder "Hmm. Salahnya di mana?"

            "Luuk memeriksa alur perhitungan, menemukan nilai input yang belum dikonversi dengan benar, lalu memperbaikinya."

            coder "Oke, sekarang coba."

            "Total harga akhirnya berubah sesuai jumlah tiket."

            coder "Nah, gini."

            "Setelah menyimpan pekerjaan, ia mengirim pesan kepada Jane."

            "Luuk (chat): Udah. Jadi main?"

            "Jane (chat): Gas."

            "Jane (chat): Gue juga baru selesai benerin layout."

            "Keduanya masuk ke voice call dan memulai pertandingan."


        "Oke, satu match dulu.":

            # Luuk memilih main dahulu.
            $ form_tiket_dikerjakan_dulu = False

            # Kemajuan website hanya bertambah 1.
            $ website_progress = min(100, website_progress + 1)

            "Luuk (chat): Oke, satu match dulu."

            "Jane (chat): Gas."

            "Luuk menyimpan file yang sedang dikerjakannya."

            "Ia membuka Marvel Rivals dan masuk ke voice call."

            designer "Wih, cepet."

            coder "Kan lo yang ngajak."

            designer "Iya, tapi gue kira lo bakal coding dulu."

            coder "Bentar aja."

            "Pertandingan dimulai."

            "Waktu berlalu lebih cepat daripada yang mereka perkirakan."

            designer "Anjir, hampir menang."

            coder "Iya."

            designer "Satu lagi?"

            coder "Tadi katanya satu."

            designer "Biar nggak ditutup kekalahan."

            coder "Yaudah."

            "Setelah beberapa pertandingan, mereka akhirnya berhenti."

            designer "Oke. Gue mau lanjut desain bentar."

            coder "Gue juga mau cek coding."

            "Luuk kembali membuka VS Code."

            "Ia sempat memperbaiki beberapa bagian form, tetapi belum menyelesaikan perhitungan harga."

            coder "Besok aja lanjutin bagian ini."


    # ========================================================
    # LANJUTAN SCENE 02
    # ========================================================

    "Dalam voice call, obrolan mereka kembali beralih ke proyek."

    designer "Eh, kalau nanti gue yang ngetes form tiketnya, gimana?"

    coder "Ya bagus."

    designer "Kalau gue salah klik terus error?"

    coder "Ya kita cek."

    designer "Respons lo pasti gitu?"


    # ========================================================
    # MENU 05 — CANDAAN SOAL ERROR WEBSITE
    #
    # Dua opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Tergantung error-nya bikin pusing apa nggak.":

            coder "Tergantung error-nya bikin pusing apa nggak."

            designer "Kalau bikin pusing?"

            coder "Gue tatap dulu layarnya."

            designer "Terus?"

            coder "Baru gue cari salahnya."

            designer "Oh, tetap dikerjain."

            coder "Ya masa dibiarin."


        "Gue salahin browser-nya dulu.":

            coder "Gue salahin browser-nya dulu."

            designer "Lah, kok browser?"

            coder "Buat pemanasan."

            designer "Terus abis itu?"

            coder "Baru cek kode sendiri."

            designer "Nah, itu baru bener."


    designer "Eh, besok jadi gue ke kontrakan lo?"

    coder "Jadi."

    designer "Gue bawa desain booking yang terbaru, ya."

    coder "Oke. Biar gue coba samain."

    designer "Laptop lo masih kuat?"

    coder "Kuat kenapa?"

    designer "Kemarin tab browser lo kayak nggak ada habisnya."

    coder "Itu namanya multitasking."

    designer "Itu namanya menyiksa RAM."


    # ========================================================
    # MENU 06 — CANDAAN SOAL RAM LAPTOP
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "RAM gue udah terbiasa menderita.":

            coder "RAM gue udah terbiasa menderita."

            designer "Kasihan banget."

            coder "Dia kuat."

            designer "Dia nggak punya pilihan."


        "Yang penting masih nyala.":

            coder "Yang penting masih nyala."

            designer "Standar hidup lo rendah banget."

            coder "Efisien."

            designer "Itu bukan efisien."


        "Laptop lo juga nggak lebih baik.":

            coder "Laptop lo juga nggak lebih baik."

            designer "Laptop gue baik-baik aja."

            coder "Kemarin kipasnya kedengeran dari voice call."

            designer "Itu efek suara."

            coder "Efek suara penderitaan."


    # ========================================================
    # PENUTUP SCENE 02
    # ========================================================

    "Obrolan berlanjut sebentar sebelum mereka mengakhiri panggilan."

    "Luuk kembali melihat folder Museum Arunika."

    "Form tiket sudah mulai terbentuk. Namun, dari daftar fitur yang mereka rencanakan, masih banyak yang belum disentuh."

    "Luuk menyimpan pekerjaan terakhirnya dan menutup laptop."

    "Besok masih ada waktu untuk melanjutkan."

    jump ch2_scene_03


# ============================================================
# SCENE 03 — LOOKS GOOD, DOESN'T WORK
# 79 DAYS LEFT
#
# Jumlah menu: 3
#
# Menu 07 = candaan soal pixel.
# Menu 08 = pilihan penting prioritas pengerjaan website.
# Menu 09 = candaan soal keahlian coding dan desain.
# ============================================================

label ch2_scene_03:

    $ days_left = 79

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    # Lokasi: Kontrakan Luuk, siang hingga sore.

    "Siang berikutnya, Jane datang ke kontrakan Luuk membawa laptop dan perlengkapan kuliah."

    "Luuk sedang menyiapkan meja agar mereka bisa membuka kedua laptop berdampingan."

    designer "Woy."

    coder "Masuk."

    designer "Lo udah makan?"

    coder "Udah."

    designer "Tumben."

    coder "Kenapa semua hal normal yang gue lakuin selalu dikomentarin?"

    designer "Karena menarik."

    "Jane meletakkan tasnya dan membuka laptop."

    designer "Gue bawa desain yang kemarin."

    coder "Sip. Gue buka web-nya dulu."

    "Luuk menjalankan website versi lokal."

    "Halaman Museum Arunika muncul dengan tampilan sederhana."

    designer "Oke, jadi sekarang udah sampai mana?"

    coder "Beranda dasar udah ada. Form tiket juga mulai jalan."

    designer "Yang bagian total harga?"


    # ========================================================
    # KONSEKUENSI PILIHAN MENU 04
    #
    # Mengecek pilihan pemain di Scene 02.
    #
    # True:
    # Luuk sebelumnya memilih menyelesaikan form tiket.
    #
    # False:
    # Luuk sebelumnya memilih main Marvel terlebih dahulu.
    # ========================================================

    if form_tiket_dikerjakan_dulu:

        coder "Udah bisa ngitung dari jumlah tiket, tapi masih sederhana."

        designer "Coba."

        "Luuk mengubah jumlah tiket. Total harga di halaman ikut berubah."

        designer "Oh, jalan."

        coder "Iya. Tapi belum masuk database."

        designer "Yang itu nanti kita kerjain juga."

    else:

        coder "Belum beres. Kemarin baru sampai bagian input."

        designer "Oh, yaudah. Sekarang bisa kita lanjut."

        coder "Iya. Gue masih harus bikin perhitungannya."

        designer "Oke. Gue bantu cocokkin tampilannya."


    # ========================================================
    # LANJUTAN SCENE 03
    # ========================================================

    "Jane membuka prototype halaman booking."

    designer "Ini tampilan yang gue buat."

    "Desain tersebut lebih rapi dibandingkan website yang sedang berjalan."

    coder "Bagus."

    designer "Nah. Masalahnya tinggal dibikin sama."

    coder "Masalahnya memang di situ."

    designer "Kenapa?"

    coder "Layout-nya ada beberapa bagian yang perlu gue ubah. Terus tombol ini juga belum punya fungsi."

    designer "Oh."

    coder "Kalau mau persis, gue harus benerin susunan form-nya dulu."

    designer "Gue bisa bantu sederhanain desainnya."

    coder "Boleh. Kita cari yang enak dipakai, tapi nggak terlalu ribet dibikin."

    designer "Oke."

    "Jane menggeser beberapa elemen pada prototype."

    designer "Kalau tombolnya pindah ke bawah, lebih gampang nggak?"

    coder "Lebih gampang."

    designer "Terus total harga di sebelah kanan?"

    coder "Boleh. Tapi kalau di HP, nanti harus turun ke bawah."

    designer "Oh, iya. Berarti gue bikin versi mobile-nya juga."

    coder "Nah."

    designer "Gue nggak begitu ngerti bagian kodingnya, jadi kalau ada yang susah, bilang."

    coder "Iya. Gue juga nggak begitu ngerti kenapa jarak tombol harus beda dua pixel."

    designer "Karena kelihatan."

    coder "Dua pixel?"

    designer "Iya."

    coder "Oke."


    # ========================================================
    # MENU 07 — CANDAAN SOAL PIXEL
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Mata lo punya fitur zoom bawaan?":

            coder "Mata lo punya fitur zoom bawaan?"

            designer "Nggak. Gue cuma lihat."

            coder "Gue nggak lihat bedanya."

            designer "Makanya gue yang desain."


        "Yaudah, gue percaya sama lo.":

            coder "Yaudah, gue percaya sama lo."

            designer "Bagus."

            coder "Asal jangan suruh geser tombol satu pixel lagi."

            designer "Nggak janji."


        "Kita kompromi tiga pixel.":

            coder "Kita kompromi tiga pixel."

            designer "Komprominya dari mana?"

            coder "Tengah-tengah."

            designer "Itu malah lebih jauh."

            coder "Oh, iya."


    # ========================================================
    # LANJUTAN SCENE 03
    # ========================================================

    "Beberapa saat kemudian, keduanya mulai bekerja."

    "Jane memperbaiki rancangan halaman booking, sedangkan Luuk mengubah kode sesuai susunan yang mereka sepakati."

    "Pada percobaan pertama, beberapa elemen tidak muncul di posisi yang seharusnya."

    designer "Lah, kok tombolnya pindah ke situ?"

    coder "Sebentar."

    "Luuk memeriksa stylesheet."

    coder "Oh, kena aturan layout yang lama."

    designer "Bisa dibenerin?"

    coder "Bisa. Ini gue ubah dulu."

    "Jane menunggu sambil mengerjakan bagian desain lain."

    "Beberapa menit kemudian, Luuk memperbarui halaman."

    designer "Nah, itu."

    coder "Udah mirip?"

    designer "Lebih mirip."

    coder "Berarti masih kurang."

    designer "Dikit."

    coder "Dikit versi lo berapa jam?"

    designer "Tergantung."

    coder "Jawaban yang mengkhawatirkan."

    "Jane tertawa sebelum kembali melihat desain."

    designer "Eh, tapi kita harus tentuin mau fokus ke mana dulu."

    coder "Maksudnya?"

    designer "Kalau semuanya kita kerjain bareng, takutnya malah pindah-pindah terus."

    coder "Bener juga."

    designer "Mau lanjut fungsi booking, atau samain tampilan dulu?"


    # ========================================================
    # MENU 08 — PILIHAN PENTING
    #
    # Pemain memilih fokus pengerjaan website.
    #
    # A. "fungsi"
    #    Fokus membuat alur booking berjalan.
    #
    # B. "desain"
    #    Fokus merapikan tampilan website.
    #
    # Nilai ini disimpan untuk cerita berikutnya.
    # ========================================================

    menu:

        "Alur booking-nya kita bikin jalan dulu.":

            # Pemain memilih mengutamakan fungsi website.
            $ prioritas_pengerjaan_website = "fungsi"

            $ website_progress = min(100, website_progress + 2)

            coder "Alur booking-nya kita bikin jalan dulu."

            designer "Berarti tampilan nggak perlu persis sekarang?"

            coder "Iya. Nanti kalau alurnya udah aman, kita rapihin lagi."

            designer "Oke. Gue sederhanain layout sementara."

            "Jane menyesuaikan desain agar lebih mudah diterapkan."

            "Luuk fokus pada pilihan tanggal, jumlah tiket, data pengunjung, dan ringkasan pemesanan."

            designer "Coba tanggalnya diganti."

            "Luuk memilih tanggal lain."

            coder "Oke."

            designer "Terus jumlah tiketnya?"

            "Luuk mengganti jumlah tiket dan memeriksa hasilnya."

            "Beberapa bagian sudah mulai bekerja."

            designer "Lumayan."

            coder "Iya. Walaupun tampilannya masih polos."

            designer "Nanti bagian gue."

            coder "Sip."


        "Kita samain tampilannya dulu.":

            # Pemain memilih mengutamakan desain website.
            $ prioritas_pengerjaan_website = "desain"

            $ website_progress = min(100, website_progress + 2)

            coder "Kita samain tampilannya dulu sama desain lo."

            designer "Boleh. Jadi nanti nggak perlu banyak bongkar."

            coder "Iya. Sekalian bikin struktur layout-nya rapi."

            "Jane menjelaskan ukuran, posisi elemen, dan tampilan untuk layar yang lebih kecil."

            "Luuk menyesuaikan struktur halaman serta stylesheet."

            designer "Nah, yang itu udah pas."

            coder "Kalau di HP gimana?"

            "Jane memeriksa tampilan mobile."

            designer "Yang ini masih kepotong."

            coder "Oke, berarti bagian ini gue ubah."

            "Mereka memperbaiki susunan halaman hingga tampilan lebih mendekati prototype."

            designer "Bagus. Sekarang lebih gampang dilihat."

            coder "Tinggal fungsi-fungsinya."

            designer "Iya. Nanti kita lanjut."


    # ========================================================
    # LANJUTAN SCENE 03
    # ========================================================

    "Menjelang sore, keduanya berhenti sebentar."

    designer "Capek juga."

    coder "Lumayan."

    designer "Tapi seru sih kalau udah kelihatan hasilnya."

    coder "Iya. Lebih enak daripada cuma mikirin mau bikin apa."

    designer "Eh, halaman koleksinya nanti gue desain model kartu-kartu gitu, ya."

    coder "Boleh."

    designer "Setiap kartu ada gambar, nama koleksi, sama deskripsi singkat."

    coder "Oke."

    designer "Yang bagian kontennya Adrian."

    coder "Iya."

    designer "Kalau bahannya udah ada, gue tinggal masukin."

    coder "Sip."

    designer "Terus halaman pembayaran?"

    coder "Kita bikin simulasi aja, sesuai rencana kemarin."

    designer "Berarti nggak perlu uang beneran?"

    coder "Nggak. Pilih metode pembayaran, konfirmasi, terus status pesanan."

    designer "Oh, oke."

    coder "Tapi itu belum sekarang. Form tiket aja belum selesai."

    designer "Iya juga."

    designer "Terus admin?"

    coder "Nanti butuh halaman buat lihat data pemesanan."

    designer "Bisa nggak gue bikinin desainnya dulu?"

    coder "Bisa. Tapi jangan semua halaman sekarang."

    designer "Kenapa?"

    coder "Nanti lo malah kebanyakan kerja."

    designer "Oh."

    designer "Yaudah, gue lanjut yang booking dulu."

    coder "Sip."

    "Jane menatap daftar rancangan yang masih harus ia buat."

    designer "Kalau dipikir-pikir, halaman yang harus kita bikin lumayan banyak juga."

    coder "Iya."

    designer "Untung kita bagi bagian coding sama desain."

    coder "Kalau gue disuruh desain semuanya, bisa bahaya."

    designer "Sebahaya apa?"


    # ========================================================
    # MENU 09 — CANDAAN SOAL KEMAMPUAN CODING DAN DESAIN
    #
    # Dua opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Semua tombol bakal bentuk kotak.":

            coder "Semua tombol bakal bentuk kotak."

            designer "Tombol emang bisa kotak."

            coder "Iya, tapi semuanya kotak. Semua halaman."

            designer "Waduh."

            coder "Konsisten, kan?"

            designer "Konsisten bukan berarti bagus."


        "Pokoknya lo bakal protes duluan.":

            coder "Pokoknya lo bakal protes duluan."

            designer "Emang iya."

            coder "Tuh, kan."

            designer "Makanya biar gue yang desain."

            coder "Dan gue yang coding."

            designer "Deal."


    # ========================================================
    # PENUTUP SCENE 03
    # ========================================================

    "Keduanya kembali membereskan file pekerjaan."

    "Tidak ada pertengkaran atau saling menyalahkan."

    "Ketika satu orang menemui masalah, yang lain membantu sebisanya."

    "Namun mereka belum menyadari bahwa daftar pekerjaan yang mereka bicarakan jauh lebih panjang daripada hasil yang sudah benar-benar selesai."

    designer "Eh, sebelum gue pulang..."

    coder "Apa?"

    designer "Malam ini Marvel?"

    coder "Lo nggak capek?"

    designer "Mainnya kan sambil duduk."

    coder "Alasan yang bagus."

    designer "Jadi?"

    coder "Nanti kabarin aja."

    "Jane tersenyum."

    "Sepertinya, hari ini belum cukup melelahkan untuk membuat mereka melewatkan satu pertandingan."

    $ website_progress = min(100, website_progress + 3)

    jump ch2_scene_04


# ============================================================
# SCENE 04 — STILL NO FILES
# 77 DAYS LEFT
#
# Jumlah menu: 3
#
# Menu 10 = respons soal jawaban Adrian.
# Menu 11 = candaan galeri museum.
# Menu 12 = pilihan bukti rahasia pertama.
# ============================================================

label ch2_scene_04:

    $ days_left = 77

    scene black with dissolve

    $ hud_visible = True

    # Lokasi: Grup chat Museum Arunika dan kontrakan Luuk.

    "Dua hari berikutnya tidak sepenuhnya digunakan untuk mengerjakan Museum Arunika."

    "Luuk disibukkan tugas Pemrograman Berorientasi Objek. Jane juga harus menyelesaikan beberapa pekerjaan kuliah."

    "Pada malam sebelumnya, mereka sempat membahas proyek lewat chat, tetapi tidak banyak yang berubah."

    "Hari ini, Jane kembali membuka grup Museum Arunika."

    "Jane (grup): Adrian, gambar sama deskripsi koleksinya gimana?"

    "Jane (grup): Ada yang udah bisa dikirim?"

    "Pesan terkirim."

    "Beberapa waktu kemudian, statusnya berubah menjadi sudah dibaca."

    "Tidak ada balasan."

    "Jane (chat pribadi): Luuk."

    "Luuk (chat): Kenapa?"

    "Jane (chat): Adrian belum bales."

    "Luuk (chat): Yang tadi?"

    "Jane (chat): Iya. Udah dibaca."

    "Luuk (chat): Gue coba tanya."

    "Luuk membuka grup."

    "Luuk (grup): Adrian, bahan museumnya udah sampai mana?"

    "Beberapa saat berlalu."

    "Adrian (grup): Belum."
    
    $ stress_level = min(100, stress_level + 3)

    "Luuk (grup): Oh, oke. Kalau ada yang susah bilang aja, ya."

    "Adrian (grup): Iya."

    "Tidak ada pesan lain."

    "Luuk menatap layar sebentar."

    coder "(Belum, ya...)"

    "Ia mengirim pesan kepada Jane."

    "Luuk (chat): Katanya belum."

    "Jane (chat): Iya, gue liat."

    designer "Jawabannya pendek banget."

    coder "Iya."

    designer "Gue kira dia bakal jelasin udah ngerjain apa."


    # ========================================================
    # MENU 10 — RESPONS SOAL ADRIAN
    #
    # Dua opsi.
    # Hanya mengubah dialog.
    # Tidak memengaruhi bukti Secret Ending.
    # ========================================================

    menu:

        "Mungkin emang belum ada yang dikerjain.":

            coder "Mungkin emang belum ada yang dikerjain."

            designer "Ya, kemungkinan."

            coder "Nanti kita tanya lagi kalau udah beberapa hari."

            designer "Oke."


        "Setidaknya sekarang kita tahu dia belum selesai.":

            coder "Setidaknya sekarang kita tahu dia belum selesai."

            designer "Iya, sih."

            coder "Daripada kita nebak-nebak."

            designer "Bener juga."


    # ========================================================
    # LANJUTAN SCENE 04
    # ========================================================

    "Luuk (chat): Yaudah, galeri pakai gambar sementara dulu."

    "Jane (chat): Oke. Nanti gue ke sana."

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Siang harinya, Jane tiba di kontrakan Luuk."

    "Ia meletakkan laptop di meja yang sama seperti dua hari sebelumnya."

    designer "Halo."

    coder "Halo."

    designer "Lagi apa?"

    coder "Tugas PBO."

    designer "Udah selesai?"

    coder "Belum."

    designer "Oke. Berarti kita sama."

    coder "Lo lagi ngerjain apa?"

    designer "Tadi Pancasila. Nanti gue mau lanjut desain museum."

    coder "Sip."

    "Jane duduk dan membuka laptop."

    designer "Yang dari Adrian masih kosong, ya."

    coder "Iya."

    designer "Padahal kalau gambar sama deskripsinya udah ada, gue bisa sekalian bikin galeri."

    coder "Sementara pakai kotak kosong dulu aja."

    designer "Iya. Tapi nanti harus diganti semua."

    coder "Nanti kalau udah ada bahannya."

    designer "Hmm."

    "Jane membuka rancangan galeri Museum Arunika."

    "Di dalamnya terdapat beberapa kartu koleksi dengan gambar dan teks sementara."

    designer "Eh, menurut lo galeri ini kebanyakan kotak nggak?"

    coder "Maksudnya?"

    designer "Kalau ada sepuluh gambar, mau ditampilin semuanya atau dibagi beberapa bagian?"

    coder "Bisa dibagi kategori."

    designer "Nah, itu. Gue juga mikir begitu."

    coder "Tapi koleksinya belum ada."

    designer "Iya..."

    designer "Gue bikin layout-nya dulu aja."

    coder "Oke."


    # ========================================================
    # MENU 11 — CANDAAN GALERI MUSEUM
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Ini museum koleksi kotak kosong.":

            coder "Ini museum koleksi kotak kosong."

            designer "Konsep abstrak."

            coder "Pengunjung bayar buat lihat kekosongan."

            designer "Seni kontemporer."

            coder "Tiketnya mahalin, berarti."

            designer "Jangan."


        "Nanti bagus kalau gambarnya udah masuk.":

            coder "Nanti bagus kalau gambarnya udah masuk."

            designer "Iya, gue juga ngerasa begitu."

            coder "Layout-nya udah enak dilihat."

            designer "Wih, makasih."

            coder "Jangan dibiasain."

            designer "Telat. Udah gue catat."


        "Bagian kotak kosongnya paling gampang dikoding.":

            coder "Bagian kotak kosongnya paling gampang dikoding."

            designer "Ya jangan dikosongin terus."

            coder "Padahal udah bagus."

            designer "Luuk."

            coder "Iya, nanti diisi."


    # ========================================================
    # LANJUTAN SCENE 04
    # ========================================================

    "Luuk kembali membuka proyek website."

    "Ia mencoba mencari file halaman booking yang terakhir diubah."

    coder "Eh, bentar."

    designer "Kenapa?"

    coder "File yang kemarin mana, ya?"

    designer "Yang booking?"

    coder "Iya."

    designer "Bukannya yang itu?"

    coder "Itu versi lama."

    designer "Lah, terus yang baru?"

    coder "Ada. Sebentar."

    "Luuk membuka beberapa folder."

    coder "Nah, ketemu."

    designer "Namanya mirip banget."

    coder "Iya."

    designer "Kita harus rapihin cara nyimpen kerjaan, deh."

    coder "Setuju."

    designer "Enaknya gimana?"


    # ========================================================
    # MENU 12 — BUKTI RAHASIA PERTAMA
    #
    # Pilihan A:
    # "Bikin catatan progres mingguan aja."
    #
    # catatan_progres_dibuat = True
    # jumlah_bukti_rahasia bertambah 1.
    #
    # Pilihan B:
    # "Rapihin folder proyeknya aja dulu."
    #
    # catatan_progres_dibuat = False
    # jumlah_bukti_rahasia tidak bertambah.
    #
    # PENTING:
    # Jangan tampilkan nilai bukti kepada pemain.
    # ========================================================

    menu:

        "Bikin catatan progres mingguan aja.":

            # Cek apakah bukti ini pernah diberikan.
            # Jika belum, tambahkan satu bukti rahasia.
            if not catatan_progres_dibuat:
                $ jumlah_bukti_rahasia += 1

            # Tandai bahwa pemain membuat catatan progres.
            $ catatan_progres_dibuat = True

            coder "Bikin catatan progres mingguan aja, gimana?"

            designer "Boleh. Isinya apa?"

            coder "Yang udah dikerjain, yang belum, sama siapa yang ngerjain."

            designer "Oh, jadi kayak daftar pekerjaan."

            coder "Iya. Sama tanggal update-nya."

            designer "Boleh. Biar nggak lupa yang kemarin udah sampai mana."

            "Jane membuka sebuah dokumen baru."

            designer "Gue bikin tabel sederhana aja, ya."

            coder "Oke."

            "Jane mulai memasukkan pembagian tugas yang sudah mereka sepakati pada Chapter 1."

            designer "Bagian lo: struktur website sama sistem tiket."

            coder "Iya."

            designer "Bagian gue: UI/UX sama prototype."

            coder "Betul."

            designer "Adrian: sepuluh gambar referensi sama lima deskripsi koleksi."

            coder "Iya."

            "Jane menambahkan kolom perkembangan pekerjaan."

            designer "Yang dari Adrian masih kosong dulu, ya."

            coder "Iya. Nanti kalau dia udah kirim, kita update."

            designer "Sip."

            "Dokumen tersebut disimpan bersama file proyek lainnya."

            designer "Nanti tiap ada progres kita isi aja."

            coder "Boleh. Jadi nggak perlu nginget semua."


        "Rapihin folder proyeknya aja dulu.":

            # Pemain tidak memilih membuat catatan progres.
            $ catatan_progres_dibuat = False

            # Tidak ada penambahan jumlah_bukti_rahasia.

            coder "Mending rapihin folder proyeknya dulu. Biar nggak ketuker."

            designer "Oke. Ini sekarang ada berapa folder?"

            coder "Lumayan."

            designer "Ada yang namanya 'baru' sama 'baru_banget'."

            coder "..."

            designer "Itu apa?"

            coder "Sejarah perkembangan proyek."

            designer "Sejarah yang membingungkan."

            "Keduanya mulai memisahkan file desain, kode, gambar sementara, dan dokumen lain."

            coder "Nah, ini lebih gampang."

            designer "Iya. Nanti kalau nyari file nggak muter-muter."

            coder "Bikin folder aset museum juga."

            designer "Oke. Nanti kalau bahan dari Adrian ada, langsung masuk situ."

            "Folder aset museum selesai disiapkan."

            "Isinya masih didominasi gambar sementara."


    # ========================================================
    # KONSEKUENSI MENU 12
    #
    # Dialog berubah berdasarkan pilihan pemain.
    # ========================================================

    if catatan_progres_dibuat:

        designer "Enak juga kalau ada catatan begini."

        coder "Kenapa?"

        designer "Jadi kelihatan terakhir kita ngerjain apa. Nggak harus nginget satu-satu."

        coder "Iya. Apalagi kalau nanti tugasnya makin banyak."

        designer "Betul."

    else:

        designer "Nah, sekarang lebih gampang nyari file."

        coder "Iya. Tadi aja gue hampir buka versi yang salah."

        designer "Jangan sampai pas presentasi begitu."

        coder "Masih lama juga presentasinya."

        designer "Iya, sih."


    # ========================================================
    # PENUTUP SCENE 04
    # ========================================================

    "Jane kembali melanjutkan desain galeri."

    "Luuk menyelesaikan sedikit tugas PBO sebelum melanjutkan halaman Museum Arunika."

    "Beberapa jam berikutnya berjalan cukup produktif, meskipun mereka sesekali berhenti untuk mengobrol."

    designer "Eh, Luuk."

    coder "Hm?"

    designer "Kalau bahan dari Adrian belum ada minggu depan gimana?"

    coder "Ya kita pakai placeholder lebih lama."

    designer "Terus kalau dia baru ngirim pas mepet?"

    coder "Nanti kita sesuaikan."

    designer "Hmm, oke."

    "Jane tidak terlalu memperpanjang pembicaraan itu."

    "Luuk juga tidak."

    "Saat itu, mereka masih mengira keterlambatan satu bagian kecil bisa diselesaikan dengan mudah."

    "Belum ada yang menyangka bahwa bagian tersebut pada akhirnya harus mereka kerjakan sendiri."

    $ website_progress = min(100, website_progress + 1)

    jump ch2_scene_05


# ============================================================
# SCENE 05 — PLENTY OF TIME
# 75 DAYS LEFT
#
# Jumlah menu: 3
#
# Menu 13 = candaan ajakan Marvel.
# Menu 14 = candaan soal satu match lagi.
# Menu 15 = candaan revisi desain.
#
# Ketiganya tidak mengubah variabel pilihan penting.
# ============================================================

label ch2_scene_05:

    $ days_left = 75

    scene black with dissolve

    $ hud_visible = True

    show coder at char_center

    # Lokasi: Kontrakan Luuk, malam hari.

    "Beberapa hari berlalu."

    "Tidak setiap hari Luuk dan Jane mengerjakan Museum Arunika bersama."

    "Kadang Jane datang ke kontrakan Luuk untuk mengerjakan desain. Kadang mereka mengerjakan bagian masing-masing dari tempat berbeda."

    "Ada hari ketika Luuk cukup lama berkutat dengan kode."

    "Ada juga hari ketika folder proyek hampir tidak dibuka sama sekali."

    "Di luar proyek museum, tugas mata kuliah lain terus berdatangan."

    "Malam ini, Luuk sedang mengerjakan tugas Pemrograman Berorientasi Objek ketika Jane mengirim pesan."

    "Jane (chat): Luuk."

    "Luuk (chat): Apa?"

    "Jane (chat): Tugas PBO udah?"

    "Luuk (chat): Belum."

    "Jane (chat): Gue juga."

    "Luuk (chat): Berarti aman."

    "Jane (chat): Aman dari mana?"

    "Luuk (chat): Setidaknya gue nggak sendirian."

    "Jane (chat): Anjir."

    "Luuk tertawa kecil."

    "Jane (chat): Eh, yang Kecerdasan Buatan gimana?"

    coder "Jangan dibahas."

    "Jane (chat): Berarti belum?"

    coder "..."

    "Jane (chat): Oke, paham."

    "Beberapa menit kemudian, Jane masuk ke voice call."

    designer "Halo."

    coder "Halo."

    designer "Lagi ngerjain PBO?"

    coder "Iya."

    designer "Gue juga."

    coder "Kok bisa sama?"

    designer "Karena tugasnya sama?"

    coder "Oh, iya."

    designer "Gue udah mulai pusing lihat tugas."

    coder "Sama."

    designer "Mau istirahat bentar?"

    coder "Bentar gimana?"

    designer "Marvel."

    "Luuk melihat jendela tugas yang masih terbuka."


    # ========================================================
    # MENU 13 — CANDAAN AJAKAN MARVEL RIVALS
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Lo nggak bosen ngajak Marvel terus?":

            coder "Lo nggak bosen ngajak Marvel terus?"

            designer "Nggak."

            coder "Jawabnya cepet banget."

            designer "Kan emang nggak."

            coder "Yaudah, gas."


        "Bentar, gue save tugas dulu.":

            coder "Bentar, gue save tugas dulu."

            designer "Oke. Jangan sampai hilang."

            coder "Iya."

            designer "Kemarin ada yang lupa save, soalnya."

            coder "Jangan diungkit."

            designer "Siapa tuh?"

            coder "Udah, gas."


        "Kalau kalah, lo yang tanggung jawab.":

            coder "Kalau kalah, lo yang tanggung jawab."

            designer "Lah, kenapa gue?"

            coder "Lo yang ngajak."

            designer "Kalau menang berarti gue juga yang berjasa."

            coder "Nggak gitu."

            designer "Yaudah, gas."


    # ========================================================
    # LANJUTAN SCENE 05
    # ========================================================

    "Luuk menyimpan pekerjaan yang sedang dibuka."

    "Tak lama kemudian, keduanya sudah berada dalam pertandingan Marvel Rivals."

    designer "Kanan!"

    coder "Gue lihat!"

    designer "Ada yang di belakang lo!"

    coder "IYA!"

    "Pertandingan berlangsung sengit."

    "Beberapa kali mereka hampir berhasil membalikkan keadaan, tetapi akhirnya kalah."

    coder "..."

    designer "..."

    coder "Hampir."

    designer "Iya."

    coder "Padahal tadi udah bagus."

    designer "Satu lagi?"

    coder "Tadi lo bilang istirahat bentar."

    designer "Iya, bentar."

    coder "Ini udah lumayan lama."

    designer "Tapi kita belum menang."

    "Luuk menghela napas kecil."

    coder "Alasan lo selalu ada."

    designer "Jadi satu lagi?"


    # ========================================================
    # MENU 14 — CANDAAN SATU MATCH LAGI
    #
    # Tiga opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Oke, tapi kali ini serius terakhir.":

            coder "Oke, tapi kali ini serius terakhir."

            designer "Iya, serius."

            coder "Gue catat."

            designer "Silakan."

            coder "Kalau nanti lo ngajak lagi, gue bacain."

            designer "Nanti juga lo yang ngajak."


        "Kita ini sebenarnya main satu match atau satu malam?":

            coder "Kita ini sebenarnya main satu match atau satu malam?"

            designer "Tergantung menangnya kapan."

            coder "Waduh."

            designer "Gas?"

            coder "Gas."


        "Besok kalau ngantuk, salahin lo.":

            coder "Besok kalau ngantuk, salahin lo."

            designer "Lo juga mau main, kan?"

            coder "Iya, tapi..."

            designer "Nah."

            coder "Oke, gue kalah debat."

            designer "Sekarang jangan kalah game."


    # ========================================================
    # LANJUTAN SCENE 05
    # ========================================================

    "Pertandingan berikutnya akhirnya dimulai."

    "Setelah beberapa waktu, mereka berhenti bermain."

    # Luuk merasa lebih santai setelah bermain bersama Jane.
    $ stress_level = max(0, stress_level - 2)

    "Luuk kembali membuka folder Museum Arunika."

    designer "Eh, ngomong-ngomong."

    coder "Hm?"

    designer "Museum kita udah sampai mana, ya?"

    coder "Udah ada halaman awal, form tiket sebagian, sama desain lo."

    designer "Oh, iya."

    coder "Galeri masih nunggu bahan."

    designer "Iya. Nanti gue lanjut."

    coder "Gue juga mau lanjut bagian booking."

    designer "Terus halaman admin?"

    coder "Belum."

    designer "Pembayarannya?"

    coder "Belum juga."

    designer "Oh."

    "Jane terdiam sebentar."

    designer "Yaudah, nanti satu-satu."

    coder "Iya. Masih ada waktu."

    designer "Betul."

    designer "Eh, kalau websitenya udah jadi, kita cobain pesan tiket nggak?"

    coder "Ya harus dicoba."

    designer "Maksud gue, kita jadi pengunjung."

    coder "Oh."

    designer "Gue pesan lima tiket."

    coder "Buat siapa?"

    designer "Nggak tahu. Tes aja."

    coder "Jangan lupa pembayarannya simulasi."

    designer "Iya. Kalau beneran, gue nggak jadi."

    coder "Lah."

    designer "Kan cuma mau ngetes."

    coder "Yaudah, nanti pas fitur tiketnya udah jalan."

    designer "Oke."

    coder "Terus kalau udah jadi, lo yang cek tampilannya."

    designer "Siap."

    coder "Kalau ada tombol yang geser dua pixel, jangan langsung panik."

    designer "Tiga pixel boleh?"

    coder "..."

    designer "Bercanda."

    coder "Gue nggak yakin."

    designer "Lo beneran takut gue nyuruh revisi lagi?"


    # ========================================================
    # MENU 15 — CANDAAN REVISI DESAIN
    #
    # Dua opsi.
    # Hanya mengubah dialog.
    # ========================================================

    menu:

        "Bukan takut. Gue cuma siap-siap mental.":

            coder "Bukan takut. Gue cuma siap-siap mental."

            designer "Separah itu?"

            coder "Kemarin dua pixel. Besok bisa satu."

            designer "Kalau memang perlu."

            coder "Nah, kan."


        "Asal jangan revisi pas gue udah ngantuk.":

            coder "Asal jangan revisi pas gue udah ngantuk."

            designer "Emang biasanya lo ngoding jam berapa?"

            coder "Tergantung."

            designer "Berarti gue harus nebak."

            coder "Mending besok aja revisinya."

            designer "Yaudah, besok."


    # ========================================================
    # PENUTUP CHAPTER 02
    # ========================================================

    "Jane tertawa."

    "Obrolan kembali beralih ke tugas kuliah dan rencana hari berikutnya."

    designer "Besok gue kayaknya nggak ke kontrakan dulu."

    coder "Kenapa?"

    designer "Mau nyelesain tugas yang lain."

    coder "Oke."

    designer "Kalau sempat, gue lanjutin desain museum."

    coder "Sip. Gue juga."

    designer "Nanti kalau ada error, kabarin."

    coder "Lo mau bantu debugging?"

    designer "Nggak. Mau tahu aja."

    coder "Kirain."

    designer "Tapi kalau tampilan yang bermasalah, gue bantu."

    coder "Nah, itu baru."

    designer "Kan bagian gue."

    coder "Iya."

    "Percakapan diakhiri tidak lama kemudian."

    "Luuk menutup voice call."

    "Ia sempat melihat daftar file proyek sebelum mematikan laptop."

    "Website Museum Arunika sudah memiliki bentuk awal."

    "Beberapa rancangan halaman selesai. Sebagian fungsi mulai bekerja. Ada pula bagian yang belum disentuh sama sekali."

    "Bahan dari Adrian masih belum tersedia."

    "Namun, tidak ada yang terasa terlalu mendesak."

    "Luuk dan Jane tetap bekerja ketika ada kesempatan."

    "Hanya saja, kesempatan itu sering dibagi dengan banyak hal lain."

    "Dan mereka belum menyadari betapa cepatnya hari-hari akan berlalu."

    "Lima belas hari telah berlalu sejak dosen memberikan tugas akhir."

    "Tujuh puluh lima hari masih tersisa."

    "Bagi Luuk dan Jane, angka itu masih terdengar besar."

    "Masih ada waktu untuk memperbaiki tampilan."

    "Masih ada waktu untuk menyelesaikan fitur tiket."

    "Masih ada waktu untuk mengurus database, halaman admin, dan pembayaran simulasi."

    "Setidaknya, itulah yang mereka pikirkan."


    # ========================================================
    # CHAPTER 02 COMPLETE
    # ========================================================

    $ hud_visible = False

    scene black with fade

    centered "{size=50}CHAPTER 02 COMPLETE{/size}\n{size=36}75 DAYS LEFT{/size}\n{size=28}We still have time.{/size}"

    jump chapter_3