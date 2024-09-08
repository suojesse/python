nimi = set()

while True:
    nimi1 = str(input("Anna nimi:"))
    if nimi1 == "":
        break
    if nimi1 in nimi:
        print("Aiemmin syötetty")
    else:
        print("Uusi nimi")
    nimi.add(nimi1)
for nimi1 in nimi:
    print(nimi1)