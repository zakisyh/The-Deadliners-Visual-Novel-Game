label start:
    play music "audio/BGM/insomniac.mp3" loop volume 0.5
    scene bg_kelas
    
    ## SCENE 01 — JUST ANOTHER DAY
    ## Location: Ruang Kelas — Siang Hari

    "Kehidupan mahasiswa."
    "Tugas, presentasi, revisi, dan deadline."
    "Empat hal yang rasanya tidak pernah benar-benar hilang dari kehidupan perkuliahan."
    "Bagi sebagian orang, kuliah adalah kesempatan untuk mengejar impian."
    "Bagi sebagian lainnya, kuliah hanyalah perjuangan untuk bertahan sampai akhir semester."
    "Dan bagi seorang mahasiswa yang lebih sering berhadapan dengan barisan kode daripada manusia..."
    "Hari ini seharusnya menjadi hari yang biasa."

    show coder at enter_center_left
    pause 0.6

    coder "(Ngantuk banget...)"
    coder "(Semoga kelas hari ini cepet selesai.)"
    coder "(Pulang, makan, terus main game kayaknya enak.)"

    show coder at move_left
    show designer at enter_right                                        
    pause 0.6

    designer "Psst."

    coder "Hm?"

    designer "Lo dengerin nggak dari tadi?"

    menu:                                                                       
        "Dengerin kok. Sedikit.":
            coder "Gw denger beberapa"
            designer "oke.."
            coder "Berarti gw masi fokus diawal"
            designer "Yaampun"

        "Jujur aja, gw nggak dengerin":
            coder "Nggak, gw ngantuk banget."
            designer "Setidaknya lo ga ketiduran"
            coder "I will try my best"
            designer "I hope so"

    hide coder
    hide designer                                                           
 
    
    "The Designer menggelengkan kepalanya."
    "Mereka sudah cukup lama bersahabat. Walaupun memiliki kepribadian dan kebiasaan yang berbeda, keduanya sering mengerjakan tugas bersama."
    "The Coder lebih nyaman menghabiskan waktunya dengan pemrograman, sedangkan The Designer lebih tertarik dengan desain dan tampilan antarmuka."
    "Satu hal yang mereka miliki bersama adalah kebiasaan meremehkan waktu yang masih tersisa."
    
    # [SFX: Ketukan meja.]
    show dosen at char_center
    dosen "Baik, semuanya. Sebelum kelas hari ini saya akhiri, ada informasi mengenai tugas akhir mata kuliah Pemrograman Web."
    "Suasana kelas perlahan menjadi tenang."
    dosen "Untuk tugas akhir semester ini, kalian diwajibkan membuat sebuah website interaktif."
    dosen "Website harus memiliki fungsi yang berjalan dengan baik, bukan hanya tampilan."
    dosen "Proyek ini akan dikerjakan secara berkelompok."
    dosen "Setiap kelompok wajib terdiri dari tiga orang. Tidak boleh kurang dan tidak boleh lebih."
    hide dosen

    show coder at char_center
    coder "(Website interaktif?)"
    coder "(Oke, masih masuk akal.)"
    hide coder

    show dosen at char_center
    dosen "Kalian diberikan waktu tiga bulan untuk menyelesaikannya."
    dosen "Manfaatkan waktu tersebut dengan baik. Saya tidak mau mendengar alasan proyek belum selesai ketika waktunya presentasi."
    hide dosen

    show coder at char_center
    coder "(Tiga bulan?)"
    coder "(Lama juga.)"
    coder "(Harusnya aman lah.)"
    
    show coder at move_left
    show designer at enter_right
    pause 0.6

    designer "Eh."

    coder "Apa?"
    
    designer "Kita sekelompok, kan?"
    
    coder "Ya iyalah."
    
    designer "Oke. Berarti kurang satu orang."
    
    coder "Gampang. Cari aja nanti."
    
    designer "Yakin?"
    
    coder "Yakin. Emangnya sesusah apa sih nyari satu orang?"
    show coder at exit_left
    show designer at exit_right
    pause 0.6
    hide coder
    hide designer

    "Kalimat yang terdengar begitu sederhana."
    "Dan, tanpa disadari The Coder, mungkin menjadi awal dari salah satu keputusan paling merepotkan dalam semester tersebut."

    
    ## SCENE 02 — LOOKING FOR A THIRD MEMBER
    ## Location: Ruang Kelas — Beberapa Menit Kemudian
    "Setelah dosen mempersilakan mahasiswa untuk menentukan kelompok, suasana kelas langsung menjadi ramai."
    "Beberapa mahasiswa mulai berpindah tempat duduk."
    "Sebagian lainnya sudah membentuk kelompok bahkan sebelum instruksi selesai disampaikan."
    
    show designer at enter_right
    show coder at enter_left
    pause 0.6

    designer "Oke. Kita ajak siapa?"

    coder "Coba yang duduk belakang."

    designer "Udah punya kelompok."

    coder "Yang depan?"

    designer "Udah juga."

    coder "Yang sebelah sana?"

    designer "Tadi gue udah tanya. Penuh."

    coder "..."

    designer "..."

    coder "Seriusan?"

    designer "Makanya. Lo tadi bilang gampang."

    coder "Ya gue kira masih banyak yang belum dapet."

    designer "Terus sekarang gimana?"

    coder "Coba kita tanya dosen aja. Siapa tahu boleh berdua."

    designer "Tadi jelas-jelas dibilang harus bertiga."

    coder "Ya siapa tahu ada pengecualian."

    hide coder
    hide designer

    "Dengan pilihan yang semakin terbatas, keduanya memutuskan untuk menghampiri dosen."
    "Namun, tepat ketika The Coder hendak berdiri dari kursinya..."
    
    show anomaly at enter_center_right
    pause 0.6

    anomaly "Permisi, Pak. Maaf saya terlambat."

    "Seorang mahasiswa laki-laki memasuki kelas."
    "Wajahnya terlihat sedikit terburu-buru, seolah baru saja berlari menuju ruangan."
    "Beberapa mahasiswa menoleh ke arahnya."

    show dosen at enter_left
    show anomaly at move_right
    pause 0.6

    dosen "Kamu baru datang?"

    anomaly "Iya, Pak. Maaf."

    dosen "Kalau begitu, kamu sudah punya kelompok untuk tugas akhir?"

    anomaly "Kelompok, Pak?"

    dosen "Iya. Tugas akhir Pemrograman Web. Satu kelompok tiga orang."

    anomaly "Oh... belum, Pak."

    dosen "Nah, kebetulan."

    dosen "Kalian berdua tadi belum dapat anggota ketiga, kan?"

    show anomaly at tengah_3
    show coder at masuk_kanan_3
    show dosen at kiri_3
    pause 0.6

    coder "Belum, Pak."

    dosen "Bagus. Berarti kalian bertiga satu kelompok."

    coder "Eh..."

    anomaly "Oh, oke, Pak."
    dosen "Sudah, berarti semua kelompok lengkap."
    show coder at exit_right
    show anomaly at move_right
    show dosen at move_left
    pause 0.6

    show anomaly at exit_right
    show dosen at back_center
    pause 0.6

    dosen "Silakan diskusikan proyek kalian masing-masing. Minggu depan saya ingin melihat gambaran awal konsep websitenya."
    hide dosen

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    "The Coder menoleh ke arah The Designer."
    "The Designer membalas tatapannya."
    "Tak satu pun dari mereka mengatakan apa-apa."
    
    coder "(Ya... setidaknya kita udah dapet anggota ketiga.)"
    coder "(Meskipun agak mendadak.)"

    designer "(Well... dapet juga akhirnya.)"

    coder "Iya."

    designer "Lo kenal dia?"

    coder "Nggak."

    designer "Gue juga nggak."

    coder "Ya udah, kenalan dulu aja."                                  
    
    ## SCENE 03 — THE NEW MEMBER
    ## Location: Ruang Kelas — Setelah Perkuliahan
    "Mahasiswa mulai meninggalkan kelas satu per satu."
    "The Coder dan The Designer menghampiri anggota kelompok baru mereka yang sedang memasukkan barang ke dalam tas."

    show anomaly at char_center                                       
    show anomaly at kiri_3
    show coder at masuk_kanan_3
    show coder at tengah_3
    show designer at masuk_kanan_3
    pause 0.6

    coder "Bro."

    anomaly "Hm?"

    coder "Kita satu kelompok tadi, kan?"

    coder "Gue yang bakal ngerjain bagian programming. Ini temen gue, dia biasanya yang ngurus bagian desain."

    designer "Hai."

    anomaly "Oh, hai."

    designer "Nanti kita perlu diskusi buat nentuin konsep website sama pembagian tugasnya."

    anomaly "Oh, oke."

    coder "Lo ada ide mau bikin website apa?"

    anomaly "Hmm..."
    anomaly "Terserah kalian aja sih."
  
    menu:                                                               
        "Oke, nanti kita pikirin bareng":
            coder "oh Oke, Nanti kita pikirin bareng aja"
            anomaly "Oke"
            designer "Gwe ada ide bagus buat nanti"
            coder "Oke, keep dulu aja"

        "Ada ide?":
            coder "Ada yang punya ide untuk sementara?"
            anomaly "Belum kepikiran sih"
            coder "Oh, coba dipikirin aja"
            designer "iya, kita masih bisa diskusi bareng"
            anomaly "Oke"                                               

    designer "Kalau gitu kita bikin grup dulu aja, ya?"

    anomaly "Boleh."                                                            

    "Mereka bertukar kontak dan membuat grup untuk koordinasi tugas."
    "Tidak ada yang terlihat terlalu aneh."
    "Anggota baru mereka memang tidak banyak berbicara, tetapi bukan berarti dia tidak bisa diajak bekerja sama."
    "Setidaknya..."
    "Belum ada alasan untuk berpikir sebaliknya."
    
    designer "Oke, udah gue masukin semua."
    designer "Lusa kita ketemu lagi buat bahas konsep awalnya. Bisa?"

    coder "Bisa."

    anomaly "Iya."

    coder "Sip. Berarti ketemu lusa."

    "Mereka kemudian berpisah."

    show designer at exit_right
    show coder at move_right
    show anomaly at move_left
    pause 0.6

    show coder at exit_right
    show anomaly at exit_left
    pause 0.6

    "The Coder dan The Designer berjalan bersama meninggalkan kelas."
    "Sementara anggota ketiga mereka pergi ke arah lain."
    "Untuk saat ini, dia hanyalah seorang anggota kelompok baru."
    "Namun, kelak A dan B akan mengenalnya dengan sebuah julukan yang cukup unik."
    "THE ANOMALY"
    "A nickname that hasn't been earned. Yet."                           
    
    ## SCENE 04 — LUNCH BREAK
    ## Location: Warung Makan Dekat Kampus
    scene kantin

    "Selesai kelas, The Coder dan The Designer memutuskan untuk makan di sebuah warung dekat kampus."
    "Tempat tersebut sudah cukup sering mereka kunjungi."
    "Bukan karena makanannya luar biasa."
    "Hanya saja, harganya cukup bersahabat dengan kondisi dompet mahasiswa."
    
    show coder at enter_left
    show designer at enter_right
    pause 0.6

    designer "Jadi, gimana menurut lo?"

    coder "Soal apa?"

    designer "Kelompok kita."

    coder "Ya bagus, kan udah lengkap."

    designer "Maksud gue anggota baru kita."

    coder "Oh."
    coder "Kenapa emangnya?"

    designer "Nggak tahu. Kayaknya dia pendiem banget."

    coder "Mungkin emang orangnya begitu."

    designer "Iya, sih."
    designer "Cuma gue berharap nanti dia bisa diajak kerja sama."

    coder "Ya pasti bisa lah."

    designer "Lo optimis banget hari ini."

    coder "Daripada pesimis mulu."

    designer "Masalahnya, ini tugas akhir. Nilainya lumayan besar."

    coder "Masih tiga bulan, santai."

    designer "Nah. Itu dia."

    coder "Apa?"

    designer "Kalimat 'masih tiga bulan' itu bahaya."

    coder "Kenapa?"

    designer "Soalnya nanti bulan depan lo bilang masih dua bulan."
    designer "Bulan depannya lagi lo bilang masih satu bulan."
    designer "Terus pas tinggal seminggu baru panik."

    coder "..."
    coder "Kayaknya lo terlalu sering mikir buruk."

    designer "Dan kayaknya lo terlalu sering ngerjain tugas H-1."

    coder "Fitnah."

    designer "Tugas kemarin siapa yang baru selesai jam tiga pagi?"

    coder "..."
    coder "Itu beda kasus."

    "The Designer tertawa kecil."
    "The Coder hanya menghela napas sebelum kembali menyantap makanannya."

    designer "Eh, tapi serius."

    coder "Hm?"

    designer "Menurut lo, kita perlu langsung nentuin jobdesk sekarang, atau tunggu diskusi lusa?"
    
    menu:
        "Mending kita tentuin dari sekarang.":
            coder "Menurut gue mending kita tentuin dari sekarang."
            coder "Biar pas ketemu lusa tinggal bahas detailnya."

            designer "Nah, tumben banget lo ngomong bener."

            coder "Maksudnya biasanya gue salah?"

            designer "N..."

            coder "..."

            designer "Oke, nanti gue coba bikin list pembagian tugas..."
            hide coder
            hide designer
            jump scene_05
        "Lusa aja, kan masih banyak waktu.":

            coder "Lusa aja lah."
            coder "Kan sekian semuanya kumpul. Biar enak dibahas bareng."

            designer "Hmm... ya masuknya juga."
            designer "Tapi jangan dulu..."

            coder "Iya, iya."

            designer "Janji?"

            coder "Iya, janji."
            hide coder
            hide designer
            jump scene_05
    
