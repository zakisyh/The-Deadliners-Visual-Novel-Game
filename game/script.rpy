# Define characters for the prologue

define coder = Character("The Coder", image="coder")
define designer = Character("The Designer")
define anomaly = Character("???")
define dosen = Character("Dosen")

# Image assets
image coder = Transform("images/Karakter/The Coder/thecoder.png", zoom=0.6)
image designer = Transform("images/Karakter/The Designer/thedesigner.png", zoom=0.6)
image bg_kelas = "images/bg/kelas.jpg"

label start:
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
    show coder
    coder "(Ngantuk banget...)"
    coder "(Semoga kelas hari ini cepet selesai.)"
    coder "(Pulang, makan, terus main game kayaknya enak.)"
    hide coder
    
    show designer
    designer "Psst."
    hide designer
    show coder
    coder "Hm?"
    hide coder
    show designer
    designer "Lo dengerin nggak dari tadi?"
    hide designer
    show coder
    coder "Dengerin apaan?"
    hide coder
    show designer
    designer "Materi dosen."
    hide designer
    show coder
    coder "Oh."
    hide coder
    show coder
    coder "..."
    coder "Emang tadi bahas apa?"
    hide coder
    show designer
    designer "Ya ampun."
    hide designer
    
    "The Designer menggelengkan kepalanya."
    "Mereka sudah cukup lama bersahabat. Walaupun memiliki kepribadian dan kebiasaan yang berbeda, keduanya sering mengerjakan tugas bersama."
    "The Coder lebih nyaman menghabiskan waktunya dengan pemrograman, sedangkan The Designer lebih tertarik dengan desain dan tampilan antarmuka."
    "Satu hal yang mereka miliki bersama adalah kebiasaan meremehkan waktu yang masih tersisa."
    
    # [SFX: Ketukan meja.]
    dosen "Baik, semuanya. Sebelum kelas hari ini saya akhiri, ada informasi mengenai tugas akhir mata kuliah Pemrograman Web."
    "Suasana kelas perlahan menjadi tenang."
    dosen "Untuk tugas akhir semester ini, kalian diwajibkan membuat sebuah website interaktif."
    dosen "Website harus memiliki fungsi yang berjalan dengan baik, bukan hanya tampilan."
    dosen "Proyek ini akan dikerjakan secara berkelompok."
    dosen "Setiap kelompok wajib terdiri dari tiga orang. Tidak boleh kurang dan tidak boleh lebih."
    show coder
    coder "(Website interaktif?)"
    coder "(Oke, masih masuk akal.)"
    hide coder
    dosen "Kalian diberikan waktu tiga bulan untuk menyelesaikannya."
    dosen "Manfaatkan waktu tersebut dengan baik. Saya tidak mau mendengar alasan proyek belum selesai ketika waktunya presentasi."
    show coder
    coder "(Tiga bulan?)"
    coder "(Lama juga.)"
    coder "(Harusnya aman lah.)"
    hide coder
    show designer
    designer "Eh."
    hide designer
    show coder
    coder "Apa?"
    hide coder
    show designer
    designer "Kita sekelompok, kan?"
    hide designer
    show coder
    coder "Ya iyalah."
    hide coder
    show designer
    designer "Oke. Berarti kurang satu orang."
    hide designer
    show coder
    coder "Gampang. Cari aja nanti."
    hide coder
    show designer
    designer "Yakin?"
    hide designer
    show coder
    coder "Yakin. Emangnya sesusah apa sih nyari satu orang?"
    hide coder
    
    "Kalimat yang terdengar begitu sederhana."
    "Dan, tanpa disadari The Coder, mungkin menjadi awal dari salah satu keputusan paling merepotkan dalam semester tersebut."
    
    ## SCENE 02 — LOOKING FOR A THIRD MEMBER
    ## Location: Ruang Kelas — Beberapa Menit Kemudian
    "Setelah dosen mempersilakan mahasiswa untuk menentukan kelompok, suasana kelas langsung menjadi ramai."
    "Beberapa mahasiswa mulai berpindah tempat duduk."
    "Sebagian lainnya sudah membentuk kelompok bahkan sebelum instruksi selesai disampaikan."
    
    show designer
    designer "Oke. Kita ajak siapa?"
    hide designer
    show coder
    coder "Coba yang duduk belakang."
    hide coder
    show designer
    designer "Udah punya kelompok."
    hide designer
    show coder
    coder "Yang depan?"
    hide coder
    show designer
    designer "Udah juga."
    hide designer
    show coder
    coder "Yang sebelah sana?"
    hide coder
    show designer
    designer "Tadi gue udah tanya. Penuh."
    hide designer
    show coder
    coder "..."
    hide coder
    show designer
    designer "..."
    hide designer
    show coder
    coder "Seriusan?"
    hide coder
    show designer
    designer "Makanya. Lo tadi bilang gampang."
    hide designer
    show coder
    coder "Ya gue kira masih banyak yang belum dapet."
    hide coder
    show designer
    designer "Terus sekarang gimana?"
    hide designer
    show coder
    coder "Coba kita tanya dosen aja. Siapa tahu boleh berdua."
    hide coder
    show designer
    designer "Tadi jelas-jelas dibilang harus bertiga."
    hide designer
    show coder
    coder "Ya siapa tahu ada pengecualian."
    hide coder

    "Dengan pilihan yang semakin terbatas, keduanya memutuskan untuk menghampiri dosen."
    "Namun, tepat ketika The Coder hendak berdiri dari kursinya..."
    
    anomaly "Permisi, Pak. Maaf saya terlambat."
    "Seorang mahasiswa laki-laki memasuki kelas."
    "Wajahnya terlihat sedikit terburu-buru, seolah baru saja berlari menuju ruangan."
    "Beberapa mahasiswa menoleh ke arahnya."
    dosen "Kamu baru datang?"
    anomaly "Iya, Pak. Maaf."
    dosen "Kalau begitu, kamu sudah punya kelompok untuk tugas akhir?"
    anomaly "Kelompok, Pak?"
    dosen "Iya. Tugas akhir Pemrograman Web. Satu kelompok tiga orang."
    anomaly "Oh... belum, Pak."
    dosen "Nah, kebetulan."
    dosen "Kalian berdua tadi belum dapat anggota ketiga, kan?"
    show coder
    coder "Belum, Pak."
    hide coder
    dosen "Bagus. Berarti kalian bertiga satu kelompok."
    show coder
    coder "Eh..."
    hide coder
    show designer
    designer "..."
    hide designer
    anomaly "Oh, oke, Pak."
    dosen "Sudah, berarti semua kelompok lengkap."
    dosen "Silakan diskusikan proyek kalian masing-masing. Minggu depan saya ingin melihat gambaran awal konsep websitenya."
    "The Coder menoleh ke arah The Designer."
    "The Designer membalas tatapannya."
    "Tak satu pun dari mereka mengatakan apa-apa."
    
    show coder
    coder "(Ya... setidaknya kita udah dapet anggota ketiga.)"
    coder "(Meskipun agak mendadak.)"
    hide coder
    show designer
    designer "(Well... dapet juga akhirnya.)"
    hide designer
    show coder
    coder "Iya."
    hide coder
    show designer
    designer "Lo kenal dia?"
    hide designer
    show coder
    coder "Nggak."
    hide coder
    show designer
    designer "Gue juga nggak."
    hide designer
    show coder
    coder "Ya udah, kenalan dulu aja."
    hide coder
    
    ## SCENE 03 — THE NEW MEMBER
    ## Location: Ruang Kelas — Setelah Perkuliahan
    "Mahasiswa mulai meninggalkan kelas satu per satu."
    "The Coder dan The Designer menghampiri anggota kelompok baru mereka yang sedang memasukkan barang ke dalam tas."
    show coder
    coder "Bro."
    hide coder
    anomaly "Hm?"
    show coder
    coder "Kita satu kelompok tadi, kan?"
    hide coder
    anomaly "Oh, iya."
    show coder
    coder "Gue yang bakal ngerjain bagian programming. Ini temen gue, dia biasanya yang ngurus bagian desain."
    hide coder
    show designer
    designer "Hai."
    hide designer
    anomaly "Oh, hai."
    show designer
    designer "Nanti kita perlu diskusi buat nentuin konsep website sama pembagian tugasnya."
    hide designer
    anomaly "Oh, oke."
    show coder
    coder "Lo ada ide mau bikin website apa?"
    hide coder
    anomaly "Hmm..."
    anomaly "Terserah kalian aja sih."
    show coder
    coder "Oh... oke."
    hide coder
    show designer
    designer "Kalau gitu kita bikin grup dulu aja, ya?"
    hide designer
    anomaly "Boleh."
    "Mereka bertukar kontak dan membuat grup untuk koordinasi tugas."
    "Tidak ada yang terlihat terlalu aneh."
    "Anggota baru mereka memang tidak banyak berbicara, tetapi bukan berarti dia tidak bisa diajak bekerja sama."
    "Setidaknya..."
    "Belum ada alasan untuk berpikir sebaliknya."
    
    show designer
    designer "Oke, udah gue masukin semua."
    designer "Lusa kita ketemu lagi buat bahas konsep awalnya. Bisa?"
    hide designer
    show coder
    coder "Bisa."
    hide coder
    anomaly "Iya."
    show coder
    coder "Sip. Berarti ketemu lusa."
    hide coder
    "Mereka kemudian berpisah."
    "The Coder dan The Designer berjalan bersama meninggalkan kelas."
    "Sementara anggota ketiga mereka pergi ke arah lain."
    "Untuk saat ini, dia hanyalah seorang anggota kelompok baru."
    "Namun, kelak A dan B akan mengenalnya dengan sebuah julukan yang cukup unik."
    "THE ANOMALY"
    "A nickname that hasn't been earned. Yet."
    
    ## SCENE 04 — LUNCH BREAK
    ## Location: Warung Makan Dekat Kampus
    "Selesai kelas, The Coder dan The Designer memutuskan untuk makan di sebuah warung dekat kampus."
    "Tempat tersebut sudah cukup sering mereka kunjungi."
    "Bukan karena makanannya luar biasa."
    "Hanya saja, harganya cukup bersahabat dengan kondisi dompet mahasiswa."
    
    show designer
    designer "Jadi, gimana menurut lo?"
    hide designer
    show coder
    coder "Soal apa?"
    hide coder
    show designer
    designer "Kelompok kita."
    hide designer
    show coder
    coder "Ya bagus, kan udah lengkap."
    hide coder
    show designer
    designer "Maksud gue anggota baru kita."
    hide designer
    show coder
    coder "Oh."
    coder "Kenapa emangnya?"
    hide coder
    show designer
    designer "Nggak tahu. Kayaknya dia pendiem banget."
    hide designer
    show coder
    coder "Mungkin emang orangnya begitu."
    hide coder
    show designer
    designer "Iya, sih."
    designer "Cuma gue berharap nanti dia bisa diajak kerja sama."
    hide designer
    show coder
    coder "Ya pasti bisa lah."
    hide coder
    show designer
    designer "Lo optimis banget hari ini."
    hide designer
    show coder
    coder "Daripada pesimis mulu."
    hide coder
    show designer
    designer "Masalahnya, ini tugas akhir. Nilainya lumayan besar."
    hide designer
    show coder
    coder "Masih tiga bulan, santai."
    hide coder
    show designer
    designer "Nah. Itu dia."
    hide designer
    show coder
    coder "Apa?"
    hide coder
    show designer
    designer "Kalimat 'masih tiga bulan' itu bahaya."
    hide designer
    show coder
    coder "Kenapa?"
    hide coder
    show designer
    designer "Soalnya nanti bulan depan lo bilang masih dua bulan."
    designer "Bulan depannya lagi lo bilang masih satu bulan."
    designer "Terus pas tinggal seminggu baru panik."
    hide designer
    show coder
    coder "..."
    coder "Kayaknya lo terlalu sering mikir buruk."
    hide coder
    show designer
    designer "Dan kayaknya lo terlalu sering ngerjain tugas H-1."
    hide designer
    show coder
    coder "Fitnah."
    hide coder
    show designer
    designer "Tugas kemarin siapa yang baru selesai jam tiga pagi?"
    hide designer
    show coder
    coder "..."
    coder "Itu beda kasus."
    hide coder
    "The Designer tertula kecil."
    "The Coder hanya menghela napas sebelum kembali menyantap makanannya."
    show designer
    designer "Eh, tapi serius."
    hide designer
    show coder
    coder "Hm?"
    hide coder
    show designer
    designer "Menurut lo, kita perlu langsung nentuin jobdesk sekarang, atau tunggu diskusi lusa?"
    hide designer
    
    # CHOICE 01 — A SMALL DECISION
    menu:
        "Mending kita tentuin dari sekarang.":
            show coder
            coder "Menurut gue mending kita tentuin dari sekarang."
            coder "Biar pas ketemu lusa tinggal bahas detailnya."
            hide coder
            show designer
            designer "Nah, tumben banget lo ngomong bener."
            hide designer
            show coder
            coder "Maksudnya biasanya gue salah?"
            hide coder
            show designer
            designer "N..."
            hide designer
            show coder
            coder "..."
            hide coder
            show designer
            designer "Oke, nanti gue coba bikin list pembagian tugas..."
            hide designer
            jump scene_05
        "Lusa aja, kan masih banyak waktu.":
            show coder
            coder "Lusa aja lah."
            coder "Kan sekian semuanya kumpul. Biar enak dibahas bareng."
            hide coder
            show designer
            designer "Hmm... ya masuknya juga."
            designer "Tapi jangan dulu..."
            hide designer
            show coder
            coder "Iya, iya."
            hide coder
            show designer
            designer "Janji?"
            hide designer
            coder "Iya, janji."
            jump scene_05
    
