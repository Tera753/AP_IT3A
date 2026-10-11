class Vozidlo:
    def __init__(self, znacka, rok_vyroby, stav_nadrze=100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze

    def zvuk_motoru(self):
        return "???"

    def info(self):
        return f"Vozidlo {self.znacka}, rok {self.rok_vyroby}"

    def startuj(self):
        if self.stav_nadrze > 0:
            return f"Vozidlo nastartovalo: {self.zvuk_motoru()}"
        return "Chyba: Došlo palivo!"


class Auto(Vozidlo):
    def __init__(self, znacka, rok_vyroby, typ_prevodovky, stav_nadrze=100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def zvuk_motoru(self):
        return "Vrum vrum!"

    def zatrub(self):
        return "Túúú!"


class Moped(Vozidlo):
    def __init__(self, znacka, rok_vyroby, ma_slapadla, stav_nadrze=100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla

    def zvuk_motoru(self):
        return "Trrrrr!"

    def slapej(self):
        return "Šlapu do pedálů!"


garaz = [
    Auto("Skoda", 2016, "manual"),
    Moped("Babetta", 1985, True)
]

for vozidlo in garaz:
    print(vozidlo.info())
    print(vozidlo.startuj())
    print()
