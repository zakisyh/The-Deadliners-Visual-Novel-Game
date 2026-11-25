# ============================================================
# THE DEADLINERS — CHAPTER 08: THE LAST THREE DAYS
# ============================================================
# Lanjutan Chapter 7 (4 DAYS LEFT).

default pemulihan_ch8 = ""

default keputusan_konten_ch8 = ""

default keputusan_build_ch8 = ""


label chapter_8:
    $ hud_visible = False
    $ days_left = 3
    scene black with fade
    centered "{size=50}CHAPTER 08{/size}\n{size=42}THE LAST THREE DAYS{/size}\n{size=34}3 DAYS LEFT{/size}"
    jump ch8_scene_01


# ============================================================
# SCENE 01 — A DIFFERENT SCREEN | H-3 (siang)
# Menu 01–03: respons dialog biasa.
# ============================================================
label ch8_scene_01:
    $ days_left = 3
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Sehari setelah pertemuan terakhir, Luuk dan Jane kembali berkumpul di area kampus."
    "Hari ini mereka tidak berencana menambah fitur. Mereka ingin menguji versi Museum Arunika seolah-olah sedang presentasi."
    designer "Laptop gue udah siap."
    coder "Oke. Gue bawa versi demo terakhir."
    designer "Jangan tes dari laptop lo terus."
    coder "Iya, makanya hari ini pakai punya lo."
    designer "Mulai dari beranda, tanpa buka halaman pakai link khusus."
    coder "Setuju."
    "Luuk menyiapkan salinan versi demo yang selama ini paling sering dijalankan di lingkungan lokalnya."
    "Jane membuka versi tersebut dari laptopnya sendiri."
    designer "Berandanya muncul."
    coder "Bagus."
    designer "Galeri juga kebuka."
    coder "Coba booking."
    "Jane masuk ke halaman pemesanan dan mengisi data uji seperti biasa."
    "Namun, saat ia melanjutkan ke ringkasan, salah satu bagian justru menampilkan data contoh lama."
    designer "Eh."
    coder "Kenapa?"
    designer "Ini bukan nama yang tadi gue masukin."
    coder "Hah?"
    "Luuk mendekat untuk membaca layar."
    designer "Tadi gue isi nama yang beda."
    coder "Coba balik dulu."
    "Jane kembali ke form, lalu mengulangi langkah yang sama."
    "Hasilnya tidak berubah."
    coder "Oke, ini aneh."
    designer "Di laptop lo kemarin bisa, kan?"
    coder "Iya. Tapi kita banyak tes pakai data lokal yang udah ada."
    designer "Berarti versi yang dipindah ini belum bawa alur yang sama?"
    coder "Kemungkinan ada sambungan atau data uji yang belum ikut. Gue harus periksa."

    if prioritas_integrasi_ch7 == "booking":
        designer "Padahal alur booking di laptop lo udah kita rapihin."
        coder "Iya. Justru itu. Versi yang jalan di mesin gue belum tentu langsung jalan di mesin lain."
    else:
        designer "Kemarin kita lebih fokus ke admin, jadi sambungan booking memang belum tuntas."
        coder "Iya. Sekarang masalahnya kelihatan jelas waktu dijalankan dari awal."

    if fokus_pengujian_ch7 == "pengunjung":
        designer "Kita juga udah tes alur pengunjung sebelumnya."
        coder "Iya, tapi belum cukup ngetes versi yang dipindah ke laptop lain."
    else:
        designer "Terakhir kita lebih banyak nguji sisi pengelola."
        coder "Iya. Ada jalur pengunjung yang belum kebagian tes lengkap."

    # MENU 01 — hanya mengubah respons.
    menu:
        "Kita cek apa yang beda antara dua laptop ini.":
            coder "Kita cek apa yang beda antara dua laptop ini."
            designer "Oke. Gue catat langkah yang bikin salah."
            coder "Jangan ubah data uji dulu, biar bisa dibandingin."
            designer "Siap."

        "Kenapa bug selalu muncul pas waktunya tinggal sedikit?":
            coder "Kenapa bug selalu muncul pas waktunya tinggal sedikit?"
            designer "Karena sekarang kita baru tes di kondisi yang beda."
            coder "Jawaban logis yang menyakitkan."
            designer "Tapi bisa kita pakai buat cari masalahnya."

        "Berarti yang kemarin berhasil belum tentu siap didemokan.":
            coder "Berarti yang kemarin berhasil belum tentu siap didemokan."
            designer "Iya. Kita butuh hasil yang bisa diulang di laptop ini juga."
            coder "Oke."

    "Mereka membuka halaman admin untuk mencocokkan data yang seharusnya tampil."

    if fokus_integrasi_ch6 == "admin" or prioritas_integrasi_ch7 == "admin":
        designer "Tabel adminnya ada, tapi beberapa data uji yang kita lihat kemarin nggak muncul."
        coder "Berarti sumber data versi demo ini harus kita cek lagi."
    else:
        designer "Bagian admin masih banyak mengandalkan data contoh terpisah."
        coder "Iya. Ini belum bisa dibilang terhubung penuh ke pesanan."

    if fokus_lanjutan_ch5 == "pembayaran" or fokus_integrasi_ch6 == "pembayaran":
        designer "Layar pembayaran simulasi masih bisa dibuka."
        coder "Tapi data yang masuk ke situ harus diuji. Jangan cuma cek halamannya muncul."
    else:
        designer "Pembayaran simulasi juga belum jadi alur yang sepenuhnya nyambung."
        coder "Iya. Kita nggak boleh memaksa seolah-olah transaksi sungguhan sudah jalan."

    # MENU 02 — dialog biasa.
    menu:
        "Tulis hasil tesnya, termasuk yang gagal.":
            coder "Tulis hasil tesnya, termasuk yang gagal."
            designer "Iya. Kita perlu bukti buat debugging, bukan sekadar ingatan."

        "Jangan bilang semuanya rusak sebelum kita tahu penyebabnya.":
            coder "Jangan bilang semuanya rusak sebelum kita tahu penyebabnya."
            designer "Benar. Yang gagal baru jalur yang kita coba tadi."
            coder "Nah. Kita cek bagian itu dulu."

    "Luuk membandingkan pengaturan dan alamat data yang dipakai pada versi lokal dengan salinan demo."
    "Salah satu sambungan masih mengarah ke lingkungan pengujian di laptop Luuk."
    coder "Nah. Ini salah satu sumber masalahnya."
    designer "Jadi bukan karena data yang gue isi?"
    coder "Bukan. Beberapa bagian masih bergantung sama lingkungan lokal gue."
    designer "Bisa diperbaiki?"
    coder "Bisa dicoba. Tapi kita harus pastikan hasilnya bisa jalan di laptop lain, bukan cuma di sini."
    designer "Oke."

    # MENU 03 — dialog biasa.
    menu:
        "Kita butuh satu versi demo yang bisa diuji tanpa trik.":
            coder "Kita butuh satu versi demo yang bisa diuji tanpa trik."
            designer "Setuju. Jangan sampai pas presentasi harus buka lima halaman manual."

        "Gue catat dulu sebelum asal mengubah kode.":
            coder "Gue catat dulu sebelum asal mengubah kode."
            designer "Bagus. Jangan sampai satu perbaikan bikin masalah baru."

    "Luuk menatap daftar error yang baru bertambah."
    "Di luar layar laptop, waktu terus berjalan."

    $ stress_level = min(100, stress_level + 7)

    jump ch8_scene_02


