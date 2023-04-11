import pygame

class Laser:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.color = (255, 0, 0)

    def draw(self, screen, camera):
        pygame.draw.line(screen, self.color, (self.source.x - camera.x, self.source.y - camera.y), (self.target.x - camera.x, self.target.y - camera.y), 2)
