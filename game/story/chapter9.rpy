# ============================================================
# CHAPTER 09 — THE PRESENTATION | H-0
# Membaca pilihan lama, bukan memberi pemain menu pemilihan ending.
# Hanya persiapan terakhir yang menambah progress atau mengurangi Stress.
# ============================================================
label chapter_9:
    $ hud_visible = False
    $ days_left = 0
    scene black with fade
    centered "{size=50}CHAPTER 09{/size}\n{size=42}THE PRESENTATION{/size}\n{size=34}DEADLINE DAY{/size}"
    jump ch9_scene_01

label ch9_scene_01:
    scene black with dissolve
    $ hud_visible = True
    show coder at char_center
    "Pagi hari. Luuk terbangun beberapa jam sebelum jadwal presentasi online."
    "Untuk pertama kalinya sejak proyek Museum Arunika dimulai, angka pada kalender tidak lagi menyisakan hari."
    "Ia membuka laptop di kamar kosnya. Notifikasi dari Jane muncul."
    "Jane (chat): Woy. Udah bangun?"
    "Luuk (chat): Udah."
    "Jane (chat): Cek mic sama koneksi dulu. Gue dari kos juga."
    "Luuk (chat): Oke."
    "Jane (chat): Jangan buka game sekarang."
    "Luuk (chat): Gue bahkan belum buka apa-apa."
    "Jane (chat): Bagus."
    "Luuk memasang headset dan membuka versi terakhir Museum Arunika."
    if keputusan_build_ch8 == "bekukan":
        "Ia mengambil versi yang telah disimpan dan diuji bersama Jane pada hari sebelumnya."
        coder "Yang ini. Jangan salah folder."
    else:
        "Ia memeriksa versi dengan tambalan terakhir, lalu memastikan salinan cadangan lama masih dapat dibuka."
        coder "Oke. Yang baru sama cadangan, dua-duanya ada."
    "Jane bergabung dalam panggilan suara untuk pemeriksaan akhir. Mereka tetap berada di kamar kos masing-masing."
    designer "Suara gue masuk?"
    coder "Masuk."
    designer "Layar nanti lo yang share, ya."
    coder "Iya. Lo jelasin alurnya."
    designer "Oke. Sebelum itu, coba kita selesain pemeriksaan yang kemarin belum sempat."
    $ stress_level = min(100, stress_level + 3)

    menu:
        "Sarapan dan minum dulu, biar bisa mikir.":
            coder "Sarapan dan minum dulu, biar bisa mikir."
            designer "Oke. Gue tunggu. Jangan lama-lama."
            "Luuk menyisihkan beberapa menit untuk makan dan menyiapkan air minum."
            $ stress_level = max(0, stress_level - 6)
        "Kita cek catatan demo dulu, pelan-pelan." if stress_level < 65:
            coder "Kita cek catatan demo dulu, pelan-pelan."
            designer "Sip. Coba urutkan dari beranda."
            "Mereka menyusun urutan berbagi layar dan data percobaan sebelum menyentuh kode."
            $ stress_level = max(0, stress_level - 2)
        "Jane, bantu gue baca daftar tes satu per satu." if stress_level >= 65:
            coder "Jane, bantu gue baca daftar tes satu per satu."
            designer "Oke. Gue bacain. Lo fokus satu langkah dulu."
            "Jane memandu pemeriksaan singkat dari catatannya."
            $ stress_level = max(0, stress_level - 6)
        "Langsung aja, gue pengin cepat selesai.":
            coder "Langsung aja, gue pengin cepat selesai."
            designer "Oke. Tapi jangan sampai salah buka versi."
            "Luuk bergegas membuka beberapa jendela sekaligus dan melewatkan persiapan catatan pribadi."
            $ stress_level = min(100, stress_level + 4)

    jump ch9_scene_02