label scene_05:
    ## SCENE 05 — THE BEGINNING OF EVERYTHING
    ## Location: Warung Makan — Menjelang Sore
    "Percakapan mengenai tugas akhirnya selesai."
    "Mereka mulai membicarakan hal-hal lain."
    "Game yang sedang mereka mainkan."
    "Tugas mata kuliah lain."
    "Dan berbagai hal kecil yang biasanya memenuhi keseharian mahasiswa."

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    pause 0.6

    designer "Eh, nanti malem lo mau ngapain?"

    coder "Kayaknya main."

    designer "Game lagi?"

    coder "Ya masa ngerjain tugas terus?"

    designer "Padahal tugas aja belum dikerjain."

    coder "Kan masih tiga bulan."

    designer "Ya ampun, itu lagi."

    "The Coder tertawa."
    "Mereka menghabiskan waktu beberapa saat sebelum akhirnya meninggalkan warung."
    
    show coder at posisi_kiri_2
    show designer at posisi_kanan_2
    pause 0.6

    "Tidak ada pertengkaran."
    "Tidak ada deadline yang mengancam."                                   
    "Tidak ada pesan grup yang harus dibalas dengan panik."
    "Hanya dua mahasiswa yang baru saja mendapatkan sebuah proyek baru."
    "Dan satu anggota kelompok yang belum mereka kenal dengan baik."
    "Seandainya mereka tahu apa yang akan terjadi selama tiga bulan berikutnya..."
    "Mungkin mereka akan membuat keputusan yang berbeda hari itu."
    "Atau mungkin..."
    "Mereka tetap akan melakukan kesalahan yang sama."

