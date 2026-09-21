class hero:
    def __init__(self, jmeno:str, lvl:int, misto:str = "domov"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.misto = misto
        pass

    def pokrik(self):
        return "Jabadabaduuu"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno}, jsem na {self.lvl} levelu."

    def kdeJsi(self):
        return f"Jsem v místě zvaném {self.misto}"

    def jdiNa(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}. {self.kdeJsi()}"

Hero = hero("Johny",25)
print(Hero.jmeno)
print(Hero.lvl)
print(Hero.pokrik())
print(Hero.predstavSe())
print(Hero.kdeJsi())
print(Hero.jdiNa("Banka"))