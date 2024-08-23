gender = input("Mies vai Nainen: ")

if gender == "Mies":
    hemo = int(input("Hemoglobiini arvosi: "))
    if 134<=hemo<=195:
        print("Hemoglobiini arvosi on normaalit.")
    elif hemo>195:
        print("Hemoglobiini arvosi on normaalia korkeammat.")
    else:
        print("Hemoglobiini arvosi on normaalia matalammat.")

if gender == "Nainen":
    hemo = int(input("Hemoglobiini arvosi: "))
    if 117<=hemo<=175:
        print("Hemoglobiini arvosi on normaalit.")
    elif hemo>175:
        print("Hemoglobiini arvosi on normaalia korkeammat.")
    else:
        print("Hemoglobiini arvosi on normaalia matalammat.")



