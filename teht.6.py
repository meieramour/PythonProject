import random

def noppa():
    return random.randint(1,6)
luku = 0
while luku != 6:
    luku = noppa()
    print(luku)                     #1

def noppa(tahkot):
    return random.randint(1,tahkot)
tahkot = int(input("Tahkot : "))
luku = 0
while luku != tahkot:
    luku = noppa(tahkot)
    print(luku)                     #2

def muuta(gallona):
    return gallona * 3.785
gallona = float(input("Gallona : "))

while gallona >= 0:
    litrat = muuta(gallona)
    print(f"{litrat} litrat")
    gallona = float(input("Gallona : "))                    #3

def summa(numerot):
    summa = 0
    for numero in numerot:
        summa += numero
    return summa
lista = [3, 5, 7, 9]
tulos = summa(lista)
print(f"Summa: {tulos}")                    #4

def parittomat(numerot):
    lista1 = []
    for numero in numerot:
        if numero % 2 == 0:
            lista1.append(numero)
    return lista1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = parittomat(lista)
print(f"Vanha lista: {lista}")
print(f"Uusi lista: {lista2}")                   #5
