# Ada satu menu tambahan pengelolaan waktu: total 16 menu pada chapter ini.
# REVISION FINAL: sistem Stress, progress, dan ending.
# Keterangan menu lama tetap sebagai riwayat rancangan; kode aktif menentukan efek.

# ============================================================
# THE DEADLINERS — CHAPTER 06: THE PARTS BETWEEN
# Ren'Py 8.5.3
# H-27 sampai H-15
# 5 scene | 15 menu
# ============================================================
#
# 12 menu dialog biasa.
# 2 menu pilihan penting.
# 1 kesempatan memperoleh bukti rahasia kelima.
#
# Variabel chapter sebelumnya JANGAN dideklarasikan ulang.
# Chapter ini tidak menentukan ending.
# ============================================================


# MENU 04: pilihan teknis pertama.
# "alur_pesanan" = menyambungkan form ke ringkasan data uji.
# "validasi_error" = memperbaiki validasi dan pesan error.
default fokus_teknis_ch6 = ""


# MENU 09: bukti rahasia kelima.
# True jika laporan pengujian beserta bukti sudah disimpan.
default laporan_uji_ch6 = False


# MENU 11: pilihan teknis kedua.
# "admin" = menghubungkan daftar admin dengan data uji.
# "pembayaran" = memperbaiki alur pembayaran simulasi.
default fokus_integrasi_ch6 = ""


# ============================================================
# PEMBUKA CHAPTER 6
# ============================================================

label chapter_6:

    $ hud_visible = False
    $ days_left = 27

    scene black with fade

    centered "{size=50}CHAPTER 06{/size}\n{size=42}THE PARTS BETWEEN{/size}\n{size=34}27 DAYS LEFT{/size}"

    jump ch6_scene_01


# ============================================================
# SCENE 01 — A SMALLER NUMBER
# 27 DAYS LEFT
#
# MENU 01, 02, 03: dialog biasa.
# ============================================================

label ch6_scene_01:

    $ days_left = 27

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari berlalu sejak Luuk dan Jane menyadari waktu pengerjaan Museum Arunika tinggal sebulan."

    "Di area duduk kampus, mereka kembali bertemu setelah menyelesaikan kelas."

    "Jane membuka laptop sambil menggeser beberapa lembar catatan ke pinggir meja."

    designer "Woy."

    coder "Woy."

    designer "Udah siap?"

    coder "Siap buat apa dulu?"

    designer "Museum."

    coder "Oh. Siap."

    designer "Jawaban lo tadi mencurigakan."

    coder "Gue kira lo mau nanya tugas kuliah."

    designer "Itu juga ada."

    coder "Nah, kan."

    designer "Tapi yang ini dulu."

    coder "Oke."

    "Jane membuka daftar target yang mereka susun pada pertemuan sebelumnya."

    designer "Sekarang kita udah lewat target tiga puluh hari."

    coder "Iya."

    designer "Rasanya baru kemarin kita bilang masih sebulan."

    coder "Kalender emang nggak mau kompromi."

    designer "Tiga hari lagi kayaknya bakal cepat juga."

    coder "Jangan bikin gue mikir begitu dulu."


    # --------------------------------------------------------
    # MENU 01 — DIALOG BIASA
    # Tidak mengubah statistik atau alur utama.
    # --------------------------------------------------------

    menu:

        "Kalender ini nggak punya tombol pause, ya?":

            coder "Kalender ini nggak punya tombol pause, ya?"

            designer "Kalau ada, pasti udah dipakai semua mahasiswa."

            coder "Server-nya langsung penuh."

            designer "Dan tugasnya tetap nggak selesai."

            coder "Tolong jangan terlalu realistis."


        "Kita pakai waktunya sebaik mungkin aja.":

            coder "Kita pakai waktunya sebaik mungkin aja."

            designer "Iya."

            coder "Daripada sibuk ngitung hari terus."

            designer "Tapi tetap harus tahu sisa waktunya."

            coder "Betul."


        "Gue masih belum siap lihat angka satu digit.":

            coder "Gue masih belum siap lihat angka satu digit."

            designer "Makanya kita kerjain dari sekarang."

            coder "Iya."

            designer "Biar nanti nggak kaget sendiri."

            coder "Semoga."


    # --------------------------------------------------------
    # LANJUTAN SEMUA PILIHAN
    # --------------------------------------------------------

    "Jane membuka halaman utama Museum Arunika pada laptopnya."

    designer "Oke. Kita lihat yang masih belum nyambung."

    coder "Booking, data pesanan, admin, pembayaran simulasi."

    designer "Sama galeri."

    coder "Iya."

    designer "Kalau dilihat satu-satu, sebagian udah ada bentuknya."

    coder "Tapi kalau dipakai dari awal sampai akhir, belum semuanya beres."

    designer "Berarti kita harus lebih sering tes alurnya."

    coder "Nah."


    # --------------------------------------------------------
    # MEMBACA PILIHAN PENTING CHAPTER 5
    # --------------------------------------------------------

    if fokus_utama_ch5 == "booking":

        designer "Kemarin form udah bisa ngirim data uji ke ringkasan."

        coder "Iya. Sekarang kita harus lihat apa yang terjadi setelah itu."

    else:

        designer "Kemarin kita lebih fokus ke daftar pesanan di admin."

        coder "Iya. Tampilan tabelnya lebih rapi, tapi data dari form belum otomatis masuk."


    if fokus_lanjutan_ch5 == "pembayaran":

        designer "Halaman pembayaran simulasinya juga udah lebih jelas."

        coder "Iya. Tapi jangan disamain sama transaksi beneran."

        designer "Oke. Kita tetap sebut simulasi."

    else:

        designer "Galeri udah lebih enak dibuka di HP."

        coder "Iya, walaupun masih pakai konten contoh."

        designer "Masih nunggu bahan yang asli."


    # --------------------------------------------------------
    # LANJUTAN SEMUA KONDISI
    # --------------------------------------------------------

    "Jane menggulir daftar pekerjaan yang belum selesai."

    designer "Ada beberapa bagian yang kalau salah satu gagal, yang lain ikut nggak bisa dipakai."

    coder "Iya. Makanya sekarang kita fokus nyambungin yang penting."

    designer "Daripada nambah halaman baru terus?"

    coder "Betul."


    # --------------------------------------------------------
    # MENU 02 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Tampilan bagus nggak bisa nyelametin tombol rusak.":

            coder "Tampilan bagus nggak bisa nyelametin tombol rusak."

            designer "Iya."

            coder "Tapi tombol bagus juga butuh tampilan yang jelas."

            designer "Nah, itu baru benar."

            coder "Gue belajar dari lo."

            designer "Bagus."


        "Sekarang yang kita butuh itu alur yang utuh.":

            coder "Sekarang yang kita butuh itu alur yang utuh."

            designer "Dari orang buka website sampai selesai pesan?"

            coder "Iya. Setidaknya bisa kita demonstrasikan tanpa loncat-loncat halaman."

            designer "Oke, masuk target utama."


    # --------------------------------------------------------
    # LANJUTAN
    # --------------------------------------------------------

    "Jane menandai dua bagian paling mendesak pada daftar itu."

    designer "Eh, kalau kita selesaiin semuanya sesuai daftar, kapan waktunya ngetes?"

    coder "Harus sambil jalan."

    designer "Bukan nanti kalau semua udah beres?"

    coder "Kalau nunggu semua beres, bug-nya bisa numpuk."

    designer "Oh, iya."

    coder "Jadi selesai satu bagian, tes. Terus lanjut."

    designer "Sip."

    "Mereka mulai membagi waktu pengerjaan dan pengujian untuk beberapa hari berikutnya."


    # --------------------------------------------------------
    # MENU 03 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Gue tulis target yang bisa dibuktikan hasilnya.":

            coder "Gue tulis target yang bisa dibuktikan hasilnya."

            designer "Misalnya?"

            coder "Bukan cuma 'booking beres', tapi data yang diisi harus muncul di ringkasan."

            designer "Nah, itu jelas."

            coder "Jadi kita tahu kalau masih gagal."


        "Jangan sampai kita cuma sibuk mindahin kotak jadwal.":

            coder "Jangan sampai kita cuma sibuk mindahin kotak jadwal."

            designer "Padahal kotaknya rapi banget."

            coder "Rapi, tapi tugasnya nggak pindah sendiri."

            designer "Oke, gue tersindir."

            coder "Gue juga."


    # --------------------------------------------------------
    # PENUTUP SCENE 01
    # --------------------------------------------------------

    "Luuk membuka editor kode, sementara Jane menyiapkan daftar pengujian."

    "Mereka belum sepenuhnya khawatir, tetapi mulai memperlakukan waktu yang tersisa sebagai batas yang nyata."

    # Tekanan meningkat karena deadline semakin dekat.
    $ stress_level = min(100, stress_level + 2)

    jump ch6_scene_02


