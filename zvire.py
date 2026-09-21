import random
class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
    def zvuk(self):
        return "???"

    def predstavSe(self):
        return f"Jmenuji se {self.jmeno}, je mi {self.vek} let."

    def kdeJsi(self):
        return f"Jsem v místě zvaném {self.misto}"

    def jdiNa(self, nMisto:str):
        self.misto = nMisto
        return f"Přesunul jsem se na {nMisto}. {self.kdeJsi()}"
    

class Pes(Zvire):
    def __init__(self, jmeno, vek, plemeno, misto = "bouda"):
        super().__init__(jmeno, vek, misto) #super: kouka do "rodice"
        self.plemeno = plemeno

    def zvuk(self):
        return "Haf, haf!"
    def aport(self):
        return f"{self.jmeno} prinesla míček."
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekla pred kartáčem"
        else:
            return f"{self.jmeno} nechala se vyčesat"
        
    def predstavSe(self):
        return f"{super().predstavSe()} jsem {self.plemeno}"

Grace = Pes("Grace", 7, " zlatý retrívr", "v přecíni")

print(Grace.jmeno)
print( Grace.plemeno)
print(Grace.zvuk())
print(Grace.predstavSe())
print(Grace.aport())
print(Grace.vycesat())
print(Grace.kdeJsi())

print("_" * 20)
class Kočka(Zvire):
    def __init__(self, jmeno, vek, Barva, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.Barva = Barva

    def zvuk(self):
        return "Mnau, mnau!"
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} tě poškrabala"
        else:
            return f"{self.jmeno} zavrněla"
Micka = Kočka("Micka", 8 , "strakatá", "venku")

print(Micka.jmeno)
print(Micka.zvuk())
print(Micka.predstavSe())
print(Micka.pohladit())
print(Micka.kdeJsi())
print("_" * 20)


class papusek(Zvire):
    def __init__(self, jmeno, vek, barvaPeri, misto = "klec"):
        super().__init__(jmeno, vek, misto)
        self.barvaPeri = barvaPeri

    def zvuk(self):
        return "pipi pi píp"
    
    def opakuj(self, slovo:str):
        return f"{self.jmeno} opakuje: {slovo}! {slovo}!" 

Svetlana = papusek ("Světlana", 10, "modrá")

print(Svetlana.jmeno)
print(Svetlana.opakuj("dvere"))
print("_" * 20)

class had(Zvire):
    def __init__(self, jmeno, vek, delkaCm:int, jedovaty:bool, misto = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.delkaCm = delkaCm
        self.jedovaty = jedovaty

    def zvuk(self):
        return "ssssssssssss"
    
    def ustknuti(self):
        if self.jedovaty:
            return f"POZOR {self.jmeno} tě uštknul a je jedovatý!!"
        else:
            return f" {self.jmeno} tě uštknul aale není jedovatej!"
        
    def predstavSe(self):
        if self.jedovaty:
            typ ="jedovatý"
        else:
            typ = "škrtič"

        return f"Ssssssss.... ja jsem {self.jmeno}, měřím {self.delkaCm} a jsem {typ}"
    
Albert = had ("Albert", 16, 150, True, "postel")
print(Albert.jmeno)
print(Albert.zvuk())
print(Albert.ustknuti())
print(Albert.predstavSe())

        
print("_" * 20)

zvire = Zvire("Luděk", 22)
print(zvire.jmeno)
print(zvire.vek)
print(zvire.zvuk())
print(zvire.predstavSe())
print(zvire.kdeJsi())
print(zvire.jdiNa("Škola"))
print("_" * 20)

zvire2 = Zvire("Amálka", 5, "na zahradě")
print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)
print(zvire2.zvuk())
print(zvire2.predstavSe())
print(zvire2.kdeJsi())
print(zvire2.jdiNa("oběd"))

print("_" * 20)

zoo =[Grace, Albert,Svetlana, Micka] # Polymorfismus

for obyvatel in zoo:
    print(obyvatel.zvuk())
    print(obyvatel.predstavSe())