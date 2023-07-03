# paper, rock, scissors - game

# no 1 - paper
# no 2 - rock
# no 3 - scissors

import random


# function converts numbers 1-3 to text paper, rock, scissors
def convert_to_text(number):
    if number == 1:
        return "paper"
    if number == 2:
        return "rock"
    if number == 3:
        return "scissors"


# random choose for computer player
def computer_choose():
    number = random.randint(1, 3)
    return number


# player choose from numbers 1-3 or q for quitting game
def player_choose():
    good_choice = False
    while not good_choice:
        text = input("What number do you choose (1-3, q to quit): ")
        if text.lower() == 'q':
            exit()
        try:
            number = int(text)
            if 1 <= number <= 3:
                good_choice = True
                return number
        except TypeError as e:
            print("Only 1-3 numbers allowed")


# checking who won round - player, computer or nobody
def player_won(pl, comp):
    if pl == comp:
        return 0
    if (pl == 1 and comp == 2) or (pl == 2 and comp == 3) or (pl == 3 and comp == 1):
        return 1
    else:
        return -1


# game rounds
def game(rounds):
    computer_wins = 0
    player_wins = 0
    for i in range(rounds):
        print(f'Round: {i + 1}')
        print('  Choose: ')
        print('     1 - paper')
        print('     2 - rock')
        print('     3 - scissors')
        player = player_choose()
        computer = computer_choose()
        print()
        print(f'Player has chosen  : {convert_to_text(player)}')
        print(f'Computer has chosen: {convert_to_text(computer)}')
        round_result = player_won(player, computer)
        if round_result == 0:
            print('  Round result: DRAW')
        if round_result == 1:
            print('  Round result: PLAYER WINS')
            player_wins += 1
        if round_result == -1:
            print('  Round result: COMPUTER WINS')
            computer_wins += 1
        print(f'TOTAL SCORE AFTER ROUND {i + 1} -> Player wins: {player_wins}, Computer wins: {computer_wins}')
        print()


# main code of game

print("Welcome to paper/rock/scissors game")
print()
how_many_rounds = input("How many rounds would you like play? (1-20): ")
try:
    number_of_rounds = int(how_many_rounds)
    game(number_of_rounds)
except ValueError as e:
    print("You can only choose numbers!")

print('GAME OVER!')
