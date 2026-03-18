import pygame as pg
from maze import Labyrinthe
from ant import Ant
from viewport import Camera

WINDOW_WIDTH, WINDOW_HEIGHT = 840, 840

pg.init()
lab = Labyrinthe(5001)
lab.generer()
ant = Ant(0, 0)

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Maze")
clock = pg.time.Clock()

offset_x, offset_y = 0, 0
run = True
is_dragging = False
cam = Camera(WINDOW_WIDTH, WINDOW_HEIGHT)
cam.offset_x, cam.offset_y = offset_x, offset_y 

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEWHEEL:
            cam.ajuster_zoom(event, lab)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                is_dragging = True
                pg.mouse.get_rel()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                is_dragging = False

    if is_dragging:
        rel_x, rel_y = pg.mouse.get_rel()
        cam.deplacer(rel_x, rel_y)

    current_time = pg.time.get_ticks()
    if current_time % 1000 < 500:
        ant.up(lab)
    else:
        ant.down(lab)

    screen.fill((255, 255, 255))
    cam.dessiner_labyrinthe(screen, lab)
    pg.display.update()
    clock.tick(30)

pg.quit()