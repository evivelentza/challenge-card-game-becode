from utils.card import Card

class Player:
    def __init__(self):
        self.cards = []      
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = [] 

player_list = []

for i in range(4):
    player = Player()
    player_list.append(player)