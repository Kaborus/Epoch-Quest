import pygame


def create(screen, window_width, window_height):
    # Draw a blue circle in the center of the screen
    circle_color = (0, 0, 255)  # Blue color (R, G, B)
    circle_center = (window_width // 2, window_height // 2)  # Center of the screen
    circle_radius = 20  # Radius of the circle
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