scene black with fade                                           # Update - Update - Update - Update Update - Update #
stop music fadeout 3.0
pause 0.8

show title_90_days at truecenter, title_fade
pause 2.5

show title_90_days at truecenter, title_disappear
pause 1.0
hide title_90_days
pause 0.5

show title_deadliners at truecenter, title_fade
pause 3.0

show title_deadliners at truecenter, title_disappear
pause 1.0
hide title_deadliners
pause 0.5

jump chapter_1

# =====================================================================
# CHAPTER 1 — THE FIRST MEETING
# 88 DAYS LEFT | Dua hari setelah prolog
# Keempat pilihan hanya memengaruhi dialog, bukan ending.
# =====================================================================

label chapter_1:
    scene black with fade
    centered "{size=50}CHAPTER 01{/size}\n{size=42}THE FIRST MEETING{/size}\n{size=34}88 DAYS LEFT{/size}"

    play music "audio/BGM/insomniac.mp3" loop volume 0.5

    jump ch1_scene_01


# =====================================================================
# SCENE 01 — TWO DAYS LATER
# Lokasi cerita: area duduk dekat perpustakaan kampus, BUKAN kelas.
# Background hitam hanya placeholder karena aset lokasi belum ada.
# =====================================================================

label ch1_scene_01:
    scene black with dissolve

    show screen website_progress_hud

    "Dua hari setelah pembentukan kelompok."
    "Sesuai janji di grup, mereka akan bertemu untuk membahas konsep proyek."
    "Tempatnya di area duduk dekat perpustakaan kampus."
    "Ketika The Coder sampai, The Designer sudah lebih dulu berada di sana."

    show designer at posisi_kanan_2
    show coder at enter_left
    pause 0.6

    designer "Eh, sini."
    coder "Lo udah lama?"
    designer "Nggak juga. Baru beberapa menit."
    coder "Gue kira gue telat."
    designer "Belum. Masih sesuai jamnya, kok."
    coder "Syukurlah."
    designer "Tapi tumben juga lo datang tepat waktu."

    # PILIHAN 1 — Hanya mengubah respons Coder
    menu:
        "Ya masa gue telat terus.":
            coder "Ya masa gue telat terus."
            designer "Kemarin pas kelas juga lo hampir kesiangan."
            coder "Iya, kan hampir. Bukan beneran."
            designer "Oke deh, terserah lo."

        "Gue juga kaget bisa tepat waktu.":
            coder "Gue juga kaget bisa tepat waktu."
            designer "Setidaknya lo sadar."
            coder "Bisa nggak sih sekali aja lo muji?"
            designer "Bagus, hari ini lo nggak telat."
            coder "Nah, gitu dong."

    designer "Btw, dia udah ngabarin belum?"
    coder "Siapa?"
    designer "Anggota ketiga kita."
    coder "Oh. Gue belum ngecek grup."
    designer "Tadi dia bilang lagi ke sini."
    coder "Yaudah, tunggu bentar aja."
    designer "Iya. Sambil nunggu, lo udah kepikiran mau bikin web apa?"
    coder "Belum yang jelas. Gue malah mau denger ide lo dulu."
    designer "Gue ada satu, sih. Nanti tunggu lengkap aja."
    coder "Oke."

    "Tak lama kemudian, anggota ketiga mereka datang sambil membawa tas."

    show coder at kiri_3
    show designer at tengah_3
    show anomaly at masuk_kanan_3
    pause 0.6

    anomaly "Eh, di sini, ya?"
    designer "Iya, sini aja."
    anomaly "Oke."
    coder "Kita juga baru mau mulai."
    anomaly "Oh, sip."

    "Dia duduk dan meletakkan tas di samping kursi."
    "Untuk beberapa saat, mereka hanya sibuk menyiapkan HP dan catatan masing-masing."

    designer "Oke, udah lengkap. Kita bahas konsepnya dulu, ya?"
    coder "Boleh."
    anomaly "Iya."

    jump ch1_scene_02


