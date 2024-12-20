from kps_peli import KPSPeli


def main():
    pelimuodot = {
        "a": KPSPelaajaVsPelaaja,
        "b": KPSTekoaly,
        "c": KPSParempiTekoaly,
    }
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        if vastaus in ["a", "b", "c"]:
            pelimuoto = pelimuodot[vastaus]()
            pelimuoto.pelaa()
        else:
            break


class KPSPelaajaVsPelaaja(KPSPeli):
    def get_input(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return ekan_siirto, tokan_siirto


class KPSTekoaly(KPSPeli):
    def get_input(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return ekan_siirto, tokan_siirto


class KPSParempiTekoaly(KPSPeli):
    def get_input(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.parempi_tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self.parempi_tekoaly.aseta_siirto(ekan_siirto)
        return ekan_siirto, tokan_siirto


if __name__ == "__main__":
    main()
