import pygame as pg
import math
import numpy as np
import colors as c
import blocks
import board


def grid_background(scr, color, color_back, size, grid, movepixels):
    global colors

    for i in range(0, 12):
        for j in range(0, 26):
            pg.draw.rect(scr, color, pg.Rect(i * size, j * size, size, size))
            if grid[i][j] < 10:
                pg.draw.rect(scr, c.colors[grid[i][j]], pg.Rect(i * size + 1, j * size + 1, size - 2, size - 2))
            else:
                pg.draw.rect(scr, c.colors[grid[i][j] - 10], pg.Rect(i * size + 1, j * size + 1, size - 2, size - 2))

    pg.draw.rect(scr, c.colors[1], pg.Rect(0, 1040, 480, 1080))

def game_start(scr, FPS, board):
    font = pg.font.Font('freesansbold.ttf', 24)
    font_big = pg.font.Font('freesansbold.ttf', 48)
    block = blocks.get_random_block()
    x = 4
    y = 0
    speed = 30
    step = 0
    blocks_counter = 0
    board.insert_block(x, y, block, block.dim, block.dim)
    manually_moved = False
    running = True
    while running:
        pg.time.Clock().tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False
                exit()

            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]:
                    board.delete_block(x, y, block, block.dim, block.dim)
                    manually_moved = True

                if pg.key.get_pressed()[pg.K_a] or pg.key.get_pressed()[pg.K_LEFT]:
                    if board.can_move_left(x, y, block, block.dim, block.dim):
                        board.delete_block(x, y, block, block.dim, block.dim)
                        x = x - 1
                        for a in range(0, block.dim):
                            try:
                                board.grid[x + block.dim][y + a] = 0
                            except:
                                pass

                if pg.key.get_pressed()[pg.K_d] or pg.key.get_pressed()[pg.K_RIGHT]:
                    if board.can_move_right(x, y, block, block.dim, block.dim):
                        board.delete_block(x, y, block, block.dim, block.dim)
                        x = x + 1
                        for a in range(0, block.dim):
                            try:
                                board.grid[x - 1][y + a] = 0
                            except:
                                pass

                if pg.key.get_pressed()[pg.K_SPACE]:
                    board.delete_block(x, y, block, block.dim, block.dim)
                    block.rotate()

                if pg.key.get_pressed()[pg.K_b]:
                    board.print_board_console()

        step += 1

        if step >= speed or manually_moved:
            step = 0
            board.delete_block(x, y, block, block.dim, block.dim)
            y = y + 1

        manually_moved = False

        # checking if block is on another block, at bottom of board or there is one or more lines filled
        if not board.check_board():
            if y > 0:
                board.upgrade_board()
                block = blocks.get_random_block()
                blocks_counter += 1
                if blocks_counter % 20 == 0:
                    speed -= 2
                y = 0
                x = 4
            else:
                print('Game over')
                running = False

        scr.fill((0, 0, 0))
        grid_background(scr, (50, 50, 50), c.colors[1], 40, board.grid, 140)
        board.insert_block(x, y, block, block.dim, block.dim)
        text = font.render(f'Score: {board.score}', True, c.colors[6], c.colors[1])
        text2 = font.render(f'Speed: {30 - speed}', True, c.colors[7], c.colors[1])
        textRect = text.get_rect()
        text2Rect = text2.get_rect()
        textRect.center = (80, 1060)
        text2Rect.center = (400, 1060)
        scr.blit(text, textRect)
        scr.blit(text2, text2Rect)
        pg.display.update()

    text = font_big.render(f'GAME OVER', True, c.colors[6], c.colors[1])
    textRect = text.get_rect()
    textRect.center = (240, 540)
    scr.blit(text, textRect)
    pg.display.update()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False
                exit()
