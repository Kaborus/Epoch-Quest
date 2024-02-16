import pygame

def main_menu():
    screen.fill(255,255,255)

    # Text
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    text_surface = my_font.render("Main Menu", False, (0, 0, 0))

    screen.blit(text_surface, (0,0))

