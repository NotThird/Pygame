import pygame

class Biome:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen, camera):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x - camera.x, self.y - camera.y, self.width, self.height))
