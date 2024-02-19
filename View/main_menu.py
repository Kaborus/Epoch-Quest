import sys
from Library.functions import *


class MainMenu:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        self.play_button = pygame.Rect(button_position_x, 200, button_width, button_height)
        self.options_button = pygame.Rect(button_position_x, 300, button_width, button_height)
        self.quit_button = pygame.Rect(button_position_x, 400, button_width, button_height)

    def draw_menu(self):

        draw_text(game_name, font, 'black', window_width // 2, 100)

        pygame.draw.rect(screen, 'gray', self.play_button)
        draw_text("Play", font, 'black', self.play_button.centerx, self.play_button.centery)

        pygame.draw.rect(screen, 'gray', self.options_button)
        draw_text("Options", font, 'black', self.options_button.centerx, self.options_button.centery)

        pygame.draw.rect(screen, 'gray', self.quit_button)
        draw_text("Quit", font, 'black', self.quit_button.centerx, self.quit_button.centery)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.collidepoint(mouse_pos):
                    self.game_state_manager.set_state('level')
                elif self.options_button.collidepoint(mouse_pos):
                    self.game_state_manager.set_state('options')
                elif self.quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def run(self):

        self.draw_menu()
        self.handle_events()

        pygame.display.flip()
