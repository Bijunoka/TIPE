import pygame as pg
import random

class Ant:
    def __init__(self, x, y, maze):
        """Initialize the ant
        Args:
            x: x position
            y: y position
            maze: maze object
        """
        self.x = x
        self.y = y
        maze.matrice[y][x] = 2

    def can_move(self, maze, direction):
        """Check if the ant can move in the given direction
        Args: 
            maze: maze object
            direction: direction to move
        Returns:
            True if the ant can move in the given direction
        """
        return maze.matrice[self.y + direction[1]][self.x + direction[0]] != 1
    
    def move(self, maze, direction):
        """Move the ant in the given direction if it is possible
        Args:

        """
        if self.can_move(maze, direction):
            # Delete the current position
            maze.matrice[self.y][self.x] = 0
            self.field_of_view(maze, 0)

            # Compute the new position
            self.x += direction[0]
            self.y += direction[1]

            # Set the new position
            maze.matrice[self.y][self.x] = 2
            self.field_of_view(maze, 3)


    def field_of_view(self, maze, value):
        """Set the given value in the field of view of the ant
        Args:
            maze: maze object
            value: value to set in the maze.matrix
        """
        # For each direction
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = self.x + dx, self.y + dy
            
            # If the first condition is false the second condition willl not be checked
            # Checking if the next tile is a wall
            while 0 <= nx < maze.n and 0 <= ny < maze.n and maze.matrice[ny][nx] != 1:
                # If the next tile is not a wall, set it to the given value
                maze.matrice[ny][nx] = value
                nx += dx
                ny += dy
    
