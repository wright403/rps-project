
from player import Player
import random


class Aiplayer(Player):
    def __init__(self,name):
        super().__init__(name)
        pass


        
    
    
    def choose_gesture(self):
        return random.choice(self.gestures)
        pass


      
       

