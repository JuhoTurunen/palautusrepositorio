from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPSPeli:
    def __init__(self):
        self.tuomari = Tuomari()
        self.tekoaly = Tekoaly()
        self.parempi_tekoaly = TekoalyParannettu(10)
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    def pelaa(self):
        ekan_siirto, tokan_siirto = self.get_input()

        print(f"Tietokone valitsi: {tokan_siirto}")
        
        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(self.tuomari)

            ekan_siirto, tokan_siirto = self.get_input()

        print("Kiitos!")
        print(self.tuomari)
        
    def get_input(self):
        return 0, 0



