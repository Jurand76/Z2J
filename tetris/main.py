import pygame as pg
import math

pg.init()

def grid_background(scr, color, color_back, size):
    for i in range(0, int(640/size)):
        for j in range(0, int(1040/size)):
            pg.draw.rect(scr, color, pg.Rect(i*size, j*size, size, size))
            pg.draw.rect(scr, color_back, pg.Rect(i * size+1, j * size+1, size-2, size-2))



FPS = 60
screen = pg.display.set_mode((640, 1040))
screen.fill((0, 0, 0))

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
            if pg.key.get_pressed()[pg.K_w]:
                print("W")
            if pg.key.get_pressed()[pg.K_a]:
                print("A")
            if pg.key.get_pressed()[pg.K_d]:
                print("D")
            if pg.key.get_pressed()[pg.K_SPACE]:
                print("Space")

    screen.fill((0, 0, 0))
    grid_background(screen, (50, 50, 50), (20, 20, 20), 40)
    pg.display.update()




