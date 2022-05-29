# pierwszaklasa.py - nauka pythona

class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")

    def info(self):
        print(f"Kolor obiektu to: {self.kolor_obiektu}")

    def info_ex(self, nazwa):
        print(f"Kolor obiektu {nazwa} to: {self.kolor_obiektu}")




def testklasy():
    paletka_a = Paletka("czerwony")
    paletka_b = Paletka("niebieski")
    print("****************************************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_a))
    print("****************************************************")
    print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_b))
    print("****************************************************")
    print(f"Kolor dla paletka_a: {paletka_a.kolor_obiektu}")
    print(f"Kolor dla paletka_b: {paletka_b.kolor_obiektu}")

    paletka_a.info()
    paletka_b.info()
    paletka_a.info_ex("Paletka_a")
    paletka_b.info_ex("Paletka_b")
