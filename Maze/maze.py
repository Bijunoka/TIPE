import pygame as pg
import random

class Labyrinthe:
    def __init__(self, n=21, tile_size=40):
        self.n = n
        if self.n % 2 == 0: self.n += 1
        self.tile_size = tile_size
        self.matrice = [[1] * self.n for _ in range(self.n)]
            
    def creuser(self, x, y):
        self.matrice[y][x] = 0

    def est_valide(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.matrice[y][x] == 1

    def generer(self, x=1, y=1):
        self.creuser(x, y)
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.est_valide(nx, ny):
                self.creuser(x + dx // 2, y + dy // 2)
                self.generer(nx, ny)

    def generer_iter(self, start_x=1, start_y=1):
        self.creuser(start_x, start_y)
        
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        pile = [[start_x, start_y, directions[:]]] 

        while pile:
            cx, cy, possibles = pile[-1]

            if possibles:
                dx, dy = possibles.pop()
                nx, ny = cx + dx, cy + dy

                if self.est_valide(nx, ny):
                    self.creuser(cx + dx // 2, cy + dy // 2)
                    self.creuser(nx, ny)
                    
                    nouvelles_dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
                    random.shuffle(nouvelles_dirs)
                    pile.append([nx, ny, nouvelles_dirs])
            else:
                pile.pop()



    def afficher(self, surface, offx=0, offy=0):
        w, h = self.tile_size, self.tile_size
        surface.fill((255, 255, 255))

        for y in range(self.n):
            for x in range(self.n):
                if self.matrice[y][x] == 1:
                    pg.draw.rect(surface, (0, 0, 0), (x * w + offx, y * h + offy, w, h))