# ============================================================
# SCENE 02 — STAY WITH ME | H-3 (malam)
# Menu 04: pilihan penting. Menu 05–06: dialog biasa.
# ============================================================
label ch8_scene_02:
    $ days_left = 3
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Malam itu, Luuk dan Jane melanjutkan pemeriksaan di kontrakan Luuk."
    "Mereka sudah mencoba beberapa perubahan kecil dan mengulang tes dari awal."
    "Sebagian halaman tampil normal. Namun, beberapa langkah masih tidak konsisten ketika diuji dengan salinan demo."
    designer "Yang beranda sama navigasi dasar udah oke."
    coder "Iya."
    designer "Tapi ringkasan dan data lanjutan masih harus dicek."
    coder "Gue tahu."
    "Luuk menggeser jendela kode dan membaca baris yang sama berulang kali."
    designer "Luuk?"
    coder "Bentar."
    "Ia mencoba menjalankan ulang tes. Hasilnya masih belum sesuai."
    coder "Kenapa, sih..."
    designer "Yang tadi beda di mana?"
    coder "Gue... nggak tahu. Barusan gue baca, terus kayak nggak masuk ke kepala."
    designer "Oke. Simpan dulu."
    coder "Kalau kita berhenti sekarang, besok tinggal dua hari."
    designer "Gue nggak bilang berhenti ngerjainnya."
    coder "Tapi ini belum nyambung. Konten juga belum ada. Admin belum seluruhnya selesai."
    coder "Gue dari tadi cuma mindahin masalah dari satu halaman ke halaman lain."
    "Jane menutup daftar tes sejenak."
    designer "Luuk."
    coder "Hm?"
    designer "Stay with me."
    "Luuk mengangkat pandangannya dari layar."
    designer "Maksud gue, jangan hilang fokus dan nyoba menyelesaikan semuanya sekaligus. Dengerin gue dulu."
    coder "...Oke."
    designer "Gue di sini buat bantu ngetes dan ngecek. Ini bukan kerjaan lo sendirian."
    coder "Iya."
    designer "Kita ambil satu masalah. Satu tes. Habis itu baru lanjut."
    coder "Oke. Satu masalah dulu."
    designer "Nah."
    "Luuk menyimpan perubahan terakhir dan menarik napas pelan."
    "Jane membuka kembali daftar pengujian, kali ini hanya menampilkan masalah yang paling menghambat."
    designer "Gini lebih kelihatan, kan?"
    coder "Iya. Maaf tadi gue mulai muter-muter sendiri."
    designer "Nggak apa-apa. Tapi kalau lo bingung, bilang. Jangan diem sambil buka dua puluh tab."
    coder "Sebenernya baru enam belas."
    designer "Luuk."
    coder "Iya, iya. Gue tutup."
    "Keduanya tertawa singkat. Keadaan belum aman, tetapi Luuk kembali bisa menentukan langkah berikutnya."

    $ stress_level = max(0, stress_level - 3)

    designer "Sekarang pilih kerjaan yang paling perlu kita selesaikan malam ini."
    coder "Ada dua cara. Kita rapihin satu jalur inti sampai bisa diuji berulang, atau coba sambung lebih banyak fitur yang masih terpisah."
    designer "Kalau yang kedua, jangan anggap otomatis semuanya stabil."
    coder "Iya."

    # MENU 04 — pilihan penting pertama.
    menu:
        "Pulihkan satu jalur demo inti agar bisa diuji di laptop Jane.":
            $ pemulihan_ch8 = "jalur_inti"
            coder "Pulihkan satu jalur demo inti agar bisa diuji di laptop lo."
            designer "Oke. Mulai dari beranda ke booking dan ringkasan yang memang bisa kita siapkan."

            if prioritas_integrasi_ch7 == "booking" or fokus_teknis_ch6 == "alur_pesanan":
                coder "Alur uji lama masih bisa dipakai. Kita perbaiki sumber data dan tujuan halamannya."
                designer "Berarti hasil sebelumnya nggak dibuang."
            else:
                coder "Karena booking belum lengkap, kita buat rute demo terbatas dengan data uji yang jelas."
                designer "Jangan klaim sudah ada penyimpanan permanen."
                coder "Setuju."

            "Luuk mengganti sambungan yang masih bergantung pada lingkungan lokalnya."
            "Jane mengulang langkah dari beranda pada salinan demo di laptopnya sendiri."
            "Pada percobaan kedua, ringkasan berhasil menampilkan data uji sesuai langkah yang baru mereka perbaiki."
            designer "Nah. Ini berhasil di laptop gue."
            coder "Iya. Tapi baru jalur yang kita uji. Bagian admin dan pembayaran lain belum otomatis beres."
            designer "Oke. Kita tandai batasnya."
            "Mereka menyimpan versi uji yang dapat menjalankan satu rute demo secara lebih konsisten."

            $ website_progress = min(100, website_progress + 5)
            $ stress_level = max(0, stress_level - 3)

        "Perbaiki beberapa sambungan booking, admin, dan simulasi sekaligus.":
            $ pemulihan_ch8 = "fitur_luas"
            coder "Perbaiki beberapa sambungan booking, admin, dan simulasi sekaligus."
            designer "Oke, tapi kita perlu tes ulang semuanya setelah itu."
            coder "Iya. Gue nggak mau cuma lihat halaman berhasil dibuka."
            "Luuk memeriksa perpindahan data dan tombol pada beberapa modul yang masih terpisah."

            if fokus_integrasi_ch6 == "admin" or prioritas_integrasi_ch7 == "admin":
                designer "Kita bisa lanjut dari daftar admin yang sudah pernah dites."
                coder "Iya, tapi data yang dibaca tetap harus dicocokkan."
            else:
                designer "Admin masih banyak pakai data contoh."
                coder "Iya. Jadi kita perbaiki navigasi dan tampilannya dulu, bukan mengaku sudah otomatis."

            if fokus_integrasi_ch6 == "pembayaran" or fokus_lanjutan_ch5 == "pembayaran":
                designer "Simulasi pembayaran yang lama bisa dites lagi."
                coder "Iya. Kita perbaiki tombol kembali dan label datanya."
            else:
                designer "Pembayaran simulasi masih terbatas."
                coder "Iya. Gue nggak bakal bikin transaksi sungguhan dalam semalam."

            "Beberapa sambungan dan tombol berhasil mereka perbaiki, tetapi belum sempat diuji menyeluruh di lingkungan berbeda."
            designer "Fitur yang bisa dibuka memang lebih banyak."
            coder "Iya. Tapi masih ada risiko alur yang belum kita tes."
            designer "Tulis begitu."

            $ website_progress = min(100, website_progress + 6)
            $ stress_level = min(100, stress_level + 2)

    "Jane mencatat hasil malam itu sesuai jalur yang dipilih."
    designer "Kita udah punya langkah yang lebih jelas."
    coder "Iya. Setidaknya sekarang gue tahu harus ngetes apa."

    # MENU 05 — dialog biasa.
    menu:
        "Besok kita tes pakai data baru, bukan data yang itu-itu aja.":
            coder "Besok kita tes pakai data baru, bukan data yang itu-itu aja."
            designer "Setuju. Kalau cuma satu contoh, kita nggak tahu masalah lainnya."

        "Gue tutup tab yang nggak dipakai dulu.":
            coder "Gue tutup tab yang nggak dipakai dulu."
            designer "Bagus. Enam belas tab juga keterlaluan."
            coder "Yang penting sekarang tinggal lima."
            designer "Masih lumayan."

        "Kita butuh air minum sebelum tambah bug lagi.":
            coder "Kita butuh air minum sebelum tambah bug lagi."
            designer "Setuju. Dan istirahat sebentar."
            coder "Oke."

    "Jane melirik jam."
    designer "Besok kita lanjut, tapi jangan asal ubah semuanya malam ini."
    coder "Iya. Gue simpan versi yang tadi dulu."
    designer "Bagus. Biar ada yang bisa dibandingkan."

    # MENU 06 — dialog biasa.
    menu:
        "Makasih udah bantu ngarahin tadi.":
            coder "Makasih udah bantu ngarahin tadi."
            designer "Ya sama-sama. Lo juga bantu bagian desain gue dari awal."
            coder "Iya."
            designer "Sekarang tutup laptop dulu."

        "Besok kita lanjut dari masalah yang paling jelas.":
            coder "Besok kita lanjut dari masalah yang paling jelas."
            designer "Deal. Dan tesnya kita catat, bukan ditebak."
            coder "Sip."

    "Malam itu mereka tidak menyatakan proyek sudah selamat."
    "Namun, di tengah tekanan, mereka kembali bekerja sebagai tim dan berhenti mengejar semua masalah sekaligus."

    jump ch8_scene_03


