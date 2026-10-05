import random
class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass
    def predstav_se(self):
        return f"Ahoj jmenuju se {self.jmeno}, a mé zdraví je {self.zdravi}"
    def ukot(self):
        return 0

class Rytir(Postava):
    def __init__(self, jmeno, zdravi, Brneni:int):
        super().__init__(jmeno, zdravi)
        self.Brneni = Brneni
    def ukot(self):
        if(random.randit(10,20) > 10):
            return