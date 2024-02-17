import sys

from Controller.functions import *

# Font
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode(screen_size)
current_state = MAIN_MENU

 # Main menu loop
def main_menu():
    while True:
        screen.fill('white')
        draw_text("Main Menu", font, 'black', window_width//2, 100)

        # Play button
        play_button = pygame.Rect(300, 200, 200, 50)
        pygame.draw.rect(screen, 'gray', play_button)
        draw_text("Play", font, 'black', play_button.centerx, play_button.centery)

        # Options button
        options_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, 'gray', options_button)
        draw_text("Options", font, 'black', options_button.centerx, options_button.centery)

        # Quit button
        quit_button = pygame.Rect(300, 400, 200, 50)
        pygame.draw.rect(screen, 'gray', quit_button)
        draw_text("Quit", font, 'black', quit_button.centerx, quit_button.centery)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    # VOEG FUNCTIE TOE VOOR HET STARTEN VAN HET SPEL
                    print("Start the game!")
                    return PLAYING
                elif options_button.collidepoint(mouse_pos):
                    # VOEG FUNCTIE TOE VOOR OPTIONS MENU
                    print("Options menu")
                    return OPTIONS
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()