# =====================================================================
# SCENE 02 — THE MUSEUM PROJECT
# Lokasi: masih di area duduk dekat perpustakaan
# =====================================================================

label ch1_scene_02:
    "The Designer membuka catatan di HP-nya."

    designer "Jadi, minggu depan dosen minta gambaran konsep web, kan?"
    coder "Iya. Belum harus jadi, yang penting arahnya jelas."
    designer "Nah, gue kepikiran bikin website museum."
    coder "Museum?"
    designer "Iya. Yang ada informasi tempatnya, koleksinya, sama pesan tiket."
    coder "Oh, bisa juga."
    designer "Menurut lo ribet nggak?"
    coder "Kalau cuma tampilan mah enggak. Yang perlu dipikirin sistem tiketnya."
    designer "Kan tugasnya memang harus interaktif."
    coder "Iya, gue tahu. Gue cuma mikirin cara bikinnya."
    designer "Misalnya pengunjung bisa pilih tanggal sama jumlah tiket."
    coder "Terus isi nama atau data pengunjung."
    designer "Habis itu ada konfirmasi pesanan."
    coder "Nah, itu masuk akal."

    "The Anomaly mengikuti pembicaraan sambil sesekali melihat catatan di layar HP-nya."

    designer "Kalau museumnya bikin sendiri aja gimana? Maksud gue, museum fiktif."
    coder "Malah lebih gampang. Kita bisa bikin informasi sama koleksinya sendiri."
    anomaly "Oh, museum buatan kita gitu?"
    designer "Iya, kurang lebih."
    anomaly "Oke."

    designer "Tema sejarah sama budaya kota mungkin cocok."
    coder "Boleh. Tapi data koleksinya jangan asal-asalan juga."
    designer "Iya, nanti kita bikin yang nyambung semua."
    coder "Terus nama museumnya?"
    designer "Gue tadi kepikiran... Museum Arunika."
    coder "Arunika?"
    designer "Iya. Gimana?"
    coder "Lumayan. Enak didenger."
    designer "Berarti oke?"
    coder "Oke."
    designer "Lo gimana?"
    anomaly "Bagus sih, menurut gue."
    designer "Yaudah, sementara itu dulu."

    coder "Berarti kita punya info museum, galeri koleksi, sama halaman tiket."
    designer "Sama jam buka dan harga tiket."
    coder "Iya. Tapi pembayaran jangan yang beneran dulu."
    designer "Maksudnya simulasi?"
    coder "Iya. Sampai ada ringkasan dan konfirmasi pesanan aja."
    designer "Setuju. Yang penting alurnya jalan."

    designer "Enaknya sekarang kita bahas dari mana dulu?"

    # PILIHAN 2 — Urutan diskusi berbeda, rencana akhirnya tetap sama
    menu:
        "Dari tampilan dan halaman websitenya dulu.":
            coder "Dari halamannya dulu aja. Biar kelihatan bagian apa yang dibutuhin."
            designer "Oke. Gue catat dulu struktur halamannya."
            coder "Beranda, info museum, koleksi, sama pemesanan tiket."
            designer "Nanti gue coba bikin sketsanya."
            coder "Sip, nanti kita cocokkin sama alur tiketnya."

        "Dari alur pemesanan tiket dulu.":
            coder "Dari alur tiket aja. Soalnya itu yang harus bener-bener berfungsi."
            designer "Oke. Mulai pilih tanggal sama jumlah tiket?"
            coder "Iya, terus isi data, cek total, baru konfirmasi."
            designer "Berarti gue perlu desain form sama halaman ringkasan."
            coder "Nah, bener."

    "Diskusi berlanjut. Mereka mencatat fitur-fitur yang disepakati."

    designer "Jadi yang wajib ada: halaman utama, informasi museum, sama galeri koleksi."
    coder "Sama pemesanan tiket dan konfirmasinya."
    designer "Untuk galeri, berarti kita butuh foto sama deskripsi tiap koleksi."
    coder "Iya, biar halamannya nggak kosong."
    designer "Kita bikin yang dasar dulu aja. Kalau langsung banyak fitur, takutnya nggak selesai."
    coder "Setuju. Mending yang penting-penting jalan."
    anomaly "Hmm."
    designer "Gimana? Ada yang kepikiran?"
    anomaly "Enggak, udah oke sih menurut gue."
    designer "Oke."

    "Belum ada perdebatan besar. Mereka justru cukup cepat menemukan konsep yang sama-sama bisa diterima."
    "Untuk pertemuan pertama, itu sudah terasa seperti awal yang bagus."

    jump ch1_scene_03


