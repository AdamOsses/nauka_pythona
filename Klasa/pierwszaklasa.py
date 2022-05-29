# pierwszaklasa.py - nauka pythona

class Paletka:
    pass

def testklasy():
    paletka_a = Paletka()
    print(f'Obiekt typu {type(paletka_a)} ma nast. metody:')
    print(dir(paletka_a)) # info o wszystkich defaultowych wlasciwosciach klasy
    # np __init__
