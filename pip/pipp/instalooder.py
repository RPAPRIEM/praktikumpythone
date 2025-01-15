import instaloader

ig = instaloader.Instaloader()
username_instagram = input("masukan username : ")

ig.download_profile(username_instagram, profile_pic_only= True)
# ig.download_profile(username_instagram, profile_pic_only= False)

# from googletrans import Translator
# tl = Translator()

# text = input("Masukkan teks : ")
# result = tl.translate(text, dest='en')
# print(result.text)