# ============================================================
# SCENE 03 — NO FILES YET | H-2
# Menu 07–08: dialog biasa. Menu 09: pilihan berpengaruh.
# ============================================================
label ch8_scene_03:
    $ days_left = 2
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Keesokan harinya, Luuk dan Jane kembali bertemu di kampus."
    "Mereka membawa hasil pengujian terbaru dan daftar konten yang belum diterima."
    designer "Gue cek folder koleksi pagi ini."
    coder "Gimana?"
    designer "Belum ada file baru dari Adrian."
    coder "Oke."

    if strategi_konten_ch7 == "tenggat":
        designer "Permintaan terakhir dengan batas waktu itu juga belum menghasilkan kiriman."
        coder "Iya. Kita sudah kasih kesempatan buat jelasin kendalanya."
    else:
        designer "Untung galeri demo kemarin udah kita kasih label contoh."
        coder "Iya. Tapi label itu bukan pengganti bahan asli."

    "Jane mengirim pesan singkat untuk memastikan keadaannya."
    "Jane (grup): Adrian, sampai pagi ini belum ada bahan koleksi yang masuk. Ada file yang bisa kamu kirim sekarang?"
    "Beberapa saat kemudian, muncul balasan."
    "Adrian (grup): Belum. Masih aku usahain."
    designer "..."
    coder "Masih belum."
    designer "Dua hari lagi, Luuk."
    coder "Iya."
    "Jane menutup grup dan memeriksa galeri yang sekarang hanya dapat diuji menggunakan konten contoh."

    $ stress_level = min(100, stress_level + 5)

    # MENU 07 — dialog biasa.
    menu:
        "Kita nggak bisa menampilkan bahan yang belum pernah kita terima.":
            coder "Kita nggak bisa menampilkan bahan yang belum pernah kita terima."
            designer "Iya. Jangan mengarang data koleksinya."
            coder "Setuju."

        "Kalau dia kirim besok, tetap harus kita periksa dulu.":
            coder "Kalau dia kirim besok, tetap harus kita periksa dulu."
            designer "Bener. Nggak bisa langsung dipakai tanpa dicek."
            coder "Apalagi waktunya tinggal sedikit."

        "Folder kosong ini udah lebih terkenal daripada museumnya.":
            coder "Folder kosong ini udah lebih terkenal daripada museumnya."
            designer "Gue mau ketawa, tapi capek."
            coder "Sama."

    "Luuk membuka daftar pekerjaan yang sudah mereka dokumentasikan."

    if rekap_pengumpulan_ch5:
        designer "Rekap berkas yang kita simpan juga menunjukkan belum ada bahan koleksi yang diterima."
        coder "Iya. Cocokkan lagi dengan folder sekarang."
    elif konfirmasi_target_adrian:
        designer "Konfirmasi tugas Adrian dulu masih ada, tapi hasil filenya belum ada."
        coder "Iya. Kita bedain janji dan kiriman yang benar-benar ada."
    else:
        designer "Kita tetap punya daftar pembagian tugas dan folder yang bisa diperiksa."
        coder "Iya. Jelaskan berdasarkan yang benar-benar kita punya."

    if laporan_uji_ch6:
        designer "Laporan tes sebelumnya juga menandai galeri konten asli sebagai belum bisa diuji."
        coder "Bagus. Jangan diubah jadi selesai tanpa tes baru."

    # MENU 08 — dialog biasa.
    menu:
        "Dokumentasi harus jujur, bukan buat menyalahkan asal-asalan.":
            coder "Dokumentasi harus jujur, bukan buat menyalahkan asal-asalan."
            designer "Setuju. Kita cuma catat fakta pekerjaan."

        "Kita juga harus siap menjelaskan bagian yang belum selesai.":
            coder "Kita juga harus siap menjelaskan bagian yang belum selesai."
            designer "Iya. Jangan pura-pura galeri final sudah lengkap."

    designer "Sekarang keputusan galeri buat latihan demo gimana?"
    coder "Ada dua cara yang sama-sama jujur. Tampilkan placeholder dengan label, atau jangan tampilkan bagian koleksi yang belum terverifikasi."
    designer "Dua-duanya nggak menggantikan bahan Adrian, ya."
    coder "Iya."

    # MENU 09 — pilihan penting kedua; BUKAN bukti keenam.
    menu:
        "Tampilkan galeri demo berlabel 'konten contoh'.":
            $ keputusan_konten_ch8 = "contoh"
            coder "Tampilkan galeri demo berlabel konten contoh."
            designer "Oke. Kita bisa jelasin layout tanpa mengaku punya konten asli."

            if strategi_konten_ch7 == "demo":
                designer "Label contoh yang kemarin sudah ada, jadi tinggal diperiksa lagi."
                coder "Iya. Pastikan semua kartu contoh konsisten."
            else:
                "Jane menambahkan penanda yang jelas pada galeri contoh dan keterangan bahwa data koleksi belum final."
                designer "Sekarang tidak terlihat seperti data museum yang sudah diverifikasi."
                coder "Bagus."

                $ website_progress = min(100, website_progress + 1)

            "Jane menguji galeri dengan beberapa ukuran layar yang pernah dipakai sebelumnya."
            designer "Setidaknya tampilan demo bisa dijelaskan sesuai kondisinya."
            coder "Iya. Konten asli tetap belum selesai."

            $ stress_level = max(0, stress_level - 1)

        "Tahan bagian koleksi yang belum terverifikasi dari demo.":
            $ keputusan_konten_ch8 = "tahan"
            coder "Tahan bagian koleksi yang belum terverifikasi dari demo."
            designer "Berarti galeri kita jelasin sebagai fitur yang belum punya bahan final?"
            coder "Iya. Lebih baik daripada menampilkan informasi yang nggak benar."
            "Jane menyesuaikan rencana demonstrasi agar halaman koleksi yang belum memiliki bahan asli tidak diperkenalkan sebagai fitur siap pakai."
            designer "Oke. Navigasi yang lain tetap kita tes."
            coder "Betul. Tapi saat presentasi, kita tetap harus jelaskan kekurangannya."

            $ stress_level = max(0, stress_level - 1)

    "Luuk memeriksa lagi urutan presentasi sementara."
    designer "Bagian gue tetap jelasin desain dan pengujian tampilan."
    coder "Gue jelasin implementasi dan batasan fungsi yang sudah diuji."
    designer "Kalau Adrian?"
    coder "Kita belum tahu dia bakal bawa apa, atau bahkan persiapannya sampai mana."
    designer "Iya. Besok harus ada kepastian kehadirannya juga."
    "Mereka mencatat masalah konten sebagai pekerjaan belum selesai, bukan sebagai hasil yang sudah berhasil."

    jump ch8_scene_04


