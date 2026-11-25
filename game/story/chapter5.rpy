# ============================================================
# THE DEADLINERS — CHAPTER 05: PIECES THAT DON'T FIT
# H-42 -> H-30 | 5 scene | 15 menu pilihan
# ============================================================
# 12 menu dialog biasa, 2 menu penting, 1 kesempatan bukti rahasia.
# Tidak ada penentuan ending di Chapter 5.

# MENU 04: memilih pekerjaan teknis utama Chapter 5.
# "booking" = menghubungkan alur form ke data pesanan untuk tes lokal.
# "admin" = melanjutkan daftar pesanan pada halaman admin.
default fokus_utama_ch5 = ""

# MENU 09: bukti rahasia keempat.
# True = rekap berkas hasil kerja per anggota dan tanggal pengumpulan disimpan.
default rekap_pengumpulan_ch5 = False

# MENU 11: memilih pekerjaan lanjutan Chapter 5.
# "pembayaran" = melanjutkan alur pembayaran simulasi.
# "galeri" = menguji dan merapikan tampilan galeri dengan placeholder.
default fokus_lanjutan_ch5 = ""

# Variabel dari chapter sebelumnya sudah ada dan JANGAN dideklarasikan lagi:
# form_tiket_dikerjakan_dulu, prioritas_pengerjaan_website,
# catatan_progres_dibuat, jumlah_bukti_rahasia,
# uji_booking_dulu, arsip_chat_kelompok_tersimpan,
# prioritas_teknis_lanjutan,
# fokus_pengerjaan_ch4, konfirmasi_target_adrian, fokus_lanjutan_ch4,
# days_left, hud_visible, website_progress, stress_level.


label chapter_5:
    $ hud_visible = False
    $ days_left = 42
    scene black with fade
    centered "{size=50}CHAPTER 05{/size}\n{size=42}PIECES THAT DON'T FIT{/size}\n{size=34}42 DAYS LEFT{/size}"
    jump ch5_scene_01


# ============================================================
# SCENE 01 — A SCHEDULE IS NOT A SOLUTION | H-42
# MENU 01, 02, 03: pilihan dialog biasa.
# ============================================================
label ch5_scene_01:
    $ days_left = 42
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari berlalu sejak Luuk dan Jane menyadari separuh waktu pengerjaan Museum Arunika telah habis."
    "Mereka mulai mencoba mengikuti jadwal yang dibuat pada akhir pertemuan sebelumnya."
    "Sore itu, keduanya duduk di area kampus dengan laptop masing-masing."
    "Di antara mereka terdapat daftar pekerjaan yang sudah diberi tanda prioritas."
    designer "Woy."
    coder "Woy."
    designer "Hari ini lo datang duluan."
    coder "Iya."
    designer "Tumben."
    coder "Apa setiap kali gue tepat waktu harus dibahas?"
    designer "Soalnya ini perkembangan besar."
    coder "Gue merasa sedang dinilai."
    designer "Memang."
    coder "Oke."
    "Jane meletakkan tasnya dan membuka laptop."
    designer "Jadwal yang kemarin udah lo lihat?"
    coder "Udah."
    designer "Ada yang bentrok?"
    coder "Yang hari Kamis sama tugas PBO."
    designer "Oh, iya. Gue juga ada tugas itu."
    coder "Jadi mending pindah Jumat."
    designer "Oke."
    coder "Asal jangan Jumat malam banget."
    designer "Kenapa?"
    coder "Gue mau masih punya waktu tidur."
    designer "Wah, sekarang lo menghargai tidur?"
    coder "Sejak kemarin."

    # MENU 01 — hanya mengubah respons.
    menu:
        "Tidur adalah bagian dari produktivitas.":
            coder "Tidur adalah bagian dari produktivitas."
            designer "Kalimat bagus."
            coder "Makasih."
            designer "Sayang lo baru sadar sekarang."
            coder "Lebih baik terlambat daripada nggak sama sekali."
            designer "Kalau soal tugas, jangan pakai prinsip itu."

        "Gue cuma nggak mau ngantuk pas coding.":
            coder "Gue cuma nggak mau ngantuk pas coding."
            designer "Emang kalau ngantuk gimana?"
            coder "Bisa salah nulis satu huruf terus nyarinya sejam."
            designer "Oh."
            coder "Pengalaman pribadi."
            designer "Pantes ngomongnya serius."

        "Kalau jadwalnya penuh, kapan kita main?":
            coder "Kalau jadwalnya penuh, kapan kita main?"
            designer "Marvel?"
            coder "Iya."
            designer "Kalau tugas hari itu beres."
            coder "Wah, ada syaratnya."
            designer "Biar kita nggak lupa waktu lagi."
            coder "Oke, masuk akal."

    "Jane membuka daftar fitur Museum Arunika."
    designer "Kita mulai dari pekerjaan yang paling nyangkut, ya."
    coder "Yang mana?"
    designer "Itu masalahnya."
    coder "Lah."
    designer "Semuanya kayak nyambung ke yang lain."
    coder "Makanya kemarin gue bilang perlu urutan."
    designer "Iya, gue ngerti sekarang."

    # Kondisi harga tiket memperhitungkan Chapter 2, 3, DAN 4.
    if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking":
        designer "Hitungan harga tiket udah ada."
        coder "Iya, tapi belum otomatis berarti seluruh pesanan bisa disimpan."
        designer "Berarti masih perlu dihubungkan."
        coder "Betul."
    else:
        designer "Hitungan harga tiket juga masih ada di daftar."
        coder "Iya. Kita belum beresin bagian itu."
        designer "Kalau begitu jangan dianggap booking udah siap."
        coder "Setuju."

    if fokus_pengerjaan_ch4 == "data_pemesanan":
        designer "Struktur data yang kemarin kita buat masih ada, kan?"
        coder "Ada. Tapi baru untuk percobaan lokal."
        designer "Oke. Setidaknya nggak mulai dari nol."
    else:
        designer "Penyimpanan pesanan belum kita kerjain banyak."
        coder "Iya. Form-nya lebih lengkap, tapi data belum punya alur penyimpanan yang rapi."
        designer "Berarti itu juga perlu."

    if fokus_lanjutan_ch4 == "admin":
        designer "Tampilan admin yang kemarin udah lumayan."
        coder "Iya, tabelnya udah kebentuk."
        designer "Tapi masih pakai data percobaan."
        coder "Benar."
    else:
        designer "Halaman admin masih belum kita urus banyak."
        coder "Iya. Kemarin kita lebih fokus ngetes booking."
        designer "Oke. Masuk daftar."

    "Jane menandai beberapa pekerjaan dengan simbol kecil di catatannya."
    designer "Kalau dilihat begini, jadwal doang nggak cukup, ya."
    coder "Jadwal ngasih tahu kapan kerja. Bukan bikin pekerjaannya selesai."
    designer "Iya juga."
    coder "Tapi lebih baik daripada ngerjain semuanya random."
    designer "Setuju."

    # MENU 02 — pilihan dialog biasa.
    menu:
        "Kita perlu daftar yang lebih jujur.":
            coder "Kita perlu daftar yang lebih jujur."
            designer "Maksudnya?"
            coder "Jangan tulis selesai kalau baru tampilan doang."
            designer "Oh. Jadi dibedain antara desain, fungsi, sama tes?"
            coder "Iya."
            designer "Oke, itu masuk akal."

        "Yang penting kita ngerjainnya rutin.":
            coder "Yang penting kita ngerjainnya rutin."
            designer "Iya. Bukan nunggu sempat."
            coder "Kalau satu hari cuma sedikit juga nggak apa-apa."
            designer "Asal jelas hasilnya."
            coder "Nah."

    "Jane menggulir sampai bagian konten koleksi."
    designer "Eh, yang ini masih kosong."
    coder "Bahan dari Adrian?"
    designer "Iya."
    coder "Belum ada kabar baru?"
    designer "Belum ada file."
    if konfirmasi_target_adrian:
        designer "Padahal waktu itu dia udah setuju sama target dua hari."
        coder "Iya. Konfirmasinya ada."
        designer "Tapi hasilnya belum."
    else:
        designer "Kita udah ingetin, tapi masih belum ada hasil."
        coder "Iya."
        designer "Nanti gue tanya lagi."
    "Jane menutup folder koleksi dan kembali ke daftar utama."
    coder "Sementara itu kita jangan berhenti di bagian lain."
    designer "Iya."
    "Luuk menyalin daftar pekerjaan yang paling mendesak ke catatannya sendiri."
    designer "Lo nulis apa?"
    coder "Yang harus berfungsi buat pengunjung."
    designer "Booking?"
    coder "Iya. Sama data pesanan dan halaman yang nyambung."
    designer "Oke."

    # MENU 03 — pilihan dialog biasa.
    menu:
        "Gue mau semua tombol punya tujuan yang jelas.":
            coder "Gue mau semua tombol punya tujuan yang jelas."
            designer "Jangan ada yang cuma buat pajangan?"
            coder "Iya. Kecuali memang dekorasi."
            designer "Oke, gue cek tombol di prototype juga."
            coder "Sip."

        "Nanti gue coba jadi pengunjung yang nyebelin.":
            coder "Nanti gue coba jadi pengunjung yang nyebelin."
            designer "Maksudnya?"
            coder "Klik semua yang mungkin diklik."
            designer "Oh, buat cari bug."
            coder "Iya."
            designer "Kayaknya lo cocok."
            coder "Sebagai pengunjung?"
            designer "Yang nyebelin."

    "Sore itu mereka belum menyelesaikan fitur baru."
    "Namun, daftar pekerjaan menjadi lebih jelas: halaman yang sudah terlihat bagus belum tentu siap digunakan."
    "Luuk mulai merasa bahwa waktu pengerjaan harus dimanfaatkan lebih teratur."
    $ stress_level = min(100, stress_level + 2)
    jump ch5_scene_02


