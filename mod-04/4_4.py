import random

luku = random.randint(1, 10)

print("Arvaa luku 1-10 väliltä!")

while True:
    arvaus = int(input("Anna arvaus: "))
    if luku == arvaus:
        break
    elif luku > arvaus:
        print("Luku on suurempi!")
    elif luku < arvaus:
        print("Luku on pienempi!")

print("Arvasit oikein!")