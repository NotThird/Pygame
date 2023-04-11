import pygame

class Player:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 5
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen, camera):
        screen.blit(self.image, (self.x - camera.x, self.y - camera.y))