lista = []
kaupungit = 0
max_kaupungit = 5

kaupunki = input("Anna kaupunki: ")
lista.append(kaupunki)

while (kaupunki != "") and kaupungit < max_kaupungit -1:
    kaupungit += 1
    kaupunki = input("Anna kaupunki: ")
    lista.append(kaupunki)

for kaupunki in lista:
    print(kaupunki)

