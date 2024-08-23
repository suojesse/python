eka_str = input("Anna leiviskät: ")
toka_str = input("Anna naulat: ")
kolmas_str = input("Anna luodit: ")
eka = float(eka_str)
tok = float(toka_str)
kolma = float(kolmas_str)
naulat = eka * 20
luodit = (tok + naulat) * 32
paino = (kolma + luodit) * 13.3

kilo = int(paino // 1000)
gramma = float(paino % 1000)
print("Massa nykymittojen mukaan: " + str(kilo) + "kg " + f"{gramma:.2f}g")