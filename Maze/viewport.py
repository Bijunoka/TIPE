import pygame as pg
import math

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0
        self.zoom_speed = 3

    def ajuster_zoom(self, event, lab):
        mouse_x, mouse_y = pg.mouse.get_pos()
        
        world_m_x = (mouse_x - self.offset_x) / lab.tile_size
        world_m_y = (mouse_y - self.offset_y) / lab.tile_size

        zoom_factor = 1.1 if event.y > 0 else 0.9
        
        lab.tile_size *= zoom_factor
        lab.tile_size = max(1, min(lab.tile_size, 200))

        self.offset_x = mouse_x - (world_m_x * lab.tile_size)
        self.offset_y = mouse_y - (world_m_y * lab.tile_size)

    def deplacer(self, rel_x, rel_y):
        self.offset_x += rel_x
        self.offset_y += rel_y

    def dessiner_labyrinthe(self, screen, lab):
        ts = lab.tile_size
        draw_size = math.ceil(ts) 
        
        start_x = max(0, int(-self.offset_x // ts))
        end_x = min(lab.n, int((self.width - self.offset_x) // ts) + 1)
        
        start_y = max(0, int(-self.offset_y // ts))
        end_y = min(lab.n, int((self.height - self.offset_y) // ts) + 1)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if lab.matrice[y][x] == 1:
                    px = x * ts + self.offset_x
                    py = y * ts + self.offset_y
                    pg.draw.rect(screen, (0, 0, 0), (px, py, draw_size, draw_size))