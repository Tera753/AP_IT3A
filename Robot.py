class Robot:
    def __init__(self, jmeno:str, oznaceni:int, baterie:int, ukol:str = "Jím baterky"):
        self.jmeno = jmeno
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        pass

    def zvuk(self):
        return "píp píp"
    def diagnostika(self):
        return f"Mé označení je {self.oznaceni}, a mám {self.baterie}%."
    def ukol(self):
        return f"Muj ukol je {self.ukol}."
    def zadej_ukol(self, Nukol:str):
        self.Nukol = Nukol
        return f"Právě {Nukol}."
    
robot = Robot("Jimmy", 266, 45)
print(robot.jmeno)
print(robot.oznaceni)
print(robot.baterie)
print(robot.zvuk())
print(robot.diagnostika())
print(robot.ukol)
print(robot.zadej_ukol("šroubuji postel"))