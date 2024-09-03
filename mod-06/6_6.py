
def laskin(pizza, hinta):
    sade = (pizza / 2) / 100
    pintaala = sade**2 * 3.14
    neliohinta = hinta / pintaala
    return neliohinta

def paaohjelma():
    pizza2 = float(input("Ensimmäisen pizzan halkaisija: "))
    hinta2 = float(input("Ensimmäisen pizzan hinta: "))

    pizza1 = float(input("Toisen pizzan halkaisija: "))
    hinta1 = float(input("Toisen pizzan hinta: "))

    neliohinta1 = laskin(pizza2, hinta2)
    neliohinta2 = laskin(pizza1, hinta1)

    print("Ensimmäisen pizzan neliöhinta on:" , neliohinta1 , "€")
    print("Toisen pizzan neliöhinta on:", neliohinta2 , "€")

    if neliohinta1 > neliohinta2:
        print("Toinen pizza on halvempi per neliömetri")
    elif neliohinta1 < neliohinta2:
        print("Ensimmäinen pizza on halvempi per neliömetri")

paaohjelma()


