import pygame as pg
import math

class Camera:
    def __init__(self, width, height):
        """Initialize the camera
        Args:
            width: width of the window
            height: height of the window
        """
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0
        self.zoom_speed = 3

    def adjust_zoom(self, event, maze):
        """Adjust the zoom of the camera
        Args:
            event: event from pygame
            maze: maze object
        """
        mouse_x, mouse_y = pg.mouse.get_pos()
        
        # Convert mouse position to world position
        world_m_x = (mouse_x - self.offset_x) / maze.tile_size
        world_m_y = (mouse_y - self.offset_y) / maze.tile_size

        zoom_factor = 1.1 if event.y > 0 else 0.9
        
        # Adjust tile size based on the zoom
        maze.tile_size *= zoom_factor
        maze.tile_size = max(1, min(maze.tile_size, 200))

        # Modify offset to keep mouse position the same compared to the world
        self.offset_x = mouse_x - (world_m_x * maze.tile_size)
        self.offset_y = mouse_y - (world_m_y * maze.tile_size)

    def move(self, rel_x, rel_y):
        """Move the camera
        Args:
            rel_x: relative x position
            rel_y: relative y position
        """
        self.offset_x += rel_x
        self.offset_y += rel_y

    def draw_maze(self, screen, maze):
        """Draw the maze on the screen
        Args:
            screen: screen to draw the maze on
            maze: maze object
        """
        ts = maze.tile_size
        # Avoid floating point errors
        draw_size = math.ceil(ts) 
        
        # Which part of the maze is visible
        start_x = max(0, int(-self.offset_x // ts))
        end_x = min(maze.n, int((self.width - self.offset_x) // ts) + 1)
        
        start_y = max(0, int(-self.offset_y // ts))
        end_y = min(maze.n, int((self.height - self.offset_y) // ts) + 1)

        # Draw the visible part of the maze
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                if maze.matrice[y][x] == 1:
                    px = x * ts + self.offset_x
                    py = y * ts + self.offset_y
                    pg.draw.rect(screen, (0, 0, 0), (px, py, draw_size, draw_size))