# length - menghitung panjang tuple
panjangtup = (1, 2, 3, 4)
print("Length", len(panjangtup))

# concatenatin - menghubungkan dua tuple
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
combined_tup = tup1 + tup2
print("concatenation", combined_tup) 

#repetition - mengulang elemen tuple
repetitiontup = ('Halo!') * 4
print("repetition:", repetitiontup)

# Membership - memeriksa apakah elemen ada di dalam tuple
member = 2 in (1, 2, 3)
print("membership:", member)

# iteration - melakukan iterasi pada tuple 
for x in (1, 2, 3):
    print(x, end=' ')

# indexing - mengakses elemen berdasarkan indeksnya
T = ('C++', 'Java', 'Python')
print(T[2])
print(T[-2])

# Slicing - mengabil bagian dari index tertentu
list = ('charger', 'ponsel', 'headphone')
print(list[1:])