
define a = Character("Alya")
define b = Character("Budi")

label start:

    scene black

    "Selamat datang di game pertamaku!"

    a "Halo! Namaku Alya."

    b "Halo Alya, senang bertemu denganmu."

    menu:
        "Apa yang ingin kamu lakukan?"

        "Menyapa Budi":
            a "Senang bertemu denganmu juga!"

        "Pergi":
            a "Aku harus pergi sekarang."

    "Terima kasih sudah bermain!"

    return
