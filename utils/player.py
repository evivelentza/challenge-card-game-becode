from utils.card import Card
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []      
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = [] 

#player_list = []

#for i in range(4):
#    player = Player()
#    player_list.append(player)

    def play(self):

        if not self.cards:
            print(f"{self.name} has no cards left.")
            return None

        card_to_play = random.choice(self.cards)
        self.cards.remove(card_to_play)

        self.turn_count += 1

        self.number_of_cards = len(self.cards)

        self.history.append(card_to_play)

        print(f"{self.name} {self.turn_count} played: {card_to_play.value} {card_to_play.icon}")
        return card_to_play