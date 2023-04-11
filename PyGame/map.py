import pygame

class Map:
    def __init__(self, screen, rows, columns, width, height):
        self.screen = screen
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.starting_position = (self.width // 2, self.height // 2)

    def draw(self, screen, camera):
        for x in range(0, self.width, self.width // self.columns):
            pygame.draw.line(screen, (128, 128, 128), (x - camera.x, 0 - camera.y), (x - camera.x, self.height - camera.y))

        for y in range(0, self.height, self.height // self.rows):
            pygame.draw.line(screen, (128, 128, 128), (0 - camera.x, y - camera.y), (self.width - camera.x, y - camera.y))
