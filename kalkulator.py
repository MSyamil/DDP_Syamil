angka1 = int(input("Masukkan angka 1: "))
angka2 = int(input("Masukkan angka 2: "))
print("""Pilih Operator: 
tambah
kurang
bagi
kali
pangkat""")
operator = input().lower()
match operator:
    case "tambah":
        hasil = angka1 + angka2
        simbol = "+"
    case "kurang":
        hasil = angka1 - angka2
        simbol = "-"
    case "bagi":
        hasil = angka1 / angka2
        simbol = "/"
    case "kali":
        hasil = angka1 * angka2
        simbol = "x"
    case "pangkat":
        hasil = angka1 ** angka2
        simbol = "^"
    case _:
        print("Operator tidak valid")
print(f"Angka pertama: {angka1}")
print(f"Angka kedua: {angka2}")
print(f"Pilihan operator: {operator}")
print(f"Hasil operator {angka1} {simbol} {angka2}: {hasil}")