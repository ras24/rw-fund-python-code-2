daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('Proses semua dengan for in')
for buku in daftar_buku:
    print(buku)
    
print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print('Kembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    

