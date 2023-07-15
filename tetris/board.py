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
                        self.grid[x+i][y+j] = block.grid[i][j]
                except:
                    pass

    def delete_block(self, x, y, block, sizeX, sizeY):
        for i in range(0, sizeX):
            for j in range(0, sizeY):
                try:
                    if block.grid[i][j] > 0:
                        self.grid[x+i][y+j] = 0
                except:
                    pass

    def check_board(self):
        canMoveDown = True
        for j in range(0, 26):
            for i in range(0, 12):
                if 10 > self.grid[i][j] > 0:
                    if j == 25:
                        print('Down od board')
                        canMoveDown = False
                        return canMoveDown
                    if self.grid[i][j+1] > 10:
                        canMoveDown = False
                        print('Cannot move lower - another block')
        return canMoveDown

    def upgrade_board(self):
        for j in range(0, 26):
            for i in range(0, 12):
                if 10 > self.grid[i][j] > 0:
                    self.grid[i][j] += 10