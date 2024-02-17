import sys
import pygame
from Controller.data import *
from Controller.functions import *


class Main_menu():
    def __init__(self):
        self.state = MAIN_MENU
        self.play_button = pygame.Rect(300, 200, 200, 50)
        self.options_button = pygame.Rect(300, 300, 200, 50)
        self.quit_button = pygame.Rect(300, 400, 200, 50)
        self.run()
        self.get_selected_option()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.collidepoint(mouse_pos):
                    print("Start the game!")
                    state = PLAYING
                    print(self.state)
                elif self.options_button.collidepoint(mouse_pos):
                    print("Options menu")
                    self.state = OPTIONS
                    print(self.state)
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

    def get_selected_option(self):
        # Return the selected option
        return self.state

    def run(self):
        while True:
            self.handle_events()
            self.draw_menu()

    pygame.display.flip()
