# game tic-tac-toe

import pygame as pg
import sys
import random

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def player_key():
    pressed = False
    while not pressed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                key = pg.key.get_pressed()
                if key[pg.K_1]:
                    return 1
                if key[pg.K_2]:
                    return 2
                if key[pg.K_3]:
                    return 3
                if key[pg.K_4]:
                    return 4
                if key[pg.K_5]:
                    return 5
                if key[pg.K_6]:
                    return 6
                if key[pg.K_7]:
                    return 7
                if key[pg.K_8]:
                    return 8
                if key[pg.K_9]:
                    return 9
                if key[pg.K_ESCAPE]:
                    pg.quit()
                    sys.exit()


def board_text(screen, text, x, y, size, color):
    font = pg.font.SysFont("Comic Cans MS", size)
    text_to_draw = font.render(text, True, color)
    screen.blit(text_to_draw, (x, y))
def display_board(screen):
    line_color = (220, 220, 220)
    text_color = (250, 230, 200)
    text_color_2 = (200, 200, 180)
    screen.fill((0,0,0))
    pg.draw.line(screen, line_color, (260, 60), (260, 420))
    pg.draw.line(screen, line_color, (380, 60), (380, 420))
    pg.draw.line(screen, line_color, (140, 180), (500, 180))
    pg.draw.line(screen, line_color, (140, 300), (500, 300))
    text = "Tic-Tac-Toe"
    board_text(screen, text, 10, 10, 25, text_color)
    board_text(screen, "1", 200, 120, 20, text_color_2)
    board_text(screen, "2", 320, 120, 20, text_color_2)
    board_text(screen, "3", 440, 120, 20, text_color_2)
    board_text(screen, "4", 200, 240, 20, text_color_2)
    board_text(screen, "5", 320, 240, 20, text_color_2)
    board_text(screen, "6", 440, 240, 20, text_color_2)
    board_text(screen, "7", 200, 360, 20, text_color_2)
    board_text(screen, "8", 320, 360, 20, text_color_2)
    board_text(screen, "9", 440, 360, 20, text_color_2)
    pg.display.flip()

def draw_player(screen, number):
    pos_x = (number - 1) % 3 * 120 + 188
    pos_y = (number - 1) // 3 * 120 + 94
    board_text(display_screen, "X", pos_x - 4, pos_y + 6, 80, (0, 0, 0))
    board_text(display_screen, "x", pos_x, pos_y, 80, (250, 0, 0))
    pg.display.flip()

def draw_computer(screen, number):
    pos_x = (number - 1) % 3 * 120 + 188
    pos_y = (number - 1) // 3 * 120 + 94
    board_text(display_screen, "X", pos_x - 4, pos_y + 6, 80, (0, 0, 0))
    board_text(display_screen, "o", pos_x, pos_y, 80, (250, 0, 0))
    pg.display.flip()

# check if someone wins
def check_winner(tab):
    if (tab[0] == tab[1] == tab[2] == 1) or (tab[3] == tab[4] == tab[5] == 1) or (tab[6] == tab[7] == tab[8] == 1):
        return 1
    if (tab[0] == tab[3] == tab[6] == 1) or (tab[1] == tab[4] == tab[7] == 1) or (tab[2] == tab[5] == tab[8] == 1):
        return 1
    if (tab[0] == tab[4] == tab[8] == 1) or (tab[2] == tab[4] == tab[6] == 1):
        return 1
    if (tab[0] == tab[1] == tab[2] == 2) or (tab[3] == tab[4] == tab[5] == 2) or (tab[6] == tab[7] == tab[8] == 2):
        return 2
    if (tab[0] == tab[3] == tab[6] == 2) or (tab[1] == tab[4] == tab[7] == 2) or (tab[2] == tab[5] == tab[8] == 2):
        return 2
    if (tab[0] == tab[4] == tab[8] == 2) or (tab[2] == tab[4] == tab[6] == 2):
        return 2
    return 0

# checks if game has ended because there is winner or there is draw
def end_game(screen, winner):
    finish_game = False
    if winner != 0:
        if winner == 1:
            board_text(screen, "You Win!", 250, 430, 50, (0, 250, 0))
            pg.display.flip()
            finish_game = True
        if winner == 2:
            board_text(screen, "Computer Wins!", 170, 430, 50, (0, 250, 0))
            pg.display.flip()
            finish_game = True

    if winner == 0 and moves_done == 9:
        board_text(screen, "Draw!", 270, 430, 50, (0, 250, 0))
        pg.display.flip()
        finish_game = True

    if finish_game:
        press_ESC = player_key()
        pg.quit()
        sys.exit()

# Main part of code

pg.init()
display_screen = pg.display.set_mode((640, 480))
display_board(display_screen)

moves_done = 0

game_over = False

while not game_over:

    good_move = False
    number = player_key()

    while not good_move:
        if board[number-1] == 0:
            draw_player(display_screen, number)
            board[number-1] = 1
            good_move = True
            moves_done += 1
        else:
            number = player_key()

    winner = check_winner(board)
    end_game(display_screen, winner)

    good_move = False
    number_comp = random.randint(1,9)

    while not good_move:
        if board[number_comp-1] == 0:
            draw_computer(display_screen, number_comp)
            board[number_comp-1] = 2
            good_move = True
            moves_done += 1
        else:
            number_comp = random.randint(1,9)

    winner = check_winner(board)
    end_game(display_screen, winner)




