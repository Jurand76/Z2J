import pygame as pg
import math
import numpy as np
import colors as c
import blocks


pg.init()


def grid_background(scr, color, color_back, size, grid):
    global colors

    for i in range(0, 12):
        for j in range(0, 26):
            pg.draw.rect(scr, color, pg.Rect(i * size, j * size, size, size))
            if grid[i][j] < 10:
                pg.draw.rect(scr, c.colors[grid[i][j]], pg.Rect(i * size + 1, j * size + 1, size - 2, size - 2))
            else:
                pg.draw.rect(scr, c.colors[grid[i][j]-10], pg.Rect(i * size + 1, j * size + 1, size - 2, size - 2))

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


FPS = 60
screen = pg.display.set_mode((480, 1040))
screen.fill((0, 0, 0))

board = Board()

block = blocks.get_random_block()

x = 4
y = 0
speed = 30
step = 0

board.insert_block(x, y, block, block.dim, block.dim)

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
                board.delete_block(x, y, block, block.dim, block.dim)
                y = y + 1
                for a in range(0, block.dim):
                    try:
                        board.grid[x+a][y-1] = 0
                    except:
                        pass

            if pg.key.get_pressed()[pg.K_a]:
                board.delete_block(x, y, block, block.dim, block.dim)
                x = x - 1
                for a in range(0, block.dim):
                    try:
                        board.grid[x + block.dim][y + a] = 0
                    except:
                        pass
            if pg.key.get_pressed()[pg.K_d]:
                board.delete_block(x, y, block, block.dim, block.dim)
                x = x + 1
                for a in range(0, block.dim):
                    try:
                        board.grid[x -1][y + a] = 0
                    except:
                        pass
            if pg.key.get_pressed()[pg.K_SPACE]:
                print("Space")
                board.delete_block(x, y, block, block.dim, block.dim)
                block.rotate()

    step += 1
    if step >= speed:
        step = 0
        board.delete_block(x, y, block, block.dim, block.dim)
        y = y + 1
        for a in range(0, block.dim):
            try:
                board.grid[x + a][y - 1] = 0
            except:
                pass

    if not board.check_board():
        print('Next klocek')
        if y > 0:
            board.upgrade_board()
            block = blocks.get_random_block()
            y = 0
            x = 4
        else:
            print('Game over')

    screen.fill((0, 0, 0))
    grid_background(screen, (50, 50, 50), c.colors[1], 40, board.grid)
    board.insert_block(x, y, block, block.dim, block.dim)
    pg.display.update()
