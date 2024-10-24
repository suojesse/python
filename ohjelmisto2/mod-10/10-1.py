class hissi:
    def __init__(self, alinkerrosnmr, ylinkerrosnmr):
        self.alinkerros = alinkerrosnmr
        self.ylinkerros = ylinkerrosnmr
        self.nykykerros = alinkerrosnmr

    def siirry(self, kerros):
        while self.nykykerros != kerros:
            if self.nykykerros < kerros:
                self.kerrosylös()
            else:
                self.kerrosalas()


    def kerrosylös(self):
        if self.nykykerros < self.ylinkerros:
            self.nykykerros += 1
            print(f"Hissi siirtyi kerroksen {self.nykykerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")


    def kerrosalas(self):
        if self.nykykerros > self.alinkerros:
            self.nykykerros -= 1
            print(f"Hissi siirtyi kerroksen {self.nykykerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")


if __name__ == "__main__":

    h = hissi(1, 10)

    h.siirry(5)

    h.siirry(1)