# ============================================================
# SCENE 02 — WHAT HAPPENS NEXT?
# 24 DAYS LEFT
#
# MENU 04: pilihan penting pertama.
# MENU 05, 06: dialog biasa.
# ============================================================

label ch6_scene_02:

    $ days_left = 24

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Jane datang ke kontrakan Luuk untuk menguji website."

    "Luuk sudah membuka halaman booking beserta beberapa data percobaan."

    designer "Halo."

    coder "Halo."

    designer "Hari ini tes apa?"

    coder "Gue mau fokus ke bagian yang bikin orang bisa melanjutkan pemesanan."

    designer "Maksudnya?"

    coder "Data dari form harus terbaca dengan benar, dan kalau ada yang salah harus kelihatan jelas."

    designer "Dua-duanya belum sempurna, kan?"

    coder "Iya."

    designer "Mau mulai yang mana?"


    # --------------------------------------------------------
    # MENU 04 — PILIHAN PENTING PERTAMA
    #
    # Pilihan ini mengubah:
    # - pekerjaan yang berhasil diselesaikan
    # - website_progress
    # - fokus_teknis_ch6
    # - dialog pada scene berikutnya
    # --------------------------------------------------------

    menu:

        "Perjelas sambungan data form ke ringkasan pesanan.":

            $ fokus_teknis_ch6 = "alur_pesanan"

            coder "Perjelas sambungan data form ke ringkasan pesanan."

            designer "Oke. Kita coba dari awal."

            coder "Iya. Pastikan data pengunjungnya nggak berubah pas pindah halaman."


            # Membaca pekerjaan Chapter 5.

            if fokus_utama_ch5 == "booking":

                designer "Kita udah punya alur uji dari form ke ringkasan kemarin."

                coder "Iya. Sekarang kita tambah pemeriksaan dan rapihin data yang dikirim."

            else:

                designer "Kemarin kita lebih banyak ngerjain admin."

                coder "Iya. Jadi sambungan form ke ringkasan masih harus gue siapin dulu."

                "Luuk membuat jalur uji sederhana dari form menuju halaman ringkasan."

                designer "Berarti ini belum nyambung ke tabel admin?"

                coder "Belum. Satu-satu dulu."


            # Mulai pengujian.

            "Jane mencoba memasukkan data pengunjung dengan nama berbeda."

            designer "Coba yang ini."

            "Pada percobaan pertama, data tanggal tidak ikut tampil dengan benar."

            coder "Oh, ada yang nggak kebaca."

            designer "Padahal tadi udah gue pilih."

            coder "Bentar, gue cek variabel yang dipakai."

            "Luuk memeriksa alur data dan memperbaiki bagian yang keliru."

            "Setelah diuji ulang, data contoh dari form muncul dengan lebih konsisten pada ringkasan."


            # Periksa apakah harga tiket sebelumnya sudah dibuat.

            if form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking" or fokus_utama_ch5 == "booking":

                designer "Total harga yang udah kita hitung juga kelihatan."

                coder "Iya. Kita pakai hasil hitungan yang udah ada."

            else:

                designer "Total harganya belum kita beresin, ya?"

                coder "Belum. Jadi ringkasan ini masih pakai nilai contoh buat bagian itu."

                designer "Berarti nanti wajib diselesaikan juga."

                coder "Iya."


            # Hasil pekerjaan jalur pertama.

            designer "Sekarang lebih jelas."

            coder "Iya. Tapi ini baru alur uji lokal. Belum seluruh pemesanan tersimpan secara permanen."

            designer "Oke, gue catat."

            # Progress +5, Stress -2.
            $ website_progress = min(100, website_progress + td_progress(5))
            $ stress_level = max(0, stress_level - 2)


        "Perbaiki validasi input dan pesan kesalahan dulu.":

            $ fokus_teknis_ch6 = "validasi_error"

            coder "Perbaiki validasi input dan pesan kesalahan dulu."

            designer "Biar pengunjung tahu kalau salah isi?"

            coder "Iya. Jangan cuma tombolnya diam."

            designer "Oke. Gue jadi pengunjung yang salah terus."

            coder "Tolong jangan terlalu menikmati perannya."


            # Membaca hasil pekerjaan Chapter 3 dan Chapter 4.

            if prioritas_teknis_lanjutan == "validasi" or fokus_pengerjaan_ch4 == "form_booking":

                designer "Kita udah punya sebagian validasi dari sebelumnya."

                coder "Iya. Sekarang gue rapihin pesannya dan coba kondisi lain."

            else:

                designer "Bagian validasi kita masih belum banyak."

                coder "Iya. Gue mulai dari input wajib dan tanggal kunjungan."


            # Pengujian.

            "Jane mengosongkan nama pengunjung dan mencoba memilih tanggal yang tidak sesuai."

            designer "Yang ini harusnya ditolak."

            coder "Iya."

            "Luuk menambahkan pemeriksaan input serta pesan yang lebih jelas."

            "Jane kembali mencoba beberapa data yang salah."

            designer "Nah, sekarang dijelasin salahnya di mana."

            coder "Iya. Jadi pengunjung nggak harus nebak."

            "Beberapa kesalahan input sekarang ditangani lebih baik, tetapi belum semua kasus pengujian tercakup."

            designer "Berarti validasinya udah final?"

            coder "Belum. Masih ada kondisi yang perlu dicek, apalagi pas datanya disimpan nanti."

            designer "Sip. Gue tulis."


            # Hasil pekerjaan jalur kedua.

            # Progress +4, Stress -2.
            $ website_progress = min(100, website_progress + td_progress(4))
            $ stress_level = max(0, stress_level - 2)


    # --------------------------------------------------------
    # LANJUTAN KEDUA PILIHAN
    # --------------------------------------------------------

    "Jane melihat hasil terbaru pada layar."

    designer "Lumayan. Setidaknya hari ini ada yang beneran berubah."

    coder "Iya."

    designer "Masalah yang belum ada juga makin kelihatan."

    coder "Itu juga hasil pengujian."

    designer "Kalimat yang menyenangkan sekaligus menyebalkan."

    coder "Selamat datang di dunia coding."


    # --------------------------------------------------------
    # MENU 05 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Di dunia coding, satu bug bisa punya saudara.":

            coder "Di dunia coding, satu bug bisa punya saudara."

            designer "Keluarga besar?"

            coder "Kadang reuni tiap kita nambah fitur."

            designer "Ngeri juga."

            coder "Iya."


        "Setidaknya sekarang kita tahu letak masalahnya.":

            coder "Setidaknya sekarang kita tahu letak masalahnya."

            designer "Iya. Sebelumnya cuma kelihatan nggak jalan."

            coder "Sekarang bisa ditulis langkah buat mengulang error-nya."

            designer "Oke. Gue catat pas tes berikutnya."


        "Gue pengin sekali aja tes pertama langsung berhasil.":

            coder "Gue pengin sekali aja tes pertama langsung berhasil."

            designer "Kalau semua berhasil, gue ngapain di sini?"

            coder "Ngecek desain."

            designer "Tetap ada pekerjaan, ya."

            coder "Selalu."


    # --------------------------------------------------------
    # LANJUTAN
    # --------------------------------------------------------

    "Jane menggeser laptop ke arah Luuk."

    designer "Ini tombol baliknya juga masih perlu dicek."

    coder "Oke. Tulis dulu."

    designer "Terus kalau pengunjung nutup halaman sebelum selesai?"

    coder "Itu juga perlu aturan."

    designer "Berarti daftar kita nambah lagi."

    coder "Iya. Tapi sekarang kita tahu prioritasnya."

    designer "Oke."


    # --------------------------------------------------------
    # MENU 06 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Jangan sampai kita lupa istirahat juga.":

            coder "Jangan sampai kita lupa istirahat juga."

            designer "Iya. Nanti kalau capek malah salah lagi."

            coder "Gue udah mulai salah baca nama variabel."

            designer "Berarti waktunya makan."

            coder "Setuju."


        "Kita simpan hasil hari ini sebelum pindah tugas.":

            coder "Kita simpan hasil hari ini sebelum pindah tugas."

            designer "Udah gue simpan desainnya."

            coder "Gue simpan kodenya juga."

            designer "Bagus. Jangan sampai hasil tesnya hilang."

            coder "Aman."


    # --------------------------------------------------------
    # PENUTUP SCENE 02
    # --------------------------------------------------------

    "Keduanya mengakhiri sesi setelah menuliskan pekerjaan yang belum dapat mereka selesaikan hari itu."

    "Satu bagian website kini lebih dapat diuji, meskipun masalah integrasi lain masih menunggu."

    jump ch6_scene_03


