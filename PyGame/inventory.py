import pygame

class Inventory:
    def __init__(self, screen):
        self.screen = screen
        self.resources = {
            'wood': 0,
            'stone': 0,
            'iron': 0,
            'gems': 0,
        }

    def add_resource(self, resource_type, amount):
        if resource_type in self.resources:
            self.resources[resource_type] += amount

    def draw(self):
        font = pygame.font.Font(None, 36)
        resource_text = ', '.join([f"{key}: {value}" for key, value in self.resources.items()])
        text = font.render(resource_text, 1, (255, 255, 255))
        self.screen.blit(text, (20, 20))
