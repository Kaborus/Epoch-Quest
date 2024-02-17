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
