from tkinter import N
from human import Human
from aiplayer import Aiplayer

class Game:
    def __init__(self):
        self.human = Human()
        self.aiplayer = Aiplayer()
        pass

    def display_greeting(self):
        self.display_greeting
        print("Welcome to RPSLS! Here are the rules: Each player chooses from a list of the following gestures: rock, scissors, paper, lizard, spock. Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. The winner is whomever wins the best 2 out of 3. Good Luck!")
        
    def player_input(self):
        self.opponent_choice = input('Will you be playing against the computer? Y or N: ')
        Y=Aiplayer
        N=Human
        while N is True: 
            self.aiplayer = Aiplayer
            if input == Y:
                print(self.aiplayer)
            if input == N:
                print("You have chosen to play against another user.")
        pass
            # else: 
            #     input != Y or input != N:
            #     print("Please enter Y or N: ")

        

   
    