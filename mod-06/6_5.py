def numero(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

def paaohjelma():
    lista = [5,3,4,5,2,7,8,5,12]


    parilliset_luvut = numero(lista)
    print(lista)
    print(parilliset_luvut)


paaohjelma()