# ============================================================
# SCENE 02 — THE PARTS HAVE TO CONNECT | H-39
# MENU 04: pilihan penting (booking / admin).
# MENU 05, 06: pilihan dialog biasa.
# ============================================================
label ch5_scene_02:
    $ days_left = 39
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk dan Jane kembali bertemu di kontrakan Luuk."
    "Mereka sengaja menyediakan waktu lebih panjang untuk Museum Arunika."
    "Di laptop Luuk, halaman pemesanan dan kode pengelolaan data sudah terbuka."
    designer "Oke, hari ini kita ngerjain yang mana?"
    coder "Ada dua bagian yang bisa kita dorong dulu."
    designer "Sebut."
    coder "Alur booking dari form sampai ringkasan, atau daftar pesanan di admin."
    designer "Dua-duanya penting."
    coder "Iya. Tapi kalau kita kerjain barengan, takutnya malah nggak ada yang beres."
    designer "Oke, pilih satu dulu."

    # MENU 04 — PILIHAN PENTING PERTAMA.
    # Pilihan disimpan dan memengaruhi dialog Scene 4 dan Scene 5.
    menu:
        "Hubungkan form booking dengan data pesanan dulu.":
            $ fokus_utama_ch5 = "booking"
            coder "Hubungkan form booking dengan data pesanan dulu."
            designer "Biar habis isi form langsung ada ringkasannya?"
            coder "Iya. Minimal buat alur uji lokal dulu."
            designer "Oke. Gue bantu tes."

            if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking":
                coder "Perhitungan harga udah ada. Gue pakai itu buat data pesanan."
                designer "Jadi nggak perlu bikin dari awal?"
                coder "Nggak. Tinggal kita cek hasilnya benar atau nggak."
            else:
                coder "Sebelum disambung, total harganya harus gue beresin dulu."
                designer "Yang kemarin masih tertunda?"
                coder "Iya."
                "Luuk memperbaiki perhitungan total harga berdasarkan jumlah tiket yang dipilih."
                "Jane mencoba beberapa jumlah tiket sampai angkanya sesuai."
                designer "Nah, sekarang totalnya berubah dengan benar."
                coder "Iya. Ini baru hitungannya, belum seluruh sistem."
                designer "Oke."

            if fokus_pengerjaan_ch4 == "data_pemesanan":
                coder "Struktur data lokal dari kemarin bisa kita pakai."
                designer "Berarti tinggal kirim hasil form ke situ?"
                coder "Iya. Tapi masih harus dicek lagi."
            else:
                coder "Kita belum punya struktur penyimpanan yang rapi. Gue bikin yang sederhana buat uji dulu."
                designer "Ini udah database final?"
                coder "Belum. Kita mulai dari penyimpanan lokal dan data tes."
                designer "Oke."

            "Luuk menghubungkan input form dengan ringkasan pemesanan sederhana."
            "Jane mencoba memasukkan nama, tanggal kunjungan, dan jumlah tiket."
            "Pada percobaan pertama, ringkasan belum menampilkan seluruh data dengan benar."
            designer "Eh, tanggalnya beda."
            coder "Bentar. Gue cek cara ngambil datanya."
            "Luuk membetulkan bagian yang salah, lalu mereka mencoba lagi."
            designer "Nah, sekarang cocok."
            coder "Iya."
            "Alur dari form menuju ringkasan pesanan mulai bekerja dengan data uji."
            "Penyimpanan permanen, pembayaran, serta penanganan semua kondisi belum selesai."
            designer "Jadi pengunjung udah bisa lihat ringkasan?"
            coder "Bisa dalam pengujian ini. Belum bisa dibilang sistem booking lengkap."
            designer "Siap."
            $ website_progress = min(100, website_progress + 5)
            $ stress_level = max(0, stress_level - 2)

        "Lanjutkan daftar pemesanan di halaman admin dulu.":
            $ fokus_utama_ch5 = "admin"
            coder "Lanjutkan daftar pemesanan di halaman admin dulu."
            designer "Oke. Biar hasil pesanan nanti gampang dilihat?"
            coder "Iya. Kita siapin tampilan dan cara nampilin datanya."
            designer "Gue bantu rapihin tabel."

            if fokus_lanjutan_ch4 == "admin":
                designer "Tabel admin yang kemarin bisa kita lanjut."
                coder "Iya. Sekarang kita tambah status dan cara lihat detail pesanan."
            else:
                designer "Berarti kita bikin kerangkanya dari awal?"
                coder "Iya. Nggak perlu rumit dulu."
                "Jane membuat rancangan tabel berisi nomor pesanan, tanggal, dan status."
                designer "Oke, bentuk dasarnya udah ada."

            if fokus_pengerjaan_ch4 == "data_pemesanan":
                coder "Data percobaan yang kemarin kita simpan bisa dipakai buat ngetes tabel."
                designer "Bagus. Jadi kelihatan kalau pesanan bertambah."
                coder "Iya, walaupun belum terhubung dengan semua halaman."
            else:
                coder "Karena penyimpanan belum siap, kita pakai data contoh dulu."
                designer "Oke. Jadi belum data dari form beneran."
                coder "Belum. Itu pekerjaan berikutnya."

            "Jane menyusun kolom agar tetap terbaca ketika beberapa pesanan ditampilkan."
            "Luuk membuat tampilan detail singkat untuk satu data percobaan."
            designer "Kalau statusnya belum dibayar, bisa dibedain?"
            coder "Bisa. Tapi itu baru status simulasi, bukan pembayaran sungguhan."
            designer "Oke."
            "Setelah beberapa revisi, tabel admin menjadi lebih mudah dibaca dan diperiksa."
            "Namun, data booking dari pengunjung belum sepenuhnya masuk otomatis ke halaman admin."
            designer "Sekarang admin-nya udah lebih jelas."
            coder "Iya. Tapi integrasi datanya tetap perlu kita kerjain."
            designer "Catat."
            $ website_progress = min(100, website_progress + 4)
            $ stress_level = max(0, stress_level - 2)

    "Jane melihat hasil pekerjaan di layar."
    designer "Akhirnya ada satu bagian yang kelihatan lebih beres."
    coder "Iya."
    designer "Tapi masih ada daftar masalahnya."
    coder "Selalu ada."
    designer "Lo ngomongnya kayak udah biasa banget."
    coder "Karena memang biasa."

    # MENU 05 — candaan sesudah bekerja, tanpa statistik.
    menu:
        "Bug adalah teman lama programmer.":
            coder "Bug adalah teman lama programmer."
            designer "Teman kok bikin susah?"
            coder "Teman yang sering datang tanpa diundang."
            designer "Berarti musuh dong."
            coder "Kadang sulit dibedain."

        "Gue cuma mau satu tombol jalan dengan tenang.":
            coder "Gue cuma mau satu tombol jalan dengan tenang."
            designer "Tombolnya bisa panik?"
            coder "Yang panik gue."
            designer "Oh, itu masuk akal."

        "Kalau semuanya langsung beres, ceritanya tamat.":
            coder "Kalau semuanya langsung beres, ceritanya tamat."
            designer "Cerita apa?"
            coder "Perjalanan kita melawan website."
            designer "Judulnya kepanjangan."
            coder "Nanti lo yang desain posternya."
            designer "Nggak mau."

    "Jane membuka daftar pekerjaan dan memeriksa fitur yang masih tertunda."
    designer "Kita nggak boleh lupa bagian yang tadi nggak dipilih."
    coder "Iya. Pilih prioritas bukan berarti yang lain hilang."
    designer "Bagus. Gue tulis."
    coder "Tulis apa?"
    designer "Jangan mengira tugas menghilang sendiri."
    coder "Itu lebih mirip nasihat hidup."
    designer "Gratis, lagi."

    # MENU 06 — dialog biasa.
    menu:
        "Tugas itu selalu nunggu orang yang salah.":
            coder "Tugas itu selalu nunggu orang yang salah."
            designer "Orang yang salah siapa?"
            coder "Gue yang berharap dia selesai sendiri."
            designer "Setidaknya sekarang lo sadar."
            coder "Iya."

        "Kita simpan hasilnya, terus istirahat sebentar.":
            coder "Kita simpan hasilnya, terus istirahat sebentar."
            designer "Oke. Jangan sampai lupa simpan."
            coder "Udah."
            designer "Beneran?"
            coder "Udah dua kali."
            designer "Bagus."

    "Luuk memastikan perubahan kode tersimpan."
    "Jane menyimpan revisi desain dan catatan pengujian."
    "Mereka menyelesaikan satu bagian dari proyek, tetapi pekerjaan lain masih menunggu giliran."
    jump ch5_scene_03