# ============================================================
# SCENE 04 — THE LAST BUILD | H-1 (pagi)
# Menu 10, 12: dialog biasa. Menu 11: pilihan penting.
# ============================================================
label ch8_scene_04:
    $ days_left = 1
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Satu hari sebelum presentasi, Luuk dan Jane kembali menguji versi Museum Arunika di dua laptop."
    "Mereka menggunakan data baru dan mengikuti tombol sesuai urutan yang akan dijelaskan saat demo."
    designer "Oke. Jangan pakai data yang kemarin lagi."
    coder "Udah gue siapin dua set baru."
    designer "Mulai dari beranda."
    "Jane mengikuti alur pengunjung, sementara Luuk mencatat hasil di laptopnya."

    if pemulihan_ch8 == "jalur_inti":
        designer "Jalur inti yang kita pulihkan sudah bisa diulang di laptop gue."
        coder "Iya. Ini versi yang paling banyak kita tes di luar laptop gue."
        designer "Tapi sisi admin dan fitur lain masih punya batasan."
        coder "Betul. Kita jangan sembunyiin itu."
    else:
        designer "Sekarang lebih banyak halaman yang bisa dibuka daripada dua hari lalu."
        coder "Iya. Tapi ada beberapa langkah yang belum kita ulang dengan semua data."
        designer "Berarti fitur luas belum otomatis berarti stabil."
        coder "Tepat."

    if fokus_pengujian_ch7 == "pengunjung":
        designer "Bug tombol kembali yang pernah kita temukan juga sudah bisa kita tes lagi."
        coder "Iya. Tapi itu baru satu bagian dari keseluruhan alur."
    else:
        designer "Kemarin kita fokus sisi pengelola. Jalur pengunjung tetap perlu dicoba pelan-pelan."
        coder "Iya. Jangan dilewati cuma karena waktunya mepet."

    "Mereka menemukan satu perbedaan kecil pada data uji baru dan memperbaiki langkah reproduksinya dalam catatan."
    designer "Masih ada masalah, tapi sekarang kita tahu letaknya."
    coder "Iya."
    designer "Terus gimana?"
    coder "Kita harus putuskan apakah memakai versi yang sudah cukup teruji, atau mencoba tambalan tambahan hari ini."

    $ stress_level = min(100, stress_level + 3)

    # MENU 10 — dialog biasa.
    menu:
        "Jangan sampai perbaikan terakhir merusak yang sudah jalan.":
            coder "Jangan sampai perbaikan terakhir merusak yang sudah jalan."
            designer "Iya. Setiap perubahan harus ada tes ulangnya."

        "Gue ingin bisa mendemokan hasil yang benar-benar kita punya.":
            coder "Gue ingin bisa mendemokan hasil yang benar-benar kita punya."
            designer "Setuju. Nggak perlu kelihatan sempurna kalau kenyataannya belum."

        "Kalendernya sekarang benar-benar nggak kasih diskon.":
            coder "Kalendernya sekarang benar-benar nggak kasih diskon."
            designer "Tinggal satu hari, Luuk."
            coder "Iya. Gue tahu."

    # MENU 11 — pilihan penting ketiga.
    menu:
        "Bekukan versi yang sudah diuji, lalu siapkan demo sesuai batasnya.":
            $ keputusan_build_ch8 = "bekukan"
            coder "Bekukan versi yang sudah diuji, lalu siapkan demo sesuai batasnya."
            designer "Oke. Jangan ada fitur baru mendadak."
            coder "Kita simpan cadangan, lalu ulang tes pada jalur yang benar-benar bisa ditunjukkan."
            "Luuk menyimpan salinan versi yang telah mereka uji pada kedua laptop."
            "Jane mengulang langkah yang dapat didemonstrasikan dan menandai keterbatasan sisanya."

            if pemulihan_ch8 == "jalur_inti":
                designer "Alur inti ini lebih bisa kita andalkan daripada percobaan pertama H-3."
                coder "Iya. Tapi nggak berarti seluruh website sudah final."
            else:
                designer "Kita pilih bagian yang terbukti berjalan dari fitur yang kemarin kita perbaiki."
                coder "Iya. Jangan pakai jalur yang belum sempat dites cuma demi kelihatan lengkap."

            "Mereka menyimpan urutan demo dan daftar keterbatasan tanpa menambahkan perubahan berisiko."

            $ website_progress = min(100, website_progress + 1)
            $ stress_level = max(0, stress_level - 3)

        "Coba satu paket perbaikan tambahan, lalu tes ulang sebisanya.":
            $ keputusan_build_ch8 = "tambal"
            coder "Coba satu paket perbaikan tambahan, lalu tes ulang sebisanya."
            designer "Oke. Tapi kalau belum teruji, jangan dibawa sebagai fitur pasti."
            coder "Setuju."
            "Luuk memperbaiki beberapa sambungan yang masih memakai pengaturan uji lama."
            "Jane memeriksa tombol dan tampilan setelah perubahan tersebut."

            if pemulihan_ch8 == "jalur_inti":
                designer "Jalur inti masih bisa dibuka, tapi perubahan baru ini butuh tes lebih banyak."
                coder "Iya. Versi cadangan lama tetap gue simpan."
            else:
                designer "Beberapa halaman sekarang lebih nyambung, tapi kita belum mencoba semua kombinasi."
                coder "Iya. Kita harus hati-hati saat memilih jalur demonstrasi."

            "Perbaikan tambahan meningkatkan cakupan fungsi yang tersedia, tetapi belum membuktikan kestabilan semua jalur."

            $ website_progress = min(100, website_progress + 4)
            $ stress_level = min(100, stress_level + 3)

    designer "Oke. Kita catat hasil yang bisa dipakai besok."
    coder "Iya. Jangan sampai lupa versi mana yang kita tes."

    # MENU 12 — dialog biasa.
    menu:
        "Simpan salinan cadangan dengan nama yang jelas.":
            coder "Simpan salinan cadangan dengan nama yang jelas."
            designer "Jangan namanya final_fix_beneran_final."
            coder "Gue nggak janji."
            designer "Luuk!"

        "Kita ulang satu kali lagi dari beranda.":
            coder "Kita ulang satu kali lagi dari beranda."
            designer "Oke. Pakai urutan yang tertulis biar nggak lompat."

        "Gue mau istirahat sebentar sebelum lanjut latihan.":
            coder "Gue mau istirahat sebentar sebelum lanjut latihan."
            designer "Iya. Biar nggak salah baca hasil tes."
            coder "Setuju."

    "Mereka mengakhiri perubahan teknis untuk sementara dan beralih ke persiapan penjelasan presentasi."
    "Tidak semua fitur menjadi sempurna dalam semalam. Namun, mereka tahu bagian mana yang telah diuji dan mana yang masih berisiko."

    jump ch8_scene_05


