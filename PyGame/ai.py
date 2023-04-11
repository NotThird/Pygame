import pygame.time
from laser import Laser
from resourcegatheringbuilding import ResourceGatheringBuilding
from pygame.math import Vector2
from math import atan2, cos, sin

class AI:
    def __init__(self, player, resource_nodes):
        self.player = player
        self.resource_nodes = resource_nodes
        self.width = 20
        self.height = 20
        self.x = player.x
        self.y = player.y
        self.speed = 3
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.building = False
        self.build_progress = 0
        self.build_time = 10000  # Build time in milliseconds (10 seconds)
        self.laser = None
        self.target = self._find_nearest_node()
        self.target_position = Vector2(self.target.x, self.target.y)

    def move(self, delta_time):
        if not self.building:
            target_pos = self.target_position
            current_pos = Vector2(self.rect.x, self.rect.y)
            distance = target_pos - current_pos

            if distance.length() > self.follow_distance:
                direction = distance.normalize()
                new_pos = current_pos + direction * self.speed * delta_time
                self.rect.x = new_pos.x
                self.rect.y = new_pos.y

    def update(self, delta_time):
        self.target_position = Vector2(self.target.x, self.target.y)
        self.move(delta_time)

        if self.building:
            self.build_progress += delta_time
            if self.build_progress >= self.build_time:
                self.finish_building()

    def _follow_player(self):
        dx = self.player.x - self.x
        dy = self.player.y - self.y
        distance = (dx**2 + dy**2)**0.5

        if distance > 0:
            direction = Vector2(dx, dy).normalize()
            angle = atan2(direction.y, direction.x) + 0.1  # Rotate angle for circling around the player
            circling_distance = 150  # The distance from the player at which the AI will circle
            circling_x = self.player.x + cos(angle) * circling_distance
            circling_y = self.player.y + sin(angle) * circling_distance

            direction_to_circle = Vector2(circling_x - self.x, circling_y - self.y).normalize()
            self.x += direction_to_circle.x * self.speed
            self.y += direction_to_circle.y * self.speed
            self.rect.x = self.x
            self.rect.y = self.y


    def _find_nearest_node(self):
        nearest_node = min(self.resource_nodes, key=lambda node: self._distance_to_node(node))
        return nearest_node

    def _distance_to_node(self, node):
        return Vector2(self.x - node.x, self.y - node.y).length()

    def _is_close_to_node(self, node):
        return self._distance_to_node(node) <= 50

    def start_building(self, target_node):
        self.build_progress = 0
        self.building_target_node = target_node
        self.laser = Laser(self, target_node)
        self.building = ResourceGatheringBuilding(target_node, self.build_progress, self.build_time)

    def update_building_progress(self, delta_time):
        if self.building and self.building.constructing:
            self.build_progress += delta_time

        if self.build_progress >= self.build_time:
            self.finish_building()

    def finish_building(self):
        self.building = False
        self.build_progress = 0
        self.building_target_node = None
        self.laser = None

    def check_for_resources_and_build(self, resources):
        for resource in resources:
            if self.rect.colliderect(resource.rect.inflate(100, 100)):
                if not self.building:
                    self.start_building(resource)  # Pass the resource node to the start_building method
                    break

    def draw(self, screen, camera):
        screen.blit(self.image, (self.x - camera.x, self.y - camera.y))
        if self.laser:
            self.laser.draw(screen, camera)
        if self.building:
            self.building.draw(screen, camera)