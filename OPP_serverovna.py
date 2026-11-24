import random
from datetime import datetime
class Server:
    def __init__(self, hostname:str, os:str, deployYear:int, warrantyYear:int= 0, storageFree:int= 100):
        self.hostname = hostname
        self.os = os
        self.deployYear = deployYear
        self.warrantyYear = warrantyYear
        self.storageFree = storageFree
        pass

    def __str__(self):
        return f"{self.hostname} ({self.os}, {self.deployYear} -volné místo: {self.storageFree}%)"
        
    def saveData(self):
        potreba = random.randint(5, 20)

        if self.storageFree>= potreba:
            self.storageFree -= potreba
            zabrano = potreba
            return f"Na serveru {self.hostname} se uložila data (Zabrano {zabrano}%). Zbývá {self.storageFree}% volného místa."
        else:
            return f"Chyba: Na serveru {self.hostname} není místo! Potřeba{potreba}%, ale k dispozici je jen {self.storageFree}%"
        

    def cleanDisk(self):
        uvolneno = 100 - self.storageFree
        self.storageFree = 100
        return f"Disko na serveru {self.hostname} byly pročištěny. Uvolni se {uvolneno}% místa."
    
    def warrantyCheck(self):
        aktualni_rok = datetime.now().year
        if self.warrantyYear < aktualni_rok:
            return f"Varování: Server {self.hostname} je mimo záruku! Záruka vypršela v roce {self.warrantyYear}."
        else:
            zbyva_let = self.warrantyYear - aktualni_rok
            return f" Server {self.hostname} je v záruce. Zákurka končí za {zbyva_let} let."
        
class ServerRoom:
    def __init__(self,name):
        self.name = name
        self.servers = []
    
    def addServer(self, server):
        self.servers.append(server)
        print(f"Do serverovny {self.name} byl přidán server: {self.hostname}")

    def showServers(self):
        if len(self.servers) == 0:
            print("Seznam serveru je prázdný.")
        else:
            print(f"Servery {self.name}:")
            for server in self.servers:
                print(f"---> {server}")

    def oldestServer(self):
        if len(self.servers) == 0:
            return None
        theOldestServer = min(self.servers, key= lambda a: a.deployYear)
        return theOldestServer

    def avgStorage(self):
        if len(self.servers) == 0:
        return 0
    print = sum(Server.storageFree for server in self.servers) /len (self.servers)


    def fullServers(self, limit= 30):
        vysledek = []
        for server in self.servers:
            if server.sotageFree < limit:
                vysledek.append(server)
        return vysledek
    
    def serversForReplacement(self): 
        aktualni_rok = datetime.now().year
        vysledek =[]
        for server in self.servers:
            if server.warrantyYear < aktualni_rok:
                vysledek.append(server)
            return vysledek
        
    def countOS(self, targetOS):
        pocet = 0
        for server in self.servers:
            if server.os == targetOS:
                pocet += 1
        return pocet


        

print("------1. Vytvoření serverovny a přidání serveru------")
datacenter = ServerRoom("SOUEPL Datacentrum")
s1 = Server("Web-Main", "Ubuntu Linux",  2018, warrantyYear=2023, storageFree=80)
s2 = Server("DB-Cluster","Windows Server", 2021, warrantyYear=2030, storageFree=100)
s3 = Server("Backup-NAS", " Debian Linux", 2015, warrantyYear=2020, storageFree=15)

datacenter.addServer(s1)
datacenter.addServer(s2)
datacenter.addServer(s3)

print("------2. Výpis serverovny------")
print(f"Servery v {datacenter.name}:")