# identifikasi input
print("apa yg ingin anda hitung(persegi, lingkaran, segitiga)?")
hitung = input().lower()

# match
match hitung:
    # jika yang dipilih adalah persegi
    case "persegi":
        # minta input nilai sisi
        print("masukkan panjang sisi")
        sisi = int(input())
        # proses
        luas = sisi * sisi
        # cetak luas dari persegi
        print(f"luasnya adalah {luas}")
        # jika yang dipilih adalah lingkaran
    case "lingkaran":
        # minta input jari-jari
        print("masukkan jari-jari")
        r = int(input())
        # proses
        luas = 3.14 * r * r
        # cetak luas dari lingkaran
        print(f"luasnya adalah {luas}")
        # jika yang dipilih adalah segitiga
    case "segitiga":
        # minta input alas
        print("masukkan alas")
        alas = int(input())
        # minta input tinggi
        print("masukkan tinggi")
        tinggi = int(input())
        # proses
        luas = alas * tinggi / 2
        # cetak luas dari segitiga
        print(f"luasnya adalah {luas}")
        # jika yang dipilih tidak ada
    case _ :
        print("salah pilih")