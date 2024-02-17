from View.game import Game
from View.main_menu import Main_menu
from Controller.data import PLAYING, OPTIONS

game = Game()
menu = Main_menu()


# while True:
#     menu.handle_events()  # Handle user input
#     menu.update()  # Update the state of the menu based on input
#
#     if menu.state == PLAYING:
#         print("test")
#         game = Game()
#
#     elif menu.state == OPTIONS:
#         # Handle options menu
#         pass
