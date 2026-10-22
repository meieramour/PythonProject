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
autot = []
for i in range (1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100,200))
    autot.append(auto)
while not any(auto.matka >= 10000 for auto in autot):
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
print(f"{'Rekisteritunnus':<20}{'Huippunopeus':<20}{'Nopeus':<20}{'Matka':<20}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<20}{auto.huippunopeus:<20}{auto.nopeus:<20}{auto.matka:<20}")

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

