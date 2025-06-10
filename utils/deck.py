
import random
from utils.player import Player
from utils.card import Card

#I created a way to add all 52 cards in a list "the Deck" called self.cards.
#This deck should be able to get shuffled, thats why we imported random.
#Show deck test to see if it worked
#
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
    

    def distribute_cards(self, players):
        while self.cards:
            for player in players:
               if self.cards:
                    player.cards.append(self.cards.pop())
                    player.number_of_cards = len(player.cards)