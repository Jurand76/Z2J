import numpy as np


class Board:
    def __init__(self):
        self.grid = np.zeros((12, 26), dtype=int)

    def check_in_console(self):
        for j in range(0, 26):
            for i in range(0, 12):
                print(self.grid[i][j], end='')
            print()

    def insert_block(self, x, y, block, sizeX, sizeY):
        for i in range(0, sizeX):
            for j in range(0, sizeY):
                try:
                    if block.grid[i][j] > 0:
                        self.grid[x + i][y + j] = block.grid[i][j]
                except:
                    pass

    def delete_block(self, x, y, block, sizeX, sizeY):
        for i in range(0, sizeX):
            for j in range(0, sizeY):
                try:
                    if block.grid[i][j] > 0:
                        self.grid[x + i][y + j] = 0
                except:
                    pass

    def can_move_left(self, x, y, block, sizeX, sizeY):
        result = True
        for i in range(0, sizeY):
            if x <= 0:
                if block.grid[0 - x][i] != 0:
                    result = False
        for j in range(0, sizeY):
            for i in range(0, sizeX - 1):
                if block.grid[i][j] != 0 and self.grid[x + i - 1][y + j] > 10:
                    # print(f"block.grid[{i}][{j}] = {block.grid[i][j]}, x = {x}")
                    # print(f"self.grid[{x-i-1}][{y+j}] = {self.grid[x-1-i][y+j]}")
                    result = False

        # print("result = ", result)
        return result

    def can_move_right(self, x, y, block, sizeX, sizeY):
        result = True
        print(" x = ", x, " y = ", y, " sizeX = ", sizeX)
        for i in range(0, sizeY):
            if x >= 12-sizeX:
                if block.grid[11-x][i] != 0:
                    result = False
        for j in range(0, sizeY):
            for i in range(0, sizeX - 1):
                if block.grid[i][j] != 0 and self.grid[x + i - 1][y + j] > 10:
                    # print(f"block.grid[{i}][{j}] = {block.grid[i][j]}, x = {x}")
                    # print(f"self.grid[{x-i-1}][{y+j}] = {self.grid[x-1-i][y+j]}")
                    result = False

        # print("result = ", result)
        return result
    def check_board(self):
        canMoveDown = True
        for j in range(0, 26):
            for i in range(0, 12):
                if 10 > self.grid[i][j] > 0:
                    if j == 25:
                        canMoveDown = False
                        return canMoveDown
                    if self.grid[i][j + 1] > 10:
                        canMoveDown = False
        return canMoveDown

    def delete_row(self, number):
        for i in range(0, 12):
            self.grid[i][number] = 0

        for j in range(0, number):
            for i in range(0, 12):
                self.grid[i][number - j] = self.grid[i][number - 1 - j]

        for i in range(0, 12):
            self.grid[i][0] = 0

    def upgrade_board(self):
        for j in range(0, 26):
            for i in range(0, 12):
                if 10 > self.grid[i][j] > 0:
                    self.grid[i][j] += 10

        for j in range(0, 26):
            completed = True
            for i in range(0, 12):
                if self.grid[i][j] == 0:
                    completed = False
            if completed:
                self.delete_row(j)
                completed = True

    def print_board_console(self):
        for j in range(0, 26):
            for i in range(0, 12):
                print(self.grid[i][j], end=' ')
            print()