label ch9_scene_02:
    scene black with dissolve
    show coder at char_center
    "Mereka memanfaatkan sisa waktu sebelum jadwal meeting untuk menuntaskan versi demonstrasi."
    designer "Jangan bikin fitur baru. Yang wajib aja."
    coder "Iya. Kita pakai yang udah dikerjain selama ini."
    if not (form_tiket_dikerjakan_dulu or uji_booking_dulu or fokus_pengerjaan_ch4 == "form_booking" or fokus_utama_ch5 == "booking" or prioritas_integrasi_ch7 == "booking"):
        "Luuk melengkapi perhitungan harga tiket pada form dan Jane mencocokkan total menggunakan beberapa jumlah tiket."
        designer "Akhirnya totalnya nggak pakai angka contoh lagi."
        coder "Iya. Sekarang tes ringkasannya."
    else:
        "Jane mencocokkan perhitungan harga yang sudah dibuat dengan nilai pada ringkasan."
    if pemulihan_ch8 == "jalur_inti":
        "Mereka memakai kembali alur inti yang telah berhasil dipulihkan di laptop Jane."
        coder "Yang ini fondasinya. Kita sambung bagian yang belum ikut."
    else:
        "Luuk memeriksa sambungan yang diperbaiki pada H-3 dan memilih versi yang dapat dijalankan di kedua laptop."
        coder "Kita cek hasilnya dari awal, bukan buka halaman satu-satu."
    "Luuk menyelesaikan pengaturan data uji lokal yang dapat dibaca oleh form dan daftar admin."
    "Ia memastikan status simulasi pembayaran tidak diklaim sebagai transaksi sungguhan. Jane memeriksa label serta tombol yang digunakan dalam demonstrasi."
    if keputusan_konten_ch8 == "contoh":
        "Jane memastikan galeri masih menyebut gambar dan deskripsi sebagai konten contoh."
    else:
        "Jane menyiapkan keterangan bahwa konten koleksi belum tersedia, tanpa menampilkan bahan yang belum terverifikasi."
    designer "Bahan Adrian tetap nggak ada. Kita jelasin batasan itu."
    coder "Iya. Jangan bilang koleksi final."
    "Perbaikan tersebut menambah bagian yang dapat didemonstrasikan, tetapi belum menjamin seluruh jalur stabil."
    $ website_progress = min(100, website_progress + td_progress(8))
    "Mereka mengulang tes pada versi yang akan dibawa ke meeting."
    if risiko_demo <= 2:
        "Alur booking, ringkasan, daftar pesanan uji, serta konfirmasi simulasi dapat diulang dengan hasil yang sesuai pada skenario yang disiapkan."
        $ website_stabil = True
        designer "Hasilnya sama di laptop gue."
        coder "Oke. Simpan versi ini."
        $ stress_level = max(0, stress_level - 3)
    else:
        "Beberapa skenario masih memperlihatkan ketidaksesuaian data atau status. Waktu yang tersisa tidak cukup untuk mengulang semua pengujian yang pernah dilewatkan."
        $ website_stabil = False
        designer "Yang belum konsisten jangan dianggap lolos."
        coder "Iya. Kita punya jalur dasar dan cadangan, tapi belum stabil semuanya."
        $ stress_level = min(100, stress_level + 4)
    "Notifikasi pengingat meeting muncul."
    designer "Udah waktunya."
    coder "Iya."
    "Tidak ada lagi waktu untuk menambah fitur."
    # Keputusan final otomatis, tepat sebelum presentasi dimulai.
    $ hasil_ending, alasan_bad = td_tentukan_ending(website_progress, jumlah_bukti_rahasia, website_stabil, poin_good, poin_bad, poin_true)
    $ adrian_hadir = hasil_ending in ("good", "bad")
    jump ch9_scene_03

label ch9_scene_03:
    scene black with fade
    "Luuk memasuki ruang meeting online dari kamar kosnya."
    "Jane sudah berada di daftar peserta. Dosen bergabung tidak lama kemudian."
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    "Tampilan meeting memperlihatkan dua kamera dari kamar yang berbeda."
    designer "Pagi, Pak."
    coder "Selamat pagi, Pak."
    dosen "Selamat pagi. Kelompok Museum Arunika, ya?"
    coder "Betul, Pak."
    dosen "Anggota kelompoknya tiga orang?"
    if adrian_hadir:
        "Nama Adrian muncul pada daftar peserta. Ia masuk ke meeting dari kamarnya sendiri."
        anomaly "Selamat pagi, Pak. Maaf, baru masuk."
        dosen "Baik. Semua sudah hadir. Kita bisa mulai."
        "Jane melirik daftar peserta sebelum memulai penjelasan."
        jump ch9_scene_04
    else:
        "Daftar peserta tetap hanya berisi Luuk, Jane, dan dosen."
        designer "Betul, Pak. Adrian belum masuk."
        dosen "Kalian sudah menghubunginya?"
        designer "Sudah, Pak. Kami sudah mengingatkan jadwal presentasi melalui grup."
        "Dosen memberikan waktu beberapa menit. Tidak ada nama baru yang muncul."
        dosen "Bagaimana kontribusi anggota yang tidak hadir ini?"
        if hasil_ending == "secret":
            designer "Izin, Pak. Kami punya dokumentasi pembagian tugas dan hasil pekerjaan yang dapat kami tunjukkan."
            coder "Kami juga sudah menyiapkan website yang bisa didemonstrasikan, Pak."
            jump ch9_secret_review
        else:
            coder "Bagian konten koleksi belum kami terima, Pak."
            designer "Kami siap menjelaskan bagian yang kami kerjakan."
            dosen "Saya mengerti. Namun ketentuan presentasi kelompok ini mewajibkan kehadiran seluruh anggota."
            designer "Apakah kami boleh tetap menunjukkan hasilnya, Pak?"
            dosen "Presentasi kelompok tidak dapat saya lanjutkan hari ini. Saya tetap akan mempertimbangkan pekerjaan individu yang sudah dikumpulkan sesuai ketentuan penilaian."
            "Luuk membuka mulut, tetapi tidak langsung menemukan jawaban."
            coder "Baik, Pak."
            designer "Baik, Pak. Terima kasih."
            "Mereka menutup meeting tanpa kesempatan mendemonstrasikan website."
            jump ch9_scene_05