# ============================================================
# SCENE 03 — PROOF OF WORK
# 21 DAYS LEFT
#
# MENU 07, 08: dialog biasa.
# MENU 09: kesempatan bukti rahasia kelima.
# ============================================================

label ch6_scene_03:

    $ days_left = 21

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk dan Jane kembali memeriksa daftar tugas di kampus."

    "Ada beberapa hasil pengujian dari sesi sebelumnya yang ingin mereka cocokkan dengan pekerjaan masing-masing."

    designer "Luuk."

    coder "Hm?"

    designer "Gue udah coba lagi galeri di HP."

    coder "Gimana?"

    designer "Tampilan dasarnya aman, tapi ada satu teks contoh yang kepanjangan."

    coder "Masih pakai placeholder?"

    designer "Masih."

    coder "Oke. Nanti kita cek lagi kalau bahan asli masuk."

    designer "Nah, itu."

    "Jane membuka folder Museum Arunika."

    "Isinya belum menunjukkan adanya bahan koleksi baru dari Adrian."

    designer "Gue belum lihat file baru."

    coder "Iya."

    designer "Padahal sekarang tinggal tiga minggu."

    coder "Hmm."

    designer "Kita harus mulai menentukan batas nunggu bahan itu, nggak sih?"

    coder "Iya. Jangan sampai baru mikir jalan lain pas udah mepet."

    designer "Setuju."

    "Jane menulis pesan di grup."

    "Jane (grup): Adrian, kami masih butuh gambar dan deskripsi koleksi. Bisa kasih kepastian bagian yang sudah ada dan kapan bisa dikirim?"

    "Tidak ada jawaban langsung."

    "Jane meletakkan ponselnya dan membuka laporan kerja mereka sendiri."

    designer "Sambil nunggu, kita lanjut yang bisa kita tes dulu."

    coder "Iya."


    # --------------------------------------------------------
    # MENU 07 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Gue nggak mau kita berhenti cuma karena folder itu kosong.":
            $ poin_true += 1

            coder "Gue nggak mau kita berhenti cuma karena folder itu kosong."

            designer "Sama."

            coder "Tapi galeri final memang butuh bahan yang bener."

            designer "Iya. Jadi harus ada rencana cadangan."


        "Tiga minggu kedengarannya masih lama, tapi nggak juga.":

            coder "Tiga minggu kedengarannya masih lama, tapi nggak juga."

            designer "Apalagi kalau masih banyak tes."

            coder "Iya."

            designer "Makanya jangan nunggu terus."


        "Folder itu lebih konsisten daripada jadwal kuliah gue.":

            coder "Folder itu lebih konsisten daripada jadwal kuliah gue."

            designer "Konsisten apa?"

            coder "Konsisten nggak nambah isinya."

            designer "Anjir."

            coder "Gue berharap minggu depan berubah."

            designer "Sama."


    # --------------------------------------------------------
    # LANJUTAN
    # --------------------------------------------------------

    "Ponsel Jane akhirnya bergetar."

    "Adrian (grup): Masih nyari. Belum bisa pasti."

    designer "..."

    coder "Gimana?"

    designer "Masih nyari. Belum bisa pasti."

    coder "Oh."

    designer "Setidaknya sekarang dia bilang belum bisa pasti."

    coder "Iya, tapi kita masih nggak punya bahannya."

    designer "Bener."

    "Keduanya diam sebentar, lalu kembali melihat laptop masing-masing."

    # Stress meningkat karena ketidakpastian bahan Adrian.
    $ stress_level = min(100, stress_level + 5)

    "Jane membuka daftar hasil tes yang sudah dibuat."

    designer "Eh, ini daftar error kita belum lengkap."

    coder "Yang mana?"

    designer "Beberapa hasil tes cuma ditulis 'sudah dicoba'."

    coder "Iya. Itu kurang jelas."

    designer "Kalau nanti error-nya muncul lagi, kita lupa tesnya pakai apa."

    coder "Betul."

    designer "Mending kasih langkah tes sama hasilnya."

    coder "Boleh."


    # --------------------------------------------------------
    # MENU 08 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Catatan tes harus nunjukin yang berhasil dan yang gagal.":

            coder "Catatan tes harus nunjukin yang berhasil dan yang gagal."

            designer "Jadi jangan cuma centang hijau?"

            coder "Iya. Kalau gagal, kita tulis juga."

            designer "Oke."


        "Kita jangan menebak-nebak hasil yang udah pernah dites.":

            coder "Kita jangan menebak-nebak hasil yang udah pernah dites."

            designer "Iya. Nanti malah ngulang hal yang sama."

            coder "Makanya catat hasil aslinya."

            designer "Sip."


    # --------------------------------------------------------
    # PERSIAPAN PILIHAN RAHASIA
    # --------------------------------------------------------

    "Jane melihat beberapa hasil uji yang tersimpan pada laptopnya."

    designer "Kalau sekalian dicatat siapa yang ngerjain dan kapan dites, gimana?"

    coder "Boleh. Biar kalau ada error, tahu bagian siapa yang harus dicek."

    designer "Tapi jangan sampai jadi laporan panjang banget."

    coder "Nggak harus. Yang penting bisa dibaca lagi."


    # --------------------------------------------------------
    # MENU 09 — BUKTI RAHASIA KELIMA
    #
    # Bukti 1: catatan progres Chapter 2.
    # Bukti 2: arsip chat Chapter 3.
    # Bukti 3: konfirmasi target Chapter 4.
    # Bukti 4: rekap berkas Chapter 5.
    # Bukti 5: laporan pengujian Chapter 6.
    #
    # Minimal 3 dari 5 bukti untuk syarat Secret Ending.
    # Pengecekan ending belum dilakukan di chapter ini.
    # --------------------------------------------------------

    menu:

        "Simpan laporan uji fitur dengan bukti layar dan penanggung jawab.":

            coder "Simpan laporan uji fitur dengan bukti layar dan penanggung jawab."

            designer "Oke. Jadi tiap tes ada hasilnya?"

            coder "Iya. Langkahnya apa, hasilnya apa, siapa yang mengerjakan bagian itu."

            designer "Kalau yang belum berfungsi?"

            coder "Tulis gagal atau belum selesai. Jangan dibuat seolah-olah sudah jalan."

            designer "Setuju."

            "Jane membuat laporan uji sederhana dengan tanggal pemeriksaan, nama fitur, hasil tes, dan penanggung jawab pekerjaan."

            "Luuk menunjukkan hasil pengujian alur yang sedang mereka kerjakan."

            "Jane menyimpan tangkapan layar bagian yang dapat ditampilkan, termasuk masalah yang masih terlihat."

            "Mereka mencatat pekerjaan desain dan coding sesuai berkas serta hasil uji yang benar-benar tersedia."

            designer "Bagian galeri dengan konten asli belum bisa dites."

            coder "Iya. Tulis kalau bahan koleksi dari Adrian belum diterima saat pemeriksaan."

            designer "Oke. Nggak usah nebak apa yang dia kerjain di tempat lain."

            coder "Betul. Kita cuma catat yang bisa dibuktikan."

            "Jane menyimpan laporan uji dan bukti layarnya bersama dokumentasi proyek."

            designer "Nah, kalau nanti ada perubahan, kita bikin hasil tes yang baru."

            coder "Sip. Ini juga berguna buat persiapan presentasi."


            # Tambah bukti rahasia hanya satu kali.
            if not laporan_uji_ch6:
                $ jumlah_bukti_rahasia += 1

            $ laporan_uji_ch6 = True


        "Cukup perbarui daftar bug yang masih harus diperbaiki.":

            coder "Cukup perbarui daftar bug yang masih harus diperbaiki."

            designer "Oke. Biar kita cepat lanjut coding."

            "Jane menulis daftar masalah yang mereka temukan tanpa membuat laporan uji lengkap atau menyimpan bukti layar per penanggung jawab."

            designer "Yang ini masih gagal, yang ini belum dicoba."

            coder "Iya. Masukin ke prioritas berikutnya."

            designer "Siap."

            # Tidak menambah bukti rahasia.


    # --------------------------------------------------------
    # LANJUTAN KEDUA PILIHAN
    # --------------------------------------------------------

    "Jane melihat tanggal pada laptopnya."

    designer "Tinggal tiga minggu."

    coder "Iya."

    designer "Besok kita lanjut bagian yang masih nyambung ke booking."

    coder "Oke."

    "Keduanya menyimpan catatan, lalu bersiap meninggalkan kampus."

    "Belum ada bahan baru dari Adrian; tetapi Luuk dan Jane mulai lebih jelas membedakan hasil kerja yang sudah diuji dari rencana yang belum dikerjakan."

    jump ch6_scene_04


