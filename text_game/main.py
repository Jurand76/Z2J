import random
import stol
import waga
import kule

etapy = ['pokoj', 'okno', 'stol', 'waga', 'kule']


def wybor(min, max):
    result = ''
    while result != '0':
        result = input(f'Twoj wybor ({min}-{max} lub 0) :')
        if result == '0':
            print('Dziekuje za gre!')
            exit()
        else:
            return result


def opis(nazwa_pliku):
    f = open(nazwa_pliku, encoding='utf-8')
    print(f.read())
    f.close()


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
    print('   2 - użyj wagi')
    print('   3 - użyj kul')
    print('   4 - odejdź od stołu')
    print('   0 - zakończ grę')
    key = wybor(1, 4)
    if key == '1':
        opis('stol.txt')
        stol.opisz_stol()
    if key == '2':
        poziom = etapy[3]
    if key == '3':
        poziom = etapy[4]
    if key == '4':
        poziom = etapy[0]


def jestes_przy_wadze():
    global poziom
    print('Jesteś przy wadze. Wybierz opcję:')
    print('   1 - opis przedmiotu')
    print('   2 - użyj przedmiotu (ważenie)')
    print('   3 - zostaw wagę')
    print('   0 - zakończ grę')
    key = wybor(1, 3)
    if key == '1':
        opis('waga.txt')
        waga.opisz_stan_wagi()
    if key == '2':
        print("Uruchomiłeś wagę")
        wynik = waga.wazenie()
        if wynik == -1:
            print('Szalka lewa opadła na dół')
        if wynik == 1:
            print('Szalka prawa opadła na dół')
        if wynik == 0:
            print('Szalki nie poruszyły się')
    if key == '3':
        poziom = etapy[2]


def jestes_przy_kulach():
    global poziom
    global kule
    global waga
    print('Jesteś przy kulach. Wybierz opcję:')
    print('   1 - opis przedmiotu')
    print('   2 - połóż kulę na wadze')
    print('   3 - zdejmij wszystkie kule z wagi na stół')
    print('   4 - odejdź od kul i wróć do wagi')
    print('   5 - rozwiąż zadanie i zakończ grę')
    print('   0 - zakończ grę')
    key = wybor(1, 3)
    if key == '1':
        opis('kule.txt')
        stol.opisz_stol()
    if key == '2':
        numerkuli_str = input("Którą kulę chcesz położyć na wadze (1-9): ")
        numer_kuli = int(numerkuli_str)
        if stol.zabierz_kule(numer_kuli) > 0:
            szalka_str = input("Na którą szalkę wagi ją położyć (L - lewa, P-prawa): ")
            szalka = szalka_str.upper()
            if szalka == 'L':
                waga.doloz_z_lewej(kule.waga(numer_kuli))
            if szalka == 'P':
                waga.doloz_z_prawej(kule.waga(numer_kuli))
    if key == '3':
        stol.oddaj_kule()
        waga.zeruj_wage()
    if key == '4':
        poziom = etapy[3]
    if key == '5':
        numerkuli_str = input("Która kula jest cięższa od pozostałych (1-9): ")
        numer_kuli = int(numerkuli_str)
        if kule.waga(numer_kuli) == 2:
            print(f'To jest prawidłowa odpowiedź! Wykonałeś zadanie używając wagi {waga.ile_wazen()} razy')
            exit()
        else:
            print(f'To nie jest prawidłowa odpowiedź. Najcięższa jest kula nr')
            exit()

poziom = etapy[0]

print('Witaj w grze')

stol = stol.Stol()
waga = waga.Waga()
kule = kule.Kule()

while True:
    if poziom == etapy[0]:
        jestes_w_pokoju()
    if poziom == etapy[1]:
        jestes_przy_oknie()
    if poziom == etapy[2]:
        jestes_przy_stole()
    if poziom == etapy[3]:
        jestes_przy_wadze()
    if poziom == etapy[4]:
        jestes_przy_kulach()
