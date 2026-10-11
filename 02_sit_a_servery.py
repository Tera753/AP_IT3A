class SitoveZarizeni:
    def __init__(self, nazev, ip_adresa, online=False):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online

    def zmen_stav(self):
        self.online = not self.online
        if self.online:
            return f"{self.nazev} je nyní online."
        return f"{self.nazev} je nyní offline."

    def diagnostika(self):
        return "Spouštím obecnou diagnostiku zařízení..."


class Router(SitoveZarizeni):
    def __init__(self, nazev, ip_adresa, pocet_portu, online=False):
        super().__init__(nazev, ip_adresa, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return super().diagnostika() + " Kontroluji LAN porty."

    def restartuj_wifi(self):
        return "Wi-Fi byla restartována."


class Server(SitoveZarizeni):
    def __init__(self, nazev, ip_adresa, os, online=False):
        super().__init__(nazev, ip_adresa, online)
        self.os = os

    def diagnostika(self):
        return super().diagnostika() + " Kontroluji vytížení CPU a stav disků."


router = Router("Router", "192.168.1.1", 4)
server = Server("Server", "192.168.1.10", "Ubuntu")
site = [router, server]

for zarizeni in site:
    print(zarizeni.zmen_stav())
    print(zarizeni.diagnostika())
    print()
