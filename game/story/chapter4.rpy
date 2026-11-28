# Ada satu menu tambahan pengelolaan waktu: total 16 menu pada chapter ini.
# REVISION FINAL: sistem Stress, progress, dan ending.
# Keterangan menu lama tetap sebagai riwayat rancangan; kode aktif menentukan efek.
# ============================================================
# THE DEADLINERS — CHAPTER 04: THE LIST KEEPS GROWING
# H-56 -> H-45 | 5 scene | 15 menu pilihan
# ============================================================

# MENU 04 — pekerjaan awal yang dipilih pemain.
# "data_pemesanan" = membuat struktur penyimpanan data pesanan.
# "form_booking" = melengkapi form booking terlebih dahulu.
default fokus_pengerjaan_ch4 = ""

# MENU 09 — bukti rahasia ketiga.
# True = Adrian telah menyetujui pembagian tugas dan target tertulis.
default konfirmasi_target_adrian = False

# MENU 11 — pekerjaan lanjutan yang dipilih pemain.
# "uji_booking" = menguji alur booking.
# "admin" = menyiapkan kerangka halaman admin.
default fokus_lanjutan_ch4 = ""

# Variabel dari chapter sebelumnya tidak perlu dideklarasikan ulang:
# form_tiket_dikerjakan_dulu, prioritas_pengerjaan_website,
# catatan_progres_dibuat, uji_booking_dulu,
# prioritas_teknis_lanjutan, arsip_chat_kelompok_tersimpan,
# jumlah_bukti_rahasia, website_progress, stress_level,
# days_left, hud_visible.


label chapter_4:
    $ hud_visible = False
    $ days_left = 56
    scene black with fade
    centered "{size=50}CHAPTER 04{/size}\n{size=42}THE LIST KEEPS GROWING{/size}\n{size=34}56 DAYS LEFT{/size}"
    jump ch4_scene_01


# ============================================================
# SCENE 01 — THE GROWING LIST | 56 DAYS LEFT
# MENU 01, 02, 03: dialog biasa
# ============================================================
label ch4_scene_01:
    $ days_left = 56
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Empat hari berlalu sejak Luuk dan Jane terakhir memeriksa seluruh pekerjaan Museum Arunika bersama."
    "Selama beberapa hari itu, mereka tetap mengerjakan bagian masing-masing ketika memiliki waktu luang."
    "Namun, tugas kuliah lain juga tidak berhenti datang."
    "Siang ini, Luuk duduk di area kampus setelah kelas."
    "Sebuah laptop terbuka di depannya. Di sebelahnya terdapat botol minuman yang hampir habis."
    "Jane datang sambil membawa tas dan beberapa lembar catatan kuliah."

    designer "Woy."
    coder "Woy."
    designer "Lagi ngapain?"
    coder "Lagi lihat tugas."
    designer "Tugas yang mana?"
    coder "Itu pertanyaan yang sulit."
    designer "Lah."
    coder "Tergantung yang paling dekat deadline-nya."
    designer "Oh, jadi sekarang lo pakai sistem prioritas?"
    coder "Iya."
    designer "Wah, berkembang."
    coder "Kenapa kedengarannya kayak lo nggak percaya?"
    designer "Gue percaya."
    coder "Serius?"
    designer "Sedikit."

    "Jane tertawa lalu duduk di sebelah Luuk."
    designer "Eh, PBO yang kemarin udah beres?"
    coder "Udah gue kumpulin."
    designer "Wih."
    coder "Jangan mulai lagi."
    designer "Apa?"
    coder "Ceramah soal perkembangan karakter gue."
    designer "Padahal gue mau bilang selamat."
    coder "Oh."
    designer "Tapi sekarang nggak jadi."
    coder "Yah."

    # MENU 01 — candaan kuliah (3 opsi, tidak mengubah statistik).
    menu:
        "Gue mulai menjadi mahasiswa teladan.":
            coder "Gue mulai menjadi mahasiswa teladan."
            designer "Mulai kapan?"
            coder "Hari ini."
            designer "Berarti kemarin belum?"
            coder "Jangan bahas masa lalu."
            designer "Masa lalu lo baru kemarin."

        "Tolong hargai perjuangan gue.":
            coder "Tolong hargai perjuangan gue."
            designer "Oke. Selamat sudah mengumpulkan tugas."
            coder "Makasih."
            designer "Semoga tugas berikutnya juga selesai."
            coder "Baru juga senang sebentar."

        "Lo sendiri udah beres semuanya?":
            coder "Lo sendiri udah beres semuanya?"
            designer "Belum."
            coder "Nah."
            designer "Tapi yang deadline besok udah."
            coder "Oke, gue tarik kembali pertanyaan gue."
            designer "Terlambat."

    "Setelah beberapa saat membahas tugas kuliah, Jane mengeluarkan laptopnya."
    designer "Eh, ngomong-ngomong Museum Arunika."
    coder "Kenapa?"
    designer "Kita cek progres lagi, yuk."
    coder "Boleh."
    designer "Soalnya kemarin kita ngerjain bagian yang beda-beda."
    coder "Iya. Gue juga mau lihat desain terbaru lo."
    designer "Oke, bentar."

    "Jane membuka file prototype Museum Arunika."
    "Halaman utama terlihat lebih rapi dibandingkan versi awal yang mereka buat."
    coder "Oh, ini udah bagus."
    designer "Yang mana?"
    coder "Bagian informasi museumnya."
    designer "Oh, iya. Gue kemarin rapihin lagi."
    coder "Yang versi mobile juga?"
    designer "Udah gue sesuaikan sebagian."
    coder "Lumayan."
    designer "Kalau dari lo?"
    coder "Bentar, gue buka."

    "Luuk membuka proyek website di laptopnya."
    "Ia menjalankan versi lokal Museum Arunika."
    "Halaman utama muncul."
    designer "Nah, udah lebih mirip desain gue."
    coder "Iya."
    designer "Tapi masih ada yang beda."
    coder "Gue tahu."
    designer "Gue belum ngomong apa-apa."
    coder "Dari nada lo udah ketahuan."
    designer "Anjir."

    # Pengaruh Chapter 2 dan 3: apakah perhitungan harga sudah selesai?
    if form_tiket_dikerjakan_dulu or uji_booking_dulu:
        coder "Bagian total harga tiket udah bisa dihitung."
        designer "Oh, iya. Yang dulu kita tes itu."
        coder "Iya."
        designer "Terus tinggal yang lain?"
        coder "Iya. Belum semua alurnya selesai."
    else:
        coder "Bagian total harga tiket masih belum selesai."
        designer "Oh, iya. Kita kemarin fokus yang lain."
        coder "Iya. Jadi jangan dianggap form-nya udah bisa dipakai penuh."
        designer "Oke, nanti kita masukin ke daftar lagi."

    # Pengaruh Chapter 3: validasi dasar atau demo pembayaran.
    if prioritas_teknis_lanjutan == "validasi":
        designer "Validasi dasarnya masih aman, kan?"
        coder "Yang kemarin udah kita bikin, iya."
        designer "Berarti nama kosong sama jumlah tiket nol udah ditolak?"
        coder "Iya. Tapi belum semua kondisi kita tes."
        designer "Oke, nanti dites lagi."
    else:
        designer "Kalau halaman pembayaran yang kemarin?"
        coder "Masih ada, tapi itu demo terpisah."
        designer "Belum nyambung ke booking?"
        coder "Belum."
        designer "Oke. Berarti nanti harus disambung."
        coder "Iya."

    # Pengaruh Chapter 3: booking atau galeri.
    if not uji_booking_dulu:
        designer "Setidaknya bagian galeri udah lebih rapi."
        coder "Iya. Versi responsif kartunya juga udah mulai kebentuk."
        designer "Tinggal konten sebenarnya."
        coder "Yang masih kosong itu."
        designer "Iya."
    else:
        designer "Galeri masih pakai banyak placeholder."
        coder "Iya. Kemarin kita lebih fokus ke booking."
        designer "Oke, nanti gue lanjut desain galeri."
        coder "Sip."

    "Jane membuka daftar pekerjaan Museum Arunika."
    if catatan_progres_dibuat:
        designer "Untung kita punya catatan progres."
        coder "Iya. Jadi gampang ngecek."
        designer "Gue update yang desain dulu."
        coder "Oke. Gue cek bagian fungsi."
        "Jane membuka dokumen progres yang sudah mereka buat."
    else:
        designer "Bentar, gue catat yang masih kurang dulu."
        coder "Oke."
        designer "Foldernya udah rapi, tapi daftar pekerjaannya masih kepisah-pisah."
        coder "Iya."
        "Jane membuka catatan sederhana untuk meninjau pekerjaan hari itu."

    designer "Beranda..."
    coder "Udah ada."
    designer "Informasi museum..."
    coder "Sebagian udah."
    designer "Galeri..."
    coder "Strukturnya ada. Kontennya belum."
    designer "Booking..."
    coder "Sebagian fungsi udah, sebagian belum."
    designer "Pembayaran..."
    coder "Masih perlu disambungin."
    designer "Database..."
    coder "Belum siap sepenuhnya."
    designer "Admin..."
    coder "Masih awal."

    "Jane berhenti mengetik."
    designer "..."
    coder "Kenapa?"
    designer "Kok kalau dibaca satu-satu, masih banyak juga, ya?"
    coder "Iya."
    designer "Padahal kalau dilihat tampilannya udah lumayan."
    coder "Tampilan sama fungsi beda."
    designer "Iya, gue mulai ngerti sekarang."
    coder "Website bisa kelihatan bagus tapi tombolnya belum ngapa-ngapain."
    designer "Atau tombolnya jalan tapi tampilannya jelek."
    coder "Nah."
    designer "Berarti kita saling melengkapi."
    coder "Iya."
    designer "Wih, jawaban lo normal."
    coder "Mau gue ganti?"
    designer "Nggak usah."

    # MENU 02 — cara meninjau daftar tugas (2 opsi, dialog saja).
    menu:
        "Kita pecah aja jadi tugas kecil.":
            coder "Kita pecah aja jadi tugas kecil."
            designer "Biar gampang dikerjain?"
            coder "Iya. Kalau satu bagian terlalu besar, nanti susah tahu mulainya dari mana."
            designer "Oke. Gue bagi yang desain juga."
            coder "Sip."

        "Kita cek dulu bagian yang saling nyambung.":
            coder "Kita cek dulu bagian yang saling nyambung."
            designer "Maksudnya booking sama pembayaran?"
            coder "Iya. Kalau satu belum selesai, bagian lain bisa ikut ketahan."
            designer "Oh, masuk akal."
            coder "Jadi kita tahu urutannya."

    designer "Eh, Adrian belum ngirim bahan juga, ya?"
    coder "Belum ada di folder."
    designer "Padahal udah beberapa kali kita tanya."
    coder "Iya."
    designer "Nanti kita ingetin lagi."
    coder "Oke."
    designer "Kalau gambarnya ada, gue bisa lihat galeri versi yang sebenarnya."
    coder "Iya. Sekarang masih banyak konten uji."
    designer "Hmm."

    "Jane kembali melihat daftar pekerjaannya."
    designer "Kayaknya minggu ini kita harus lebih sering buka proyek museum."
    coder "Boleh."
    designer "Nggak harus ketemu terus. Yang penting ada hasil."
    coder "Setuju."
    designer "Besok lo sempat?"
    coder "Sore mungkin."
    designer "Oke, gue kabarin."
    coder "Sip."
    designer "Tapi jangan lupa tugas kuliah yang lain."
    coder "Kenapa setiap pembicaraan produktif harus ditutup dengan ancaman?"
    designer "Itu bukan ancaman."
    coder "Terus?"
    designer "Pengingat ramah."
    coder "Ramahnya di mana?"
    designer "Di niatnya."

    # MENU 03 — pengingat Jane (2 opsi, dialog saja).
    menu:
        "Pengingat lo lebih rajin daripada alarm HP.":
            coder "Pengingat lo lebih rajin daripada alarm HP."
            designer "Bagus, kan?"
            coder "Alarm bisa gue matiin."
            designer "Kalau gue?"
            coder "Masih nyari caranya."
            designer "Nggak bakal ketemu."

        "Oke, besok kita fokus museum.":
            coder "Oke, besok kita fokus museum."
            designer "Siap."
            coder "Tapi tugas yang deadline besok tetap gue kerjain dulu."
            designer "Ya iyalah."
            coder "Gue kira lo bakal protes."
            designer "Gue bukan musuh pendidikan."

    "Mereka menyimpan perubahan terakhir, lalu menutup laptop masing-masing."
    "Hari ini tidak ada fitur besar yang selesai."
    "Namun mereka mulai memahami satu hal: membuat halaman website dan membuat website yang benar-benar dapat digunakan adalah dua pekerjaan yang berbeda."
    "Daftar tugas Museum Arunika tidak berkurang sebanyak yang mereka kira."
    "56 DAYS LEFT."

    # Stress mulai naik sedikit karena Luuk melihat banyaknya sisa pekerjaan.
    # Website Progress tidak naik karena tidak ada fitur yang selesai.
    $ stress_level = min(100, stress_level + 2)
    jump ch4_scene_02

