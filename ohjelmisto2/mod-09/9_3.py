class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekisteritunnus =rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenmuutos):
        uusi_nopeus = self.nopeus + nopeudenmuutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        kuljettu_matka = self.nopeus * tuntimaara
        self.matka += kuljettu_matka


if __name__ == "__main__":

    auto1 = Auto("ABC-123", 142)
    auto1.kiihdyta(60)

    print(f"Auton tämänhetkinen nopeus: {auto1.nopeus} km/h")
    print(f"Auton kulkema matka ennen ajamista: {auto1.matka} km")


    auto1.kulje(1.5)


    print(f"Auton kulkema matka ajon jälkeen: {auto1.matka} km")

