from game import Game
from player import Player

player1 = Player("Tom", "Paper")
player2 = Player("Jerry", "Scissors")

# choice1 = player1.get_choice()
# choice2 = player2.get_choice()

game = Game()

results = game.play_game(player1,player2)