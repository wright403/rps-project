from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        pass
  
    def choose_gesture(self):
         input(f'please choose between {self.gestures}')
         return self.gestures
        