import pygame
from enum import Enum

fps = 60

#Colors
red = (255, 0,0)
green = (0, 255, 0)
blue=(0,0,255)
yellow=(255,255,0)

#Dictionary of available colours
colors = {"red": red, "green": green, "blue":blue, "yellow":yellow}
clock = pygame.time.Clock()

class Radius(Enum):
    MIN = 20
    MAX = 40

def create(screen, radius, color_name, window_width, window_height):
    if radius not in (Radius.MIN.value, Radius.MAX.value):
        raise ValueError(f"Radius can only be {Radius.MIN.value} or {Radius.MAX.value}")

    circle_radius = radius
    color = colors.get(color_name)
    circle_center = (window_width, window_height)

    pygame.draw.circle(screen, color, circle_center, circle_radius)