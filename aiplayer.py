
from player import Player
import random


class Aiplayer(Player):
    def __init__(self):
        super().__init__()


        
    
    
    def choose_gesture(self):
        return random.choice(self.gestures)


      
       

