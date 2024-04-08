from settings import *
from game import Game

the_game = Game()

while the_game.running:
    the_game.current_menu.display_menu()
    the_game.game_loop()
