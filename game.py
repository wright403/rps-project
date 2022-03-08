
from human import Human
from aiplayer import Aiplayer

class Game:
    def __init__(self):
        self.human = Human()
        self.aiplayer = Aiplayer()
        
        


    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.choose_opponent()
        self.play_game()
        self.display_winner()


    def display_greeting(self):
        print("Welcome to RPSLS!")
        
    def display_rules(self):    
        print('Here are the rules: Each player chooses from a list of the following gestures: rock, scissors, paper, lizard, spock. Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock. The winner is whomever wins the best 2 out of 3. Good Luck!')
        
    def choose_opponent(self):
        self.opponent_choice = input('Will you be playing against the computer? Y or N: ')
        has_chosen = False
        while has_chosen is False:
            if self.opponent_choice == 'Y':
                print(f'you have chosen {self.player_one}')
                break
            elif self.opponent_choice == 'N':
                print('you have chosen multiplayer')
                break
            else:
                print('please Enter Y or N')
                break


                  
    def create_player_one(self):
        player_one = Human()
        player_two = Human()


    def create_player_two(self):
        player_two = Aiplayer()      


            
            
    
    
    def play_game(self):
        pass
                    
        






    def display_winner(self):
        pass    
        

   
    