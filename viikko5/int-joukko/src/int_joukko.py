KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if kapasiteetti <= 0 or kasvatuskoko <= 0:
            raise ValueError("Kapasiteetin ja kasvatuskoon on oltava positiivisia kokonaislukuja.")
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm >= len(self.ljono):
            uusi_koko = len(self.ljono) + self.kasvatuskoko
            uusi_ljono = self._luo_lista(uusi_koko)
            self.kopioi_lista(self.ljono, uusi_ljono)
            self.ljono = uusi_ljono

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1
        return True

    def poista(self, n):
        for i in range(self.alkioiden_lkm):
            if self.ljono[i] == n:
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]
                self.ljono[self.alkioiden_lkm - 1] = 0
                self.alkioiden_lkm -= 1
                return True
        return False

    def kopioi_lista(self, src, dest):
        for i in range(len(src)):
            dest[i] = src[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        result = self._luo_lista(self.alkioiden_lkm)
        for i in range(self.alkioiden_lkm):
            result[i] = self.ljono[i]
        return result

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        for n in a.to_int_list():
            yhdiste.lisaa(n)
        for n in b.to_int_list():
            yhdiste.lisaa(n)
        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        b_list = b.to_int_list()
        for n in a.to_int_list():
            if n in b_list:
                leikkaus.lisaa(n)
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        b_set = set(b.to_int_list())
        for n in a.to_int_list():
            if n not in b_set:
                erotus.lisaa(n)
        return erotus

    def __str__(self):
        elements = ", ".join(str(self.ljono[i]) for i in range(self.alkioiden_lkm))
        return "{" + elements + "}"
