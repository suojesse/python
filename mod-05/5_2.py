n = []
while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luku = int(syote)
    n.append(luku)

n.sort(reverse=True)
print(n[0:5])
