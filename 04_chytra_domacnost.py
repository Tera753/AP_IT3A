class ChytreZarizeni:
    def __init__(self, nazev, mistnost, zapnuto=False):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto

    def prepni_stav(self):
        self.zapnuto = not self.zapnuto
        if self.zapnuto:
            return f"{self.nazev} je zapnuto."
        return f"{self.nazev} je vypnuto."

    def proved_akci(self):
        return "Zařízení čeká na příkaz."


class ChytraZarovka(ChytreZarizeni):
    def __init__(self, nazev, mistnost, barva="bílá"):
        super().__init__(nazev, mistnost)
        self.barva = barva

    def proved_akci(self):
        if self.zapnuto:
            return f"Žárovka svítí barvou {self.barva}."
        return "Je zhasnuto."

    def zmen_barvu(self, nova_barva):
        self.barva = nova_barva
        return f"Barva změněna na {nova_barva}."


class ChytraZasuvka(ChytreZarizeni):
    def __init__(self, nazev, mistnost, aktualni_odber_w):
        super().__init__(nazev, mistnost)
        self.aktualni_odber_w = aktualni_odber_w

    def proved_akci(self):
        if self.zapnuto:
            return f"Zásuvka propouští proud. Odběr: {self.aktualni_odber_w} W."
        return "Zásuvka je vypnutá."


domacnost = [
    ChytraZarovka("Žárovka", "Obývák"),
    ChytraZasuvka("Zásuvka", "Kuchyň", 60)
]

for zarizeni in domacnost:
    print(zarizeni.prepni_stav())
    print(zarizeni.proved_akci())
    print()
