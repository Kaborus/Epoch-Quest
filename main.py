import pygame
import sys
from level import Level
import data


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(data.screen_size)
        pygame.display.set_caption(data.name)
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(data.white)
            self.level.run()
            pygame.display.update()
            self.clock.tick(data.fps)


if __name__ == "__main__":
    game = Game()
    game.run()

from game import game
from data import *
from mainMenu import *

global current_state
main_menu = main_menu()
game = game()

while True:
    if current_state == MAIN_MENU:
        new_state = main_menu.run()
        if new_state == PLAYING:
            current_state = PLAYING
    elif current_state == PLAYING:
        game.run()
    elif current_state == OPTIONS:
        pass
    elif current_state == PAUSED:
        pass