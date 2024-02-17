from game import game
from data import *
from mainMenu import *

global current_state
main_menu = main_menu()
game = game()

while True:
    if current_state == MAIN_MENU:
        new_state = main_menu.run()
        if new_state == PLAYING:
            current_state = PLAYING
    elif current_state == PLAYING:
        game.run()
    elif current_state == OPTIONS:
        pass
    elif current_state == PAUSED:
        pass

