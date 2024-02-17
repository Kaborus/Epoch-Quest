import pygame
import data

movement_speed = data.movement_speed
player_size = data.player_size
center = data.center
white = data.white


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("characterSprite1.png").convert()
        self.image = pygame.transform.scale(self.image, player_size)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = center


    def update(self, pressed_keys):
        # Update the player's position based on user input
        if pressed_keys[pygame.K_w]:
            self.rect.y -= movement_speed
        if pressed_keys[pygame.K_s]:
            self.rect.y += movement_speed
        if pressed_keys[pygame.K_a]:
            self.rect.x -= movement_speed
        if pressed_keys[pygame.K_d]:
            self.rect.x += movement_speed
