import random

arpakuutio = int(input("Anna arpakuutioiden lukumäärän: "))
luku = []
for _ in range(arpakuutio):
    luku.append(random.randint(1, 6))
    n = sum(luku)
print("Heitit" , arpakuutio , "arpakuutiota joiden luvut olivat:" , luku)
print("Arpakuutioitten yhteissumma on:" , n)


