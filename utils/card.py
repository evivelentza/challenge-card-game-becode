import random
from utils.player import Player

class Symbol:
    def __init__(self, color: str, icon):
        self.color = color
        self.icon = icon
    

class Card(Symbol):
    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color, icon)
        self.value = value
    
class Deck:
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        color = ["red", "red", "black", "black"]
        icons = ["♥", "♦", "♣", "♠"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in range(4):
            for value in values:
                card = Card(color[i], icons[i], value)
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def show_deck(self):
        for card in self.cards:
            print(f"{card.value} of {card.icon} ({card.color})")
    

    def distribute_cards(self, player = List:[Player]):
        card_for_player = random.choice(self_cards)
        self_cards.remove(card_for_player)



deck = Deck()
deck.fill_deck()
deck.show_deck()
