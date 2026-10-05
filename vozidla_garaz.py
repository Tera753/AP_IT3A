class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:str = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass

    def Zvuk(self):
        return f"???"

    def info(self):
        return f"Vozidlo značky {self.znacka} vyrobeno v roce {self.rok_vyroby}, stav nádrže je {self.stav_nadrze}."
    
    def startuj(self):
        if self.stav_nadrze > 0:
            return f"auto se nastartovalo {self.Zvuk}"
        else:
            return f" Bráško, došla ti štáva."
        
#Ford_GT40 = Vozidlo("Ford", 1964)

#print(Vozidlo.Zvuk,
       # Vozidlo.info,
        #Vozidlo.startuj)


class Auto(Vozidlo):
    def __init__(self, znacka, rok_vyroby, stav_nadrze = 100, typ_prevodovky:str = "Manuál"):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def Zvuk(self):
        return "Vrumm, Vrummm!"
    #def zatrub():

Ford_GT40 = Auto("Ford", 1964)

print(Auto.Zvuk,
        Auto.info,
        Auto.startuj)

#Raketka = Auto("Agila", 1985)

#print(Raketka.Zvuk)


class Moped(Vozidlo):
    def __init__(self, znacka, rok_vyroby, Ma_slapadla:bool,  stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.Ma_slapadla = Ma_slapadla

    def Zvuk(self):
        return f"vrrrr!"
    




