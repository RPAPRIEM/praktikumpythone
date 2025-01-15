# import webbrowser

# def buka_youtube(video_title):
    # url = f"https://www.youtube.com/results?search_query={video_title.replace(' ', '+')}"
    # Membuka URL di browser default
    # webbrowser.open(url)
    # print(f"Membuka pencarian YouTube untuk: {video_title}")

# Meminta pengguna untuk memasukkan judul video
# judul_video = input("Masukkan judul video YouTube yang ingin dibuka: ")
# buka_youtube(judul_video)

import webbrowser

def buka_Instagram(username):
    url = f"https://www.instagram.com/{username.replace(' ', '+')}"
    # Membuka URL di browser default
    webbrowser.open(url)
    print(f"Membuka pencarian YouTube untuk: {username}")

# Meminta pengguna untuk memasukkan judul video
judul_video = input("Masukkan judul video YouTube yang ingin dibuka: ")
buka_Instagram(judul_video)
