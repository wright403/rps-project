
from ast import Pass
from human import Human
from aiplayer import Aiplayer
# from player import Player

class Game:
    def __init__(self):
        self.player_1 = Human("Buzz")
        self.player_2 = Aiplayer("Terminator")
        pass

    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.choose_opponent()
        self.play_game()
        self.display_winner()
        pass

    def display_greeting(self):
        print("Welcome to RPSLS!")
        
    def display_rules(self):    
        print('Here are the rules: Each player chooses from a list of the following gestures: rock, scissors, paper, lizard, spock. Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. The winner is whomever wins the best 2 out of 3. Good Luck!')
        
    def choose_opponent(self):
        self.opponent_choice = input('Will you be playing against the computer? Y or N: ')
        has_chosen = False
        while has_chosen is False:
            if self.opponent_choice == 'Y':
                self.player_2 = Aiplayer('Terminator')
                print ('You have chosen single player')
                break
            elif self.opponent_choice == 'N':
                self.player_1 = Human('Buzz')
                print('You have chosen multi player')
                break
            else:
                self.opponent_choice = input('Will you be playing against the computer? Y or N: ')
                has_chosen = False
    
    def play_game(self):
        while self.player_1 <= 2 and self.player_2 <= 2:
            if self.player_1:
             pass


        
                    
        






    def display_winner(self):
        pass    
        

   
    