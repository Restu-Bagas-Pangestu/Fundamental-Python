daftar_buku = ['seven habits','How to influence people', 'first things first']
print('tampilkan variable daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in ')
for buku in daftar_buku:
    print(buku)
print('\ntampilkan isi daftar_buku pada index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\ntampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku= [1, 'kenji volume 2', -313, 3.14]
print('\ntampilkan dengan for in range, dimana tipe data tiap elemen berbeda2')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal daftar buku')
daftar_buku = ['seven habits','How to influence people', 'first things first']
print('\ntambahkan 1 buku baru')
daftar_buku.append('dunia matematika kelas 5')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nganti element pertama')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
daftar_buku[0]= 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nganti element ke-2')
buku=daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang diambil tadi')
print(buku)

print('\npop -1')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\npop -1')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start dan end')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
del daftar_buku[0:3]#start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start dan end')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
del daftar_buku[0:-2]#start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start dan end')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
del daftar_buku[0::2]#start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembuat list baru')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
daftar_buku_baru=daftar_buku
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku[i])
print('\nmembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension')
daftar_buku = ['seven habits','How to influence people', 'first things first','4DX']
daftar_buku_baru=daftar_buku [:] #list comprehension untuk membuat list yang terpisah (sama kaya .copy())
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku[i])
print('\nmembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 seven habits','2 How to influence people', '3 first things first','4 4DX']
daftar_buku_baru=daftar_buku [0::2] #start:stop
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension: genap')
daftar_buku = ['1 seven habits','2 How to influence people', '3 first things first','4 4DX']
daftar_buku_baru=daftar_buku [1::2] #start:stop
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension: buang diujung')
daftar_buku = ['1 seven habits','2 How to influence people', '3 first things first','4 4DX']
daftar_buku_baru=daftar_buku[0:-1:2] #start:stop
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 seven habits','2 How to influence people', '3 first things first','4 4DX']
print(daftar_buku [0::2]) #start:stop
