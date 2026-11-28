# ============================================================
# CHAPTER 10 — AFTER THE DEADLINE
# ============================================================
label chapter_10:
    $ hud_visible = False
    $ days_left = 0
    scene black with fade
    stop music fadeout 2.0
    centered "{size=50}CHAPTER 10{/size}\n{size=42}AFTER THE DEADLINE{/size}"
    "Beberapa hari setelah presentasi, hasil penilaian Museum Arunika diumumkan."
    if hasil_ending == "secret":
        jump td_ending_secret
    elif hasil_ending == "good":
        jump td_ending_good
    elif hasil_ending == "true":
        jump td_ending_true
    else:
        jump td_ending_bad

label td_ending_good:
    scene kantin with dissolve
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    "Luuk dan Jane kembali duduk di tempat makan kampus. Tidak ada laptop yang terbuka di meja."
    designer "Nilainya udah keluar."
    coder "Serius?"
    designer "Lihat sendiri."
    "Luuk membuka halaman penilaian pada ponselnya."
    centered "{size=40}HASIL PENILAIAN MUSEUM ARUNIKA{/size}\n\nLuuk — A\nJane — A\nAdrian — A"
    coder "A."
    designer "Iya!"
    coder "Anjir, akhirnya."
    designer "Tiga bulan, Luuk. TIGA BULAN."
    coder "Gue tahu. Gue ada di sana."
    "Keduanya tertawa. Jane kembali membaca hasil penilaian."
    designer "Eh. Adrian juga A."
    coder "Iya."
    designer "Padahal sampai terakhir kita nggak dapat bahan dari dia."
    coder "Dosen menilai hasil kelompoknya."
    designer "Gue seneng kita berhasil. Tapi bagian itu... ya, agak kesel."
    coder "Sama."
    "Sebuah pesan masuk ke grup."
    "Adrian (grup): Wah, A. Makasih ya semuanya."
    "Jane membaca pesan itu, lalu meletakkan ponselnya."
    designer "Hmm."
    coder "Udahlah. Kita tahu siapa yang ngerjain apa."
    designer "Iya. Jangan sampai semester depan kita ulang pola yang sama."
    menu:
        "Yang penting kita akhirnya berhasil.":
            coder "Yang penting kita akhirnya berhasil."
            designer "Iya. Dan kita belajar banyak."
        "Lain kali pembagian tugasnya harus lebih tegas.":
            coder "Lain kali pembagian tugasnya harus lebih tegas."
            designer "Setuju. Dari awal."
    "Mereka membeli es krim setelah makan. Untuk sekali ini, tidak ada daftar bug yang harus dibawa pulang."
    designer "Malam ini Marvel?"
    coder "Boleh. Sekarang nggak ada museum yang ngejar gue."
    designer "Satu match?"
    coder "Jangan mulai."
    "Jane tertawa."
    "Museum Arunika berhasil dipresentasikan. Mereka mendapatkan hasil yang mereka inginkan, tetapi tidak semua orang mendapatkan nilai itu dengan usaha yang sama."
    scene black with fade
    centered "{size=52}GOOD ENDING{/size}\n{size=30}A shared victory.{/size}"
    jump td_final_credits

label td_ending_bad:
    scene kantin with dissolve
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    "Luuk menerima pesan dari Jane tentang nilai. Mereka bertemu di kampus setelah kelas."
    designer "Lo udah lihat?"
    coder "Belum."
    "Luuk membuka hasil penilaian."
    centered "{size=40}HASIL PENILAIAN MUSEUM ARUNIKA{/size}\n\nLuuk — C\nJane — C\nAdrian — C"
    "Tidak ada yang langsung berbicara."
    coder "C."
    designer "Iya."
    if alasan_bad == "progress":
        coder "Kita nggak sempat nyelesain fungsi yang diminta."
        designer "Iya. Ada bagian yang kelihatan jadi, tapi belum siap dipakai."
        coder "Harusnya beberapa pekerjaan kita mulai lebih awal."
        designer "Dan kita harus lebih jujur sama jadwal sendiri."
    else:
        coder "Padahal udah banyak yang kita bikin."
        designer "Iya. Tapi pas demo, kita nggak bisa nunjukkin hasilnya dengan baik."
        coder "Gue terlalu banyak ngejar yang baru dan nggak cukup meriksa yang lama."
        designer "Kita juga kurang siap kalau skenarionya berubah."
    "Luuk membuka grup. Adrian belum memberikan penjelasan baru mengenai bahan koleksi."
    designer "Gue kesel sama hasilnya."
    coder "Gue juga."
    designer "Tapi gue nggak mau kita cuma nyalahin satu orang terus lupa apa yang bisa kita perbaiki."
    coder "Iya. Gue perlu belajar ngatur waktu dan cara ngetes."
    designer "Gue juga."
    menu:
        "Gue pengin belajar dari ini.":
            coder "Gue pengin belajar dari ini."
            designer "Sama. Biar proyek berikutnya beda."
        "Hari ini gue butuh istirahat dulu.":
            coder "Hari ini gue butuh istirahat dulu."
            designer "Oke. Nanti kalau udah siap, baru kita evaluasi."
    "Mereka tidak mencoba berpura-pura bahwa nilai C merupakan hasil yang mereka inginkan."
    "Namun, mereka tetap berjalan pulang sebagai sahabat. Tugas itu telah berakhir, dan kesempatan untuk belajar belum berakhir."
    scene black with fade
    centered "{size=52}BAD ENDING{/size}\n{size=30}Not enough time.{/size}"
    jump td_final_credits

