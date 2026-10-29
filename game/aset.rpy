# =========================================================================================================================
# Character Auto Brightness
# =========================================================================================================================
init python:                                        

    def atur_cahaya(event, speaker=None, **kwargs):

        if event != "begin":
            return

        for nama in ("coder", "designer", "anomaly", "dosen"):

            if renpy.showing(nama):

                if nama == speaker:
                    renpy.show(nama, at_list=[ngomong])

                else:
                    renpy.show(nama, at_list=[diam])

# =========================================================================================================================
# Define Character
# =========================================================================================================================
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

# =========================================================================================================================
# Image Char Assets
# =========================================================================================================================
image coder = Transform("images/Karakter/The Coder/thecoder.png", zoom=0.58)
image designer = Transform("images/Karakter/The Designer/thedesigner.png", zoom=0.58)
image dosen = Transform("images/Karakter/Dosen/dos.png", zoom=0.7)
image anomaly = Transform("images/Karakter/The-Anomaly/ano.png", zoom=0.7)

# =========================================================================================================================
# Image Background Assets
# =========================================================================================================================
image bg_kelas = "images/bg/kelas.jpg"
image kantin = "images/bg/kantin-kampus.jpg"

# =========================================================================================================================
# KECERAHAN KARAKTER
# =========================================================================================================================
transform ngomong:
    ease 0.2 matrixcolor BrightnessMatrix(0.0)          # Karakter sedang berbicara (terang)

transform diam:
    ease 0.2 matrixcolor BrightnessMatrix(-0.35)        # Karakter tidak berbicara (gelap)

# =========================================================================================================================
# ANIMASI 1 KARAKTER
# =========================================================================================================================
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


# =========================================================================================================================
# ANIMASI 2 KARAKTER
# =========================================================================================================================
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

# =======================================================================================================================
# ANIMASI 3 KARAKTER
# =======================================================================================================================
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

# ====================================================================================================================
# TITLE CARD PROLOG
# ====================================================================================================================
transform title_fade:
    alpha 0.0
    ease 1.5 alpha 1.0

transform title_disappear:
    ease 1.0 alpha 0.0

image title_90_days = Text(
    "90 DAYS LEFT",
    size=90,
    color="#FFFFFF",
    bold=True
)

image title_deadliners = Text(
    "THE DEADLINERS",
    size=85,
    color="#FFFFFF",
    bold=True
)