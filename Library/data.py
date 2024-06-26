import pygame

game_name = "Epoch Quest"

# Sprite images
world_image = 'Images/ground_map.png'
player_image = 'Images/player_sprite.png'
tile_image = 'Images/epoch_sprite.png'

# Font
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

# Frames
fps = 60

# Window measurements
window_height = 720
window_width = 1280

screen_size = window_width, window_height

window_center = (window_width / 2, window_height / 2)

screen = pygame.display.set_mode(screen_size)

# Menu button measurements
button_width = 200
button_height = 50
button_position_x = window_width / 2 - button_width / 2

# Level
tile_size = 64
