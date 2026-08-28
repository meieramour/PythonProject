import random

arpa = int(input("Anna noppien määrä: "))
sum = 0
for i in range(arpa):
    sum += random.randint(1, 6)
print("Silmälukujen summa: ", sum)              #1

luvut = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    luvut.append(float(luku))
luvut.sort(reverse=True)
for luku in luvut[:5]:
    print(luku)             #2

luku = int(input("Anna kokonaisluku: "))
if luku <2:
    print("Ei ole alkuluku.")
else:
    alkuluku = True
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("Alkuluku.")
    else:
        print("Ei ole alkuluku.")               #3

k = []
for i in range(5):
    k1 = input("Anna kaupunki: ")
    k.append(k1)
for k1 in k:
    print(k1)               #4
