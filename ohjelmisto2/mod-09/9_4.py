import random

class Auto:
    def __init__(self, rekkari):
        self.rekkari =rekkari
        self.huippunopeus = random.randint(100, 200)
        self.kuljettumatka = 0

    def kiihdyta(self):
        muutos = random.randint(-10, 15)
        self.huippunopeus = max(0, self.huippunopeus + muutos)

    def kulje(self):
        self.kuljettumatka += self.huippunopeus



if __name__ == "__main__":

    autot = [Auto(f"ABC-{i + 1}") for i in range(10)]

    while True:
        for auto in autot:
            auto.kiihdyta()
            auto.kulje()

            if auto.kuljettumatka >= 10000:
                print(f"{auto.rekkari} on voittanut kilpailun!")
                break
        else:
            continue
        break

    print(f"{'Rekisteritunnus' :<10} {'Huippunopeus (km/h)':<20} {'Kuljettu matka (km)':<20}")
    print("-" * 50)
    for auto in autot:
        print(f"{auto.rekkari:<10} {auto.huippunopeus:<20} {auto.kuljettumatka:<20}")