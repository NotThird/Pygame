class Camera:
    def __init__(self, target, screen_width, screen_height, map_width, map_height):
        self.target = target
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.map_width = map_width
        self.map_height = map_height
        self.x = target.x - screen_width // 2
        self.y = target.y - screen_height // 2

    def update(self, target):
        self.x = target
        self.x = target.x - self.screen_width // 2
        self.y = target.y - self.screen_height // 2

        # Clamp the camera position to the map boundaries
        self.x = max(0, min(self.x, self.map_width - self.screen_width))
        self.y = max(0, min(self.y, self.map_height - self.screen_height))

