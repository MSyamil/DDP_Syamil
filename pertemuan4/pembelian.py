jumlah_pembelian = int(input("masukan jumlah pembelian : "))
diskon = jumlah_pembelian * 10/100 if jumlah_pembelian > 100 else 0
total = jumlah_pembelian - diskon
print(f"total pembeliannya adalah : {total}")