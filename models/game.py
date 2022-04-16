class Game():
    def __init__(self, input_game_name):
        self.game_name = input_game_name
    
    def game(player1, player2):
        
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