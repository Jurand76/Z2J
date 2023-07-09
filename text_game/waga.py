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
        if self.szalka_lewa > self.szalka_prawa:
            self.liczba_wazen += 1
            return -1
        if self.szalka_lewa < self.szalka_prawa:
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

    def zeruj_wage(self):
        self.szalka_lewa = 0
        self.szalka_prawa = 0
        self.liczba_prawa = 0
        self.liczba_lewa = 0

    def ile_wazen(self):
        return self.liczba_wazen

    def opisz_stan_wagi(self):
        print(f'Na wadze na szalce lewej jest kul: {self.liczba_lewa}, na szalce prawej kul: {self.liczba_prawa}')
        print(f'Licznik ważen wskazuje: {self.liczba_wazen}')
