import pygame

class ResourceGatheringBuilding:
    def __init__(self, node, build_progress, build_time):
        self.x = node.x
        self.y = node.y
        self.width = 64
        self.height = 64
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.constructing = True
        self.build_progress = build_progress
        self.build_time = build_time


    def update(self, inventory):
        if not self.constructing:
            inventory.add_resource(self.target_node.resource_type, 1)
            
    def finish_building(self):
        self.building.constructing = False
        self.laser = None
        self.building = None

    def draw(self, screen, camera):
     if self.constructing:
        progress = self.build_progress / self.build_time
        alpha = int(255 * progress)
        image = self.image.copy()
        image.set_alpha(alpha)
        screen.blit(image, (self.x - camera.x, self.y - camera.y))
     else:
        screen.blit(self.image, (self.x - camera.x, self.y - camera.y))