# ============================================================
# SCENE 04 — THE CONNECTION TEST
# 18 DAYS LEFT
#
# MENU 10, 12: dialog biasa.
# MENU 11: pilihan penting kedua.
# ============================================================

label ch6_scene_04:

    $ days_left = 18

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk dan Jane kembali bekerja di kontrakan Luuk."

    "Di layar terdapat beberapa halaman yang masing-masing sudah terlihat cukup rapi."

    designer "Kalau dilihat begini, kelihatannya udah banyak."

    coder "Iya."

    designer "Tapi kalau dicoba sambung satu sama lain, masih ada yang nggak jalan."

    coder "Nah. Itu yang perlu kita kerjain."

    designer "Hari ini nggak bikin halaman baru dulu?"

    coder "Kecuali diperlukan buat alur yang kita tes."

    designer "Oke."

    "Jane menjalankan beberapa langkah pengujian."

    "Ia membuka form, mencoba melanjutkan pemesanan, lalu memeriksa bagian yang seharusnya menerima hasilnya."


    # --------------------------------------------------------
    # MEMBACA PILIHAN MENU 04 CHAPTER 6
    # --------------------------------------------------------

    if fokus_teknis_ch6 == "alur_pesanan":

        designer "Data form ke ringkasan udah lebih konsisten dari kemarin."

        coder "Iya. Sekarang kita cek sistem setelah ringkasan."

    else:

        designer "Pesan error form udah lebih jelas."

        coder "Iya. Tapi sambungan data ke bagian lain belum kita beresin."


    # --------------------------------------------------------
    # MEMBACA PILIHAN CHAPTER 5
    # --------------------------------------------------------

    if fokus_utama_ch5 == "admin":

        designer "Tabel admin kita juga udah punya bentuk."

        coder "Iya, walaupun data booking belum masuk penuh."

    else:

        designer "Admin masih belum banyak kita sambungin."

        coder "Iya. Kita punya ringkasan lokal, tapi belum alur admin lengkap."


    # --------------------------------------------------------
    # LANJUTAN
    # --------------------------------------------------------

    "Luuk mencoba membuka dua halaman yang seharusnya berkaitan."

    "Hasil uji memperlihatkan masih ada data yang harus mereka isi ulang secara manual."

    designer "Ini tadi udah gue isi, kok harus diketik lagi?"

    coder "Karena sambungannya belum lengkap."

    designer "Oh."

    coder "Kalau nanti didemokan begitu, kelihatan banget belum selesai."

    designer "Iya, sih."

    # Stress naik karena integrasi masih bermasalah.
    $ stress_level = min(100, stress_level + 3)


    # --------------------------------------------------------
    # MENU 10 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Website ini kayak kelompok yang belum kompak.":

            coder "Website ini kayak kelompok yang belum kompak."

            designer "Karena halamannya jalan sendiri-sendiri?"

            coder "Nah."

            designer "Perumpamaan lo kali ini masuk akal."

            coder "Makasih."


        "Gue nggak mau pengunjung isi data dua kali.":

            coder "Gue nggak mau pengunjung isi data dua kali."

            designer "Iya. Kalau gue jadi pengunjung, pasti malas."

            coder "Berarti kita harus sambungin alurnya."

            designer "Oke."


        "Tombol pindah halaman ternyata belum cukup.":

            coder "Tombol pindah halaman ternyata belum cukup."

            designer "Karena datanya juga harus pindah?"

            coder "Iya."

            designer "Sekarang gue ngerti kenapa ini lama."

            coder "Nah."


    # --------------------------------------------------------
    # LANJUTAN
    # --------------------------------------------------------

    "Jane melihat pekerjaan yang masih tersedia."

    designer "Oke. Kalau kita punya waktu beberapa jam, prioritasnya yang mana?"

    coder "Kita bisa sambungin pembacaan data di admin, atau rapihin alur pembayaran simulasi."

    designer "Dua-duanya bakal dipakai waktu demo."

    coder "Iya. Tapi tetap satu dulu."


    # --------------------------------------------------------
    # MENU 11 — PILIHAN PENTING KEDUA
    #
    # Memengaruhi pekerjaan dan dialog Scene 5.
    # --------------------------------------------------------

    menu:

        "Hubungkan daftar admin ke data pesanan yang tersedia untuk uji.":

            $ fokus_integrasi_ch6 = "admin"

            coder "Hubungkan daftar admin ke data pesanan yang tersedia untuk uji."

            designer "Jadi nggak cuma tabel contoh lagi?"

            coder "Iya. Kita coba dengan satu set data uji yang sama."


            # Periksa ketersediaan data dari chapter lama.

            if fokus_pengerjaan_ch4 == "data_pemesanan" or fokus_utama_ch5 == "booking" or fokus_teknis_ch6 == "alur_pesanan":

                coder "Kita udah punya beberapa data uji pemesanan yang bisa dipakai."

                designer "Oke. Jadi admin bisa baca data yang sama?"

                coder "Kita buat jalur lokalnya dulu."

            else:

                coder "Kita belum punya alur penyimpanan yang rapi. Gue siapin data uji terstruktur dulu."

                designer "Berarti ini belum pesanan asli dari pengunjung?"

                coder "Belum. Masih percobaan."


            # Periksa halaman admin sebelumnya.

            if fokus_lanjutan_ch4 == "admin" or fokus_utama_ch5 == "admin":

                designer "Tabel admin yang kemarin bisa dipakai lagi."

                coder "Iya. Sekarang kita ubah cara dia menampilkan datanya."

            else:

                designer "Berarti tampilan admin juga harus kita siapkan lebih jelas."

                coder "Iya. Kita bikin versi sederhana yang bisa diuji."


            # Pengerjaan integrasi admin.

            "Luuk membuat jalur pembacaan data percobaan pada halaman admin."

            "Jane mencoba menambah dan mengubah beberapa data uji untuk melihat apakah daftar ikut diperbarui."

            designer "Nah, yang ini sekarang muncul."

            coder "Iya. Tapi belum semua bagian otomatis dan belum siap dipakai sebagai database final."

            designer "Oke. Yang penting jelas sekarang apa yang sudah jalan."

            "Daftar admin mulai dapat menampilkan data uji yang sama dengan modul percobaan, meskipun pengelolaan pesanan penuh masih tertunda."


            # Hasil pilihan admin.
            $ website_progress = min(100, website_progress + td_progress(5))
            $ stress_level = max(0, stress_level - 2)


        "Rapikan perpindahan dari ringkasan ke pembayaran simulasi.":

            $ fokus_integrasi_ch6 = "pembayaran"

            coder "Rapikan perpindahan dari ringkasan ke pembayaran simulasi."

            designer "Oke. Jadi waktu demo nggak perlu buka halamannya manual?"

            coder "Itu targetnya. Tapi tetap bukan transaksi sungguhan."


            # Periksa fitur pembayaran sebelumnya.

            if prioritas_teknis_lanjutan == "pembayaran" or fokus_lanjutan_ch5 == "pembayaran":

                designer "Demo pembayaran yang kemarin udah ada, kan?"

                coder "Iya. Kita lanjut sambungin perpindahan halamannya."

            else:

                designer "Kita belum banyak ngerjain demo pembayaran."

                coder "Iya. Gue siapkan layar konfirmasi simulasi sederhana dulu."

                designer "Oke. Jangan tambahin fitur yang nggak dibutuhkan."

                coder "Setuju."


            # Periksa ringkasan pesanan.

            if fokus_utama_ch5 == "booking" or fokus_teknis_ch6 == "alur_pesanan":

                designer "Kita bisa mulai dari ringkasan data uji yang udah ada."

                coder "Iya. Coba pindah ke simulasi dari sana."

            else:

                designer "Ringkasan dari form masih belum lengkap alurnya."

                coder "Iya. Buat sekarang kita uji perpindahannya pakai ringkasan data contoh."

                designer "Berarti belum alur dari pengunjung sampai akhir."

                coder "Belum."


            # Pengujian simulasi.

            "Jane menekan tombol melanjutkan dari ringkasan ke halaman konfirmasi simulasi."

            "Awalnya salah satu tombol masih kembali ke halaman yang tidak sesuai."

            designer "Eh, kok balik ke awal?"

            coder "Bentar. Tujuan tombolnya belum gue perbarui."

            "Luuk memperbaiki perpindahan tersebut dan mereka menguji lagi."

            designer "Nah, sekarang urutannya masuk akal."

            coder "Iya. Tapi data pembayaran asli, penyimpanan, dan seluruh kondisi gagal masih belum ada."

            designer "Oke. Ini memang khusus simulasi."

            "Urutan halaman ringkasan dan konfirmasi simulasi menjadi lebih dapat didemonstrasikan menggunakan data uji."


            # Hasil pilihan pembayaran.
            $ website_progress = min(100, website_progress + td_progress(4))
            $ stress_level = max(0, stress_level - 2)


    # --------------------------------------------------------
    # LANJUTAN SEMUA PILIHAN
    # --------------------------------------------------------

    "Jane menyandarkan badan ke kursi setelah sesi pengujian."

    designer "Lumayan melelahkan."

    coder "Iya."

    designer "Padahal kita nggak bikin banyak halaman baru."

    coder "Karena kita benerin cara halaman yang ada saling bekerja."

    designer "Iya juga."


    # --------------------------------------------------------
    # MENU 12 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Yang susah bukan bikin tombolnya, tapi apa yang terjadi setelah diklik.":

            coder "Yang susah bukan bikin tombolnya, tapi apa yang terjadi setelah diklik."

            designer "Sekarang kalimat itu terasa banget."

            coder "Iya."

            designer "Setidaknya hari ini beberapa tombol punya tujuan lebih jelas."


        "Gue mau makan dulu sebelum ngetes ulang.":

            coder "Gue mau makan dulu sebelum ngetes ulang."

            designer "Setuju."

            coder "Kalau lanjut sekarang, gue takut salah baca lagi."

            designer "Oke. Kita istirahat sebentar."


        "Kita tandai yang masih belum siap biar nggak ketuker.":

            coder "Kita tandai yang masih belum siap biar nggak ketuker."

            designer "Oke. Jadi pas demo latihan nanti nggak salah klaim."

            coder "Iya. Yang belum selesai ya belum selesai."

            designer "Sip."


    # --------------------------------------------------------
    # PENUTUP SCENE 04
    # --------------------------------------------------------

    "Luuk dan Jane menyimpan perubahan, lalu memperbarui daftar pengujian mereka."

    "Website menjadi lebih terhubung daripada sebelumnya, tetapi belum seluruh fungsi menyatu dan belum semua masalah selesai."

    # MENU TAMBAHAN — pengelolaan waktu dan Stress (berpengaruh).
    "Ada satu sesi kecil sebelum mereka pulang."
    designer "Kita lanjut sedikit atau istirahat dulu?"
    menu:
        "Makan dulu, baru lanjut besok.":
            coder "Makan dulu, baru lanjut besok."
            "Mereka membeli makan, membicarakan tugas kuliah lain, dan mengakhiri pekerjaan hari itu."
            $ stress_level = max(0, stress_level - 3)

        "Kita perbaiki cara halaman menampilkan status kosong dan gagal." if stress_level < 65:
            coder "Kita perbaiki cara halaman menampilkan status kosong dan gagal."
            "Luuk memperbaiki pesan data kosong dan Jane mengulang dua skenario gagal dengan data contoh."
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

        "Kita tambahkan beberapa perubahan status tanpa mengulang skenario gagal.":
            coder "Kita tambahkan beberapa perubahan status tanpa mengulang skenario gagal."
            designer "Tapi kalau nggak dites ulang, masih ada risikonya."
            "Luuk menambah tampilan status, tetapi beberapa skenario gagal belum sempat diperiksa."
            $ website_progress = min(100, website_progress + td_progress(4))
            $ poin_bad += 2
            $ risiko_demo += 2
            $ stress_level = min(100, stress_level + 6)

    jump ch6_scene_05


