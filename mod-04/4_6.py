import random

p_maara = int(input("Kuinka monta pistettä arvotaan: "))

p = 0

for _ in range(p_maara):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        p += 1

likiarvo = 4 * p / p_maara

print("Piin likiarvo on: " , likiarvo)