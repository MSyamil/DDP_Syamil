class orang():
    def __init__(self, nama, umur, gender, alamat = "depok"):
        self.nama = nama
        self.umur = umur
        self.gender = gender
        self.alamat = alamat
    
    # fungsi
    def ngomong(self):
        print("saya bisa berbicara karena saya, ", self.gender)
        
    def jalan(self, kata):
        print("saya bisa berjalan", kata)

# supir = orang()
# print(supir.nama)
# supir.nama = "budi"
# print(supir.nama)
# supir.sim = "A"
# supir.ngomong()
# supir.jalan("ke kiri")
# print(supir.sim)

# #MAHASISWA
# mahasiswa = orang()
# print(mahasiswa.nama)