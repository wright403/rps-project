from human import Human
from aiplayer import Aiplayer

class Game:
    def __init__(self):
        self.human = Human()
        self.aiplayer = Aiplayer()
        pass

    def display_greeting(self):
        self.display_greeting = input("Welcome to RPSLS! Here are the rules:")
        
    def player_input(self):
        self.player_input("Will you be playing against the computer? Please enter Y or N: ")
        

   
    