# =====================================================================
# SCENE 03 — DIVIDING THE WORK
# Lokasi: masih di area duduk dekat perpustakaan
# =====================================================================

label ch1_scene_03:
    designer "Nah, sekarang pembagian kerja."
    coder "Gue coding, ya. Struktur web sama fitur tiketnya."
    designer "Oke. Gue UI/UX, layout, sama prototype."
    coder "Nanti kalau desain form tiketnya udah ada, kirim ke gue."
    designer "Iya, biar nggak beda pas dibikin."
    coder "Terus buat konten museumnya gimana?"

    "The Coder dan The Designer menoleh ke anggota ketiga mereka."

    anomaly "Hmm..."
    anomaly "Gue ikut pembagiannya aja sih."

    # PILIHAN 3 — Cara mengajak Anomaly, pembagian akhirnya sama
    menu:
        "Tanya dia lebih nyaman ngerjain bagian apa.":
            coder "Kalau lo sendiri lebih nyaman bagian apa?"
            anomaly "Belum kepikiran juga."
            coder "Oh, oke."
            designer "Kalau bagian konten sama cari referensi gambar gimana?"
            anomaly "Boleh, kayaknya bisa."

        "Tawarkan bagian aset dan informasi museum.":
            coder "Gimana kalau lo bantu cari aset sama informasi buat museumnya?"
            anomaly "Oh, yang buat isi websitenya?"
            coder "Iya, foto referensi sama deskripsi koleksi."
            anomaly "Oke, boleh."

    designer "Sip. Berarti kita bertiga udah punya bagian masing-masing."
    coder "Yang penting nanti kalau ada yang nggak jelas, langsung tanya aja."
    anomaly "Iya."
    designer "Biar gampang, kita tentuin target awal juga, ya."
    coder "Boleh. Biar pas ketemu lagi ada yang bisa dibahas."
    designer "Gue usahain minggu depan udah ada wireframe beberapa halaman."
    coder "Gue bikin struktur proyek sama alur form tiketnya dulu."
    designer "Terus buat kontennya, kita butuh beberapa bahan."
    anomaly "Kayak apa?"
    designer "Buat awal, coba kumpulin sepuluh gambar referensi dan deskripsi singkat lima koleksi museum."
    anomaly "Sepuluh gambar, lima deskripsi?"
    designer "Iya. Nggak perlu panjang-panjang dulu. Nanti kita sesuaikan sama desain."
    anomaly "Oke."
    coder "Kalau susah cari referensi, bilang di grup aja."
    anomaly "Iya, siap."

    "The Designer merapikan catatannya lalu mengirim ringkasan pembagian tugas ke grup yang sudah mereka buat saat prolog."

    designer "Udah gue kirim di grup, ya. Coba cek."
    coder "Masuk."
    anomaly "Iya, masuk."
    designer "Nanti kita lihat progresnya minggu depan."
    coder "Oke. Masih cukup waktu buat mulai pelan-pelan."
    designer "Pelan-pelan boleh, asal mulai."
    coder "Iya, iya."

    jump ch1_scene_04


