import random
daftar_khodam = {
    "Khodam jin" : "sedot wc"
}
def acak_khodam ():
    nama_khodam = random.choice(list(daftar_khodam.keys()))
    deskripsi = daftar_khodam [nama_khodam]
    # return f"khodam {import_nama} adalah {nama_khodam}:"
    return f"khodam {input_nama} adalah {nama_khodam}:{deskripsi}"
input_nama = input ("masukkan nama kamu :")
hasil = acak_khodam()
print(hasil)
