class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
class Kirja(Julkaisu):
    def __init__(self, nimi, krj, svm):
        super().__init__(nimi)
        self.krj = krj
        self.svm = svm
    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.krj)
        print(self.svm)
class Lehti(Julkaisu):
    def __init__(self, nimi, pt):
        super().__init__(nimi)
        self.pt = pt
    def tulosta_tiedot(self):
        print(self.nimi)
        print(self.pt)

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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akk):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akk = akk
class Polttomotooriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankki = tankki

l = Lehti("Aku Ankka", "Aki Hyyppä")
l.tulosta_tiedot()
k = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
k.tulosta_tiedot()
s = Sähköauto("ABC-15", 180, 52.5)
s.kiihdytä(109)
s.kulje(3)
print(s.matka)
p = Polttomotooriauto("ACD-123", 165, 32.3)
p.kiihdytä(76)
p.kulje(3)
print(p.matka)