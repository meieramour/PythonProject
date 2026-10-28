class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros
    def kerros_ylös(self):
        if self.kerros >= self.ylin_kerros:
            pass
        else:
            self.kerros += 1
            print(self.kerros)
    def kerros_alas(self):
        if self.kerros <= self.alin_kerros:
           pass
        else:
            self.kerros -= 1
            print(self.kerros)
    def siirry_kerrokseen(self, kerros1):
        if kerros1 > self.ylin_kerros or kerros1 < self.alin_kerros:
            return
        while self.kerros < kerros1:
            self.kerros_ylös()
        while self.kerros > kerros1:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, h_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.h_lkm = []
        for i in range(1, h_lkm + 1):
            s = Hissi(alin_kerros, ylin_kerros)
            self.h_lkm.append(s)
    def aja_hissiä(self, h_numero, kerros1):
        f = 0
        while f < len(self.h_lkm):
            if f == h_numero - 1:
                self.h_lkm[f].siirry_kerrokseen(kerros1)
                break
            else:
                f += 1
    def palohälytys(self):
        for r in self.h_lkm:
            r.siirry_kerrokseen(self.alin_kerros)

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
t = Talo(2, 15, 6)
t.aja_hissiä(2, 11)
t.palohälytys()