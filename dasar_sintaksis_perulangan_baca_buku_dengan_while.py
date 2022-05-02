"""
Program perulangan membaca buku dengan while
"""
jumlah_buku = 10
print('Ibu berkata, "Baca semua buku"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while jumlah_buku_yang_sudah_dibaca_dan_dipahami < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
    print(f"Baca ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')