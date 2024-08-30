luku = int(input("Anna kokonaisluku: "))

if luku > 1:

    for i in range(2, (luku//2)+1):

        if (luku % i) == 0:
            print(luku, "ei ole alkuluku")
            break
    else:
        print(luku, "on alkuluku")
else:
    print(luku, "ei ole alkuluku")