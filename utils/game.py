from utils.deck import Deck
from utils.player import Player

class Board():
    def __init__(self):
        self.players = []
        for i in range (4):
            player = Player(name=f"Player {i+1}")
            self.players.append(player)
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
    

    def play_turn(self):
        for player in self.players:
            if player.cards:
                card_played = player.play()
                self.active_cards.append(card_played)
                self.history_cards.append(card_played)

                print(f"{player.name} ({self.turn_count} played: {card_played.value}{card_played.icon})")
