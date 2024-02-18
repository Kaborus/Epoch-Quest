import sys
import pygame

from View.main_menu import MainMenu
from View.level import Level
from data import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(game_name)
        self.clock = pygame.time.Clock()

        screen.fill('white')

        self.game_state_manager = GameStateManager('start')
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.level = Level(self.screen, self.game_state_manager)

        self.states = {'start': self.main_menu, 'level': self.level}

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.game_state_manager.get_state()].run()


            pygame.display.update()
            self.clock.tick(fps)

            screen.fill('white')



class GameStateManager:
    def __init__(self, current_state):
        self.current_state = current_state

    def get_state(self):
        return self.current_state

    def set_state(self, state):
        self.current_state = state
