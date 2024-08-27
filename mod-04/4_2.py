mitta = int(input("Anna mitta tuumissa: "))

while mitta >= 0:
    print(mitta * 2.54 , "cm")
    mitta = int(input("Anna mitta tuumissa: "))
    if mitta < 0:
        exit()