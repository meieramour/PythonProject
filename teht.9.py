import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tunnit):
        matka1 = tunnit * self.nopeus
        self.matka += matka1
class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
    def tunti_kuluu(self):
        for a in self.autot:
            a.kiihdytä(random.randint(-10, 15))
            a.kulje(1)
    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<20}{'Huippunopeus':<20}{'Nopeus':<20}{'Matka':<20}")
        for b in self.autot:
            print(f"{b.rekisteritunnus:<20}{b.huippunopeus:<20}{b.nopeus:<20}{b.matka:<20}")
    def kilpailu_ohi(self):
        for c in self.autot:
            if c.matka >= self.pituus:
                return True
        return False

autot = []
for i in range (1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100,200))
    autot.append(auto)
k = Kilpailu("Suuri romuralli", 8000, autot)
tt = 0
while not k.kilpailu_ohi():
    k.tunti_kuluu()
    tt += 1
    if tt % 10 == 0:
        k.tulosta_tilanne()
k.tulosta_tilanne()
fAuto = Auto("ABC-123", 142)
print(fAuto.rekisteritunnus)
print(fAuto.huippunopeus)
print(fAuto.nopeus)
print(fAuto.matka)                          #1

fAuto.kiihdytä(30)
fAuto.kiihdytä(70)
fAuto.kiihdytä(50)
print(fAuto.nopeus)
fAuto.kiihdytä(-200)
print(fAuto.nopeus)

fAuto.kiihdytä(60)
fAuto.kulje(1.5)
print(fAuto.matka)

