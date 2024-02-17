from Model.level import Level
from View.mainMenu import *


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


if __name__ == "__main__":
    game = Game()
    game.run()


# global current_state
# main_menu = main_menu()
# game = game()
#
# while True:
#     if current_state == MAIN_MENU:
#         new_state = main_menu.run()
#         if new_state == PLAYING:
#             current_state = PLAYING
#     elif current_state == PLAYING:
#         game.run()
#     elif current_state == OPTIONS:
#         pass
#     elif current_state == PAUSED:
#         pass