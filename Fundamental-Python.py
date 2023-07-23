""""
program perulangan membaca buku (for)
"""
jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0

for i in range (1,11):
    print(f'buku ke {i} sudah dibaca')
print(jumlah_buku_yang_sudah_dibaca)

for jumlah_buku_yang_sudah_dibaca in range (1,jumlah_buku+1):
    print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah di baca')
print(jumlah_buku_yang_sudah_dibaca)
print(f'Jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')

""""
program perulangan membaca buku dengan while
"""

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    print('baca 1 buku yang belum dibaca')
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca+1
print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')
print(f'Jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0

while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca+1
    print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')
print(f'Jumlah buku yang sudah di baca {jumlah_buku_yang_sudah_dibaca}')