class Naradi:
    def __init__(self, znacka, model):
        self.znacka = znacka
        self.model = model

    def identifikace(self):
        return f"Nářadí: {self.znacka}, model {self.model}"

    def pracuj(self):
        return "Nářadí pracuje."


class AkuVrtacka(Naradi):
    def __init__(self, znacka, model, baterie):
        super().__init__(znacka, model)
        self.baterie = baterie

    def pracuj(self):
        if self.baterie > 0:
            self.baterie = max(0, self.baterie - 10)
            return f"Vrtačka vrtá. Baterie: {self.baterie} %"
        return "Nutno nabít!"


class MotorovaPila(Naradi):
    def __init__(self, znacka, model, nadrz_plna):
        super().__init__(znacka, model)
        self.nadrz_plna = nadrz_plna

    def pracuj(self):
        if self.nadrz_plna:
            return "Motorová pila řeže dřevo."
        return "Pila nemá palivo!"


vrtacka = AkuVrtacka("Bosch", "GSR", 50)
print(vrtacka.identifikace())

while vrtacka.baterie > 0:
    print(vrtacka.pracuj())

print(vrtacka.pracuj())
