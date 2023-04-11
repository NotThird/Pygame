import pygame
import random

class ResourceNode:
    def __init__(self, x, y, resource_type, color):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.resource_type = resource_type
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen, camera):
        screen.blit(self.image, (self.x - camera.x, self.y - camera.y))

    @staticmethod
    def generate_random_resource():
        resource_types = ['wood', 'stone', 'iron', 'gems']  # Replace this list with your actual resource types
        resource_type = random.choice(resource_types)
        node_width = 20
        node_height = 20
        x = random.randint(0, 2400 - node_width)
        y = random.randint(0, 2400 - node_height)

        if resource_type == 'wood':
          color = (139, 69, 19)
        elif resource_type == 'stone':
            color = (128, 128, 128)
        elif resource_type == 'iron':
            color = (105, 105, 105)
        elif resource_type == 'gems':
            color = (255, 0, 255)

        return ResourceNode(x, y, resource_type, color)
