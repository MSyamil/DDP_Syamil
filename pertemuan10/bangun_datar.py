def persegi(sisi):
    luas = sisi * sisi
    print(f"Luas persegi dengan sisi {sisi} = {luas}")
    
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} = {luas}")
    
def segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} = {luas}")
    
def jajar_genjang(alas, tinggi):
    luas = alas * tinggi
    print(f"Luas jajar genjang dengan alas {alas} dan tinggi {tinggi} = {luas}")
    
def trapesium(atas, bawah, tinggi):
    luas = (atas + bawah) * tinggi / 2
    print(f"Luas trapesium dengan atas {atas}, bawah {bawah}, dan tinggi {tinggi} = {luas}")
    
def lingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    print(f"Luas lingkaran dengan jari-jari {jari_jari} = {luas}")