label ch9_secret_review:
    "Jane membagikan dokumentasi yang benar-benar disimpan sepanjang proyek, bukan bukti yang baru dibuat pada hari presentasi."
    if catatan_progres_dibuat:
        designer "Ini catatan progres mingguan dan pekerjaan yang tercatat, Pak."
    if arsip_chat_kelompok_tersimpan:
        designer "Ini arsip percakapan pembagian tugas dalam grup."
    if konfirmasi_target_adrian:
        designer "Ini konfirmasi target pengumpulan yang disetujui Adrian."
    if rekap_pengumpulan_ch5:
        coder "Ini rekap berkas per anggota berdasarkan folder dan tanggal pemeriksaan."
    if laporan_uji_ch6:
        coder "Ini laporan pengujian dengan tangkapan layar dan penanggung jawab fitur."
    dosen "Baik. Saya akan memeriksa dokumentasi ini."
    "Beberapa saat berlalu. Luuk dan Jane menunggu tanpa menyela."
    dosen "Dari dokumen yang kalian tunjukkan, pekerjaan kalian dapat dipisahkan dari kontribusi anggota yang tidak hadir."
    dosen "Saya beri kesempatan kalian berdua mendemonstrasikan pekerjaan sebagai duo. Penilaiannya akan saya pisahkan."
    designer "Terima kasih, Pak."
    coder "Terima kasih, Pak."
    jump ch9_scene_04

