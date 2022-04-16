class Player():

    def __init__(self, input_name, input_choice):
        self.name = input_name
        self.choice = input_choice
    
    def get_choice(self):
        return self.choice