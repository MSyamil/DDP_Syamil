def kubus (sisi):
    luas = 6 * sisi * sisi
    print(f"Luas kubus dengan sisi {sisi} = {luas}")

def balok (panjang, lebar, tinggi):
    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print(f"Luas balok dengan panjang {panjang}, lebar {lebar}, dan tinggi {tinggi} = {luas}")

def tabung (jari_jari, tinggi):
    luas = 2 * 3.14 * jari_jari * (jari_jari + tinggi)
    print(f"Luas tabung dengan jari-jari {jari_jari} dan tinggi {tinggi} = {luas}")

    
def limas_segitiga (alas, tinggi_alas, t1, t2, t3):
    luas_alas = alas * tinggi_alas / 2
    jml_luas_tegak = alas * t1 / 2 + alas * t2 / 2 + alas * t3 / 2
    luas = luas_alas + jml_luas_tegak
    print(f"Luas limas segitiga dengan alas {alas}, tinggi alas {tinggi_alas}, tinggi sisi tegak 1 {t1}, tinggi sisi tegak 2 {t2}, tinggi sisi tegak 3 {t3} = {luas}")

def prisma(alas, t_alas, t_prisma, p1, p2, p3):
    luas = alas * t_alas + ((p1 + p2 + p3) * t_prisma)
    print(f"Luas prisma dengan alas {alas}, tinggi alas {t_alas}, tinggi prisma {t_prisma}, panjang sisi tegak 1 {p1}, panjang sisi tegak 2 {p2}, panjang sisi tegak 3 {p3} = {luas}")