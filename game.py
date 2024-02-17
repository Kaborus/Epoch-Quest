import pygame
import sys
from camera import Camera
from player import Player
import data
from mainMenu import main_menu


def game():
    # Initialize Pygame
    pygame.init()

    screen_size = data.screen_size

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Epoch Quest")

    clock = pygame.time.Clock()

    background = data.white

    player = Player()

    # Create camera object
    camera = Camera()

    print("Starting the game...")

    # Game loop
    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('white')
        pygame.display.flip()

        # Get the keys currently pressed
        keys = pygame.key.get_pressed()


        # Update player position based on key presses
        player.update(keys)

        # Update camera position to follow the player
        camera.update(player)

        # Clear the screen
        screen.fill(background)

        pygame.draw.circle(screen, data.red, (100, 100), 50)

        # Render player and other game objects with camera offset
        screen.blit(player.image, camera.apply(player))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
