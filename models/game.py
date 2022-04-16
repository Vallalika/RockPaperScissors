from models.player import Player
import random

class Game():

    def __init__(self):
        computer_choice = None
    
    def get_computer_choice(self):
        return self.computer_choice
    
    def set_computer_choice(self, computer_choice):
        self.computer_choice = computer_choice
    
    def play_game(self, player1, player2):
        
        # ***** Game rules *****

        winning_combo1 = (player1.choice == "paper") and (player2.choice == "rock")
        winning_combo2 = (player1.choice == "rock") and (player2.choice == "scissors")
        winning_combo3 = (player1.choice == "scissors") and (player2.choice == "paper")

        if winning_combo1 or winning_combo2 or winning_combo3:
            return True
        
        elif player1.choice == player2.choice:
            return None
        
        else:
            return False
    
    def play_with_computer(self, human_player):
        choices = ["paper","rock","scissors"]
        computer = Player("computer",random.choice(choices))
        self.set_computer_choice(computer.choice)
        return self.play_game(human_player, computer)