# ============================================================
# SCENE 05 — FIFTEEN DAYS LEFT
# 15 DAYS LEFT
#
# MENU 13, 14, 15: dialog biasa.
# ============================================================

label ch6_scene_05:

    $ days_left = 15

    scene black with dissolve

    $ hud_visible = True

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    "Tiga hari kemudian, Luuk dan Jane bertemu lagi di area duduk kampus."

    "Udara sore terasa lebih tenang daripada suasana pekerjaan di laptop mereka."

    "Di hadapan keduanya terdapat daftar pengujian dan target yang harus diselesaikan sebelum presentasi."

    designer "Woy."

    coder "Woy."

    designer "Udah lihat daftar terbaru?"

    coder "Udah."

    designer "Gimana menurut lo?"

    coder "Lebih jelas daripada bulan lalu."

    designer "Iya, tapi masih banyak yang merah."

    coder "Itu yang bikin kita tahu harus mulai dari mana."

    designer "Hmm."


    # --------------------------------------------------------
    # EVALUASI PILIHAN PENTING CHAPTER 6
    # --------------------------------------------------------

    if fokus_teknis_ch6 == "alur_pesanan":

        designer "Sambungan form ke ringkasan sekarang udah lebih konsisten."

        coder "Iya. Tapi belum berarti seluruh booking selesai."

        designer "Masih ada penyimpanan permanen sama integrasi lainnya."

        coder "Betul."

    else:

        designer "Pesan kesalahan di form sekarang lebih jelas."

        coder "Iya. Tapi sambungan data ke halaman lain tetap harus dikerjain."

        designer "Oke."


    if fokus_integrasi_ch6 == "admin":

        designer "Data uji di admin juga mulai bisa dibaca dari modul yang sama."

        coder "Iya. Masih ada bagian manual dan masih perlu pengujian."

    else:

        designer "Perpindahan dari ringkasan ke pembayaran simulasi udah lebih enak."

        coder "Iya. Tapi itu baru alur demo, bukan pembayaran asli."


    # --------------------------------------------------------
    # EVALUASI PILIHAN CHAPTER 5
    # --------------------------------------------------------

    if fokus_lanjutan_ch5 == "galeri":

        designer "Galeri responsif dari kemarin masih cukup rapi."

        coder "Iya. Tapi belum diuji dengan gambar koleksi aslinya."

    else:

        designer "Galeri masih harus kita tes lebih jauh nanti."

        coder "Iya, terutama kalau bahan asli udah masuk."


    # --------------------------------------------------------
    # MASALAH ADRIAN MASIH BERLANJUT
    # --------------------------------------------------------

    designer "Ngomong-ngomong bahan asli..."

    coder "Belum ada?"

    designer "Belum."

    coder "Hmm."

    designer "Minggu ini harus ada keputusan kalau tetap nggak dikirim."

    coder "Iya. Kita nggak bisa terus menunggu tanpa batas."

    designer "Kalau perlu cari jalan lain buat konten, kita harus tahu dari sekarang."

    coder "Setuju. Tapi jangan menganggap tugas Adrian sudah selesai kalau memang belum."

    designer "Iya."


    # --------------------------------------------------------
    # MEMBACA BUKTI DARI CHAPTER SEBELUMNYA
    # --------------------------------------------------------

    if laporan_uji_ch6:

        designer "Untung hasil tes yang kemarin ada bukti layarnya."

        coder "Iya. Jadi kita bisa lihat apa yang benar-benar sudah berfungsi."

        designer "Dan bagian mana yang belum bisa diuji karena bahan belum masuk."

    elif rekap_pengumpulan_ch5:

        designer "Rekap file yang kemarin juga bisa kita cek lagi."

        coder "Iya. Kalau ada bahan baru, pasti kelihatan tanggal masuknya."

    else:

        designer "Daftar pekerjaan kita harus tetap diperbarui."

        coder "Iya. Jangan sampai ada yang dianggap selesai cuma karena pernah dibahas."


    # --------------------------------------------------------
    # DEADLINE TINGGAL 15 HARI
    # --------------------------------------------------------

    "Jane menatap kalender di layar laptop."

    designer "Luuk."

    coder "Hm?"

    designer "Lima belas hari."

    coder "Apa?"

    designer "Tinggal lima belas hari lagi."

    coder "..."

    designer "Cepet banget, ya."

    coder "Iya."

    "Luuk memperhatikan daftar pekerjaannya sekali lagi."

    "Ia mengingat berbagai masalah kecil yang muncul setiap kali website diuji."

    "Dulu ia bisa mengatakan bahwa masih banyak waktu. Sekarang ia tidak lagi yakin kalimat itu cukup."

    # Stress naik karena deadline semakin dekat.
    $ stress_level = min(100, stress_level + 4)

    designer "Lo lagi mikir apa?"

    coder "Gue lagi nyoba nentuin mana yang wajib kita selesain sebelum presentasi."

    designer "Bukan semuanya sekaligus?"

    coder "Kalau bisa semua, bagus. Tapi yang penting jangan sampai alur utamanya gagal."

    designer "Iya."

    coder "Kita juga harus nyiapin waktu buat tes ulang."

    designer "Setuju."


    # --------------------------------------------------------
    # MENU 13 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Gue nggak mau presentasi sambil berharap tombolnya baik hati.":

            coder "Gue nggak mau presentasi sambil berharap tombolnya baik hati."

            designer "Tombolnya punya perasaan?"

            coder "Kalau punya, semoga dia suka sama kita."

            designer "Mending dites daripada berharap."

            coder "Nah, itu."


        "Kita harus punya alur demo yang bisa diulang tanpa kejutan.":

            coder "Kita harus punya alur demo yang bisa diulang tanpa kejutan."

            designer "Iya. Dari beranda sampai hasil pemesanan."

            coder "Yang belum berfungsi harus kita beresin dulu atau tandai jelas."

            designer "Oke."


        "Dua minggu lagi rasanya pendek banget.":

            coder "Dua minggu lagi rasanya pendek banget."

            designer "Masih sedikit lebih dari dua minggu."

            coder "Iya. Tapi pekerjaannya nggak sedikit."

            designer "Makanya kita atur dari sekarang."

            coder "Setuju."


    # --------------------------------------------------------
    # LANJUTAN
    # --------------------------------------------------------

    "Jane menyusun ulang daftar target berdasarkan fungsi yang benar-benar diperlukan untuk demonstrasi."

    designer "Kita mulai dari alur booking yang paling penting, terus admin, sama konten koleksi."

    coder "Iya. Pembayaran tetap sesuai kebutuhan simulasi."

    designer "Berarti nggak nambah fitur aneh-aneh dulu."

    coder "Jangan."

    designer "Padahal gue sempat kepikiran animasi kecil buat galeri."

    coder "Boleh nanti kalau yang wajib udah aman."

    designer "Oke, gue simpan idenya."

    coder "Makasih."

    designer "Kenapa makasih?"

    coder "Karena nggak langsung nyuruh gue coding animasi sekarang."

    designer "Anjir."


    # --------------------------------------------------------
    # MENU 14 — DIALOG BIASA
    # --------------------------------------------------------

    menu:

        "Animasi bisa nunggu, tombol booking jangan.":

            coder "Animasi bisa nunggu, tombol booking jangan."

            designer "Iya, iya."

            coder "Kalau tombol gagal, animasinya jadi hiburan doang."

            designer "Gue ngerti."


        "Kalau fitur wajib udah stabil, baru kita poles lagi.":

            coder "Kalau fitur wajib udah stabil, baru kita poles lagi."

            designer "Setuju."

            coder "Jadi bukan nggak boleh bagus, tapi urutannya jelas."

            designer "Nah, itu."


        "Gue mulai rindu waktu kita cuma debat ukuran tombol.":

            coder "Gue mulai rindu waktu kita cuma debat ukuran tombol."

            designer "Dua pixel?"

            coder "Jangan diingetin."

            designer "Itu masa-masa indah."

            coder "Sekarang debatnya data yang nggak mau pindah halaman."

            designer "Lebih menyeramkan."


    # --------------------------------------------------------
    # PENUTUP CHAPTER 6
    # --------------------------------------------------------

    "Sebelum pulang, Jane menunjukkan jadwal dua minggu ke depan."

    designer "Besok kita mulai tes alur utama lagi."

    coder "Oke."

    designer "Terus kita lihat langkah buat bahan koleksi."

    coder "Iya. Jangan sampai cuma nunggu jawaban yang sama."

    designer "Sip."

    "Jane menutup laptop, tetapi masih memperhatikan Luuk yang sedang memeriksa daftar kerja."

    designer "Luuk."

    coder "Apa?"

    designer "Kalau ada bagian yang berat, bilang aja. Jangan diam terus."

    coder "Iya."

    designer "Kita ngerjainnya berdua."

    coder "Gue tahu."

    designer "Oke."

    "Luuk akhirnya menutup laptopnya."

    "Mereka tidak bertengkar, dan tidak ada janji bahwa semuanya pasti akan baik-baik saja."

    "Yang ada hanyalah kesepakatan untuk kembali bekerja besok, dengan daftar tugas yang semakin jelas dan waktu yang semakin sedikit."


    # --------------------------------------------------------
    # MENU 15 — DIALOG BIASA PENUTUP
    # --------------------------------------------------------

    menu:

        "Besok kita mulai dari tes booking yang paling penting.":

            coder "Besok kita mulai dari tes booking yang paling penting."

            designer "Oke. Gue siapin skenario pengunjungnya."

            coder "Gue siapin kodenya."

            designer "Sip."


        "Besok kita rapihin prioritas dan cek bahan koleksi lagi.":

            coder "Besok kita rapihin prioritas dan cek bahan koleksi lagi."

            designer "Oke. Jangan sampai bagian itu terlupakan."

            coder "Iya. Kita tetap lanjut yang bisa dikerjain."

            designer "Siap."


    # --------------------------------------------------------
    # PENUTUP SEMUA PILIHAN
    # --------------------------------------------------------

    "Mereka meninggalkan area kampus ketika hari mulai sore."

    "Museum Arunika sudah memiliki banyak halaman dan beberapa fungsi yang bisa diuji, tetapi belum menjadi sistem yang sepenuhnya siap."

    "Sambungan antara booking, data pesanan, admin, dan pembayaran simulasi masih perlu diperiksa dan diselesaikan sesuai pekerjaan yang dipilih."

    "Konten koleksi yang ditunggu dari Adrian belum juga tersedia."

    "Luuk dan Jane tetap bekerja sama, tetapi kini sadar bahwa dua minggu terakhir akan menentukan apakah website mereka benar-benar dapat dipresentasikan."

    "15 DAYS LEFT."

    $ hud_visible = False

    scene black with fade

    centered "{size=50}CHAPTER 06 COMPLETE{/size}\n{size=36}15 DAYS LEFT{/size}\n{size=28}The Parts Between."

    jump chapter_7