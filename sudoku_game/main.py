import random


def generate_numbers(size):
    table = []
    for i in range(1, size * size + 1):
        table.append(i)
    return table


def generate_one_sudoku(size):
    numbers = generate_numbers(size)
    sudoku_pow = size * size
    sudoku = []
    for i in range(1, sudoku_pow + 1):
        random_number = random.randint(1, sudoku_pow + 1 - i)
        sudoku.append(numbers[random_number - 1])
        numbers.remove(sudoku[i - 1])
    return sudoku

def check_sudoku(table, size):
    sum_list = []
    sum_1 = 0
    sum_2 = 0

    result = True

    for a in range(0, size):
        for b in range(0, size):
            sum_1 = sum_1 + table[a * size + b]
            sum_2 = sum_2 + table[a + b * size]
        sum_list.append(sum_1)
        sum_list.append(sum_2)
        sum_1 = 0
        sum_2 = 0

    for a in range(0, len(sum_list) - 1):
        if sum_list[a] != sum_list[a + 1]:
            result = False

    return result

def draw_board(table, size):
    for i in range(1, size ** 2 + 1):
        print(' ', end='')
        print(table[i - 1], ' ', end='')
        if table[i - 1] < 10:
            print(' ', end='')
        if i % size == 0:
            print()

input_str = input("Podaj szerokość planszy (2-20): ")
board_size = int(input_str)
input_str = input("Podaj ile wygenerować plansz(4/9/16/25): ")
board_count = int(input_str)

sudoku_board = generate_one_sudoku(board_size)
draw_board(sudoku_board, board_size)


if check_sudoku(sudoku_board, board_size):
    print("To jest poprawnie wykonane sudoku")
else:
    print("To nie jest poprawnie wykonane sudoku")
