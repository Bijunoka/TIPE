import pygame as pg
from maze import Maze
from ant import Ant
from viewport import Camera

# Constantes
WINDOW_WIDTH, WINDOW_HEIGHT = 840, 840

# Initialisation
pg.init()
lab = Maze(5001)
lab.generate()
ant = Ant(0, 0)

# Window setup
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Maze")
clock = pg.time.Clock()

offset_x, offset_y = 0, 0
run = True
is_dragging = False
cam = Camera(WINDOW_WIDTH, WINDOW_HEIGHT)
cam.offset_x, cam.offset_y = offset_x, offset_y 

while run:
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        # Zoom
        if event.type == pg.MOUSEWHEEL:
            cam.adjust_zoom(event, lab)

        # Drag
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                is_dragging = True
                pg.mouse.get_rel()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                is_dragging = False

    if is_dragging:
        rel_x, rel_y = pg.mouse.get_rel()
        cam.move(rel_x, rel_y)

    # Draw
    screen.fill((255, 255, 255))
    cam.draw_maze(screen, lab)
    pg.display.update()
    clock.tick(30)

pg.quit()