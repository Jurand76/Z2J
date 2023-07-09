class Stol:
    liczba_kul = 0

    def __init__(self):
        self.liczba_kul = 9
        self.kule_na_stole = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    def zabierz_kule(self, number):
        if self.liczba_kul > 0:
            if self.kule_na_stole[number-1] == 0:
                print("Ta kula jest już na wadze")
                return 0
            self.liczba_kul -= 1
            self.kule_na_stole[number-1] = 0
            return number
        else:
            print('Nie ma żadnej kuli na stole')
            return 0

    def oddaj_kule(self):
        self.kule_na_stole = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.liczba_kul = 9

    def opisz_stol(self):
        if self.liczba_kul > 0:
            print(f'Na stole jest następująca liczba kul: {self.liczba_kul}')
            print(f'Ich numery to: ', end='')
            for i in range(len(self.kule_na_stole)):
                if self.kule_na_stole[i] == 1:
                    print(i+1, ', ', end='')
            print()
        if self.liczba_kul < 9:
            print('Reszta kul leży na szalkach wagi')