label td_ending_true:
    scene kantin with dissolve
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    "Hasil penilaian muncul beberapa hari setelah presentasi yang dibatalkan. Luuk dan Jane membukanya bersama di kampus."
    centered "{size=40}HASIL PENILAIAN MUSEUM ARUNIKA{/size}\n\nLuuk — C\nJane — B\nAdrian — E"
    coder "...C."
    designer "Gue B."
    "Mereka membaca hasil itu sekali lagi."
    designer "Luuk..."
    coder "Gue nggak ngerti."
    designer "Gue juga berharap hasilnya beda."
    "Luuk masih menyimpan salinan website yang mereka siapkan untuk hari presentasi."
    coder "Kita udah ngerjain ini tiga bulan."
    designer "Iya."
    coder "Gue udah siap jelasin. Bahkan belum sempet share screen."
    designer "Gue tahu."
    "Dosen mempertimbangkan pekerjaan individu yang telah dikumpulkan, termasuk desain Jane dan implementasi Luuk, tetapi demonstrasi kelompok yang menjadi bagian dari penilaian tidak terlaksana."
    "Adrian tidak hadir dan tidak memperoleh penilaian yang memadai atas kontribusinya."
    coder "Gue bukan kesel karena nilai lo B."
    designer "Gue tahu."
    coder "Gue cuma... pengin punya kesempatan nunjukkin kerjaan gue."
    designer "Iya. Lo memang pantas dapat kesempatan itu."
    "Jane tidak mencoba mengatakan bahwa hasil tersebut adil."
    menu:
        "Gue tetap bangga sama kerjaan kita.":
            coder "Gue tetap bangga sama kerjaan kita."
            designer "Sama. Nilai ini nggak menghapus hasil kerja kita."
        "Lain kali kita harus punya dokumentasi yang lebih kuat.":
            coder "Lain kali kita harus punya dokumentasi yang lebih kuat."
            designer "Iya. Bukan buat cari musuh, tapi supaya kontribusi kita jelas."
    "Luuk menutup halaman penilaian. Ia menyimpan proyeknya, bukan karena ingin mengulang presentasi yang telah lewat, melainkan karena itu adalah hasil pekerjaannya sendiri."
    "Mereka kembali membicarakan kelas berikutnya. Percakapan berjalan pelan, tetapi mereka masih saling mendengarkan."
    "Deadline telah berlalu. Website yang mereka kerjakan tidak pernah mendapat kesempatan untuk ditunjukkan dalam presentasi kelompok."
    scene black with fade
    centered "{size=52}TRUE ENDING{/size}\n{size=30}The work nobody saw.{/size}"
    jump td_final_credits

label td_ending_secret:
    scene kantin with dissolve
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    "Jane mengirim pesan singkat kepada Luuk. Nilai telah diumumkan."
    "Mereka bertemu di kampus dan membuka hasilnya bersama."
    centered "{size=40}HASIL PENILAIAN MUSEUM ARUNIKA{/size}\n\nLuuk — A\nJane — A\nAdrian — E"
    "Luuk terdiam selama beberapa detik."
    designer "Luuk?"
    coder "A."
    designer "Iya. Gue juga A."
    coder "Beneran?"
    designer "Lo mau gue screenshot-in?"
    coder "Gue lagi lihat sendiri."
    "Keduanya tertawa."
    "Dokumentasi yang mereka simpan dan demonstrasi yang berhasil telah memberi dosen dasar untuk menilai Luuk dan Jane sebagai duo. Adrian dinilai terpisah karena tidak hadir dan tidak menunjukkan kontribusi yang memadai."
    designer "Ternyata catatan yang kita simpan dari awal ada gunanya juga."
    coder "Iya. Bukan cuma buat nginget bug."
    designer "Dan untung website kita bisa jalan waktu diminta demo."
    coder "Kalau cuma punya dokumen tapi websitenya gagal, beda lagi ceritanya."
    designer "Bener."
    "Jane menutup ponselnya."
    designer "Gue seneng karena kita akhirnya bisa nunjukkin apa yang kita kerjain."
    coder "Gue juga."
    designer "Nggak perlu ngakuin kerjaan orang lain, nggak perlu bikin alasan."
    coder "Cukup hasil yang ada."
    menu:
        "Tim yang bagus itu bukan cuma soal hasil.":
            coder "Tim yang bagus itu bukan cuma soal hasil."
            designer "Iya. Soal tanggung jawab juga."
        "Kita akhirnya dapat kesempatan yang adil.":
            coder "Kita akhirnya dapat kesempatan yang adil."
            designer "Dan kita nggak nyia-nyiainnya."
    "Mereka membeli es krim dan duduk sedikit lebih lama daripada biasanya."
    designer "Marvel malam ini?"
    coder "Gas."
    designer "Dua match."
    coder "Beneran dua."
    designer "Iya."
    coder "Gue simpan chat-nya, ya?"
    designer "ANJIR."
    "Mereka tertawa. Kali ini tidak ada deadline yang menunggu."
    "Tiga bulan lalu, mereka memulai proyek itu sebagai sebuah kelompok. Pada akhirnya, kerja keras mereka mendapatkan pengakuan yang layak."
    scene black with fade
    centered "{size=52}SECRET ENDING{/size}\n{size=30}Credit where it is due.{/size}"
    jump td_final_credits

label td_final_credits:
    $ hud_visible = False
    scene black with fade
    centered "{size=55}THE DEADLINERS{/size}\n\n{size=30}90 days. One project. Different consequences.{/size}"
    centered "{size=36}THANK YOU FOR PLAYING{/size}"

    return
