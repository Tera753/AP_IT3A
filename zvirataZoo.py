import random
from datetime import datetime 

class Animal:
    def __init__(self, druh:str, name:str, birthYear:int, checkupYear: int = 0, energy: int = 100):
        self.druh = druh
        self.name = name
        self.birthYear = birthYear
        self.checkupYear = checkupYear
        self.energy = energy
        pass
    def __str__(self):
        return f"{self.druh} {self.name} ({self.birthYear}) - energie: {self.energy}"
    
    def play(self):
        usage = random.randint(5, 20)
        if self.energy >= usage:
            self.energy-= usage
            return f"{self.druh} {self.name} Spotřeboval pri hře {usage} % energie a zbývá mu{self.energy}"
        else:
            return f"{self.druh} {self.name} je moc unavený. Potřebuje {usage} % energie, ale má jen {self.energy} %"
        
    def feed(self):
        filled = 100 - self.energy
        self.energy = 100
        return f"{self.druh} {self.name} byl nakrmen a doplnil {filled} % energie."

    def vetCheck(self):
        if self.checkupYear < datetime.now().year:
            return f" {self.druh} {self.name} musí k veterináři - platnost prohlídky skončila v roce{self.checkupYear}"
        else:
            return f"{self.druh} {self.name} má prohlídku v pořádku. další kontrola bude za následující počet let: {self.checkupYear - datetime.now().year}"    


animal1 = Animal("Lev", "Monty", 2005, 2024)


print(animal1)