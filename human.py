from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()


    
    
    
    def choose_gesture(self):
        user_input = input(f'please choose one of the following {self.gestures}')
        print(user_input)
        