# ============================================================
# SCENE 02 — ONE THING LEADS TO ANOTHER | 53 DAYS LEFT
# MENU 04: pilihan penting (data pemesanan / form booking)
# MENU 05, 06: dialog biasa
# ============================================================
label ch4_scene_02:
    $ days_left = 53
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Jane datang ke kontrakan Luuk."
    "Di meja sudah tersedia dua laptop dan beberapa catatan kecil yang dibuat pada pertemuan sebelumnya."
    "Luuk sedang membuka editor kode ketika Jane masuk."
    designer "Halo."
    coder "Halo."
    designer "Udah mulai?"
    coder "Baru nyalain proyeknya."
    designer "Oke."

    "Jane meletakkan tas dan membuka laptop."
    "Ia memperhatikan beberapa catatan di meja."
    designer "Ini tulisan lo?"
    coder "Iya."
    designer "Yang ini bacaannya apa?"
    coder "Validasi."
    designer "Oh."
    coder "Kenapa?"
    designer "Gue kira 'vaksinasi'."
    coder "..."
    designer "Bercanda."
    coder "Tulisan gue nggak separah itu."
    designer "Ada bagian yang mirip resep dokter."
    coder "Yang penting gue ngerti."
    designer "Nanti kalau lo lupa sendiri gimana?"
    coder "..."
    designer "Nah."
    coder "Oke, nanti gue ketik."

    "Luuk membuka halaman booking Museum Arunika."
    "Jane menyiapkan file prototype untuk membandingkan tampilan dengan kode yang sudah dibuat."
    designer "Oke. Jadi hari ini kita mau fokus apa?"
    coder "Gue tadi lihat alur booking lagi."
    designer "Terus?"
    coder "Beberapa bagian masih belum saling nyambung."
    designer "Yang mana?"
    coder "Misalnya, setelah pengunjung isi data, kita harus nyimpen pesanannya."
    designer "Iya."
    coder "Terus data itu dipakai buat ringkasan dan nantinya ditampilkan di halaman admin."
    designer "Oh, jadi nggak bisa cuma bikin halaman admin sendiri?"
    coder "Bisa bikin tampilannya dulu. Tapi data benerannya harus dari pemesanan."
    designer "Hmm."
    coder "Pembayaran simulasi juga perlu tahu pesanan yang sedang diproses."
    designer "Oh, pantes."
    coder "Kenapa?"
    designer "Gue kira tinggal bikin halamannya, terus disambung pakai tombol."
    coder "Tombolnya bisa nyambung. Datanya belum tentu."
    designer "Oke, gue mulai paham."

    "Jane melihat beberapa halaman website yang terbuka."
    designer "Berarti kalau satu bagian belum selesai, yang lain bisa ikut ketahan."
    coder "Iya."
    designer "Lumayan ribet."
    coder "Namanya juga website."
    designer "Website Museum Arunika."
    coder "Iya."
    designer "Museum yang belum ada pengunjung, tapi udah punya masalah administrasi."
    coder "Akurat."

    # MENU 04 — pilihan penting pertama.
    # "data_pemesanan": struktur penyimpanan data, belum integrasi penuh.
    # "form_booking": form + harga (jika belum) + validasi dasar.
    menu:
        "Kita siapkan penyimpanan data pemesanan dulu.":
            $ fokus_pengerjaan_ch4 = "data_pemesanan"
            coder "Kita siapkan penyimpanan data pemesanan dulu."
            designer "Berarti mulai bagian database?"
            coder "Struktur dasarnya dulu. Kita tentuin data apa aja yang perlu disimpan."
            designer "Misalnya nama pengunjung?"
            coder "Iya. Tanggal kunjungan, jumlah tiket, total harga, sama status pemesanan."
            designer "Oke."

            "Luuk mulai membuat struktur data pemesanan dan mencoba memasukkan beberapa data percobaan."
            "Jane memperhatikan hasilnya."
            designer "Kalau pengunjungnya dua orang berbeda, nanti datanya terpisah, kan?"
            coder "Iya. Setiap pesanan punya identitas sendiri."
            designer "Oh, bagus."

            if form_tiket_dikerjakan_dulu or uji_booking_dulu:
                coder "Perhitungan total harga udah ada. Nanti hasilnya bisa dipakai buat ringkasan pesanan."
                designer "Oke. Jadi nggak perlu dihitung ulang?"
                coder "Nanti tinggal pastiin datanya benar."
            else:
                coder "Total harga masih belum beres. Jadi buat ngetes penyimpanan, gue pakai nilai contoh dulu."
                designer "Oh, berarti ini belum alur asli?"
                coder "Belum. Masih ngetes struktur datanya."
                designer "Oke. Nanti perhitungan harga harus kita beresin juga."

            "Setelah beberapa percobaan, data contoh berhasil tersimpan dalam pengujian lokal yang sederhana."
            designer "Nah, sekarang datanya ada."
            coder "Iya. Tapi jangan dianggap database keseluruhan udah selesai."
            designer "Kenapa?"
            coder "Ini baru dasar. Belum semua halaman tersambung."
            designer "Oke. Setidaknya udah ada tempat buat menyimpan data pesanan."
            coder "Nah."

            # Yang selesai baru struktur dasar, bukan sistem database lengkap.
            $ website_progress = min(100, website_progress + td_progress(4))
            $ stress_level = max(0, stress_level - 1)

        "Kita bereskan bagian form booking yang tertunda dulu.":
            $ fokus_pengerjaan_ch4 = "form_booking"
            coder "Kita bereskan bagian form booking yang tertunda dulu."
            designer "Biar pengunjung bisa isi data dengan benar?"
            coder "Iya. Kalau datanya masih salah, disimpan juga percuma."
            designer "Bener juga."

            if not (form_tiket_dikerjakan_dulu or uji_booking_dulu):
                coder "Gue beresin perhitungan harga dulu."
                designer "Yang jumlah tiket dikali harga?"
                coder "Iya."
                "Luuk kembali membuka kode perhitungan harga."
                "Ia memperbaiki nilai input dan mencoba beberapa jumlah tiket."
                "Percobaan pertama belum sesuai."
                coder "Kok masih salah?"
                designer "Bagian mana?"
                coder "Bentar. Gue cek."
                "Setelah memperbaiki alur perhitungan, total harga akhirnya berubah sesuai jumlah tiket yang dipilih."
                designer "Nah, sekarang jalan."
                coder "Iya."
                designer "Berarti satu masalah selesai?"
                coder "Satu bagian dari satu masalah."
                designer "Waduh."
            else:
                coder "Total harga udah ada. Sekarang kita cek input lainnya."
                designer "Oke. Mau gue tes?"
                coder "Boleh."

            if prioritas_teknis_lanjutan == "validasi":
                designer "Yang nama kosong sama tiket nol udah kita cegah kemarin."
                coder "Iya. Sekarang coba tanggal yang udah lewat."
                "Jane memilih tanggal kunjungan yang seharusnya tidak bisa digunakan."
                "Sistem belum menangani kondisi itu dengan sempurna."
                coder "Nah, ini yang perlu gue tambah."
                designer "Oke."
                "Luuk memperbaiki pemeriksaan tanggal."
                "Setelah diuji ulang, beberapa tanggal tidak valid mulai ditolak dengan benar."
                designer "Lumayan."
                coder "Iya. Tapi masih harus dites lagi."
            else:
                designer "Kemarin kita fokus bikin demo pembayaran. Berarti validasinya masih belum banyak, ya?"
                coder "Iya. Sekarang gue kerjain dasarnya."
                designer "Oke. Gue coba isi data kosong."
                "Luuk mulai menambahkan pemeriksaan terhadap beberapa kolom wajib."
                "Jane mencoba mengosongkan nama pengunjung dan memasukkan jumlah tiket nol."
                "Setelah beberapa perbaikan, form mulai menampilkan peringatan pada input yang tidak sesuai."
                designer "Nah, itu."
                coder "Lumayan. Tapi belum semua kondisi gue periksa."

            "Form booking menjadi lebih lengkap."
            "Namun, penyimpanan data pemesanan dan hubungan dengan halaman lain masih membutuhkan pekerjaan lanjutan."
            designer "Berarti yang ini udah lebih aman dipakai."
            coder "Lebih aman buat tes. Belum buat dipakai beneran."
            designer "Iya, gue tahu."

            $ website_progress = min(100, website_progress + td_progress(3))
            $ stress_level = max(0, stress_level - 1)

    "Beberapa saat kemudian, Jane mencoba mengisi data pengunjung percobaan."
    designer "Gue pakai nama siapa kali ini?"
    coder "Bebas."
    designer "Jangan bebas."
    coder "Kenapa?"
    designer "Nanti gue malah mikir."
    coder "Nama random aja."
    designer "Oke. Tapi yang lucu."

    # MENU 05 — candaan data tes (3 opsi, dialog saja).
    menu:
        "Pengunjung Nomor Satu.":
            coder "Tulis Pengunjung Nomor Satu."
            designer "Kreatif banget."
            coder "Namanya juga data tes."
            designer "Kalau pengunjung kedua?"
            coder "Pengunjung Nomor Dua."
            designer "Wah, konsepnya konsisten."

        "Direktur Museum Arunika.":
            coder "Tulis Direktur Museum Arunika."
            designer "Emang ada direkturnya?"
            coder "Sekarang ada."
            designer "Siapa?"
            coder "Yang lagi beli tiket."
            designer "Direkturnya beli tiket ke museumnya sendiri?"
            coder "Mendukung usaha lokal."

        "Nama lo lagi aja.":
            coder "Nama lo lagi aja."
            designer "Gue terus?"
            coder "Pelanggan setia."
            designer "Tapi museumnya belum buka."
            coder "Setia sejak sebelum dibuka."
            designer "Oke, itu lumayan lucu."

    "Jane mencoba beberapa tindakan pada halaman website."
    designer "Eh, kalau pengunjung salah masukin nomor telepon gimana?"
    coder "Harus diperiksa juga."
    designer "Kalau tanggal yang dipilih penuh?"
    coder "Nanti perlu batas kapasitas."
    designer "Oh."
    coder "Kenapa?"
    designer "Baru inget satu lagi."
    coder "Apa?"
    designer "Kalau pengunjung mau ganti tanggal setelah memilih tiket?"
    coder "..."
    designer "Kenapa?"
    coder "Daftar pekerjaan kita bertambah."
    designer "Oh."
    coder "Iya."
    designer "Maaf."
    coder "Nggak apa-apa. Memang harus dipikirin."
    designer "Tapi nggak semuanya sekarang, kan?"
    coder "Iya. Kita tentuin mana yang wajib dulu."
    designer "Sip."

    # MENU 06 — daftar pekerjaan (2 opsi, dialog saja).
    menu:
        "Website ini makin lama makin banyak maunya.":
            coder "Website ini makin lama makin banyak maunya."
            designer "Websitenya atau kita?"
            coder "Dua-duanya."
            designer "Setidaknya kita kompak."
            coder "Kompak nambah pekerjaan."

        "Tulis dulu, jangan langsung bikin semuanya.":
            coder "Tulis dulu, jangan langsung bikin semuanya."
            designer "Oke. Biar nggak pindah-pindah fokus."
            coder "Iya. Yang wajib harus selesai dulu."
            designer "Sip. Gue catat sebagai pekerjaan nanti."

    "Sore itu, mereka menyimpan hasil pekerjaan."
    "Salah satu bagian website menjadi lebih baik, tetapi belum semua sistem tersambung."
    "Jane memeriksa daftar yang mereka buat."
    designer "Lumayan."
    coder "Iya."
    designer "Tapi yang belum selesai juga masih banyak."
    coder "Iya. Pelan-pelan."
    designer "Minggu ini kita lanjut lagi, ya."
    coder "Siap."
    "Luuk menutup editor setelah memastikan pekerjaan terakhirnya tersimpan."
    "Membuat sebuah fitur ternyata tidak cukup."
    "Mereka juga perlu membuatnya bekerja bersama fitur lainnya."
    "53 DAYS LEFT."
    jump ch4_scene_03

