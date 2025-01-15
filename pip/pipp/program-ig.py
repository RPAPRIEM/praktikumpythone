# KODE INSTAGRAM

import webbrowser

def buka_instagram(username):
    url = f"https://www.instagram.com/{username.replace(' ', '+')}"
    # Membuka URL di browser default
    webbrowser.open(url)
    print(f"Membuka pencarian intagram untuk: {username}")

# Meminta pengguna untuk memasukkan judul video
username_instagram = input("Masukkan username yang ingin dibuka: ")
buka_instagram(username_instagram)