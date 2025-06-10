from utils.card import Card
import random

#Creating a player having all the attributes from challenge, info on what cards he has at hands, how many are they, turns, and history of played cards
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []      
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = [] 

#now we need a loop to be activated during the game. The player if he has cars on hand to be able to play a random card and this card to not be on his hands afterwards/
#If he doesnt have cards anymore a message will be returned.
#The card will be added to the list of history for this player and the turn should be +1. A message is printed in the end after he played.

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