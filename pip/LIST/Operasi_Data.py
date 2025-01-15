# length - menghitung panjang list 
panjanglist = [1, 2, 3, 4]
print("Length", len(panjanglist))

# concatenatin - menghubungkan dua ilst
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("concatenation", combined_list) 

#repetition - mengulang elemen list
repetitionlist = ['Halo!'] * 4
print("repetition:", repetitionlist)

# Membership - memeriksa apakah elemen ada di dalam list
member = 2 in [1, 2, 3]
print("membership:", member)

# iteration - melakukan iterasi pada list 
for x in [1, 2, 3]:
    print(x, end=' ')

# indexing - mengakses elemen berdasarkan indeksnya
L = ['C++', 'Java', 'Python']
print(L[2])
print(L[-2])

# Slicing - mengabil bagian dari index tertentu
list = ['charger', 'ponsel', 'headphone']
print(list[1:])