# ============================================================
# SCENE 03 — STILL WAITING | 50 DAYS LEFT
# MENU 07, 08: dialog biasa
# MENU 09: bukti rahasia ketiga (konfirmasi target Adrian)
# ============================================================
label ch4_scene_03:
    $ days_left = 50
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari berlalu."
    "Luuk dan Jane kembali disibukkan dengan kegiatan kuliah."
    "Pada siang hari, keduanya bertemu di koridor kampus setelah kelas."
    "Jane sedang membuka ponselnya."
    coder "Woy."
    designer "Woy."
    coder "Lagi lihat apa?"
    designer "Grup museum."
    coder "Kenapa?"
    designer "Belum ada file baru."
    coder "Dari Adrian?"
    designer "Iya."
    coder "Hmm."
    designer "Padahal sekarang udah lewat cukup lama dari pembagian tugas awal."
    coder "Iya."
    designer "Gue kira setidaknya beberapa gambar udah ketemu."
    coder "Sama."

    "Jane membuka folder yang disiapkan untuk bahan koleksi Museum Arunika."
    "Di dalamnya hanya terdapat aset sementara yang digunakan untuk menguji desain."
    designer "Lihat."
    coder "Masih gambar uji?"
    designer "Iya."
    coder "Yang asli belum ada?"
    designer "Belum."
    coder "Hmm."
    designer "Sebenernya gue bisa lanjut desain, tapi gue pengin lihat hasil kalau kontennya udah beneran masuk."
    coder "Iya. Ukuran gambar sama panjang teks juga bisa beda-beda nanti."
    designer "Nah, itu."
    coder "Kalau deskripsinya kepanjangan, layout-nya juga harus disesuaikan."
    designer "Makanya gue nunggu."

    "Jane kembali membuka grup percakapan."
    designer "Gue tanya lagi, ya?"
    coder "Boleh."
    "Jane (grup): Adrian, ada update bahan museum?"
    "Jane (grup): Kalau gambarnya belum lengkap, yang udah ada boleh dikirim dulu."
    "Pesan terkirim."
    "Beberapa saat kemudian, ponsel Jane bergetar."
    "Adrian (grup): Belum. Lagi cari."
    designer "..."
    coder "Gimana?"
    designer "Katanya masih cari."
    coder "Oh."
    designer "Gue bingung."
    coder "Kenapa?"
    designer "Udah beberapa minggu, tapi belum ada satu file pun."
    coder "Iya."
    designer "Kalau ada kendala, kan bisa bilang."
    coder "Bener."
    designer "Tapi dia juga nggak jelasin apa-apa."
    coder "Hmm."

    "Jane menghela napas."
    "Ia tidak terlihat marah besar, tetapi mulai merasa pekerjaannya terhambat."
    designer "Apa kita yang salah jelasin tugasnya?"
    coder "Menurut gue udah jelas."
    designer "Sepuluh gambar sama lima deskripsi."
    coder "Iya."
    designer "Bahan referensi juga boleh."
    coder "Iya. Nggak harus sempurna dulu."
    designer "Terus kenapa belum ada juga?"
    coder "Gue nggak tahu."

    # Keterlambatan Adrian kali ini mulai menghambat pekerjaan Jane.
    $ stress_level = min(100, stress_level + 4)

    # MENU 07 — tanggapan Luuk tentang Adrian (3 opsi, dialog saja).
    menu:
        "Mungkin kita perlu jelasin targetnya lagi.":
            $ poin_good += 2
            coder "Mungkin kita perlu jelasin targetnya lagi."
            designer "Iya, sih."
            coder "Bukan cuma nanya udah selesai atau belum."
            designer "Jadi kita kasih target yang lebih jelas?"
            coder "Iya. Biar nggak ada yang bingung."

        "Kita kerjain bagian lain dulu.":
            $ poin_true += 2
            coder "Kita kerjain bagian lain dulu."
            designer "Sambil nunggu?"
            coder "Iya. Yang nggak tergantung bahan museum."
            designer "Oke. Tapi galeri tetap harus diselesaikan."
            coder "Iya, gue tahu."

        "Gue juga mulai bingung mau nanya apa lagi.":
            coder "Gue juga mulai bingung mau nanya apa lagi."
            designer "Kan udah berkali-kali."
            coder "Iya. Jawabannya juga mirip."
            designer "Belum. Nanti. Lagi cari."
            coder "Nah."
            designer "Kayak paket jawaban."
            coder "Paket hemat."
            designer "Anjir."

    "Jane membuka kembali desain halaman koleksi."
    designer "Gue sebenarnya udah siapin tempat buat sepuluh gambar."
    coder "Oke."
    designer "Kalau nantinya cuma lima yang ada, berarti layout-nya harus disesuaikan."
    coder "Bisa."
    designer "Kalau nggak ada sama sekali?"
    coder "..."
    designer "Kenapa diam?"
    coder "Ya kita cari solusi lain."
    designer "Berarti kita sendiri yang cari?"
    coder "Kalau benar-benar nggak ada, mungkin."
    designer "Tapi itu kan tugas dia."
    coder "Iya."
    designer "Hmm."

    "Luuk memperhatikan layar laptop Jane."
    "Ia mulai memahami bahwa keterlambatan Adrian tidak hanya membuat satu folder kosong."
    "Keterlambatan itu juga membuat pekerjaan lain sulit dipastikan hasil akhirnya."
    coder "Untuk sekarang, placeholder-nya jangan dihapus dulu."
    designer "Iya."
    coder "Setidaknya kita masih bisa ngetes tampilan galeri."
    designer "Oke."

    "Jane kembali menatap layar."
    designer "Eh, menurut lo kartu galeri ini lebih bagus tiga kolom atau dua?"
    coder "Tergantung ukuran layar."
    designer "Kalau laptop?"
    coder "Tiga masih oke."
    designer "Kalau tablet?"
    coder "Mungkin dua."
    designer "Kalau HP?"
    coder "Satu."
    designer "Wah."
    coder "Kenapa?"
    designer "Jawaban lo sekarang udah kayak desainer."
    coder "Gue sering denger lo ngomong."
    designer "Berarti ilmu gue terserap."
    coder "Sedikit."
    designer "Sedikit banget?"

    # MENU 08 — Luuk belajar desain dari Jane (2 opsi, dialog saja).
    menu:
        "Gue belajar karena sering dikoreksi.":
            coder "Gue belajar karena sering dikoreksi."
            designer "Bagus, kan?"
            coder "Iya. Walaupun kadang koreksinya cuma soal jarak dua pixel."
            designer "Masih lo inget?"
            coder "Sulit dilupakan."

        "Gue masih menyerahkan keputusan desain ke lo.":
            coder "Gue masih menyerahkan keputusan desain ke lo."
            designer "Bagus."
            coder "Gue cuma kasih tahu batasan dari kode yang gue buat."
            designer "Nah, itu memang yang gue butuh."
            coder "Berarti kita cocok buat kerja kelompok."
            designer "Selama lo nggak ngilang."
            coder "Gue masih di sini."

    "Beberapa menit kemudian, pembicaraan mereka kembali ke pekerjaan kelompok."
    "Jane membuka pesan pembagian tugas awal."

    if catatan_progres_dibuat:
        designer "Catatan progres kita masih ada."
        coder "Iya."
        designer "Bagian Adrian masih belum ada file masuk."
        coder "Berarti statusnya jangan diubah dulu."
        designer "Iya."
    else:
        designer "Kita punya daftar tugas awal, tapi belum pernah bikin rekap rutin."
        coder "Iya."
        designer "Setidaknya pembagiannya masih ada di chat."
        coder "Bener."

    if arsip_chat_kelompok_tersimpan:
        designer "Arsip percakapan kemarin juga udah gue simpan."
        coder "Sip."
        designer "Jadi kalau mau lihat yang awal, nggak harus scroll grup jauh-jauh."
        coder "Iya."
    else:
        designer "Pengingat yang kemarin gue buat masih ada di HP."
        coder "Bagus."
        designer "Tapi sekarang kita perlu tentuin target berikutnya juga."
        coder "Iya."

    designer "Menurut lo, kita harus ngapain supaya bahan museum ini bisa jelas kapan ada?"
    coder "Hmm."
    designer "Kalau cuma nanya terus, jawabannya belum tentu beda."
    coder "Bener juga."

    # MENU 09 — BUKTI RAHASIA KETIGA.
    # Jika Adriannya mengonfirmasi tugas dan tenggat secara tertulis,
    # poin bukti bertambah tepat satu kali dalam alur normal.
    # Jangan tampilkan jumlah_bukti_rahasia kepada pemain.
    menu:
        "Kirim rangkuman tugas dan target tanggal, lalu minta konfirmasi.":
            coder "Kita kirim rangkuman tugas sama target tanggal yang jelas aja."
            designer "Buat semuanya?"
            coder "Iya. Biar kita punya patokan yang sama."
            designer "Oke. Target buat bahan koleksinya kapan?"
            coder "Coba minta dua hari lagi. Kalau belum bisa, dia harus bilang kendalanya apa."
            designer "Oke, gue tulis."

            "Jane mengetik sebuah pesan di grup Museum Arunika."
            "Jane (grup): Aku rangkum tugas kelompok lagi, ya."
            "Jane (grup): Luuk: coding dan sistem website. Jane: UI/UX dan prototype. Adrian: 10 gambar referensi dan 5 deskripsi koleksi."
            "Jane (grup): Buat bahan koleksi, targetnya dua hari lagi dulu."
            "Jane (grup): Kalau ada kendala atau belum bisa, kabarin sebelum targetnya, ya. Biar kita bisa atur bagian galeri."
            "Jane (grup): Semuanya oke dengan pembagian dan target ini?"

            "Luuk membaca kembali pesan tersebut."
            coder "Udah jelas."
            designer "Oke."
            "Beberapa saat kemudian, Adrian mengirim balasan."
            "Adrian (grup): Iya, siap."
            designer "Nah, dibales."
            coder "Oke. Berarti dia udah tahu targetnya."
            designer "Iya."
            "Jane menyimpan konfirmasi tersebut bersama catatan pekerjaan kelompok."
            # Bukti ke-3: konfirmasi tugas dan target benar-benar diterima.
            # Tambah poin hanya jika bukti ini belum pernah dicatat.
            if not konfirmasi_target_adrian:
                $ jumlah_bukti_rahasia += 1
            $ konfirmasi_target_adrian = True
            coder "Nanti kita lihat pas targetnya tiba."
            designer "Oke."
            "Sampai saat itu, belum ada bahan koleksi yang dikirim Adrian."

        "Ingatkan seperti biasa saja di grup.":
            # Tidak mendapat poin rahasia di jalur pengingat biasa.
            coder "Ingatkan seperti biasa aja dulu."
            designer "Oke."
            coder "Bilang kita masih butuh bahannya."
            designer "Sip."
            "Jane mengetik pesan singkat."
            "Jane (grup): Adrian, jangan lupa bahan museumnya, ya. Kita masih butuh buat galeri."
            "Setelah beberapa saat, Adrian membalas."
            "Adrian (grup): Iya, nanti."
            designer "Oke, udah diingetin."
            coder "Iya."
            designer "Semoga segera ada."
            coder "Semoga."

    "Luuk dan Jane kembali mengerjakan bagian website yang bisa mereka kerjakan."
    "Tidak ada bahan baru dari Adrian hari itu."
    "Namun, sekarang keduanya mulai lebih memahami bahwa pekerjaan anggota ketiga mereka bisa menjadi hambatan jika terus dibiarkan."
    designer "Yaudah. Kita lanjut yang lain dulu."
    coder "Iya."
    designer "Galeri tetap gue siapkan."
    coder "Sip."
    "Jane menutup grup percakapan."
    "Luuk memperhatikan daftar tugas di laptopnya."
    "Lima puluh hari masih tersisa."
    "Angka tersebut masih cukup besar untuk membuat mereka merasa tenang."
    "Tetapi pekerjaan yang belum selesai juga tidak sedikit."
    "50 DAYS LEFT."
    jump ch4_scene_04

