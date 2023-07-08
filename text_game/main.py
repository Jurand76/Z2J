import random

etapy = ['pokoj', 'okno', 'stol', 'waga', 'kule']

def wybor(min, max):
    result = ''
    while result is not '0':
        result = input(f'Twoj wybor ({min}-{max} lub 0) :')
        if result == '0':
            print('Dziekuje za gre!')
            exit()
        else:
            return result


def opis(nazwa_pliku):
    f = open(nazwa_pliku)
    print(f.read())
    f.close()

class Kule:
    kule = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    def __init__(self):
        ciezsza = random.randint(1,9)
        self.kule[ciezsza] = 2

    def waga(self, numer):
        return self.kule[numer]


class Waga:
    liczba_wazen = 0

    def __init__(self):
        self.szalka_lewa = 0
        self.szalka_prawa = 0
        self.liczba_lewa = 0
        self.liczba_prawa = 0
    def wazenie(self):
        if (self.szalka_lewa == 0) and (self.szalka_prawa == 0):
            print("Szalki wagi są puste")
            return 0
        if self.szalka_lewa < self.szalka_prawa:
            self.liczba_wazen += 1
            return -1
        if self.szalka_lewa > self.szalka_prawa:
            self.liczba_wazen += 1
            return 1
        if self.szalka_lewa == self.szalka_prawa:
            self.liczba_wazen += 1
            return 0

    def doloz_z_lewej(self, ciezar):
        self.szalka_lewa = self.szalka_lewa + ciezar
        self.liczba_lewa += 1

    def doloz_z_prawej(self, ciezar):
        self.szalka_prawa = self.szalka_prawa + ciezar
        self.liczba_prawa += 1

    def zabierz_z_lewej(self, ciezar):
        if self.liczba_lewa > 0:
            self.szalka_lewa = self.szalka_lewa - ciezar
            self.liczba_lewa -= 1
        else:
            print("Nie ma nic na lewej szalce")

    def zabierz_z_prawej(self, ciezar):
        if self.liczba_prawa > 0:
            self.szalka_prawa = self.szalka_prawa - ciezar
            self.liczba_prawa -= 1
        else:
            print("Nie ma nic na prawej szalce")

    def zeruj_wage(self):
        self.szalka_lewa = 0
        self.szalka_prawa = 0


class Stol:
    liczba_kul = 0

    def __init__(self):
        self.liczba_kul = 9

    def zabierz_kule(self):
        if self.liczba_kul > 0:
            self.liczba_kul -= 1
            return 1
        else:
            print('Nie ma nic na stole')
            return 0

    def opisz_stol(self):
        print(f'Na stole jest następująca liczba kul: {self.liczba_kul}')

def zmien_pozycje():
    global poziom
    print('Co chcesz zrobić?')
    print('   1 - podejdź do okna')
    print('   2 - podejdź do stołu')
    print('   0 - zakończ grę')
    key = wybor(1, 2)
    if key == '1':
        poziom = etapy[1]
    if key == '2':
        poziom = etapy[2]

def jestes_w_pokoju():
    global poziom
    print('Jesteś w pokoju. Wybierz opcję:')
    print('   1 - opis pomieszczenia')
    print('   2 - zmień pozycję')
    print('   0 - zakończ grę')
    key = wybor(1, 2)
    if key == '1':
        opis('pokoj.txt')
    if key == '2':
        zmien_pozycje()

def jestes_przy_oknie():
    global poziom
    print('Jesteś przy oknie. Wybierz opcję:')
    print('   1 - opis przedmiotu')
    print('   2 - użyj przedmiotu')
    print('   3 - zmień pozycję')
    print('   0 - zakończ grę')
    key = wybor(1, 3)
    if key == '1':
        opis('okno.txt')
    if key == '2':
        print('Okno nie daje się otworzyć.')
    if key == '3':
        zmien_pozycje()

def jestes_przy_stole():
    global poziom
    print('Jesteś przy stole. Wybierz opcję:')
    print('   1 - opis przedmiotu')
    print('   2 - użyj przedmiotu')
    print('   3 - odejdź od stołu')
    print('   0 - zakończ grę')
    key = wybor(1, 3)
    if key == '1':
        opis('stol.txt')
    if key == '2':
        poziom = etapy[3]
    if key == '3':
        poziom = etapy[0]

poziom = etapy[0]

print('Witaj w grze')

while True:
    if poziom == etapy[0]:
        jestes_w_pokoju()
    if poziom == etapy[1]:
        jestes_przy_oknie()
    if poziom == etapy[2]:
        jestes_przy_stole()
