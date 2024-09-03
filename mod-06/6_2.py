import random

luku = int(input("Anna nopan maksimiluku: "))

def nopanheitto():
    return random.randint(1,luku)


while True:
    silmaluku = nopanheitto()
    print("Nopan silmäluku:" , silmaluku)
    if silmaluku == luku:
        break