class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekisteritunnus = rekkari
        self.huippunopeus = huippunopeus

        self.nopeus=0
        self.matka=0

    def kiihdyta(self, nopeudenmuutos):
        uusi_nopeus = self.nopeus + nopeudenmuutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

if __name__ == '__main__':

    auto1 = Auto("ABC-123", 142)
    auto1.kiihdyta(30)
    auto1.kiihdyta(70)
    auto1.kiihdyta(50)

    print(f"Aton tämänhetkinen nopeus: {auto1.nopeus} km/h")

    auto1.kiihdyta(-200)


    print(f"Auton uusi nopeus hätäjarrutuken jälkeen: {auto1.nopeus} km/h")