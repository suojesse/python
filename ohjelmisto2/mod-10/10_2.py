class Hissi:
    def __init__(self, alinkerrosnmr, ylinkerrosnmr):
        self.alinkerros = alinkerrosnmr
        self.ylinkerros = ylinkerrosnmr
        self.nyky_kerros = alinkerrosnmr

    def siirry_kerrokseen(self, kerros):

        while self.nyky_kerros != kerros:
            if self.nyky_kerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.nyky_kerros < self.ylinkerros:
            self.nyky_kerros += 1
            print(f"Hissi siirtyi kerrokseen {self.nyky_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nyky_kerros > self.alinkerros:
            self.nyky_kerros -= 1
            print(f"Hissi siirtyi kerrokseen {self.nyky_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


class Talo:
    def __init__(self, alinkerrosnmr, ylinkerrosnmr, hissien_lkm):
        self.alinkerros = alinkerrosnmr
        self.ylinkerros = ylinkerrosnmr
        # Luodaan lista hissejä
        self.hissit = [Hissi(alinkerrosnmr, ylinkerrosnmr) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohdekerros):
        if 1 <= hissi_numero <= len(self.hissit):
            hissi = self.hissit[hissi_numero - 1]
            print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohdekerros}.")
            hissi.siirry_kerrokseen(kohdekerros)


if __name__ == "__main__":
    talo = Talo(1, 10, 2)
    talo.aja_hissiä(1, 5)
    talo.aja_hissiä(2, 8)
