vuosi = int(input("Anna vuosiluku: "))

if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(str(vuosi) + " Tämä vuosi on karkausvuosi.")
else:
    print(str(vuosi) + " Tämä vuosi ei ole karkausvuosi.")
