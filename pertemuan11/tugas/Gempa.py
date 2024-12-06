class gempa:
    lokasi = ""
    skala = ""
    
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self):
        if self.skala < 2 :
            print("gempa tidak terasa")
        elif self.skala < 4 :
            print("bangunan retak")
        elif self.skala < 6 :
            print("bangunan roboh")
        else :
            print("bangunan roboh dan berpotensi tsunami")