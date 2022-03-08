from secrets import choice
from player import Player
import random


class Aiplayer(Player):
    def __init__(self):
     super().__init__()
    pass
    def create_player(self):
        player_2=Aiplayer("Player 2")

    def givengesture(self):
        super().givengesture()
        return random(choice)

    givengesture = Aiplayer("Player 2", givengesture)
    print(givengesture.name)