import pygame as pg
import math
import numpy as np
import colors as c
import blocks
import board
import game

pg.init()

# initialization game parameters, game board and starting game

FPS = 60
screen = pg.display.set_mode((480, 1180))
screen.fill((0, 0, 0))
board = board.Board()
game.game_start(screen, FPS, board)



