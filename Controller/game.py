from Controller.game_state_manager import GameStateManager
from View.main_menu import MainMenu
from View.level import Level
from View.options import Options
from Library.data import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption(game_name)
        self.clock = pygame.time.Clock()

        screen.fill('white')

        self.game_state_manager = GameStateManager('main_menu')
        self.main_menu = MainMenu(self.screen, self.game_state_manager)
        self.level = Level(self.screen, self.game_state_manager)
        self.options = Options(self.screen, self.game_state_manager)

        self.states = {'main_menu': self.main_menu, 'level': self.level, 'options':self.options}

        self.run()

    def run(self):
        while True:
            self.states[self.game_state_manager.get_state()].run()
            self.clock.tick(fps)
            pygame.display.update()

            screen.fill('white')
