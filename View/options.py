import sys
from Library.functions import *


class Options:
    def __init__(self, display, game_state_manager):
        self.display = display
        self.game_state_manager = game_state_manager

        self.video_button = pygame.Rect(button_position_x, 200, button_width, button_height)
        self.audio_button = pygame.Rect(button_position_x, 300, button_width, button_height)
        self.back_button = pygame.Rect(button_position_x, 400, button_width, button_height)

    def draw_menu(self):

        draw_text(game_name, font, 'black', window_width // 2, 100)

        pygame.draw.rect(screen, 'gray', self.video_button)
        draw_text("Video", font, 'black', self.video_button.centerx, self.video_button.centery)

        pygame.draw.rect(screen, 'gray', self.audio_button)
        draw_text("Audio", font, 'black', self.audio_button.centerx, self.audio_button.centery)

        pygame.draw.rect(screen, 'gray', self.back_button)
        draw_text("Back", font, 'black', self.back_button.centerx, self.back_button.centery)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.video_button.collidepoint(mouse_pos):
                    pass
                elif self.audio_button.collidepoint(mouse_pos):
                    pass
                elif self.back_button.collidepoint(mouse_pos):
                    self.game_state_manager.set_state('main_menu')

    def run(self):
        self.draw_menu()
        self.handle_events()

        pygame.display.flip()
