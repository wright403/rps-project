from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass
  
    def choose_gesture(self):
        user_input = input(f'please choose one of the following {self.gestures}: ')
            if user_input == 'rock':
                return 'rock'
            if user_input == 'paper':
                return 'paper'
            if user_input == 'scissors':
                return 'scissors'
            if user_input == 'lizard':
                return 'lizard'
            if user_input == 'spock': 
                return 'spock'   
            pass
        
# "copy and paste like 19 times"