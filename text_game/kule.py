import random
class Kule:
    kule = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    def __init__(self):
        ciezsza = random.randint(1, 9)
        self.kule[ciezsza-1] = 2

    def waga(self, numer):
        return self.kule[numer-1]