# =====================================================================
# SCENE 04 — SOMETHING FEELS OFF
# Lokasi: masih di area duduk dekat perpustakaan
# Tidak ada pilihan. Anomaly tetap pendiam dan wajar.
# =====================================================================

label ch1_scene_04:
    "Rapat sudah hampir selesai."
    "The Designer memeriksa catatannya satu kali lagi sebelum menutup HP."

    designer "Bentar. Minggu depan berarti kita cek hasil awal, ya."
    coder "Iya."
    designer "Gue bawa wireframe. Lo bawa struktur web sama form tiket."
    coder "Siap."

    "HP di tangan anggota ketiga mereka menyala sebentar. Dia melihat layarnya."

    designer "Terus buat konten museum..."
    designer "Lo ingat targetnya, kan?"
    anomaly "Hm?"
    anomaly "Oh, iya. Sepuluh gambar sama lima deskripsi koleksi."
    designer "Iya, itu."
    anomaly "Oke."

    "Dia mematikan layar HP dan kembali memperhatikan pembicaraan."
    "The Coder sempat melihatnya sekilas, lalu kembali ke catatannya sendiri."

    coder "Kalau gitu buat sekarang udah cukup, ya?"
    designer "Kayaknya udah. Nanti kalau ada yang kepikiran, tinggal bahas di grup."
    anomaly "Iya."

    "Mereka mulai merapikan barang."

    anomaly "Gue balik duluan, ya."
    coder "Oh, oke."
    designer "Oke, hati-hati."
    anomaly "Iya, sampai nanti."

    show anomaly at exit_right
    show coder at move_left
    show designer at move_right
    pause 0.6
    hide anomaly

    $ website_progress = min(100, website_progress + 10)

    "Tinggal The Coder dan The Designer di tempat duduk itu."

    designer "Yaudah, kita juga beres-beres."
    coder "Eh, lo langsung pulang?"
    designer "Belum tahu. Laper, sih."
    coder "Nah, sama."
    designer "Makan dulu aja, yuk."
    coder "Ayo."

    jump ch1_scene_05


