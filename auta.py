import random
from datetime import datetime 
class Car:
    def __init__(self, znacka:str, model:str, year:int, stkYear:int, fuel:int = 100):
        self.znacka = znacka
        self.model = model
        self.year = year
        self.stkYear = stkYear
        self.fuel = fuel
        pass

    def __str__(self):
        return f"{self.znacka} {self.model} ({self.year}) - palivo: {self.fuel}"
    
    def move(self):
        usage = random.randint(5, 20)
        if self.fuel >= usage:
            self.fuel -= usage
            return f"{self.znacka} {self.model} spotřeboval {usage} % paliva a zbývá mu {self.fuel}"
        else:
            return f"{self.znacka} {self.model} by do cíle nedojel. Potřeuje {usage} tolik aby dojel."

    def fullFill(self):
        filled = 100 - self.fuel
        self.fuel = 100
        return f"{self.znacka} {self.model} natankoval {filled} % paliva"
    
    def STK(self):
        if self.stkYear < datetime.now().year:
            return f"{self.znacka} {self.model} musí na technickou - technicka skoncila v roce {self.stkYear}"
        else:
            return f" {self.znacka} {self.model} na technickou bude muset za následující počet let: {self.stkYear - datetime.now().year}"


car1 = Car("Škoda", "Octavie 3", 2016, 2026, 85)
car2 = Car("Hyundai", "Getz", 2018, 2022, 3 )
car3 = Car("Toyota", "Hilux", 2014, 2028, 34)

print(car1,  car2,  car3)
print(70*"=")

#testování jízdy
print(car1.move())
print(car1.move())

print(70*"=")

print(car2.move())
print(car2.fullFill())
print(car2.move())

print(70*"=")

print(car3.move())
print(car3.move())

print(70*"=")

#testování stk
print(car1.STK())
print(car2.STK())
print(car3.STK())
print(70*"=")

class Garage:
    def __init__(self, name:str):
        self.name = name
        self.cars = []
        pass
    def addCar(self, car:Car):
        self.cars.append(car)
        return f" Do garáže {self.name} bylo přidáno auto: {car.znacka} {car.model}"
    def showCars(self):
        if len(self.cars) == 0:
            print(f"V garáži {self.name} není žádné auto")
        else:
            print(f"auta v garáži: {self.name}")
            for car in self.cars:
                print("-->", car)
            
    def oldestCar(self):
        if len(self.cars) == 0:
            return None

        theOldest = min(self.cars, key=lambda a: a.year)
        return theOldest

    def avgFuel(self):
        if len(self.cars) == 0:
            return 0
        return sum(Car.fuel for Car in self.cars)/len(self.cars)

    
garage= Garage("Orange county Choppers")
garage.showCars()
print(70*"=")
print(garage.addCar(car1))
print(garage.addCar(car2))
print(garage.addCar(car3))
print(70*"=")
garage.showCars()

print("==========================Nejstarší auto========================")
oldest = garage.oldestCar()
if oldest:
    print(f"nejstarší auto v garáži je: {oldest.znacka} {oldest.model}, ({oldest.year})")

print("====================Pruměsná hodnota paliva=========================")
print(f"{garage.avgFuel():.1f} %")

print("===============Jizda specifického auta v garáži=======================")
print(garage.cars[2].move())

print("=======================Jízda všech aut v garáži====================")
for JizdaAut in garage.cars:
    print(JizdaAut.move())

print("=====================Hromadná kontrola STK===========================")
for shroub in garage.cars:
    print(shroub.STK())