label ch9_scene_04:
    "Jane memulai penjelasan dan Luuk membagikan layar laptopnya."
    designer "Museum Arunika dirancang agar pengunjung dapat melihat informasi museum, membuka galeri, dan mencoba alur pemesanan tiket."
    coder "Untuk transaksi, sistem ini menggunakan simulasi. Tidak ada pembayaran uang sungguhan."
    if keputusan_konten_ch8 == "contoh":
        designer "Konten yang tampil di galeri masih berupa contoh, Pak. Bahan koleksi final belum tersedia."
    else:
        designer "Kami menahan bagian koleksi yang belum mempunyai bahan terverifikasi."
    dosen "Baik. Tolong tunjukkan fungsi pemesanannya."
    if hasil_ending == "bad" and alasan_bad == "progress":
        "Luuk membuka form dan mencoba melanjutkan ke ringkasan pesanan."
        "Bagian yang belum selesai tidak dapat menerima data secara konsisten. Beberapa fungsi masih memakai data contoh atau memerlukan langkah manual."
        dosen "Apakah seluruh alur pemesanan dan pengelolaan data sudah selesai?"
        coder "Belum, Pak. Ada sambungan yang belum berhasil kami tuntaskan."
        designer "Kami bisa menunjukkan desain dan bagian yang sudah berjalan, tetapi alur lengkapnya belum siap."
        dosen "Baik. Saya catat bahwa fungsi utama belum memenuhi target."
    elif hasil_ending == "bad":
        "Beranda dan form dapat dibuka. Luuk memulai demonstrasi dengan data percobaan."
        "Ketika diminta mengulang langkah dengan data yang berbeda, Luuk kebingungan menentukan versi dan langkah pemulihan yang tepat."
        if not website_stabil:
            "Salah satu sambungan yang sebelumnya belum diuji ulang menampilkan data lama. Perbaikan cepat yang tersimpan tidak menyelesaikan masalah tersebut."
        else:
            "Alur uji sebelumnya berhasil, tetapi pergantian skenario dan persiapan demonstrasi yang tidak lengkap membuat Luuk tidak dapat mengulang hasil itu secara konsisten di hadapan dosen."
        if stress_level >= 65:
            "Luuk membaca catatan berkali-kali. Semakin ia terburu-buru, semakin sulit ia mengikuti langkah yang telah disiapkan."
            designer "Luuk, coba versi cadangan."
        else:
            designer "Coba ulang dari beranda. Kita cek data yang tadi."
        coder "Sebentar, Pak. Mohon maaf."
        "Mereka mencoba memulihkan demonstrasi, tetapi waktu presentasi yang diberikan telah habis."
        dosen "Saya melihat sebagian besar pekerjaan sudah dibuat. Namun, fungsi yang diperagakan belum dapat dibuktikan bekerja secara konsisten dalam demonstrasi ini."
        coder "Baik, Pak."
    else:
        if hasil_ending == "good" and not website_stabil:
            "Luuk memilih jalur inti dari salinan cadangan yang dapat dijalankan dan menjelaskan skenario yang belum lolos tes."
            coder "Kami menggunakan alur yang sudah dapat diuji, Pak. Ada skenario tambahan yang masih perlu perbaikan."
        "Luuk memasukkan data percobaan pada form. Harga dan ringkasan ditampilkan, kemudian ia menunjukkan daftar pesanan uji serta konfirmasi simulasi."
        "Jane menjelaskan alasan penempatan tombol, pesan kesalahan, dan urutan langkah bagi pengunjung."
        dosen "Coba ganti jumlah tiketnya."
        "Luuk mengulang langkah dengan jumlah yang berbeda. Nilai pada jalur demo berubah sesuai masukan."
        dosen "Baik. Saya bisa melihat fungsi utama serta hubungan desain dengan implementasinya."
        if hasil_ending == "good":
            dosen "Adrian, ada tambahan?"
            anomaly "Untuk bagian konten masih belum lengkap, Pak."
            dosen "Baik. Saya catat keterbatasannya."
        else:
            dosen "Untuk dokumentasi kontribusi, saya akan mempertimbangkannya dalam penilaian individu kalian."
            designer "Baik, Pak."
        "Mereka menyelesaikan demonstrasi dan menjawab pertanyaan terakhir berdasarkan pekerjaan yang benar-benar mereka lakukan."
    dosen "Terima kasih. Hasil penilaian akan diumumkan setelah pemeriksaan tugas."
    coder "Terima kasih, Pak."
    designer "Terima kasih, Pak."
    if adrian_hadir:
        anomaly "Terima kasih, Pak."
    "Meeting berakhir."
    jump ch9_scene_05

label ch9_scene_05:
    scene black with dissolve
    show coder at char_center
    "Layar meeting tertutup. Luuk masih duduk di depan laptopnya."
    "Panggilan dari Jane masuk beberapa saat kemudian."
    designer "Woy."
    coder "Woy."
    if hasil_ending == "true":
        designer "Gue masih nggak percaya kita nggak bisa presentasi."
        coder "Iya. Gue juga."
        designer "Padahal kita udah bawa semuanya."
        coder "Hmm."
    elif hasil_ending == "bad":
        designer "Tadi berat banget, ya."
        coder "Iya. Gue pengin hasilnya beda."
        designer "Gue juga. Kita tunggu hasilnya dulu."
    else:
        designer "Akhirnya selesai juga."
        coder "Iya. Tadi gue sempet tegang pas ditanya."
        designer "Kelihatan. Tapi lo masih bisa jawab."
    menu:
        "Gue mau matiin laptop sebentar.":
            coder "Gue mau matiin laptop sebentar."
            designer "Iya. Udah cukup buat hari ini."
        "Makasih udah bareng gue sampai sekarang.":
            coder "Makasih udah bareng gue sampai sekarang."
            designer "Sama-sama. Kita emang ngerjainnya bareng."
    "Untuk pertama kalinya selama tiga bulan terakhir, mereka tidak membuat jadwal pengerjaan baru."
    "Yang tersisa sekarang adalah hasil penilaian."

    $ hud_visible = False
    scene black with fade
    centered "{size=50}CHAPTER 09 COMPLETE{/size}\n{size=36}0 DAYS LEFT{/size}"
    
    jump chapter_10
