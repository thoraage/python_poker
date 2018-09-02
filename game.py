from hand import Hand
from deck import Deck
from player import *

class Round:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players

    def play(self):
        for player in self.players:
            player.set_hand(Hand(self.deck.get_cards(5)))
        for player in self.players:
            keep_cards = player.keep_cards()
            player.set_hand(Hand(self.deck.get_cards(5 - len(keep_cards)) + keep_cards))
        for player in self.players:
            player.bet_or_fold()
        self.players.sort(key = lambda player: player.compare_key())
        for player in self.players:
            print("Player " + player.name + ", combination: " + str(player.compare_key()) + ", hand: " + str(player.hand))

round = Round([RandomAIPlayer("Player 1"), RandomAIPlayer("Player 2")])
round.play()