# ============================================================
# SCENE 03 — THE EMPTY FOLDER | H-36
# MENU 07, 08: dialog biasa.
# MENU 09: kesempatan bukti rahasia keempat.
# ============================================================
label ch5_scene_03:
    $ days_left = 36
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk dan Jane bertemu di koridor kampus setelah kelas."
    "Jane membawa laptop karena ingin memeriksa kembali isi galeri Museum Arunika."
    "Luuk baru selesai mengumpulkan sebuah tugas ketika Jane memanggilnya."
    designer "Luuk!"
    coder "Woy."
    designer "Sini bentar."
    coder "Kenapa?"
    designer "Gue mau lihat folder koleksi sama lo."
    coder "Udah ada file baru?"
    designer "Nah, itu yang mau gue tunjukin."
    "Mereka duduk di bangku dekat koridor."
    "Jane membuka folder bahan Museum Arunika."
    "Beberapa gambar contoh masih tersimpan di sana, tetapi belum ada bahan koleksi yang diberikan Adrian."
    designer "Masih sama."
    coder "Masih placeholder?"
    designer "Iya."
    coder "Hmm."
    designer "Gue udah cek folder sama grup."
    coder "Nggak ada yang baru?"
    designer "Nggak ada."
    if konfirmasi_target_adrian:
        designer "Target yang dia setujui kemarin juga udah lewat."
        coder "Iya, gue ingat."
        designer "Tapi belum ada file yang masuk."
        coder "Berarti kita perlu tahu kendalanya apa."
    else:
        designer "Kita udah beberapa kali ingetin."
        coder "Iya."
        designer "Tapi hasilnya masih nggak kelihatan."
        coder "Mungkin kita perlu minta penjelasan lebih jelas."

    "Jane mengetik pesan singkat di grup kelompok."
    "Jane (grup): Adrian, bahan koleksi Museum Arunika sudah ada yang bisa dikirim? Kalau belum, kendalanya apa?"
    "Mereka menunggu sambil memeriksa kembali desain galeri."
    "Beberapa menit kemudian, Adrian membalas."
    "Adrian (grup): Belum lengkap. Nanti kalau udah aku kirim."
    designer "..."
    coder "Belum lengkap."
    designer "Iya."
    coder "Berarti memang belum ada yang bisa dipakai sekarang."
    designer "Padahal yang udah ada juga boleh dikirim sebagian."
    coder "Iya."
    designer "Kalau memang susah cari gambar, tinggal bilang."
    coder "Bener."
    "Jane kembali menatap folder kosong."
    designer "Gue jadi nggak tahu harus nunggu sampai kapan."
    coder "Kita tetap bisa ngerapihin layout."
    designer "Bisa, tapi nanti kalau datanya beda, harus revisi lagi."
    coder "Iya. Itu yang bikin repot."

    # MENU 07 — dialog biasa, bukan konfrontasi besar.
    menu:
        "Kita minta yang sudah ada aja dulu.":
            coder "Kita minta yang sudah ada aja dulu."
            designer "Tadi udah gue bilang begitu."
            coder "Oh, iya."
            designer "Tapi jawabannya tetap belum lengkap."
            coder "Berarti kita belum tahu ada berapa yang jadi."
            designer "Nah."

        "Kalau nunggu terus, galeri nggak bakal dites pakai konten asli.":
            coder "Kalau nunggu terus, galeri nggak bakal dites pakai konten asli."
            designer "Itu yang gue khawatirin."
            coder "Placeholder masih bisa dipakai buat desain dasar."
            designer "Tapi nggak bisa buat memastikan hasil akhirnya."
            coder "Iya."

        "Gue kira kata 'nanti' sudah jadi anggota kelompok keempat.":
            coder "Gue kira kata 'nanti' sudah jadi anggota kelompok keempat."
            designer "Anjir."
            coder "Paling sering muncul di grup."
            designer "Tapi kontribusinya juga nggak ada."
            coder "Nah, cocok."
            designer "Gue ketawa, tapi sedih."

    "Luuk membuka daftar pembagian tugas yang sudah mereka gunakan sejak awal."
    coder "Kita bisa cek kerjaan yang udah selesai dari file aslinya."
    designer "Maksudnya?"
    coder "Yang kita buat selama ini ada filenya, kan?"
    designer "Iya. Desain sama kode."
    coder "Nah. Jadi bisa dilihat mana yang udah beneran dikumpulin."
    designer "Oh, iya."
    if catatan_progres_dibuat:
        designer "Catatan progres mingguan juga bisa dicocokkan."
        coder "Iya. Tapi tetap periksa filenya, jangan cuma baca status."
    else:
        designer "Selama ini kita lebih sering lihat daftar tugas biasa."
        coder "Iya. Tapi daftar tugas belum tentu nunjukin hasil yang udah ada."
    if arsip_chat_kelompok_tersimpan:
        designer "Riwayat chat awal juga masih tersimpan."
        coder "Sip. Tapi itu catatan komunikasi, beda sama hasil file."
    else:
        designer "Pesan-pesan lama masih ada di grup, sih."
        coder "Iya. Tapi kita perlu lihat hasil pekerjaannya juga."

    "Jane membuka folder desain dan menunjukkan beberapa versi prototype."
    designer "Kalau punyaku ini. Ada file yang terakhir gue update."
    coder "Oke. Punya gue juga ada riwayat versi kodenya."
    designer "Kalau folder Adrian..."
    "Jane berhenti sejenak."
    designer "Kosong, selain bahan contoh yang kita masukin sendiri."
    coder "Iya."
    designer "Hmm."
    "Luuk menutup daftar sementara itu."

    # MENU 08 — respons dialog biasa.
    menu:
        "Setidaknya kita tahu apa yang benar-benar sudah ada.":
            coder "Setidaknya kita tahu apa yang benar-benar sudah ada."
            designer "Iya. Jadi nggak asal ngira."
            coder "Yang belum ada tetap kita tulis belum ada."
            designer "Oke."

        "Beda antara 'lagi dikerjain' dan 'sudah dikirim' ternyata jauh.":
            coder "Beda antara 'lagi dikerjain' dan 'sudah dikirim' ternyata jauh."
            designer "Iya."
            coder "Kalau belum dikirim, kita nggak bisa pakai."
            designer "Benar. Dan gue butuh kontennya buat galeri."

    designer "Menurut lo, daftar filenya cukup kita lihat sekarang, atau perlu dibikin rekap?"
    coder "Hmm."
    designer "Biar nanti gampang tahu mana yang udah beneran masuk."

    # MENU 09 — KESEMPATAN BUKTI RAHASIA KEEMPAT.
    # Bukti ini BERBEDA dari catatan progres, arsip chat,
    # dan konfirmasi tenggat: isinya hasil file + tanggal per anggota.
    menu:
        "Simpan rekap file yang benar-benar dikumpulkan tiap anggota.":
            coder "Simpan rekap file yang benar-benar dikumpulkan tiap anggota."
            designer "Lengkap sama tanggalnya?"
            coder "Iya. Biar kalau ada file baru, kita tahu kapan masuk."
            designer "Oke. Kita bikin daftar sederhana."
            "Jane membuat tabel berisi nama anggota, bagian tugas, berkas yang tersedia, dan tanggal pembaruan."
            "Mereka memeriksa ulang folder desain, folder kode, serta folder bahan koleksi."
            designer "Punya gue masuk. Punya lo juga."
            coder "Iya."
            designer "Kalau Adrian, belum ada bahan yang dia kirim."
            coder "Tulis sesuai isi folder saat kita periksa. Jangan nambah-nambah."
            designer "Oke."
            "Jane mencatat bahwa folder bahan koleksi belum memiliki kiriman Adrian pada tanggal pemeriksaan itu."
            "Ia menyimpan rekap dan salinan daftar berkas bersama dokumentasi proyek."
            designer "Nah, sekarang kalau ada yang masuk nanti, tinggal diperbarui."
            coder "Sip. Jadi jelas hasil nyatanya."
            # Tambah tepat satu bukti, tidak pernah mengulang poin pada alur normal.
            if not rekap_pengumpulan_ch5:
                $ jumlah_bukti_rahasia += 1
            $ rekap_pengumpulan_ch5 = True

        "Cukup tulis daftar pekerjaan yang masih kurang.":
            coder "Cukup tulis daftar pekerjaan yang masih kurang."
            designer "Oke, biar nggak ribet."
            "Jane menuliskan bahwa konten koleksi asli belum diterima dan perlu ditindaklanjuti."
            coder "Yang penting kita nggak lupa."
            designer "Iya. Nanti gue cek lagi."
            # Tidak menambah bukti rahasia; tidak mengubah bukti lama.

    "Jane kembali membuka prototype galeri."
    designer "Untuk sekarang gue lanjut pakai placeholder dulu."
    coder "Iya. Yang penting tampilannya tetap bisa kita tes."
    designer "Tapi kalau konten asli masuk, masih perlu dicek ulang."
    coder "Pasti."
    "Luuk memperhatikan tanggal pada layar laptopnya."
    "Sudah beberapa minggu sejak pembagian tugas pertama, dan bahan Adrian belum kunjung tersedia."
    "Situasi itu mulai mengganggu pekerjaan yang sebenarnya dapat mereka lanjutkan."
    $ stress_level = min(100, stress_level + 4)
    designer "Yaudah. Kita kerjain yang masih bisa dulu."
    coder "Sip."
    "Keduanya kembali ke pekerjaan masing-masing, tanpa memperpanjang perdebatan tentang Adrian hari itu."
    jump ch5_scene_04