# ============================================================
# SCENE 04 — DOES IT ACTUALLY WORK? | 47 DAYS LEFT
# MENU 10: dialog biasa
# MENU 11: pilihan penting kedua (uji booking / admin)
# MENU 12: dialog biasa
# ============================================================
label ch4_scene_04:
    $ days_left = 47
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk kembali membuka proyek Museum Arunika dari kontrakannya."
    "Hari itu Jane datang setelah menyelesaikan kelas."
    "Ia membawa laptop dan beberapa catatan desain."
    designer "Halo."
    coder "Halo."
    designer "Udah mulai?"
    coder "Baru mau ngetes website."
    designer "Oke. Gue ikut."

    "Jane duduk dan membuka laptop."
    "Sebelum mulai bekerja, ia memeriksa grup kelompok."

    # Jika pada H-50 Adrian menerima target dua hari, maka pada H-47
    # target tersebut sudah lewat satu hari tanpa pengiriman bahan.
    if konfirmasi_target_adrian:
        designer "Eh, Luuk."
        coder "Kenapa?"
        designer "Target bahan dari Adrian udah lewat kemarin."
        coder "Oh, iya."
        designer "Tapi belum ada file masuk."
        coder "Belum?"
        designer "Belum."
        coder "Hmm."
        designer "Padahal waktu itu dia udah bilang siap."
        coder "Iya."
        designer "Nanti kita tanya lagi. Sekarang gue mau lanjut yang bisa dikerjain."
        coder "Oke."
    else:
        designer "Adrian belum kirim bahan juga."
        coder "Belum?"
        designer "Belum ada di folder."
        coder "Oh."
        designer "Kemarin udah gue ingetin."
        coder "Iya."
        designer "Nanti gue coba tanya lagi. Sekarang kita lanjut dulu."
        coder "Oke."

    "Luuk menjalankan website Museum Arunika."
    "Halaman utama muncul di layar."
    "Jane menggeser kursinya agar bisa melihat lebih jelas."
    designer "Oke. Coba buka booking."
    coder "Bentar."
    "Luuk menekan tombol pemesanan tiket."
    "Halaman booking berhasil ditampilkan."
    designer "Nah. Dari beranda udah bisa pindah."
    coder "Iya."
    designer "Terus setelah isi form?"
    coder "Itu yang masih harus diberesin sampai lengkap."
    designer "Oh."
    coder "Kita udah bikin beberapa bagian, tapi belum semuanya nyambung."
    designer "Berarti bentuknya udah ada, alurnya belum tentu selesai."
    coder "Betul."
    "Jane memperhatikan layar laptop."
    designer "Kalau dilihat sekilas, orang mungkin kira udah bisa dipakai."
    coder "Iya."
    designer "Padahal belum."
    coder "Belum."
    designer "Hmm."
    coder "Kenapa?"
    designer "Agak menipu juga, ya."
    coder "Namanya masih tahap pengembangan."
    designer "Iya, sih."
    coder "Jangan dipromosikan dulu."
    designer "Selamat datang di Museum Arunika."
    coder "Jangan."
    designer "Silakan pesan tiket."
    coder "Jangan dulu."
    designer "Fitur sedang dalam pengerjaan."
    coder "Nah, itu baru jujur."

    # Melihat alur belum terhubung memberi tekanan, terlepas dari jalur.
    $ stress_level = min(100, stress_level + 2)

    # MENU 10 — candaan website tahap pengembangan (3 opsi).
    menu:
        "Museum belum buka, tapi bug-nya udah banyak.":
            coder "Museum belum buka, tapi bug-nya udah banyak."
            designer "Pengunjungnya siapa?"
            coder "Gue sama lo."
            designer "Berarti pengunjung pertama malah nemuin masalah."
            coder "Pelayanan istimewa."

        "Kita butuh papan 'sedang dibangun'.":
            coder "Kita butuh papan 'sedang dibangun'."
            designer "Di halaman utama?"
            coder "Iya. Besar banget."
            designer "Nanti pengunjung nggak lihat museumnya."
            coder "Setidaknya mereka tahu kondisinya."
            designer "Jangan dulu deh."

        "Makanya semua tombol harus dites.":
            coder "Makanya semua tombol harus dites."
            designer "Iya. Nggak cukup kelihatan bagus."
            coder "Betul."
            designer "Gue bantu bagian interaksinya."
            coder "Sip. Lo coba pakai kayak pengunjung biasa."

    "Jane mencoba beberapa halaman website."
    "Ia berpindah dari beranda ke halaman koleksi, kemudian kembali menuju halaman pemesanan."
    designer "Yang navigasi ini udah enak."
    coder "Iya."
    designer "Tapi bagian ini masih perlu diperbaiki."
    coder "Yang mana?"
    designer "Kalau balik dari booking, tampilannya sedikit berubah."
    coder "Oh, iya. Gue lihat."
    designer "Bisa dibenerin?"
    coder "Bisa. Gue catat dulu."
    "Jane mencoba beberapa tombol lainnya."
    "Sebagian sudah menuju halaman yang benar."
    "Sebagian masih menampilkan halaman percobaan."
    designer "Oke, ternyata masih ada beberapa."
    coder "Iya."
    designer "Kita mau ngapain sekarang?"
    coder "Ada dua pilihan yang masuk akal."
    designer "Apa aja?"
    coder "Kita uji bagian yang udah ada, atau mulai siapkan halaman admin."
    designer "Hmm."
    coder "Dua-duanya perlu."
    designer "Berarti pilih salah satu dulu."

    # MENU 11 — pilihan penting kedua.
    # "uji_booking": memperbaiki navigasi dan mendata bug tersisa.
    # "admin": membangun kerangka tabel; data riil belum terhubung.
    menu:
        "Uji dan perbaiki alur pemesanan yang sudah ada.":
            $ fokus_lanjutan_ch4 = "uji_booking"
            coder "Kita uji dan perbaiki alur pemesanan yang udah ada dulu."
            designer "Oke. Gue jadi pengunjung lagi."
            coder "Siap."
            "Jane membuka halaman booking."
            "Ia mencoba memilih tanggal, mengisi data pengunjung, dan menentukan jumlah tiket."

            if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking":
                designer "Total harga sekarang udah muncul."
                coder "Iya."
                designer "Berarti yang itu aman?"
                coder "Perhitungan dasarnya jalan. Tapi kita tetap harus cek input lain."
            else:
                designer "Yang total harga ini masih belum jalan."
                coder "Iya. Itu masih jadi hambatan."
                designer "Berarti nggak bisa tes seluruh pemesanannya dulu?"
                coder "Belum sampai akhir. Tapi bagian lain tetap bisa kita periksa."

            "Jane mencoba mengosongkan beberapa kolom."
            if prioritas_teknis_lanjutan == "validasi" or fokus_pengerjaan_ch4 == "form_booking":
                designer "Beberapa input sekarang udah ditolak."
                coder "Iya. Validasi dasarnya mulai ada."
                designer "Tapi masih ada kondisi yang perlu dites lebih jauh."
                coder "Betul."
            else:
                designer "Yang input kosong ini masih bisa lewat."
                coder "Iya. Itu berarti masih perlu validasi."
                designer "Oke, gue tulis."

            "Mereka melanjutkan pengujian pada bagian yang memang sudah tersedia."
            "Jane mencoba berpindah halaman dan mengisi beberapa kombinasi data."
            "Luuk memperbaiki sejumlah kesalahan kecil yang mereka temukan."
            designer "Nah, sekarang tombol baliknya udah nggak aneh."
            coder "Iya. Tadi ada bagian yang salah."
            designer "Terus yang ini?"
            coder "Masih belum selesai."
            designer "Oke."
            "Setelah beberapa pengujian, navigasi dan sebagian interaksi menjadi lebih konsisten."
            "Namun, alur pemesanan belum sepenuhnya terhubung dengan penyimpanan data dan pembayaran simulasi."
            designer "Lumayan."
            coder "Iya. Setidaknya kita tahu masalahnya ada di mana."
            designer "Berarti nanti nggak nebak-nebak lagi."
            coder "Betul."

            $ website_progress = min(100, website_progress + td_progress(3))
            $ stress_level = max(0, stress_level - 2)

        "Siapkan kerangka halaman admin dulu.":
            $ fokus_lanjutan_ch4 = "admin"
            coder "Kita siapkan kerangka halaman admin dulu."
            designer "Oke. Gue bikin desain tabelnya."
            coder "Sip. Nanti isinya daftar pemesanan."
            designer "Kolomnya apa aja?"
            coder "Nomor pesanan, nama pengunjung, tanggal kunjungan, jumlah tiket, dan status pesanan."
            designer "Total harga juga?"
            coder "Iya. Tapi buat sekarang pakai data contoh dulu kalau diperlukan."
            designer "Oke."
            "Jane mulai membuat tampilan admin sederhana."
            "Ia menempatkan daftar pemesanan dalam tabel yang mudah dibaca."
            coder "Jangan terlalu banyak informasi dalam satu baris."
            designer "Iya. Nanti sempit."
            coder "Yang penting kebaca dulu."
            designer "Sip."

            if fokus_pengerjaan_ch4 == "data_pemesanan":
                coder "Kita udah punya struktur data buat percobaan kemarin."
                designer "Bisa dipakai buat tabel ini?"
                coder "Bisa buat ngetes sebagian tampilannya."
                designer "Oke."
                "Luuk menampilkan beberapa data uji menggunakan struktur yang sudah disiapkan."
            else:
                coder "Karena penyimpanan pesanan belum kita kerjain, gue pakai data contoh dulu."
                designer "Oke. Yang penting kita lihat tampilannya."
                coder "Iya."
                "Luuk menambahkan data uji untuk memeriksa susunan halaman admin."

            designer "Nah, kalau ada banyak pesanan, nanti tabelnya panjang banget."
            coder "Iya. Kita bisa tambah pencarian atau pembagian halaman nanti."
            designer "Jangan semua sekarang."
            coder "Tumben lo yang bilang."
            designer "Gue belajar."
            coder "Bagus."
            "Kerangka halaman admin mulai terbentuk."
            "Tabel dan beberapa elemen dasarnya sudah dapat ditampilkan."
            "Namun, halaman ini masih menggunakan data percobaan dan belum menjadi sistem administrasi yang terhubung penuh."
            designer "Lumayan. Setidaknya halaman admin udah ada bentuknya."
            coder "Iya."
            designer "Tinggal nanti disambung sama booking."
            coder "Nah, itu bagian berikutnya."

            $ website_progress = min(100, website_progress + td_progress(3))
            $ stress_level = max(0, stress_level - 2)

    "Menjelang sore, keduanya berhenti bekerja."
    "Jane meregangkan tangan dan bersandar."
    designer "Capek juga."
    coder "Lumayan."
    designer "Padahal tadi cuma mau ngerjain satu bagian."
    coder "Satu bagian bisa punya banyak masalah."
    designer "Iya, sekarang gue percaya."
    coder "Terus besok mau lanjut?"
    designer "Lihat jadwal kuliah dulu."
    coder "Sama."
    designer "Makin banyak tugas, ya."
    coder "Iya."
    designer "Kayaknya semester ini nggak ngasih waktu kosong."
    coder "Ada."
    designer "Kapan?"
    coder "Pas tidur."
    designer "Anjir."
    coder "Itu juga kalau nggak kepikiran tugas."
    designer "Nah, berarti nggak kosong."

    # MENU 12 — tugas dan waktu luang (3 opsi, dialog saja).
    menu:
        "Gue pengin libur dari semua deadline.":
            coder "Gue pengin libur dari semua deadline."
            designer "Liburnya berapa lama?"
            coder "Seminggu."
            designer "Habis itu tugasnya tetap ada."
            coder "Jangan rusak mimpi gue."

        "Kita butuh fitur menyelesaikan tugas otomatis.":
            coder "Kita butuh fitur menyelesaikan tugas otomatis."
            designer "Bisa lo coding?"
            coder "Kalau bisa, gue udah pakai."
            designer "Berarti belum ditemukan teknologinya."
            coder "Sayangnya."

        "Yang penting hari ini ada hasil.":
            coder "Yang penting hari ini ada hasil."
            designer "Iya."
            coder "Walaupun belum banyak."
            designer "Tapi ada yang selesai dan ada yang jelas harus dikerjain berikutnya."
            coder "Nah, itu."
            designer "Lumayan."

    "Luuk dan Jane menyimpan pekerjaan masing-masing."
    "Website Museum Arunika semakin memiliki bentuk."
    "Namun, setiap kali mereka melakukan pengujian, mereka menemukan bagian yang masih harus diperbaiki."
    "Beberapa halaman sudah terlihat rapi."
    "Beberapa fungsi sudah mulai berjalan."
    "Tetapi belum semuanya saling terhubung."
    "Dan bahan koleksi yang menjadi tanggung jawab Adrian masih belum tersedia."
    # MENU TAMBAHAN — pengelolaan waktu dan Stress (berpengaruh).
    "Masih ada sedikit waktu sebelum sesi berakhir."
    designer "Kita lanjut sedikit atau istirahat dulu?"
    menu:
        "Makan es krim dulu, yuk.":
            coder "Makan es krim dulu, yuk."
            "Luuk dan Jane membeli es krim di warung dekat kontrakan, lalu mengobrol tentang hal lain."
            $ stress_level = max(0, stress_level - 4)

        "Kita periksa tautan beranda, galeri, dan booking." if stress_level < 65:
            coder "Kita periksa tautan beranda, galeri, dan booking."
            "Keduanya memperbaiki tujuan dua tautan dan mengulang navigasi dari beranda."
            $ website_progress = min(100, website_progress + td_progress(3))
            $ risiko_demo = max(0, risiko_demo - 1)
            $ stress_level = max(0, stress_level - 2)

        "Jane, bantu gue tes satu bagian kecil dulu." if stress_level >= 65:
            coder "Jane, bantu gue tes satu bagian kecil dulu."
            designer "Oke. Satu bagian aja, habis itu berhenti."
            $ stress_level = max(0, stress_level - 5)
            "Jane membantu mengulang satu tes dan Luuk membetulkan masalah kecil yang mereka temukan."
            $ website_progress = min(100, website_progress + td_progress(2))
            $ risiko_demo = max(0, risiko_demo - 1)

        "Kita rapikan beberapa tautan tanpa tes ulang.":
            coder "Kita rapikan beberapa tautan tanpa tes ulang."
            designer "Tapi kalau nggak dites ulang, masih ada risikonya."
            "Luuk mengubah beberapa tujuan tautan sekaligus. Mereka menyimpan perubahan tanpa mengulang seluruh navigasi."
            $ website_progress = min(100, website_progress + td_progress(4))
            $ poin_bad += 2
            $ risiko_demo += 2
            $ stress_level = min(100, stress_level + 6)

    "47 DAYS LEFT."
    jump ch4_scene_05

