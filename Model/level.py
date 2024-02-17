import pygame
from data import *
from tile import Tile
from Model.player import Player


class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(world_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player =Player((x, y), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
