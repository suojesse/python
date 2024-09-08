kausi = (("kesä" , (6, 7, 8)),
        ("kevät" , (3, 4, 5)),
        ("syksy" , (9, 10, 11)),
        ("talvi" , (12, 1, 2))
)

kuunum = int(input("Anna kuukautesi numerona: "))

for aika, num in kausi:
    if kuunum in num:
        print("Kuukausi" , kuunum , "kuulu vuoden aikaan:" , aika)