# =====================================================================
# SCENE 05 — JUST ANOTHER LUNCH
# Lokasi: warung makan dekat kampus, seperti di prolog
# =====================================================================

label ch1_scene_05:
    scene kantin with dissolve

    "Seperti dua hari lalu, mereka mampir ke warung dekat kampus."
    "Setelah memesan makanan, keduanya duduk di meja yang biasa mereka pilih."

    show coder at posisi_kiri_2
    show designer at posisi_kanan_2

    coder "Akhirnya makan juga."
    designer "Lo tadi belum sarapan?"
    coder "Cuma minum. Tadi buru-buru."
    designer "Pantes dari tadi liat jam mulu."
    coder "Gue liat jam karena lapar, bukan karena rapatnya lama."
    designer "Iya, iya."

    designer "Tapi tadi lumayan, ya. Udah ada konsep."
    coder "Iya. Museum Arunika."
    designer "Gue pengen coba bikin tampilan berandanya malam ini."
    coder "Gue mungkin mulai nyusun folder proyek dulu."
    designer "Mungkin?"
    coder "Ya, kalau nggak ketiduran."
    designer "Nah, mulai."
    coder "Lo juga belum tentu langsung ngerjain, kan?"
    designer "Iya sih. Gue masih ada tugas UI/UX yang lain."
    coder "Tuh, kan."
    designer "Tapi gue mau nyicil, minimal sketsanya dulu."
    coder "Oke, gue usahain mulai juga."

    "Mereka sempat membahas beberapa hal kecil tentang tugas mata kuliah lain."
    "Obrolannya lalu kembali ke rapat tadi."

    designer "Eh, menurut lo anggota ketiga kita gimana?"
    coder "Gimana apanya?"
    designer "Tadi dia lebih banyak diem."
    coder "Iya, emang pendiem kayaknya."
    designer "Bukan masalah sih. Gue cuma belum tahu dia udah paham apa belum."
    coder "Pas kita ulangin targetnya, dia inget kok."
    designer "Iya, bener."
    designer "Cuma nanti kan bagian galeri butuh bahan dari dia."
    coder "Hmm."

    # PILIHAN 4 — Respons Coder, bukan penilaian atau hukuman untuk Anomaly
    menu:
        "Kasih dia waktu dulu aja.":
            coder "Baru rapat pertama. Kasih dia waktu dulu aja."
            designer "Iya juga. Gue nggak mau langsung mikir yang aneh-aneh."
            coder "Nanti juga kelihatan pas progres minggu depan."
            designer "Oke. Semoga lancar."

        "Kita saling ingetin progres di grup.":
            coder "Kita saling ingetin progres di grup aja."
            designer "Boleh. Jadi kalau ada yang bingung bisa langsung ngomong."
            coder "Buat semuanya, termasuk gue sama lo."
            designer "Iya, justru itu."

    "Tak lama kemudian, pesanan mereka datang."
    "Topik mengenai anggota kelompok pun selesai sampai di situ."

    coder "Eh, nanti malam lo ada kegiatan?"
    designer "Paling ngerjain tugas kalau nggak keburu capek. Kenapa?"
    coder "Gue mau main bentar kayaknya."
    designer "Game lagi?"
    coder "Ya habis itu ngerjain."
    designer "Yang bener aja."
    coder "Iya. Gue juga pengen proyek ini kelar, kok."
    designer "Gue tahu. Cuma jangan kebiasaan bilang nanti."
    coder "Lo juga suka nunda kadang-kadang."
    designer "Iya, makanya gue ngomong ke kita berdua."
    coder "Yaudah. Nanti malam kita kabarin progres masing-masing aja."
    designer "Boleh."

    "Mereka melanjutkan makan sambil ngobrol tentang kelas dan rencana akhir pekan."
    "Tidak ada pertengkaran hari itu."
    "Tidak ada yang menuduh siapa pun."
    "Mereka baru saja memilih konsep, membagi pekerjaan, dan menetapkan target pertama."
    "Semuanya terasa cukup terkendali."
    "Dan waktu yang tersisa masih terlihat panjang."

    scene black with fade
    stop music fadeout 2.0
    centered "{size=50}CHAPTER 01 COMPLETE{/size}\n{size=36}88 DAYS LEFT{/size}"

    return                                                          # Update - Update - Update - Update Update - Update #