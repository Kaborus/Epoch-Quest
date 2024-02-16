import pygame
import sys


def screen():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Epoch Quest")

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state

        # Draw graphics
        screen.fill((255, 255, 255))  # Fill the screen with white
        # Additional drawing can be done here

        pygame.display.flip()  # Update the display

    # Quit Pygame
    pygame.quit()
    sys.exit()
