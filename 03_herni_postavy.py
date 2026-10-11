import random


class Postava:
    def __init__(self, jmeno, zdravi):
        self.jmeno = jmeno
        self.zdravi = zdravi

    def predstav_se(self):
        print(f"Jsem {self.jmeno} a mám {self.zdravi} zdraví.")

    def utok(self):
        return 0


class Rytir(Postava):
    def __init__(self, jmeno, zdravi, brneni):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni

    def utok(self):
        poskozeni = random.randint(10, 20)
        return f"{self.jmeno} seká mečem za {poskozeni} poškození!"

    def zablokuj(self):
        return f"{self.jmeno} blokuje útok štítem!"


class Mag(Postava):
    def __init__(self, jmeno, zdravi, mana):
        super().__init__(jmeno, zdravi)
        self.mana = mana

    def utok(self):
        if self.mana >= 10:
            self.mana -= 10
            poskozeni = random.randint(25, 40)
            return f"{self.jmeno} sesílá kouzlo za {poskozeni} poškození!"
        return f"{self.jmeno} útočí holí za 5 poškození."


class Lukostrelec(Postava):
    def __init__(self, jmeno, zdravi, sipy):
        super().__init__(jmeno, zdravi)
        self.sipy = sipy

    def utok(self):
        if self.sipy > 0:
            self.sipy -= 1
            return f"{self.jmeno} vystřelil šíp za 15 poškození!"
        return f"{self.jmeno} nemá šípy!"


druzina = [
    Rytir("Aragorn", 100, 20),
    Mag("Gandalf", 80, 30),
    Lukostrelec("Legolas", 90, 5)
]

for postava in druzina:
    postava.predstav_se()
    print(postava.utok())
    if isinstance(postava, Rytir):
        print(postava.zablokuj())
    print()
