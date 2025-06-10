from utils.deck import Deck
from utils.card import Card
from utils.player import Player

class Board:
    def __init__(self):
        self.players = [Player(f"Player {i+1}") for i in range(4)]
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []
        

    def start_game(self):
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute_cards(self.players)

#randomly pick a Card from their hand. Play itm delete it from hand.
#Add the Card to the Player's history.
#Print: {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}.
#Return the Card.
    
        while any(player.cards for player in self.players):
            self.turn_count += 1
            print(f"\n--- Turn {self.turn_count} ---")
            self.active_cards.clear()

            for player in self.players:
                if player.cards:
                    card = player.play()
                    if card:
                        self.active_cards.append(card)
                        self.history_cards.append(card)

            print(f"Active cards: {[str(card) for card in self.active_cards]}")
            print(f"History size: {len(self.history_cards)}")

    #def play_turn(self):
     #   for player in self.players:
      #      if player.cards:
       #         card_played = player.play()
        #        self.active_cards.append(card_played)
         #       self.history_cards.append(card_played)

          #      print(f"{player.name} ({self.turn_count} played: {card_played.value}{card_played.icon})")
