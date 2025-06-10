from utils.game import Board
from utils.player import Player
from utils.deck import Deck

deck = Deck()
deck.fill_deck()
deck.shuffle()

players = []
for i in range(4):
    player = Player(name=f"Player {i+1}")
    players.append(player)

deck.distribute_cards(players)


for player in players:
    print(f"\n{player.name} has {len(player.cards)} cards:")
    for card in player.cards:
        print(f" - {card.value} of {card.icon} ({card.color})")
