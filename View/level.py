import sys
from Library.data import *
from Model.tile import Tile
from Model.player import Player
from Model.camera import Camera


class Level:
    def __init__(self, display, game_state_manager):

        self.display = display
        self.game_state_manager = game_state_manager

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = Camera()
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
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

        # temporary
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game_state_manager.set_state('main_menu')
