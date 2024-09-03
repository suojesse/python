import random

def nopanheitto():
    return random.randint(1,6)


while True:
    silmaluku = nopanheitto()
    print("Nopan silmäluku:" , silmaluku)
    if silmaluku == 6:
        break
