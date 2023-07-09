import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sudoku = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def check_sudoku(table, size):
    sum_list = []
    sum_1 = 0
    sum_2 = 0

    result = True

    for a in range(0, size):
        for b in range(0, size):
            sum_1 = sum_1 + sudoku[a*size + b]
            sum_2 = sum_2 + sudoku[a+b*size]
        sum_list.append(sum_1)
        sum_list.append(sum_2)
        sum_1 = 0
        sum_2 = 0

    for a in range(0, len(sum_list)-1):
        if sum_list[a] != sum_list[a+1]:
            result = False

    return result

for i in range(1, 10):
    print(' ', end='')
    random_number = random.randint(1,10-i)
    sudoku[i-1] = numbers[random_number-1]
    print(sudoku[i-1],' ', end='')
    numbers.remove(sudoku[i-1])
    if i % 3 == 0:
        print()

if check_sudoku(sudoku, 3):
    print("To jest poprawnie wykonane sudoku")
else:
    print("To nie jest poprawnie wykonane sudoku")

