n = []
while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luku = int(syote)
    n.append(luku)

pienin = min(n)
suurin = max(n)

print(pienin , suurin)