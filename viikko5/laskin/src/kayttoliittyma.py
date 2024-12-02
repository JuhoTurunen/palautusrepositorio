from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
            Komento.KUMOA: Kumoa(sovelluslogiikka)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except Exception:
            pass
    
    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        """ 
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except Exception:
            pass

        if komento == Komento.SUMMA:
            self._sovelluslogiikka.plus(arvo)
        elif komento == Komento.EROTUS:
            self._sovelluslogiikka.miinus(arvo)
        elif komento == Komento.NOLLAUS:
            self._sovelluslogiikka.nollaa()
        elif komento == Komento.KUMOA:
            pass
        """
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
class Summa:
    def __init__(self, logiikka, input):
        self.logiikka = logiikka
        self.input = input

    def suorita(self):
        self.logiikka.plus(self.input())

class Erotus:
    def __init__(self, logiikka, input):
        self.logiikka = logiikka
        self.input = input

    def suorita(self):
        self.logiikka.miinus(self.input())
        
class Nollaus:
    def __init__(self, logiikka):
        self.logiikka = logiikka

    def suorita(self):
        self.logiikka.nollaa()
        
class Kumoa:
    def __init__(self, logiikka):
        self.logiikka = logiikka
        self.input = input

    def suorita(self):
        pass