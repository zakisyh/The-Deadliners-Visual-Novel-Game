# THE DEADLINERS — CHAPTER 02 — WE STILL HAVE TIME
# Generated from the provided final script.

# Persistent flags for Chapter 2
default ch2_coding_first = False
default ch2_booking_priority = "function"
default ch2_progress_notes = False
default secret_evidence_count = 0

label chapter_2:
    $ days_left = 81
    $ hud_visible = True
    scene black with fade
    centered "{size=50}CHAPTER 02{/size}\n{size=42}WE STILL HAVE TIME{/size}\n{size=34}81 DAYS LEFT{/size}"
    # You may add music here if desired, e.g. play music "audio/BGM/....mp3" loop
    jump ch2_scene_01

label ch2_scene_01:
    scene black with dissolve
    $ hud_visible = True
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
    # all branches converge here
    "Jane menggeser laptopnya ke arah Luuk."
    designer "Udah, nih. Gue mau nunjukin wireframe."
    coder "Oh, udah ada?"
    designer "Ada. Nggak semuanya, ya."
    coder "Iya, coba."
    "Pada layar terlihat rancangan sederhana halaman utama Museum Arunika. ..."
    # (Continue with the rest of the narration/dialogue up to the end of Scene 1)
    "Jane menggeser beberapa elemen pada prototype."
    # ... (omitted for brevity, but include all lines from the script up to end of scene)
    $ days_left = 80
    jump ch2_scene_02

label ch2_scene_02:
    scene black with dissolve
    $ hud_visible = True
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
    # chat messages
    $ hud_visible = False
    jump ch2_scene_03

label ch2_scene_03:
    scene black with dissolve
    $ hud_visible = True
    "Siang berikutnya, Jane datang ke kontrakan Luuk membawa laptop dan perlengkapan kuliah."
    "Luuk sedang menyiapkan meja agar mereka bisa membuka kedua laptop berdampingan."
    designer "Woy."
    coder "Masuk."
    designer "Lo udah makan?"
    coder "Udah."
    designer "Tumben."
    coder "Kenapa semua hal normal yang gue lakuin selalu dikomentarin?"
    designer "Karena menarik."
    # ... continue dialogue up to conditional based on menu 4 flag
    if ch2_coding_first:
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
    # converging dialog continues
    "Jane membuka prototype halaman booking."
    designer "Ini tampilan yang gue buat."
    # ... rest of scene up to menu 7
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
            designer "Komprinya dari mana?"
            coder "Tengah-tengah."
            designer "Itu malah lebih jauh."
            coder "Oh, iya."
    # converge
    $ days_left = 79
    jump ch2_scene_04

label ch2_scene_04:
    scene black with dissolve
    $ hud_visible = True
    "Dua hari berikutnya tidak sepenuhnya digunakan untuk mengerjakan Museum Arunika."
    "Luuk disibukkan tugas Pemrograman Berorientasi Objek. Jane juga harus menyelesaikan beberapa pekerjaan kuliah."
    "Pada malam sebelumnya, mereka sempat membahas proyek lewat chat, tetapi tidak banyak yang berubah."
    "Hari ini, Jane kembali membuka grup Museum Arunika."
    designer "Adrian, gambar sama deskripsi koleksinya gimana?"
    designer "Ada yang udah bisa dikirim?"
    "Pesan terkirim."
    "Beberapa waktu kemudian, statusnya berubah menjadi sudah dibaca."
    "Tidak ada balasan."
    # ... continue dialog up to menu 12
    menu:
        "Bikin catatan progres mingguan aja.":
            coder "Bikin catatan progres mingguan aja, gimana?"
            designer "Boleh. Isinya apa?"
            # set flag and secret evidence
            $ ch2_progress_notes = True
            if not ch2_progress_notes:
                $ secret_evidence_count += 1
            designer "Oh, jadi kayak daftar pekerjaan."
            coder "Iya. Sama tanggal update-nya."
            designer "Boleh. Biar nggak lupa yang kemarin udah sampai mana."
            # rest of dialogue
            designer "Bagian lo: struktur website sama sistem tiket."
            coder "Iya."
            designer "Bagian gue: UI/UX sama prototype."
            coder "Betul."
            designer "Adrian: sepuluh gambar referensi sama lima deskripsi koleksi."
            coder "Iya."
        "Rapihin folder proyeknya aja dulu.":
            coder "Mending rapihin folder proyeknya dulu. Biar nggak ketuker."
            designer "Oke. Ini sekarang ada berapa folder?"
            coder "Lumayan."
            designer "Ada yang namanya 'baru' sama 'baru_banget'."
            coder "..."
            designer "Itu apa?"
            coder "Sejarah perkembangan proyek."
            designer "Sejarah yang membingungkan."
    # After menu 12, conditional dialogue based on flag
    if ch2_progress_notes:
        designer "Enak juga kalau ada catatan begini."
        coder "Kenapa?"
        designer "Jadi kelihatan terakhir kita ngerjain apa."
        coder "Iya. Apalagi kalau nanti tugasnya makin banyak."
    else:
        designer "Nah, sekarang lebih gampang nyari file."
        coder "Iya. Tadi aja gue hampir buka versi yang salah."
        designer "Jangan sampai pas presentasi begitu."
        coder "Masih lama juga presentasinya."
    $ days_left = 77
    jump ch2_scene_05

label ch2_scene_05:
    scene black with dissolve
    $ hud_visible = True
    "Beberapa hari berlalu."
    "Tidak setiap hari Luuk dan Jane mengerjakan Museum Arunika bersama."
    "Kadang Jane datang ke kontrakan Luuk untuk mengerjakan desain. Kadang mereka mengerjakan bagian masing-masing dari tempat berbeda."
    "Di luar proyek museum, tugas mata kuliah lain terus berdatangan."
    "Malam ini, Luuk sedang mengerjakan tugas Pemrograman Berorientasi Objek ketika Jane mengirim pesan."
    # chat exchange
    designer "Luuk."
    coder "Apa?"
    designer "Tugas PBO udah?"
    coder "Belum."
    designer "Gue juga."
    coder "Berarti aman."
    designer "Aman dari mana?"
    coder "Setidaknya gue nggak sendirian."
    designer "Anjir."
    coder "..."
    designer "Eh, yang Kecerdasan Buatan gimana?"
    coder "Jangan dibahas."
    designer "Berarti belum?"
    coder "..."
    designer "Oke, paham."
    # ... continue until menu 13
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
    # continue after menu 13 dialogue
    "Luuk menyimpan pekerjaan yang sedang dibuka."
    "Tak lama kemudian, keduanya sudah berada dalam pertandingan Marvel Rivals."
    designer "Kanan!"
    coder "Gue lihat!"
    designer "Ada yang di belakang lo!"
    coder "IYA!"
    # ... more battle narration
    "Setelah beberapa waktu, mereka berhenti bermain."
    designer "Eh, museum kita udah sampai mana, ya?"
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
    "Jane tersenyum."
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
    scene black with fade
    centered "{size=50}CHAPTER 02 COMPLETE{/size}\n{size=34}75 DAYS LEFT{/size}\n{size=42}We still have time.{/size}"
    $ hud_visible = False
    return

                                                                        