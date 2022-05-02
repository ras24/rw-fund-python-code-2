print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First', '4DX']
del daftar_buku[0:1] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First', '4DX']
del daftar_buku[0:1] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])    
    
print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'How to Influence People', 'Fist Things First', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])