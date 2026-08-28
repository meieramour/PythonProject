import random

i = 1

while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1              #1

tuumat = float(input("Anna tuumien määrä: "))
while tuumat >= 0:
    cm = tuumat * 2.54
    print("Senttimetrienä:", cm)
    tuumat = float(input("Anna tuumien määrä: "))

print("Ohjelma päätyi.")                #2

luvut = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luvut.append(float(luku))

    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))               #3

oikea = random.randint(1, 10)
while True:
    arvo = input("Arvaa luku: ")
    if arvo > oikea:
        print("Liian suuri arvaus")
    elif arvo < oikea:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break               #4

kn = "python"
sls = "rules"
tory = 0
while tory < 5:
    kayt = input("Anna käyttäjänimi: ")
    sals = input("Anna salasana: ")
    if kayt == kn and sals == sls:
        print("Tervetuloa!")
        break
    tory += 1
    if tory == 5:
        print ("Pääsy evätty.")             #5


