class Robot:
    def __init__(self, oznaceni, baterie):
        self.oznaceni = oznaceni
        self.baterie = baterie

    def hlaseni_stavu(self):
        return f"{self.oznaceni}: baterie {self.baterie} %."

    def proved_misi(self):
        return "Čekám na zadání souřadnic."

    def nabij_baterii(self):
        self.baterie = 100
        return f"{self.oznaceni} je nabitý na 100 %."


class Kvadrokoptera(Robot):
    def __init__(self, oznaceni, baterie, max_vyska):
        super().__init__(oznaceni, baterie)
        self.max_vyska = max_vyska

    def proved_misi(self):
        if self.baterie >= 25:
            self.baterie -= 25
            return f"Dron letí do výšky {self.max_vyska} m a pořizuje snímky."
        return "Dron nemá dostatek baterie ke vzletu."


class PruzkumnyPasak(Robot):
    def __init__(self, oznaceni, baterie, ma_termokameru):
        super().__init__(oznaceni, baterie)
        self.ma_termokameru = ma_termokameru

    def proved_misi(self):
        if self.baterie < 15:
            return "Pásový rover nemá dostatek baterie."
        self.baterie -= 15
        zprava = "Rover projíždí těžkým terénem."
        if self.ma_termokameru:
            zprava += " Skenuje teplo termokamerou."
        return zprava


dron = Kvadrokoptera("Dron", 100, 120)
rover = PruzkumnyPasak("Rover", 80, True)
roboti = [dron, rover]

for robot in roboti:
    print(robot.proved_misi())
    print(robot.hlaseni_stavu())
    print(robot.nabij_baterii())
    print()
