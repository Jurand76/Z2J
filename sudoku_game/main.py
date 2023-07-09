import random

def check_sudoku(table, size):
    sum_list = []
    sum_1 = 0
    sum_2 = 0

    result = True

    for a in range(0, size):
        for b in range(0, size):
            sum_1 = sum_1 + sudoku[a * size + b]
            sum_2 = sum_2 + sudoku[a + b * size]
        sum_list.append(sum_1)
        sum_list.append(sum_2)
        sum_1 = 0
        sum_2 = 0

    for a in range(0, len(sum_list) - 1):
        if sum_list[a] != sum_list[a + 1]:
            result = False

    return result


def generate_numbers(size):
    table = []
    for i in range(1, size * size + 1):
        table.append(i)
    return table


sudoku_size = 4
sudoku_pow = sudoku_size * sudoku_size
numbers = generate_numbers(sudoku_size)
sudoku = []

for i in range(1, sudoku_pow+1):
    print(' ', end='')
    random_number = random.randint(1, sudoku_pow+1-i)
    sudoku.append(numbers[random_number-1])
    print(sudoku[i - 1], ' ', end='')
    if sudoku[i-1] < 10:
        print(' ', end='')
    numbers.remove(sudoku[i - 1])
    if i % sudoku_size == 0:
        print()

if check_sudoku(sudoku, sudoku_size):
    print("To jest poprawnie wykonane sudoku")
else:
    print("To nie jest poprawnie wykonane sudoku")