# ============================================================
# SCENE 05 — HALFWAY THERE? | 45 DAYS LEFT
# Rekap menghormati jalur Chapter 2, 3, dan 4.
# ============================================================
label ch4_scene_05:
    $ days_left = 45
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Dua hari kemudian, Luuk dan Jane bertemu di area duduk kampus setelah menyelesaikan kelas."
    "Sore itu suasana kampus mulai lebih sepi."
    "Beberapa mahasiswa masih duduk mengerjakan tugas."
    "Luuk baru saja menutup laptopnya ketika Jane datang membawa minuman."

    designer "Luuk."
    coder "Hm?"
    designer "Udah selesai?"
    coder "Tugas yang tadi? Udah."
    designer "Wih."
    coder "Jangan komentar lagi."
    designer "Gue belum ngomong apa-apa."
    coder "Udah kebaca."
    designer "Oke, oke."

    "Jane duduk dan membuka catatan di laptopnya."
    designer "Eh, gue mau lihat daftar museum sebentar."
    coder "Oke."
    designer "Kita udah ngerjain lumayan banyak, tapi masih ada bagian yang belum."
    coder "Iya."
    designer "Gue mau pastiin minggu depan kita fokus ke yang penting dulu."
    coder "Boleh."
    "Jane meninjau pekerjaan yang sudah mereka lakukan."

    # Rekap pilihan Chapter 2 — fungsi atau desain.
    if prioritas_pengerjaan_website == "fungsi":
        designer "Dari awal kita lebih banyak nyicil fungsi booking dulu."
        coder "Iya. Tampilan beberapa bagian masih perlu dirapihin."
        designer "Oke. Nanti bagian gue."
    else:
        designer "Tampilan booking sekarang udah cukup dekat sama prototype."
        coder "Iya. Tapi bagian fungsi yang belum jalan masih perlu dikerjain."
        designer "Oke. Nanti kita lanjut."

    # Rekap MENU 04 Chapter 4.
    if fokus_pengerjaan_ch4 == "data_pemesanan":
        designer "Struktur data pesanan udah mulai ada."
        coder "Iya. Tapi baru diuji secara lokal dan belum semua halaman nyambung."
        designer "Berarti belum selesai seluruhnya."
        coder "Belum."
    else:
        designer "Form booking udah lebih lengkap sekarang."
        coder "Iya. Tapi bagian penyimpanan data masih harus kita lanjut."
        designer "Oke."

    # Rekap MENU 11 Chapter 4.
    if fokus_lanjutan_ch4 == "uji_booking":
        designer "Yang kemarin kita tes udah lebih jelas masalahnya."
        coder "Iya. Beberapa kesalahan kecil juga udah dibenerin."
        designer "Tapi alur lengkapnya belum selesai."
        coder "Betul."
    else:
        designer "Halaman admin sekarang udah ada bentuknya."
        coder "Iya. Tapi belum nyambung ke seluruh data booking."
        designer "Nanti kita sambungin."
        coder "Sip."

    designer "Terus pembayaran?"
    # Rekap Chapter 3: demo pembayaran tidak dianggap integrasi penuh.
    if prioritas_teknis_lanjutan == "pembayaran":
        coder "Demo pembayarannya udah ada, tapi masih terpisah dari alur utama."
        designer "Oh, iya. Yang kemarin kita coba."
        coder "Iya."
    else:
        coder "Masih perlu dibuat dan disambungin ke data pemesanan."
        designer "Oke. Berarti itu nanti juga."

    designer "Galeri?"
    coder "Strukturnya udah ada."
    designer "Konten aslinya masih belum."
    coder "Iya."
    designer "Adrian belum ngirim sampai sekarang."
    coder "Belum."

    "Jane melihat daftar pekerjaan yang tersisa."
    designer "Hmm."
    coder "Kenapa?"
    designer "Kalau dibaca begini, masih banyak banget, ya."
    coder "Lumayan banyak."
    designer "Tapi kan kita juga udah ngerjain banyak."
    coder "Iya."
    designer "Berarti masih seimbang?"
    coder "Belum tentu."
    designer "Kenapa?"
    coder "Ada bagian yang kecil, ada yang butuh waktu lama."
    designer "Oh, iya."
    coder "Misalnya database sama integrasi sistem."
    designer "Hmm."
    "Jane memperhatikan daftar itu lebih lama daripada biasanya."
    "Namun ia masih berusaha melihat perkembangan yang sudah mereka capai."
    designer "Setidaknya sekarang kita tahu apa aja yang belum selesai."
    coder "Iya."
    designer "Daripada baru sadar nanti."
    coder "Bener."

    # MENU 13 — respons melihat daftar pekerjaan (dialog saja).
    menu:
        "Daftar tugasnya lebih panjang daripada kelihatannya.":
            coder "Daftar tugasnya lebih panjang daripada kelihatannya."
            designer "Iya, sih."
            coder "Setiap satu bagian selesai, kadang muncul dua yang lain."
            designer "Kayak tugas kuliah."
            coder "Nah. Sama-sama berkembang biak."

        "Setidaknya website kita udah punya bentuk.":
            coder "Setidaknya website kita udah punya bentuk."
            designer "Iya. Nggak kayak awal lagi."
            coder "Beranda, booking, galeri, semuanya mulai kelihatan."
            designer "Tinggal dibikin berfungsi penuh."
            coder "Nah, itu masalahnya."

        "Berarti minggu depan harus lebih teratur.":
            coder "Berarti minggu depan harus lebih teratur."
            designer "Setuju."
            coder "Kita tentuin target yang realistis."
            designer "Oke. Jangan terlalu banyak."
            coder "Iya. Yang penting bisa selesai."
            designer "Sip."

    "Jane membuka kalender di laptopnya."
    "Ia menghitung sisa waktu pengerjaan proyek."
    designer "Eh."
    coder "Apa?"
    designer "Sekarang udah tanggal segini, ya."
    coder "Iya."
    designer "Berarti sisa hari buat tugas akhir..."
    "Jane memeriksa kalender sekali lagi."
    designer "Empat puluh lima?"
    coder "Hah?"
    designer "Empat puluh lima hari lagi."
    coder "Serius?"
    designer "Iya."
    "Luuk melihat kalendernya sendiri."
    "Angkanya benar."
    "Dari sembilan puluh hari yang diberikan, empat puluh lima hari telah berlalu."
    coder "Oh."
    designer "Kenapa?"
    coder "Berarti udah setengah."
    designer "Iya."
    coder "Cepet juga."
    designer "Padahal kemarin rasanya masih dua bulan lebih."
    coder "Iya."

    "Untuk beberapa saat, keduanya diam."
    "Bukan karena mereka tiba-tiba panik."
    "Mereka hanya mulai menyadari bahwa waktu bergerak lebih cepat daripada yang mereka perkirakan."
    # Belum masuk fase H-3: sedikit tegang, belum krisis.
    $ stress_level = min(100, stress_level + 2)

    designer "Tapi masih empat puluh lima hari."
    coder "Iya."
    designer "Masih bisa dikerjain."
    coder "Bisa. Asal jangan terlalu santai lagi."
    designer "Setuju."
    "Jane kembali menatap layar."
    designer "Eh, minggu depan kita bikin jadwal yang jelas, ya."
    coder "Boleh."
    designer "Biar nggak cuma ngerjain pas ada waktu."
    coder "Iya. Kita sengaja nyediain waktu."
    designer "Nah, itu."

    # MENU 14 — reaksi pada rencana membuat jadwal (dialog saja).
    menu:
        "Kita mulai berubah jadi mahasiswa rajin.":
            coder "Kita mulai berubah jadi mahasiswa rajin."
            designer "Mulai?"
            coder "Iya."
            designer "Berarti selama ini?"
            coder "Mahasiswa yang sedang mencari jati diri."
            designer "Anjir."

        "Jadwalnya jangan bentrok sama semua tugas lain.":
            coder "Jadwalnya jangan bentrok sama semua tugas lain."
            designer "Iya. Kita lihat jadwal kuliah dulu."
            coder "Biar nggak bikin janji yang akhirnya nggak ditepati."
            designer "Oke. Kita atur yang masuk akal."

        "Kita harus berhenti bilang 'nanti' terus.":
            coder "Kita harus berhenti bilang 'nanti' terus."
            designer "Iya, sih."
            coder "Kalau bisa dikerjain sekarang, kita kerjain sekarang."
            designer "Oke."
            coder "Setidaknya yang penting dulu."
            designer "Setuju."

    "Jane menyimpan jadwal sementara yang baru mereka diskusikan."
    coder "Eh, malam ini lo masih ada tugas?"
    designer "Ada."
    coder "Yang mana?"
    designer "PBO sama satu lagi."
    coder "Oh."
    designer "Lo?"
    coder "Ada juga."
    designer "Berarti malam ini nggak Marvel dulu?"
    coder "Kayaknya jangan lama-lama kalau main."
    designer "Wih."
    coder "Kenapa?"
    designer "Biasanya lo langsung gas."
    coder "Gue juga bisa belajar dari pengalaman."
    designer "Pengalaman berapa match?"
    coder "Jangan dihitung."
    designer "Takut?"
    coder "Iya."
    "Jane tertawa kecil."
    designer "Yaudah, kita selesain tugas dulu."
    coder "Oke."
    designer "Kalau udah, nanti lihat lagi."
    coder "Sip."
    "Mereka mulai membereskan barang untuk pulang dari kampus."
    "Sebelum pergi, Jane kembali membuka daftar pekerjaan Museum Arunika."
    designer "Luuk."
    coder "Hm?"
    designer "Minggu depan yang ini kita harus mulai seriusin, ya."
    coder "Iya."
    designer "Soalnya kalau kita terus nunggu semua bagian siap sendiri..."
    coder "Nggak bakal jalan semuanya."
    designer "Nah."
    coder "Gue ngerti."
    designer "Oke."

    # MENU 15 — pilihan respons penutup (dialog saja).
    menu:
        "Minggu depan kita mulai dari yang paling penting.":
            coder "Minggu depan kita mulai dari yang paling penting."
            designer "Oke."
            coder "Booking, data, admin, dan konten yang masih kurang."
            designer "Iya. Kita tentuin urutannya."
            coder "Sip."

        "Kita bagi targetnya per minggu biar jelas.":
            coder "Kita bagi targetnya per minggu biar jelas."
            designer "Boleh."
            coder "Jadi kita tahu minggu ini harus selesai apa."
            designer "Oke. Nanti gue bantu susun."
            coder "Sip."

    "Luuk dan Jane meninggalkan area duduk kampus."
    "Hari mulai sore."
    "Di sepanjang perjalanan pulang, mereka kembali membicarakan tugas kuliah lain, jadwal pertemuan, dan hal-hal kecil yang biasanya menjadi bahan candaan mereka."
    "Tidak ada pertengkaran."
    "Tidak ada keputusan dramatis."
    "Namun ada sesuatu yang mulai berubah."
    "Untuk pertama kalinya, mereka benar-benar memperhatikan berapa banyak waktu yang sudah berlalu."
    "Separuh masa pengerjaan Museum Arunika telah habis."
    "Website mereka sudah jauh berkembang dibandingkan pada hari pertama."
    "Tetapi banyak bagian penting belum menjadi satu sistem yang utuh."
    "Penyimpanan data masih perlu disempurnakan."
    "Alur booking dan pembayaran simulasi belum sepenuhnya tersambung."
    "Halaman admin masih membutuhkan pekerjaan."
    "Galeri masih menunggu bahan koleksi yang sebenarnya."
    "Dan Adrian belum memberikan hasil pekerjaan yang bisa digunakan."
    "Luuk dan Jane masih yakin bahwa proyek tersebut dapat diselesaikan."
    "Hanya saja, keyakinan itu sekarang mulai disertai kesadaran baru."
    "Mereka tidak bisa terus mengandalkan waktu yang tersisa."
    "Karena waktu yang sudah lewat tidak akan kembali."
    "45 DAYS LEFT."

    $ hud_visible = False
    scene black with fade
    centered "{size=50}CHAPTER 04 COMPLETE{/size}\n{size=36}45 DAYS LEFT{/size}\n{size=28}The List Keeps Growing."

    jump chapter_5
