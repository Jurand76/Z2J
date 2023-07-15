import numpy as np
import random


class BlockI:
    def __init__(self):
        self.dim = 4
        self.grid = np.zeros((4, 4), dtype=int)
        self.grid[0][1] = 2
        self.grid[1][1] = 2
        self.grid[2][1] = 2
        self.grid[3][1] = 2

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)


class BlockL:
    def __init__(self):
        self.dim = 3
        self.grid = np.zeros((3, 3), dtype=int)
        self.grid[0][1] = 3
        self.grid[1][1] = 3
        self.grid[2][1] = 3
        self.grid[2][0] = 3

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)


class BlockJ:
    def __init__(self):
        self.dim = 3
        self.grid = np.zeros((3, 3), dtype=int)
        self.grid[0][1] = 4
        self.grid[1][1] = 4
        self.grid[2][1] = 4
        self.grid[2][2] = 4

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)


class BlockZ:
    def __init__(self):
        self.dim = 3
        self.grid = np.zeros((3, 3), dtype=int)
        self.grid[0][1] = 5
        self.grid[1][1] = 5
        self.grid[1][2] = 5
        self.grid[2][2] = 5

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)

class BlockS:
    def __init__(self):
        self.dim = 3
        self.grid = np.zeros((3, 3), dtype=int)
        self.grid[0][2] = 8
        self.grid[1][2] = 8
        self.grid[1][1] = 8
        self.grid[2][1] = 8

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)

class BlockT:
    def __init__(self):
        self.dim = 3
        self.grid = np.zeros((3, 3), dtype=int)
        self.grid[0][1] = 6
        self.grid[1][1] = 6
        self.grid[2][1] = 6
        self.grid[1][2] = 6

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)

class BlockR:
    def __init__(self):
        self.dim = 2
        self.grid = np.zeros((2, 2), dtype=int)
        self.grid[0][0] = 7
        self.grid[0][1] = 7
        self.grid[1][0] = 7
        self.grid[1][1] = 7

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)

def get_random_block():
    result = BlockI()
    number = random.randint(0, 6)
    if number == 0:
        result = BlockI()
    if number == 1:
        result = BlockT()
    if number == 2:
        result = BlockJ()
    if number == 3:
        result = BlockZ()
    if number == 4:
        result = BlockL()
    if number == 5:
        result = BlockR()
    if number == 6:
        result = BlockS()
    return result