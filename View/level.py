import sys
from Library.data import *
from Model.tile import Tile
from Model.player import Player
from Model.camera import Camera
from Library.support import *
from random import choice


class Level:
    def __init__(self, display, game_state_manager):

        self.display = display
        self.game_state_manager = game_state_manager

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = Camera()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('CSV/boundary.csv'),
            'grass': import_csv_layout('CSV/grass.csv'),
            'object': import_csv_layout('CSV/object.csv')
        }
        graphics = {
            'grass': import_folder('Images/Grass'),
            'objects': import_folder('Images/Objects')
        }
        print(graphics)
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * tile_size
                        y = row_index * tile_size
                        if style == 'boundary':
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
        self.player = Player((2000, 1500), [self.visible_sprites], self.obstacle_sprites)

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
