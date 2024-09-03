bensa = int(input("Anna bensan määrä galloneissa: "))

def bensamaara():
    return bensa * 3.785

while True:
    if bensa <= 0 or bensa == "":
        break
    litrat = bensamaara()
    print("Galloni määrä minkä syötit on litroina:" , litrat)
    bensa = int(input("Anna bensan määrä galloneissa: "))
