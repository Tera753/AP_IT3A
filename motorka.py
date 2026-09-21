class Motorka:
    def __init__(self, znacka:str, kategorie:str, stav_nadrze:int, stav_stojanku:str = "Vyklopený"):
        self.znacka = znacka
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku
        pass
    def zatoc_plyn(self):
        return f"vrrrummmm vrummm vruuummmm"
    def popis(self):
        return f"Značka motorky je {self.znacka} tato motorka patří do kategorie {self.kategorie}, obsah nádrže je {self.stav_nadrze} a trojánek je {self.stav_stojanku}."
    def znema_stojanku(self, Nstojanek:str):
        self.stav_stojanku = Nstojanek
        return f"stav stojánku byl zmemen na {Nstojanek}."
    def popojed(self,Nstav_nadrze:int):
        self.stav_nadrze = Nstav_nadrze
        return f"Popojel jsem a stav nádrže se změnil na{Nstav_nadrze}"
    



motorka = Motorka("Yamaha", "silnicka", 50)
print(motorka.znacka, motorka.kategorie, motorka.stav_nadrze)
print(motorka.zatoc_plyn())
print(motorka.popis())
print(motorka.stav_stojanku)
print(motorka.znema_stojanku("zaklopen"))
print(motorka.popojed)
