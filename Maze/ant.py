import pygame as pg
import random

class Ant:
    def __init__(self, x, y, food=25):
        self.x = x
        self.y = y
        self.food = 0
        self.orientation = 0
        self.vivante = True
        self.food = food



    def up(self, labyrinthe):
        if labyrinthe.est_valide(self.x, self.y - 1):
            self.y -= 1
    
    def down(self, labyrinthe):
        if labyrinthe.est_valide(self.x, self.y + 1):
            self.y += 1

    def left(self, labyrinthe):
        if labyrinthe.est_valide(self.x - 1, self.y):
            self.x -= 1

    def right(self, labyrinthe):
        if labyrinthe.est_valide(self.x + 1, self.y):
            self.x += 1
            

    
