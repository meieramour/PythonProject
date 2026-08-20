import random

nimi = input('Kirjoita sunin nimesi: ');
print(f'Hei, {nimi}!');

r = float(input('Anna ympyrän säde: '));
pintaala = r**2 * 3,14;
print(f'Ympyrän pinta-ala: {pintaala}');

kanta = float(input('Suorakulmion kanta: '))
korkeus = float(input('Suorakulmion korkeus: '))
piiri = 2 * (kanta + korkeus)
ala = kanta * korkeus
print(f'Suorakulmion piiri: {piiri}');
print(f'Suorakulmion ala: {ala}'); #teht 2

luku1 = int(input('Kirjoita luku1: '));
luku2 = int(input('Kirjoita luku2: '));
luku3 = int(input('Kirjoita luku3: '));
summa = luku1 + luku2 + luku3;
tulo = luku1 * luku2 * luku3;
keskiarvo = (luku1 + luku2 + luku3) / 3;
print(f'Summa: {summa}');
print(f'Tulo: {tulo}');
print(f'Keskiarvo: {keskiarvo}');

leviska = float(input('Anna leviskät: '));
naulat = float(input('Anna naulat: '));
luoti = float(input('Anna luoti: '));
yhteensa = leviska * 20 * 32 + naulat * 32 + luoti
g = yhteensa * 13.3

kg = int(g // 1000)
loppu = g % 1000

print(f"Massa nykymittojen mukaan: ")
print(f"{kg} kilogrammaa ja {loppu} grammaa.")

x = random.randint(0,9)
y = random.randint(0,9)
z = random.randint(0,9)

l = random.randint(1,6)
u = random.randint(1,6)
k = random.randint(1,6)
u1 = random.randint(1,6)

print(f"{x}{y}{z}")
print(f"{l}{u}{k}{u1}")

