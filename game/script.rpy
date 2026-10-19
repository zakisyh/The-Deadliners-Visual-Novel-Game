
# Define characters for the opening scene
# TODO: Replace placeholder names with the actual protagonist and friend names from the story
define p = Character("Protagonist")
define f = Character("Friend")

label start:
    scene black
    # Opening narration describing the initial situation
    "Dua mahasiswa tingkat akhir sedang berjuang menyelesaikan dua proyek besar dalam satu minggu: Tugas Akhir UI/UX dan Pemrograman Web Interaktif."
    "Mereka berada dalam kelompok tiga orang, namun anggota ketiga adalah seorang \"Anomali\" yang jarang muncul dan tidak berkontribusi."
    # Dialog between the protagonist and their friend
    p "Kita harus selesaikan semuanya sebelum deadline, ya?"
    f "Iya, kalau tidak kita bakal gagal di semua mata kuliah."
    # TODO: Add branching menu choices based on the story's decision points
    return
