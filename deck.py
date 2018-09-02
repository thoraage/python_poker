from card import *
from enum import auto
import random

class Deck:
    def __init__(self):
        self.cards = [Card(value, colour)
                      for value in list(Value)
                      for colour in list(Colour)]
        random.shuffle(self.cards)

    def get_cards(self, n):
        deal_cards = self.cards[0:n]
        self.cards = self.cards[n:]
        return deal_cards