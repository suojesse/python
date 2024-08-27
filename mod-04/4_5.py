yritykset = 0

maks_yritykset = 5

user = input("Enter your name: ")
password = input("Enter your password: ")


while (user != "python" and password != "rules") and yritykset < maks_yritykset -1:
    yritykset += 1
    user = input("Enter your name: ")
    password = input("Enter your password: ")

if user == "python" and password == "rules":
    print("Tervetuloa!")
else:
    print("Pääsy evätty!")
