init python:                                        # Update - Update - Update - Update Update - Update #

    def atur_cahaya(event, speaker=None, **kwargs):

        if event != "begin":
            return

        for nama in ("coder", "designer", "anomaly", "dosen"):

            if renpy.showing(nama):

                if nama == speaker:
                    renpy.show(nama, at_list=[ngomong])

                else:
                    renpy.show(nama, at_list=[diam])

# Define Character ----------------------------------------------------------------------------------------------
define coder = Character(
    "The Coder",
    image="coder",
    callback=atur_cahaya,
    cb_speaker="coder"
)

define designer = Character(
    "The Designer",
    callback=atur_cahaya,
    cb_speaker="designer"
)

define anomaly = Character(
    "???",
    callback=atur_cahaya,
    cb_speaker="anomaly"
)

define dosen = Character(
    "Dosen",
    callback=atur_cahaya,
    cb_speaker="dosen"
)

define narrator = Character(
    None,
    callback=atur_cahaya,
    cb_speaker="narrator"
)

# Image Char Assets ---------------------------------------------------------------------------------------------
image coder = Transform("images/Karakter/The Coder/thecoder.png", zoom=0.58)
image designer = Transform("images/Karakter/The Designer/thedesigner.png", zoom=0.58)
image dosen = Transform("images/Karakter/Dosen/dos.png", zoom=0.7)
image anomaly = Transform("images/Karakter/The-Anomaly/ano.png", zoom=0.7)

# Image Background Assets ---------------------------------------------------------------------------------------
image bg_kelas = "images/bg/kelas.jpg"

# ===========================================================================================================
# KECERAHAN KARAKTER
# ===========================================================================================================
transform ngomong:
    ease 0.2 matrixcolor BrightnessMatrix(0.0)          # Karakter sedang berbicara (terang)

transform diam:
    ease 0.2 matrixcolor BrightnessMatrix(-0.35)        # Karakter tidak berbicara (gelap)

# ==================================================================================================
# ANIMASI 1 KARAKTER
# ==================================================================================================
transform char_center:
    xanchor 0.5
    xpos 0.50
    yalign 1.0                                      # Langsung muncul di tengah

transform enter_center_left:
    xanchor 0.5
    xpos -0.30
    yalign 1.0
    ease 0.6 xpos 0.50                              # Masuk dari kiri menuju tengah

transform enter_center_right:
    xanchor 0.5
    xpos 1.30
    yalign 1.0
    ease 0.6 xpos 0.50                              # Masuk dari kanan menuju tengah

transform exit_left:
    ease 0.6 xpos -0.30                             # Keluar ke kiri

transform exit_right:
    ease 0.6 xpos 1.30                              # Keluar ke kanan


# ================================================================================================
# ANIMASI 2 KARAKTER
# ================================================================================================
transform move_left:
    ease 0.6 xpos 0.30                              # Karakter bergeser ke kiri

transform move_right:
    ease 0.6 xpos 0.70                              # Karakter bergeser ke kanan

transform enter_left:
    xanchor 0.5
    xpos -0.30
    yalign 1.0
    ease 0.6 xpos 0.30                              # Karakter kedua masuk dari kiri

transform enter_right:
    xanchor 0.5
    xpos 1.30
    yalign 1.0
    ease 0.6 xpos 0.70                              # Karakter kedua masuk dari kanan

transform back_center:
    ease 0.6 xpos 0.50                              # Karakter yang tersisa kembali ke tengah

transform posisi_kiri_2:
    xanchor 0.5
    xpos 0.30
    yalign 1.0                                      # Langsung muncul di kiri

transform posisi_kanan_2:
    xanchor 0.5
    xpos 0.70
    yalign 1.0                                      # Langsung muncul di kanan

# ===============================================================================================================
# ANIMASI 3 KARAKTER
# ===============================================================================================================
transform kiri_3:
    xanchor 0.5
    yalign 1.0
    ease 0.6 xpos 0.20                              # Geser ke posisi kiri

transform tengah_3:
    xanchor 0.5
    yalign 1.0
    ease 0.6 xpos 0.50                              # Geser ke posisi tengah

transform kanan_3:
    xanchor 0.5
    yalign 1.0
    ease 0.6 xpos 0.80                              # Geser ke posisi kanan

transform masuk_kiri_3:
    xanchor 0.5
    xpos -0.30
    yalign 1.0
    ease 0.6 xpos 0.20                              # Karakter ketiga masuk dari kiri

transform masuk_kanan_3:
    xanchor 0.5
    xpos 1.30
    yalign 1.0
    ease 0.6 xpos 0.80                              # Karakter ketiga masuk dari kanan



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

    coder "Dengerin apaan?"
    
    designer "Materi dosen."
    
    coder "Oh."
    coder "..."
    coder "Emang tadi bahas apa?"

    designer "Ya ampun."

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

    coder "Ya udah, kenalan dulu aja."                                  # Update - Update - Update - Update Update - Update #
    
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
