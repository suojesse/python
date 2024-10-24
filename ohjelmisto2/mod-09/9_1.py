class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekisteritunnus = rekkari
        self.huippunopeus = huippunopeus

        self.nopeus=0
        self.matka=0

auto1 = Auto("ABC-123", 142)
print("Auto-tyyppisen olion ominaisuudet:")
print(f"Rekkari: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus}")
print(f"Auton tämänhetkinen nopeus: {auto1.nopeus} km/h")
print(f"Auton kuljettu matka: {auto1.matka} km")
