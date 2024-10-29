class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = float(huippunopeus)
        self.nopeus = 0
        self.matkamittari = 0

    def aseta_nopeus(self, nopeus):
        self.nopeus = min(nopeus, self.huippunopeus)

    def aja(self, tunnit):
        self.matkamittari += self.nopeus * tunnit


class BensaAuto(Auto):
    def __init__(self, rekkari, huippunopeus, tankki):
        super().__init__(rekkari, huippunopeus)
        self.tankki = float(tankki)


class SahkoAuto(Auto):
    def __init__(self, rekkari, huippunopeus, akku):
        super().__init__(rekkari, huippunopeus)
        self.akku = float(akku)


if __name__ == "__main__":
    bensa_auto = BensaAuto("ABC-1", 165, 32.3)
    sahko_auto = SahkoAuto("ABC-2", 180, 52.5)

    bensa_auto.aseta_nopeus(130)
    sahko_auto.aseta_nopeus(180)

    bensa_auto.aja(3)
    sahko_auto.aja(3)

    print(f"Sähköauto ({sahko_auto.rekkari}) matkamittarilukema: {sahko_auto.matkamittari} km")
    print(f"Polttomoottoriauto ({bensa_auto.rekkari}) matkamittarilukema: {bensa_auto.matkamittari} km")