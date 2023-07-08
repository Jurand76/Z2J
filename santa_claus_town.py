class Position:
    pos_x = 0
    pos_y = 0

    def set_position(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y

    def get_position(self):
        return self.pos_x, self.pos_y


class SantaClaus(Position):
    # initialization
    def __init__(self, name, age, gifts_counter, pos_x, pos_y):
        self.name = name
        self.age = age
        self.gifts_counter = gifts_counter
        self.pos_x = pos_x
        self.pos_y = pos_y

    # give package with gift
    def give_gift(self):
        if self.gifts_counter > 0:
            self.gifts_counter -= 1
            return "This surprise gift is for you"
        else:
            return "Try next year"

    # take package
    def pickup_gift(self, number):
        self.gifts_counter = self.gifts_counter + number

    # move to another child
    def move_to_another_place(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    # look for child in exact place with position x, y
    def look_for_child(self, ch_pos_x, ch_pos_y):
        if ch_pos_x == self.pos_x and ch_pos_y == self.pos_y:
            return True
        else:
            return False

    # where are you?
    def return_position(self):
        return self.pos_x, self.pos_y


class Child(Position):
    # initialization
    def __init__(self, name, age, pos_x, pos_y):
        self.name = name
        self.age = age
        self.pos_x = pos_x
        self.pox_y = pos_y

    # say thanks to Santa Claus
    def thank_you_gift(self):
        return "Thanks Santa Claus"

    # introduce yourself with name and age
    def introduce_yourself(self):
        print(f'My name is {self.name}, I am {self.age} years old.')


class Elven:
    gifts_produced = 0

    # initialization
    def __init__(self, name):
        self.name = name

    # create new gift
    def produce_gift(self):
        self.gifts_produced += 1

    # give all produced gifts
    def gifts_to_take(self):
        return self.gifts_produced


class Reindeer:
    # initialization
    def __init__(self, name):
        self.name = name


class ToothFairy(Position):
    # initialization
    def __init__(self, cash):
        self.cash = cash

    # try to pick up tooth
    def take_tooth(self, payment):
        if payment <= self.cash:
            print("Thanks for you tooth.")
            self.cash = self.cash - payment
            return True
        else:
            print("Sorry, this tooth is too expensive")
            return False

    # are you rich enough for picking up teeth?
    def how_much_cash(self):
        return self.cash

    # if no - take cash from bank
    def take_cash_from_bank(self, withdrawal):
        self.cash = self.cash + withdrawal