label scene_05:
    ## SCENE 05 — THE BEGINNING OF EVERYTHING
    ## Location: Warung Makan — Menjelang Sore
    "Percakapan mengenai tugas akhirnya selesai."
    "Mereka mulai membicarakan hal-hal lain."
    "Game yang sedang mereka mainkan."
    "Tugas mata kuliah lain."
    "Dan berbagai hal kecil yang biasanya memenuhi keseharian mahasiswa."
    show designer
    designer "Eh, nanti malem lo mau ngapain?"
    hide designer
    show coder
    coder "Kayaknya main."
    hide coder
    show designer
    designer "Game lagi?"
    hide designer
    show coder
    coder "Ya masa ngerjain tugas terus?"
    hide coder
    show designer
    designer "Padahal tugas aja belum dikerjain."
    hide designer
    show coder
    coder "Kan masih tiga bulan."
    hide coder
    show designer
    designer "Ya ampun, itu lagi."
    hide designer
    "The Coder tertawa."
    "Mereka menghabiskan waktu beberapa saat sebelum akhirnya meninggalkan warung."
    "Tidak ada pertengkaran."
    "Tidak ada deadline yang mengancam."
    "Tidak ada pesan grup yang harus dibalas dengan panik."
    "Hanya dua mahasiswa yang baru saja mendapatkan sebuah proyek baru."
    "Dan satu anggota kelompok yang belum mereka kenal dengan baik."
    "Seandainya mereka tahu apa yang akan terjadi selama tiga bulan berikutnya..."
    "Mungkin mereka akan membuat keputusan yang berbeda hari itu."
    "Atau mungkin..."
    "Mereka tetap akan melakukan kesalahan yang sama."
    "90 DAYS LEFT"
    "THE DEADLINERS"
    "We still have time."
    "END OF PROLOGUE"
    return
