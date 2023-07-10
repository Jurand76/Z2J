import pygame as pg
import math

pg.init()


FPS = 60
screen = pg.display.set_mode((640, 1040))
screen.fill((0, 0, 0))
posx = 200
posy = 200
rot = 0
klocek_szer = 40



running = True
while running:
    pg.time.Clock().tick(FPS)
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
        if event.type == pg.KEYDOWN:
            if pg.key.get_pressed()[pg.K_s]:
                print("S")
            if pg.key.get_pressed()[pg.K_w]:
                print("W")
            if pg.key.get_pressed()[pg.K_a]:
                print("A")
            if pg.key.get_pressed()[pg.K_d]:
                print("D")
            if pg.key.get_pressed()[pg.K_SPACE]:
                print("Space")

    pg.display.update()




