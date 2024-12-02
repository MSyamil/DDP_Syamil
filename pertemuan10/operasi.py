import math

def tambah(a, b):
    hasil = a + b
    print(f"Hasil penjumlahan {a} + {b} = {hasil}")

def kurang(a, b):
    hasil = a - b
    print(f"Hasil pengurangan {a} - {b} = {hasil}")

def kali(a, b):
    hasil = a * b
    print(f"Hasil perkalian {a} * {b} = {hasil}")

def bagi(a, b):
    hasil = a / b    
    print(f"Hasil pembagian {a} / {b} = {hasil}")

def pangkat(a, b):
    hasil = math.pow(a, b)
    print(f"Hasil pangkat {a} pangkat {b} = {hasil}")

a = 0
b = 0