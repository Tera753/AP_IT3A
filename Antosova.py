
class VesmirnaLod:
    def __init__(self, nazev:str, palivo:int = 0):
        self.nazev = nazev
        self.palivo = palivo
        pass

    def Predstav_se(self):
        return f"Zde lod {self.nazev}."
    
    def let_na(self, cil:str):
        self.cil = cil
        if self.palivo >= 10:
            self.palivo -= 10
            return f"Zahajuji podsvětlený let na {self.cil}. Zbývá {self.palivo}%"
        else:
            return f"Nedostatek paliva pro let"
    
class PozemskyKriznik(VesmirnaLod):
    def __init__(self, nazev, velitel: str,cil:str, palivo = 30):
        super().__init__(nazev, palivo)
        self.velitel = velitel
        

    def Predstav_se(self):
        return f"Zde pozemský křížník {self.nazev}, velí  velitel {self.velitel}."
    
    def let_na(self, cil:str):
        self.cil = cil
        if self.palivo >= 30:
            self.palivo -= 30
            return f"Otevírám hyperprostorové okno k cíli {self.cil}. zbývá {self.palivo}%"
        else:
            return f"Nedostatek paliva pro let"
        
daedalus = PozemskyKriznik("Daedalus", 20, "Brčka")  

print(daedalus.Predstav_se())
print(daedalus.let_na("domu")) 

print("____" *20)
class PuddleJumper(VesmirnaLod):
    def __init__(self, nazev, maskovani_aktivni: bool, palivo = 0):
        super().__init__(nazev, palivo)
        self.maskovani_aktivni = maskovani_aktivni
    
    def Predstav_se(self):
        return f"Zde antický Jumper {self.nazev}."
    
    def let_na(self, cil):
        return super().let_na(cil)
    
    def Zamaskuj_se(self):
        if self.maskovani_aktivni == True:
            self.maskovani_aktivni = False
            return f"{self.nazev} maskování aktivováno"

        else:
            self.maskovani_aktivni = True
        return f"{self.nazev} maskování neaktivováno"
    
Lod_atlamtis = PuddleJumper("Lod z Atlantis", 50, True)
print(Lod_atlamtis.let_na("cil"))
print(Lod_atlamtis.maskovani_aktivni)
print(Lod_atlamtis.Zamaskuj_se())
print(Lod_atlamtis.Zamaskuj_se())
print("____" *20)

class Teltak(VesmirnaLod):
    def Predstav_se(self):
        return super().Predstav_se()
    
    def let_na(self, cil):
        return super().let_na(cil)
    
    def naloz_naklad(self, polozka: str):
        self.polozka = polozka
        return f"Na lod {self.nazev} bylo naloženo: {polozka}"
    
nakladni_lod = Teltak ("Goa'uldska nakladni lod")
print(nakladni_lod.Predstav_se())
print(nakladni_lod.let_na("cil"))
print(nakladni_lod.naloz_naklad("vybavení"))
print("____" *20)

Flotila = [
    nakladni_lod,Lod_atlamtis,daedalus
]
spolecny_cil = "Planeta Lantea"

for lod in Flotila:
    print(lod.Predstav_se())
    print(lod.let_na(spolecny_cil))