# ============================================================
# SCENE 05 — TOMORROW | H-1 (sore)
# Menu 13–15: dialog biasa. Presentasi belum terjadi.
# ============================================================
label ch8_scene_05:
    $ days_left = 1
    scene black with dissolve
    $ hud_visible = True
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Sore harinya, Luuk dan Jane duduk di area kampus dengan dua laptop yang sudah ditutup."
    "Mereka sudah menyiapkan urutan demo serta catatan fungsi yang dapat dan belum dapat dijalankan."
    designer "Gue mau baca urutan presentasinya sekali lagi."
    coder "Oke."
    designer "Gue mulai dari tujuan desain, navigasi, dan alur pengunjung."
    coder "Terus gue jelasin implementasi, cara tes, sama keterbatasan teknisnya."
    designer "Bagian koleksi gimana?"

    if keputusan_konten_ch8 == "contoh":
        designer "Kita jelasin kalau galeri yang tampil masih pakai konten contoh."
        coder "Iya. Jangan bilang gambar itu bahan koleksi asli."
    else:
        designer "Bagian koleksi tanpa data terverifikasi nggak kita tonjolkan di demo."
        coder "Iya. Tapi tetap jelaskan kalau bahannya belum diterima."

    if keputusan_build_ch8 == "bekukan":
        designer "Kita bawa versi yang sudah kita simpan dan tes, dengan fitur yang masih terbatas."
        coder "Iya. Kalau ditanya yang belum jalan, jawab sesuai hasilnya."
    else:
        designer "Perbaikan terakhir nambah beberapa fungsi, tapi ada jalur yang belum diuji lengkap."
        coder "Iya. Kita tetap siapkan cadangan dan jangan mengklaim semuanya stabil."

    designer "Sekarang soal Adrian."
    coder "Iya."
    "Jane membuka grup dan mengetik pesan terakhir mengenai kesiapan presentasi."
    "Jane (grup): Adrian, besok presentasi kelompok. Tolong konfirmasi kehadiranmu dan kirim bahan yang sudah selesai malam ini jika ada."
    "Mereka menunggu beberapa menit."
    "Balasan akhirnya muncul."
    "Adrian (grup): Aku usahain datang besok. Bahan belum siap."
    "Jane membaca pesan itu sekali lagi."
    designer "'Usahain datang'."
    coder "Iya. Itu belum pasti."
    designer "Dan bahan masih belum siap."
    coder "Iya."
    "Mereka tidak tahu apakah Adrian benar-benar akan hadir besok."
    "Keputusan itu belum berada di tangan Luuk atau Jane."
    "Yang bisa mereka lakukan malam ini hanyalah menyiapkan hasil kerja sendiri dengan jujur."

    $ stress_level = min(100, stress_level + 3)

    # MENU 13 — dialog biasa.
    menu:
        "Besok kita jelaskan hasil kerja yang benar-benar ada.":
            coder "Besok kita jelaskan hasil kerja yang benar-benar ada."
            designer "Iya. Jangan menutup kekurangan dengan janji."
            coder "Setuju."

        "Kalau Adrian datang, kita tetap harus tahu dia bawa apa.":
            coder "Kalau Adrian datang, kita tetap harus tahu dia bawa apa."
            designer "Benar. Nggak bisa langsung bilang kontribusinya selesai."
            coder "Iya."

        "Gue nggak mau debat lewat chat malam sebelum presentasi.":
            coder "Gue nggak mau debat lewat chat malam sebelum presentasi."
            designer "Sama. Kita udah punya fakta yang bisa dijelaskan."
            coder "Oke."

    "Jane membuka dokumentasi proyek yang tersedia."

    if jumlah_bukti_rahasia >= 3:
        designer "Catatan kontribusi dan hasil kerja yang kita kumpulkan lumayan lengkap."
        coder "Iya. Kita simpan sesuai aslinya, kalau perlu menjelaskan prosesnya nanti."
        designer "Tapi dokumentasi itu juga nggak otomatis bikin website selesai."
        coder "Betul. Dua hal itu beda."
    else:
        designer "Dokumentasi kita ada, meskipun nggak semuanya lengkap."
        coder "Iya. Kalau ditanya, jawab hanya dari catatan dan file yang benar-benar ada."
        designer "Setuju."

    if laporan_uji_ch6:
        designer "Hasil uji dengan tangkapan layar juga siap kalau perlu dicek."
        coder "Oke. Jangan ubah status gagal jadi berhasil."
    elif catatan_progres_dibuat:
        designer "Catatan progres lama juga bisa bantu mengingat pekerjaan yang sudah dilakukan."
        coder "Iya. Tapi untuk fungsi website, tetap lihat hasil tes terakhir."

    "Jane mengembalikan laptopnya ke dalam tas."
    designer "Lo udah siap?"
    coder "Siap menjelaskan yang gue kerjain. Kalau ditanya semua bakal berhasil, gue nggak bisa janji."
    designer "Gue juga."
    coder "Tapi kita sudah berusaha bikin hasilnya bisa diuji."
    designer "Iya."

    # MENU 14 — dialog biasa.
    menu:
        "Kita tetap satu tim buat bagian yang memang kita kerjain.":
            coder "Kita tetap satu tim buat bagian yang memang kita kerjain."
            designer "Iya. Gue jelasin desainnya, lo jelasin kodenya."
            coder "Dan kita sama-sama tahu hasil tesnya."

        "Besok jangan mengarang jawaban kalau nggak tahu.":
            coder "Besok jangan mengarang jawaban kalau nggak tahu."
            designer "Setuju. Bilang belum selesai atau belum diuji kalau memang begitu."
            coder "Oke."

        "Setelah besok, gue pengin tidur tanpa mikirin tombol.":
            coder "Setelah besok, gue pengin tidur tanpa mikirin tombol."
            designer "Gue pengin buka Marvel tanpa lihat daftar tugas."
            coder "Impian sederhana."
            designer "Susah dicapai ternyata."

    "Luuk melihat catatan H-3 ketika versi demo pertama kali gagal di laptop Jane."
    "Ia masih ingat bagaimana kepalanya terasa penuh dan betapa sulitnya memutuskan harus mulai dari mana."
    "Ia juga ingat Jane meminta mereka kembali fokus pada satu masalah."
    "Hasilnya belum sempurna, tetapi mereka tidak lagi bekerja dengan menebak-nebak."
    designer "Luuk."
    coder "Apa?"
    designer "Malam ini jangan buka proyek sampai pagi."
    coder "Iya. Gue cek cadangannya sekali, terus tidur."
    designer "Sekali, ya."
    coder "Iya."
    designer "Besok ketemu sebelum masuk ruangan."
    coder "Sip."

    # MENU 15 — dialog penutup biasa.
    menu:
        "Sampai besok. Kita bawa hasil terbaik yang kita punya.":
            coder "Sampai besok. Kita bawa hasil terbaik yang kita punya."
            designer "Oke. Jangan lupa laptop sama catatan."
            coder "Aman."

        "Gue tidur dulu biar besok bisa mikir jelas.":
            coder "Gue tidur dulu biar besok bisa mikir jelas."
            designer "Bagus. Gue juga."
            coder "Sampai besok."
            designer "Sampai besok."

    "Mereka pulang dengan persiapan yang tidak sepenuhnya sempurna, tetapi dengan gambaran yang lebih jujur tentang kondisi Museum Arunika."
    "Adrian belum memberikan bahan dan kehadirannya belum pasti."
    "Website yang akan ditunjukkan besok bergantung pada keputusan teknis serta pengujian yang dilakukan pemain sejak awal."
    "Dan apa pun yang terjadi, Luuk dan Jane harus menjelaskan hasilnya di hadapan dosen."
    "1 DAY LEFT."

    $ hud_visible = False
    scene black with fade
    centered "{size=50}CHAPTER 08 COMPLETE{/size}\n{size=36}1 DAY LEFT{/size}\n{size=28}The Last Three Days."

    return