# ============================================================
# SCENE 04 — ANOTHER TEST, ANOTHER LIST | H-33
# MENU 10, 12: dialog biasa.
# MENU 11: pilihan penting (pembayaran simulasi / galeri).
# ============================================================
label ch5_scene_04:
    $ days_left = 33
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk dan Jane kembali bertemu di kontrakan Luuk."
    "Kali ini mereka ingin menguji bagian website yang sudah dibuat, bukan sekadar melihat tampilannya."
    designer "Oke, laptop gue udah siap."
    coder "Sama."
    designer "Kita mulai dari mana?"
    coder "Dari halaman utama, kayak pengunjung biasa."
    designer "Sip."
    "Jane membuka beranda Museum Arunika, lalu berpindah ke halaman galeri dan booking."
    "Navigasi dasar sudah berjalan, tetapi beberapa bagian masih memakai data percobaan."
    designer "Kalau buka di layar laptop, lumayan."
    coder "Coba kecilin jendelanya."
    "Jane mengecilkan ukuran jendela browser."
    designer "Eh."
    coder "Apa?"
    designer "Yang ini jadi mepet banget."
    coder "Oh, iya."
    designer "Padahal di prototype nggak begitu."
    coder "Mungkin ada ukuran yang belum ngikutin layar."
    designer "Oke, masuk daftar perbaikan."
    "Mereka menemukan beberapa masalah tampilan dan alur saat ukuran layar berubah."
    designer "Sepertinya kalau dites beneran, selalu ada masalah baru."
    coder "Karena sebelumnya kita ngetesnya belum selengkap ini."
    designer "Hmm."
    coder "Bagus kita nemuin sekarang."
    designer "Iya, daripada pas presentasi."
    "Luuk menandai beberapa bagian yang perlu diperbaiki."
    $ stress_level = min(100, stress_level + 2)

    # MENU 10 — candaan saat menguji website.
    menu:
        "Bug-nya cuma nunggu kita buka layar lebih kecil.":
            coder "Bug-nya cuma nunggu kita buka layar lebih kecil."
            designer "Berarti kalau layarnya besar, dia sembunyi?"
            coder "Mungkin."
            designer "Jahat juga."
            coder "Dia punya strategi."

        "Website ini ternyata punya banyak kejutan.":
            coder "Website ini ternyata punya banyak kejutan."
            designer "Kejutan ulang tahun?"
            coder "Bukan. Kejutan bikin kerjaan baru."
            designer "Oh, itu nggak menyenangkan."
            coder "Iya."

        "Untung yang ngetes kita, bukan dosen.":
            coder "Untung yang ngetes kita, bukan dosen."
            designer "Jangan ngomong gitu."
            coder "Kenapa?"
            designer "Gue langsung kebayang pas presentasi."
            coder "Oke, maaf."
            designer "Sekarang jadi pengin ngetes semuanya."

    "Jane memeriksa ulang catatan prioritas."
    designer "Kita masih punya dua bagian yang perlu didorong."
    coder "Pembayaran simulasi sama galeri?"
    designer "Iya. Yang satu butuh alur yang jelas, yang satu perlu tampilan yang konsisten."
    coder "Kita fokus satu dulu, nanti sisanya masuk jadwal berikutnya."
    designer "Oke."

    # MENU 11 — PILIHAN PENTING KEDUA.
    # Dua pilihan menghasilkan fitur berbeda, bukan hanya dialog berbeda.
    menu:
        "Lanjutkan ringkasan dan pembayaran simulasi.":
            $ fokus_lanjutan_ch5 = "pembayaran"
            coder "Lanjutkan ringkasan dan pembayaran simulasi."
            designer "Oke. Biar orang tahu urutannya setelah pesan tiket."
            coder "Iya. Tapi tetap simulasi, bukan transaksi asli."
            designer "Siap."

            if prioritas_teknis_lanjutan == "pembayaran":
                coder "Demo pembayaran dari Chapter sebelumnya bisa kita lanjut."
                designer "Yang kemarin masih terpisah itu?"
                coder "Iya. Kita rapihin hubungan tampilannya dengan ringkasan."
            else:
                coder "Kita belum punya demo pembayaran yang rapi. Gue buat layar simulasi dasarnya dulu."
                designer "Oke. Nggak perlu sistem bank beneran, kan?"
                coder "Nggak. Cukup simulasi sesuai kebutuhan tugas."

            # Harga hanya dipastikan ada jika jalur lama atau menu utama Ch5 booking.
            if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking" or fokus_utama_ch5 == "booking":
                designer "Total harga tiketnya bisa kita tampilkan di ringkasan."
                coder "Iya. Tapi kita tetap harus cek apakah nilainya sampai ke halaman berikutnya."
                "Luuk mencoba mengirim nilai total harga dari data uji ke ringkasan pembayaran."
                designer "Nah, sekarang angkanya muncul."
                coder "Iya."
            else:
                designer "Total harga tiket kita masih belum selesai."
                coder "Iya. Jadi untuk sekarang simulasi ini pakai angka contoh."
                designer "Berarti belum nyambung ke perhitungan asli."
                coder "Belum. Itu tetap masuk daftar wajib."

            if fokus_utama_ch5 == "booking":
                designer "Ringkasan dari form yang kemarin bisa dipakai buat tes."
                coder "Iya. Kita coba pindah dari ringkasan ke pembayaran simulasi."
                "Jane menguji perpindahan halaman menggunakan data percobaan."
            else:
                designer "Karena tadi kita fokus admin, alur dari form ke ringkasan belum lengkap."
                coder "Iya. Kita tes bagian simulasi ini sendiri dulu."
                "Jane menguji halaman pembayaran dengan data contoh."

            "Luuk menambahkan halaman konfirmasi simulasi dan memperbaiki beberapa perpindahan tombol."
            designer "Kalau pengunjung kembali ke ringkasan, datanya masih ada?"
            coder "Untuk percobaan ini, iya. Tapi belum semua kondisi ditangani."
            designer "Oke."
            "Alur pembayaran simulasi menjadi lebih jelas, tetapi belum terhubung penuh dengan seluruh sistem booking dan admin."
            designer "Lumayan. Sekarang urutan halamannya lebih masuk akal."
            coder "Iya. Tinggal nanti semua datanya disatukan."
            $ website_progress = min(100, website_progress + 4)
            $ stress_level = max(0, stress_level - 2)

        "Uji dan rapikan galeri di berbagai ukuran layar.":
            $ fokus_lanjutan_ch5 = "galeri"
            coder "Uji dan rapikan galeri di berbagai ukuran layar."
            designer "Oke. Ini bagian gue."
            coder "Gue bantu cek kode responsifnya."
            designer "Sip."

            if not uji_booking_dulu:
                designer "Dulu kita udah mulai bikin kartu galeri responsif."
                coder "Iya. Sekarang kita tes lagi di ukuran lain."
            else:
                designer "Dulu kita lebih banyak fokus booking. Jadi galeri perlu perhatian lebih."
                coder "Iya. Kita rapihin kerangkanya dulu."

            "Jane membandingkan tampilan galeri di layar laptop, tablet, dan ukuran ponsel."
            "Beberapa kartu terlalu rapat dan ada teks contoh yang keluar dari batas."
            designer "Nah, yang ini jelek."
            coder "Iya, teksnya kepanjangan."
            designer "Gue atur lagi jaraknya."
            "Luuk memperbaiki ukuran elemen dan perpindahan kolom pada layout."
            "Jane menguji ulang beberapa variasi panjang teks menggunakan konten contoh."
            designer "Sekarang lebih rapi."
            coder "Iya. Tapi kita belum punya bahan koleksi asli."
            designer "Gue tahu. Jadi ini baru tes tampilan."
            coder "Kalau gambar aslinya masuk, harus dites ulang."
            designer "Siap."
            "Tampilan galeri pada beberapa ukuran layar menjadi lebih konsisten."
            "Namun, seluruh konten koleksi masih menunggu bahan sebenarnya."
            $ website_progress = min(100, website_progress + 3)
            $ stress_level = max(0, stress_level - 2)

    "Menjelang sore, keduanya menutup halaman pengujian."
    designer "Oke, hari ini hasilnya kelihatan."
    coder "Iya."
    designer "Masih ada bug, tapi setidaknya yang tadi udah dibenerin."
    coder "Betul."
    designer "Gue mau istirahat sebentar sebelum lanjut tugas lain."
    coder "Sama."

    # MENU 12 — dialog biasa, tidak mengubah statistik.
    menu:
        "Istirahat dulu, otak gue udah penuh tabel.":
            coder "Istirahat dulu, otak gue udah penuh tabel."
            designer "Tabel yang mana?"
            coder "Semua tabel yang pernah gue lihat hari ini."
            designer "Berarti kalau lihat jadwal kuliah juga pusing?"
            coder "Jangan dites."

        "Gue mau makan sebelum ketemu bug baru.":
            coder "Gue mau makan sebelum ketemu bug baru."
            designer "Setuju."
            coder "Setidaknya makan nggak perlu debugging."
            designer "Kecuali salah pesan."
            coder "Kenapa lo harus bilang itu?"

        "Besok kita lanjut yang belum sempat dikerjain.":
            coder "Besok kita lanjut yang belum sempat dikerjain."
            designer "Oke. Nanti gue lihat kelas dulu."
            coder "Yang tadi nggak kita pilih jangan lupa."
            designer "Udah gue catat."
            coder "Sip."

    "Mereka mengakhiri sesi kerja dan menyimpan semua hasil percobaan."
    "Beberapa bagian website memang membaik, tetapi setiap perbaikan memperlihatkan pekerjaan lain yang belum terselesaikan."
    jump ch5_scene_05


