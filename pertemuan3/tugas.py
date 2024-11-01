# BIODATA
print("~~~~~~~~~~~~~~Biodata Diri~~~~~~~~~~~~~~")
# input
nama = input("masukkan nama anda :")
nim = input("masukkan nim anda :")
rombel = input("masukkan rombel anda :")
no_tel = input("masukkan nomor telepon anda :")
alamat = input("masukkan alamat anda : ")
# output
print("Hasil Biodata diri")
print("Nama anda : ",nama)
print("nomor NIM anda : ",nim)
print("Rombel anda adalah : ",rombel)
print("nomor telepon anda : ",no_tel)
print("alamat anda : ",alamat)

# BIODATA Teman
print("~~~~~~~~~~~~~~Biodata Teman~~~~~~~~~~~~~~")
# input
nama_teman = input("masukkan nama teman anda :")
nim_teman = input("masukkan nim teman anda :")
rombel_teman = input("masukkan rombel teman anda :")
no_tel_teman = input("masukkan nomor telepon teman anda :")
alamat_teman = input("masukkan alamat teman anda : ")
# output
print("Hasil Biodata teman")
print("Nama teman anda : ",nama_teman)
print("nomor NIM teman anda : ",nim_teman)
print("Rombel teman anda adalah : ",rombel_teman)
print("nomor telepon teman anda : ",no_tel_teman)
print("alamt teman anda : ",alamat_teman)

# Berat Badan Ideal
print("~~~~~~~~~~~~~~Berat Badan Ideal~~~~~~~~~~~~~~")
# input
tb = int(input("masukkan tinggi badan anda (dalam cm) : "))
# proses
bb_ideal = (tb-100) - ((tb - 100) * 0.1)
# output
print("berat badan ideal anda = ",bb_ideal, "kg")

# Celcius to Fahrenheit
print("~~~~~~~~~~~~~~Celcius to Fahrenheit~~~~~~~~~~~~~~")
# input
celcius = input("masukkan suhu dalam celcius : ")
# proses
fahrenheit = 9/5 * int(celcius) + 32
# output
print("suhu dalam fahrenheit = ",fahrenheit)

# Luas dan Volume Tabung
print("~~~~~~~~~~~~~~Luas dan Volume Tabung~~~~~~~~~~~~~~")
# input
jari_jari = input("masukkan jari-jari tabung : ")
tinggi = input("masukkan tinggi tabung : ")
phi = 3.14
# proses
volume = phi * int(jari_jari) * int(jari_jari) * int(tinggi)
luas = 2 * phi * int(jari_jari) * (int(jari_jari) + int(tinggi))
# output
print("luas tabung = ",luas)
print("volume tabung = ",volume)