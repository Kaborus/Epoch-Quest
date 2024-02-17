import pygame
from Model.level import Level
from View.main_menu import *
from Controller.data import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(game_name)
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(white)
            self.level.run()
            pygame.display.update()
            self.clock.tick(fps)
