import random
import math


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


def draw_one_board(table, size):
    for i in range(0, size ** 2):
        print(' ', end='')
        print(table[i], ' ', end='')
        if table[i] < 10:
            print(' ', end='')
        if (i+1) % size == 0:
            print()


def draw_boards(tables, size, boards_count):

    width = int(math.sqrt(boards_count))
    spaces = size * width * 5 + 3 * width

    print("szerokosc: ",width)
    for c in range(0, width):
        for b in range(0, size):
            for a in range(0, width):
                for i in range(0, size):
                    print(' ', end='')
                    print(tables[a+c][i+b*size], ' ', end='')
                    if tables[a+c][i+b*size] < 10:
                        print(' ', end='')
                    if (i+1) % size == 0:
                        print(' | ', end='')
            print()
        for i in range(0, spaces):
            print('-', end='')
        print()


def generate_few_sudoku(size, number_of_boards):
    big_sudoku = []
    for i in range(0, number_of_boards):
        table = generate_one_sudoku(size)
        big_sudoku.append(table)
    return big_sudoku


input_str = input("Podaj szerokość planszy (2-20): ")
board_size = int(input_str)
input_str = input("Podaj ile wygenerować plansz(4/9/16/25): ")
board_count = int(input_str)

sudoku_board = generate_one_sudoku(board_size)
draw_one_board(sudoku_board, board_size)

if check_sudoku(sudoku_board, board_size):
    print("To jest poprawnie wykonane sudoku")
else:
    print("To nie jest poprawnie wykonane sudoku")

print()
sudoku_few_boards = generate_few_sudoku(board_size, board_count)
draw_boards(sudoku_few_boards, board_size, board_count)
