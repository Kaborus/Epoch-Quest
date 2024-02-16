import pygame
import sys
from character import create


def screen():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Epoch Quest")

    circle_x = window_width // 2
    circle_y = window_height // 2

    # Game loop
    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Update game state

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            circle_y -= 1
        if keys[pygame.K_s]:
            circle_y += 1
        if keys[pygame.K_a]:
            circle_x -= 1
        if keys[pygame.K_d]:
            circle_x += 1

        # Draw graphics
        screen.fill((255, 255, 255))  # Fill the screen with white
        create(screen, circle_x, circle_y)

        # Additional drawing can be done here

        pygame.display.flip()  # Update the display

    # Quit Pygame
    pygame.quit()
    sys.exit()
