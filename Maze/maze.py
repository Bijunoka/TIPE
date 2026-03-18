import pygame as pg
import random

class Maze:
    def __init__(self, n=21, tile_size=40):
        """Initialize the maze
        Args:
            n: size of the maze (n x n)
            tile_size: size of each tile
        """
        self.n = n
        if self.n % 2 == 0: self.n += 1
        self.tile_size = tile_size
        self.matrice = [[1] * self.n for _ in range(self.n)]
            
    def dig(self, x, y):
        """Dig a hole at (x, y)
        Args:
            x: x position
            y: y position
        """
        self.matrice[y][x] = 0

    def is_valid(self, x, y):
        """Check if (x, y) is a valid position for a hole to be digged
        Args:
            x: x position
            y: y position
        Returns:
            True if (x, y) is a valid position
        """
        return 0 <= x < self.n and 0 <= y < self.n and self.matrice[y][x] == 1

    def generate(self, start_x=1, start_y=1):
        """Generate the maze
        Args:
            start_x: x position of the start
            start_y: y position of the start
        """
        # Initialize the maze
        self.dig(start_x, start_y)
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        stack = [[start_x, start_y, directions[:]]] 

        # Generate the maze
        while stack:
            
            # Get the last element of the stack
            current_x, current_y, possibles = stack[-1]
            
            # If there are still possible directions
            if possibles:
                dir_x, dir_y = possibles.pop()
                new_x, new_y = current_x + dir_x, current_y + dir_y
                
                # If the new position is valid
                if self.is_valid(new_x, new_y):
                    
                    # Dig a hole at the new position and between the current position and the new position
                    self.dig(current_x + dir_x // 2, current_y + dir_y // 2)
                    self.dig(new_x, new_y)  

                    # Add the new position to the stack  
                    new_dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)]
                    random.shuffle(new_dirs)
                    stack.append([new_x, new_y, new_dirs])
            
            # Otherwise, pop the last element of the stack
            else:
                stack.pop()

    def display(self, surface, offx=0, offy=0):
        """Display the maze on the surface
        Args:
            surface: surface to display the maze on
            offx: offset x
            offy: offset y
        """
        w, h = self.tile_size, self.tile_size
        surface.fill((255, 255, 255))

        for y in range(self.n):
            for x in range(self.n):
                if self.matrice[y][x] == 1:
                    pg.draw.rect(surface, (0, 0, 0), (x * w + offx, y * h + offy, w, h))

