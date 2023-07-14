import pygame as pg
import math
import numpy as np

pg.init()

colors = []
value = (0, 0, 0)
colors.append(value)  # 0 - black
value = (20, 20, 20)
colors.append(value)  # 1 - gray
value = (255, 0, 0)   # 2 - red
colors.append(value)
value = (0, 255, 0)   # 3 - green
colors.append(value)
value = (0, 0, 255)   # 4 - blue
colors.append(value)


def grid_background(scr, color, color_back, size, grid):
    global colors

    for i in range(0, 12):
        for j in range(0, 26):
            pg.draw.rect(scr, color, pg.Rect(i * size, j * size, size, size))
            if grid[i][j] < 10:
                pg.draw.rect(scr, colors[grid[i][j]], pg.Rect(i * size + 1, j * size + 1, size - 2, size - 2))
            else:
                pg.draw.rect(scr, colors[grid[i][j]-10], pg.Rect(i * size + 1, j * size + 1, size - 2, size - 2))

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
                self.grid[x+i][y+j] = block.grid[i][j]

class BlockI:
    def __init__(self):
        self.grid = np. zeros((4, 4), dtype=int)
        self.grid[0][1] = 2
        self.grid[1][1] = 2
        self.grid[2][1] = 2
        self.grid[3][1] = 2

    def rotate(self):
        self.grid = np.rot90(self.grid, 1)

FPS = 60
screen = pg.display.set_mode((480, 1040))
screen.fill((0, 0, 0))

board = Board()

block = BlockI()

x = 4
y = 0

board.insert_block(x, y, block, 4, 4)

running = True
while running:
    pg.time.Clock().tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit()
        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_s]:
                print("S")
                y = y + 1
            if pg.key.get_pressed()[pg.K_w]:
                print("W")
            if pg.key.get_pressed()[pg.K_a]:
                print("A")
                x = x - 1
            if pg.key.get_pressed()[pg.K_d]:
                print("D")
                x = x + 1
            if pg.key.get_pressed()[pg.K_SPACE]:
                print("Space")
                block.rotate()
                board.insert_block(x, y, block, 4, 4)

    screen.fill((0, 0, 0))
    grid_background(screen, (50, 50, 50), colors[1], 40, board.grid)
    pg.display.update()
