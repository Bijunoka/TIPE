import pygame as pg

from maze import Labyrinthe
from ant import Ant

lab = Labyrinthe(75)
lab.generer()

ant = Ant(0, 0)


pg.init()
screen = pg.display.set_mode((840, 840))
pg.display.set_caption("Maze")
clock = pg.time.Clock()

offset_x, offset_y = 0, 0
run = True
is_dragging = False
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEWHEEL:
            mouse_x, mouse_y = pg.mouse.get_pos()

            world_m_x = (mouse_x - offset_x) / lab.tile_size
            world_m_y = (mouse_y - offset_y) / lab.tile_size

            lab.tile_size += event.y * 3
            lab.tile_size = max(2, lab.tile_size)

            offset_x = mouse_x - (world_m_x * lab.tile_size)
            offset_y = mouse_y - (world_m_y * lab.tile_size)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                is_dragging = True
                pg.mouse.get_rel()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                is_dragging = False

    if is_dragging:
        rel_x, rel_y = pg.mouse.get_rel()
        offset_x += rel_x
        offset_y += rel_y
    time = pg.time.get_ticks()
    if time % 1000 < 500:
        ant.up(lab)
    else:
        ant.down(lab)
    clock.tick(30)

    lab.afficher(screen, offset_x, offset_y)
    pg.display.update()

if is_dragging:
    rel_x, rel_y = pg.mouse.get_rel()
    offset_x += rel_x
    offset_y += rel_y
pg.quit()