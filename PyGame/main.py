import random
import pygame
from pygame.math import Vector2

from ai import AI
from biome import Biome
from map import Map
from camera import Camera
from inventory import Inventory
from player import Player
from resourcenode import ResourceNode
from resourcegatheringbuilding import ResourceGatheringBuilding

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Set up the game screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Set the title of the window
pygame.display.set_caption('Resource Gathering Game')

# Create the map
map = Map(screen, 10, 10, 2400, 2400)
resources = [ResourceNode.generate_random_resource() for _ in range(10)]
# Create the player
player = Player(map.starting_position[0], map.starting_position[1], WIDTH, HEIGHT)

# Create the AI companion
ai_companion = AI(player.rect, resources)


# Create the inventory
inventory = Inventory(screen)

# Create the camera
camera = Camera(player.rect, WIDTH, HEIGHT, map.width, map.height)

# Create an initial set of resources
resources = [ResourceNode.generate_random_resource() for _ in range(10)]

# Create biomes
biomes = [
    Biome(0, 0, 2400, 2400, (173, 216, 230)),
    Biome(2400, 0, 2400, 2400, (173, 255, 47)),
    Biome(0, 2400, 2400, 2400, (32, 178, 170)),
    Biome(2400, 2400, 2400, 2400, (210, 180, 140)),
]

def draw_background(screen, camera):
    screen.fill((135, 206, 250))  # Light blue color for the sky

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT + 1:
            ai_companion.finish_building()

    # Get the currently pressed keys
    keys = pygame.key.get_pressed()

    # Update the player and AI companion
    player.update(keys)
    ai_companion.update(delta_time)  # Keep only this call to ai_companion.update
    ai_companion.check_for_resources_and_build(resources)



    # Update the camera based on the player's position
    camera.update(player.rect)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background
    draw_background(screen, camera)

    # Draw the map
    map.draw(screen, camera)

    # Draw the biomes
    for biome in biomes:
        biome.draw(screen, camera)

    # Draw the resources
    for resource in resources:
        resource.draw(screen, camera)
    
    # Draw the AI companion and building
    ai_companion.draw(screen, camera)

    # Draw the player
    player.draw(screen, camera)

    # Draw the inventory
    inventory.draw()

    # Update the display
    pygame.display.flip()

    # Wait a short amount of time
    pygame.time.delay(25)

# Quit pygame when the game loop is finished
pygame.quit()
