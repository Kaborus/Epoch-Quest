import sys
from functions import *


class MainMenu:
    def __init__(self, display, game_state_manager):

        self.display = display
        self.game_state_manager = game_state_manager

        self.play_button = pygame.Rect(300, 200, 200, 50)
        self.options_button = pygame.Rect(300, 300, 200, 50)
        self.quit_button = pygame.Rect(300, 400, 200, 50)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.collidepoint(mouse_pos):
                    pass
                elif self.options_button.collidepoint(mouse_pos):
                    pass
                elif self.quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def draw_menu(self):
        screen.fill('white')
        draw_text("Main Menu", font, 'black', window_width // 2, 100)
        pygame.draw.rect(screen, 'gray', self.play_button)
        draw_text("Play", font, 'black', self.play_button.centerx, self.play_button.centery)
        pygame.draw.rect(screen, 'gray', self.options_button)
        draw_text("Options", font, 'black', self.options_button.centerx, self.options_button.centery)
        pygame.draw.rect(screen, 'gray', self.quit_button)
        draw_text("Quit", font, 'black', self.quit_button.centerx, self.quit_button.centery)
        pygame.display.flip()


    def run(self):
        self.handle_events()
        self.draw_menu()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.game_state_manager.set_state('level')

    pygame.display.flip()