# ============================================================
# SCENE 05 — THIRTY DAYS | H-30
# MENU 13, 14, 15: pilihan dialog biasa.
# Penutup Chapter 5. Belum menentukan ending apa pun.
# ============================================================
label ch5_scene_05:
    $ days_left = 30
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari berlalu."
    "Sore itu Luuk dan Jane kembali duduk di area kampus setelah kelas."
    "Keduanya membawa laptop, tetapi hari ini mereka lebih dulu meninjau hasil pekerjaan selama beberapa minggu terakhir."
    designer "Eh, bentar."
    coder "Apa?"
    designer "Gue mau lihat jadwal kita."
    coder "Oke."
    "Jane membuka tabel rencana kerja yang telah mereka susun."
    designer "Beberapa target minggu ini udah ada yang selesai."
    coder "Lumayan."
    designer "Tapi ada yang harus dipindah ke minggu depan juga."
    coder "Iya."
    designer "Kayaknya tiap minggu bakal ada yang pindah."
    coder "Asal nggak semuanya."
    designer "Bener juga."

    "Mereka mulai meninjau hasil website Museum Arunika."
    if fokus_utama_ch5 == "booking":
        designer "Form booking sekarang udah bisa mengirim data uji ke ringkasan."
        coder "Iya. Tapi penyimpanan permanen sama integrasi admin masih belum lengkap."
        designer "Berarti jangan dicentang selesai penuh dulu."
        coder "Betul. Tulis sedang diuji."
    else:
        designer "Tabel admin sekarang lebih enak dibaca."
        coder "Iya. Tapi data dari form belum masuk otomatis dengan benar."
        designer "Berarti masih harus disambungkan."
        coder "Iya."

    if fokus_lanjutan_ch5 == "pembayaran":
        designer "Simulasi pembayarannya juga udah lebih jelas."
        coder "Iya. Halamannya lebih nyambung, tapi belum bisa dianggap alur final."
        designer "Karena data sama booking masih harus dites lengkap?"
        coder "Nah."
    else:
        designer "Galeri sekarang lebih rapi kalau dibuka di HP."
        coder "Iya. Tapi masih pakai konten contoh."
        designer "Kalau bahan asli masuk, kita harus tes lagi."
        coder "Betul."

    if fokus_pengerjaan_ch4 == "data_pemesanan":
        designer "Setidaknya struktur data lokal dari bulan lalu masih bisa kita lanjut."
        coder "Iya. Tapi belum seluruh sistem database selesai."
    else:
        designer "Form yang kita rapihin bulan lalu juga masih perlu pengujian lagi."
        coder "Iya. Belum semua kasus kita coba."

    if fokus_lanjutan_ch4 == "admin" and fokus_utama_ch5 == "admin":
        designer "Admin udah kita kerjain dua kali, tapi masih ada sambungan data yang tertunda."
        coder "Iya. Tampilan yang rapi belum sama dengan sistem yang selesai."
    elif fokus_lanjutan_ch4 == "uji_booking" and fokus_utama_ch5 == "booking":
        designer "Dua kali kita fokus booking, sekarang hasil uji lokalnya lumayan."
        coder "Iya. Tapi sistemnya belum ujung ke ujung."
    else:
        designer "Kita udah nyicil beberapa bagian yang berbeda."
        coder "Iya. Tinggal bikin semuanya bekerja bersama."

    "Jane meninjau kembali kolom konten koleksi."
    designer "Yang ini masih jadi masalah."
    coder "Adrian?"
    designer "Iya. Belum ada bahan asli masuk."
    coder "Hmm."
    if rekap_pengumpulan_ch5:
        designer "Dari rekap file kemarin juga kelihatan belum ada kirimannya."
        coder "Iya. Kalau nanti ada yang masuk, kita perbarui sesuai tanggalnya."
        designer "Oke."
    elif konfirmasi_target_adrian:
        designer "Padahal waktu itu dia udah setuju sama targetnya."
        coder "Iya. Tapi sampai sekarang hasilnya belum ada."
    else:
        designer "Kita udah ingetin beberapa kali."
        coder "Iya. Kita perlu tindak lanjut, bukan sekadar nunggu."

    "Jane menatap daftar pekerjaan."
    designer "Kalau bahan itu nggak datang, kita bakal kerepotan."
    coder "Iya. Tapi kita juga belum kehabisan pilihan."
    designer "Maksudnya?"
    coder "Kita bisa lanjut bagian yang nggak butuh konten dulu. Sambil tentuin batas kapan harus cari solusi lain."
    designer "Oke. Jadi bukan cuma nunggu tanpa rencana."
    coder "Iya."

    # MENU 13 — respons dialog biasa.
    menu:
        "Kita nggak bisa terus mengandalkan kata 'nanti'.":
            coder "Kita nggak bisa terus mengandalkan kata 'nanti'."
            designer "Setuju."
            coder "Kalau belum selesai, kita butuh tahu kapan dan kenapa."
            designer "Iya. Biar bisa ngatur pekerjaan lain."

        "Kita tetap lanjut bagian kita, tapi jangan pura-pura semuanya aman.":
            coder "Kita tetap lanjut bagian kita, tapi jangan pura-pura semuanya aman."
            designer "Iya."
            coder "Kalau ada masalah, harus ditulis jelas."
            designer "Oke. Jadi nggak ketutup sama halaman yang udah bagus."

        "Gue harap folder koleksi nggak kosong terus.":
            coder "Gue harap folder koleksi nggak kosong terus."
            designer "Sama."
            coder "Placeholder-nya udah kayak penghuni tetap."
            designer "Jangan sampai dia lulus bareng kita."
            coder "Anjir."

    "Jane mengubah beberapa tanda prioritas pada jadwal."
    designer "Oke. Minggu depan fokusnya integrasi dan tes lagi."
    coder "Iya."
    designer "Sama urusan konten."
    coder "Betul."
    "Luuk melihat jam pada ponselnya."
    coder "Eh, sekarang sisa berapa hari, sih?"
    designer "Bentar."
    "Jane membuka kalender."
    designer "Tiga puluh."
    coder "Hah?"
    designer "Tiga puluh hari lagi."
    coder "Oh."
    designer "Udah tinggal sebulan."
    coder "Iya."
    "Luuk terdiam beberapa saat."
    "Ketika mereka memulai proyek ini, sembilan puluh hari terasa seperti waktu yang panjang."
    "Sekarang dua pertiga waktunya telah berlalu."
    "Website memang terus berkembang, tetapi beberapa bagian penting belum menjadi satu sistem yang siap ditunjukkan."
    $ stress_level = min(100, stress_level + 3)

    designer "Lo kenapa diam?"
    coder "Lagi ngitung di kepala."
    designer "Ngitung apa?"
    coder "Pekerjaan kita sama waktu yang tersisa."
    designer "Hmm."
    coder "Kayaknya bulan terakhir bakal lumayan sibuk."
    designer "Iya."
    coder "Tapi masih bisa kita atur kalau mulai lebih disiplin."
    designer "Setuju."
    "Jane menutup kalendernya."
    designer "Berarti kita mulai lebih serius minggu depan."
    coder "Iya."
    designer "Tapi jangan langsung begadang tiap malam."
    coder "Tenang. Gue juga nggak mau."
    designer "Bagus."

    # MENU 14 — dialog biasa, tidak menaikkan/menurunkan statistik.
    menu:
        "Kita bikin target mingguan yang benar-benar bisa dites.":
            coder "Kita bikin target mingguan yang benar-benar bisa dites."
            designer "Contohnya?"
            coder "Bukan cuma 'booking selesai', tapi kondisi apa aja yang harus jalan."
            designer "Oh, jadi ada daftar pengujiannya juga."
            coder "Iya."
            designer "Oke, gue suka."

        "Yang penting jangan sampai semua dikerjain malam terakhir.":
            coder "Yang penting jangan sampai semua dikerjain malam terakhir."
            designer "Itu sih wajib."
            coder "Gue nggak mau ketemu bug baru pas mau tidur."
            designer "Berarti kita tes dari sekarang."
            coder "Nah."

        "Gue masih mau punya waktu buat istirahat.":
            coder "Gue masih mau punya waktu buat istirahat."
            designer "Ya harus."
            coder "Takutnya kalau capek, malah banyak salah."
            designer "Iya. Jadwalnya kita atur supaya masuk akal."
            coder "Sip."

    "Jane menyimpan jadwal dan kembali melihat Luuk."
    designer "Eh."
    coder "Apa?"
    designer "Jadi malam ini masih main Marvel?"
    coder "Lo serius nanya sekarang?"
    designer "Nanya doang."
    coder "Tugas lo udah beres?"
    designer "Belum semua."
    coder "Nah."
    designer "Lah, sekarang lo yang ngingetin?"
    coder "Gantian."
    designer "Wah."
    coder "Apa?"
    designer "Perkembangan karakter bagian kedua."
    coder "Jangan mulai."
    "Jane tertawa."
    designer "Oke, kerjain tugas dulu."
    coder "Iya. Kalau udah selesai, baru lihat lagi."
    designer "Deal."

    # MENU 15 — penutup, pilihan dialog biasa.
    menu:
        "Besok kita periksa bagian yang belum nyambung.":
            coder "Besok kita periksa bagian yang belum nyambung."
            designer "Oke. Gue siapin daftar desain yang harus dicek."
            coder "Gue cek bagian kode dan datanya."
            designer "Sip."

        "Kita jangan lupa minta kepastian bahan dari Adrian.":
            coder "Kita jangan lupa minta kepastian bahan dari Adrian."
            designer "Iya. Tapi besok sekalian kita atur langkah kalau belum ada."
            coder "Setuju."
            designer "Biar nggak muter di pertanyaan yang sama."

    "Mereka menutup laptop setelah menyimpan seluruh catatan pertemuan."
    "Luuk dan Jane masih bercanda seperti biasa, tetapi pembicaraan tentang proyek kini lebih sering berakhir pada daftar pekerjaan yang harus dituntaskan."
    "Mereka belum menyerah dan belum saling menyalahkan."
    "Keduanya tetap bekerja bersama, meskipun mulai memahami bahwa pekerjaan yang tertunda tidak akan hilang hanya karena mereka menunggu."
    "Alur booking masih membutuhkan integrasi yang lebih lengkap."
    "Halaman admin dan database belum sepenuhnya terhubung."
    "Pembayaran simulasi belum siap dianggap sebagai sistem final."
    "Galeri masih menunggu bahan koleksi asli."
    "Dan Adrian belum menyumbangkan hasil yang dapat mereka gunakan."
    "Satu bulan tersisa."
    "Untuk pertama kalinya, waktu yang tersisa terasa lebih singkat daripada daftar pekerjaan mereka."
    "30 DAYS LEFT."

    $ hud_visible = False
    scene black with fade
    centered "{size=50}CHAPTER 05 COMPLETE{/size}\n{size=36}30 DAYS LEFT{/size}\n{size=28}Pieces That Don't Fit.{/size}"

    jump chapter_6
