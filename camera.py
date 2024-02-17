import pygame
import data


class Camera:
    def __init__(self):
        self.camera = pygame.Rect(0, 0, data.window_width, data.window_height)
        self.width = data.window_width
        self.height = data.window_height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + self.width / 2
        y = -target.rect.centery + self.height / 2

        # Adjust x and y to keep player within screen bounds
        x = min(0, max(self.width - target.rect.width, x))
        y = min(0, max(self.height - target.rect.height, y))

        self.camera = pygame.Rect(x, y, self.width, self.height)
