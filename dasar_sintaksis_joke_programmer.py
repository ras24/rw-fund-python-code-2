"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi manjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 0
jumlah_telur = 2
print(f"Jumlah botol susu {jumlah_botol_susu} botoh")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi membeli 1 botol susu")
    if jumlah_telur == 0:
        print("Budi tidak jadi membeli telur")
    else:
        print("Budi membeli 6 butir telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu")