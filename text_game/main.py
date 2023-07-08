def wybor():
    result = ''
    while result is not '0':
        result = input('Twoj wybor (1-3 lub 0) :')
        if result == '0':
            print('Dziekuje za gre!')
            exit()
        if (result is not '1') and (result is not '2') and (result is not '3'):
            print('Nie ma takiej opcji')
        else:
            return result

def opis_pomieszczenia():
    print("Znajdujesz się w pokoju, na środku pokoju jest stół, a na nim waga")
    print("Waga ma dwie szalki. Jeśli na którejś z nich leży cięższy przedmiot - szalka idzie w dół.")
    print("Obok wagi jest 9 tak samo wyglądających kul. Jedna z kul jest odrobinę cięższa od pozostałych.")
    print("Znajdź najcięższą kulę.")

class Kula:
    def __init__(self, numer, waga):
        self.numer = numer
        self.waga = waga

class Waga:
    def __init__(self, szalka_lewa, szalka_prawa):
        self.szalka_lewa = szalka_lewa
        self.szalka_prawa = szalka_prawa

    def wazenie(self):
        if self.szalka_lewa < self.szalka_prawa:
            return -1
        if self.szalka_lewa > self.szalka_prawa:
            return 1
        if self.szalka_lewa == self.szalka_prawa:
            return 0

    def doloz_z_lewej(self, ciezar):
        self.szalka_lewa = self.szalka_lewa + ciezar

    def doloz_z_prawej(self, ciezar):
        self.szalka_prawa = self.szalka_prawa + ciezar

    def zeruj_wage(self):
        self.szalka_lewa = 0
        self.szalka_prawa = 0



print('Witaj w grze')
print('Wybierz opcję:')
print('   1 - opis pomieszczenia')
print('   2 - zabierz przedmiot')
print('   3 - użyj przedmiot')
print('   0 - zakończ grę')

key = wybor()
print(key)







