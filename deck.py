from card import *
from enum import auto

class Deck:

    def __init__(self):
        self.cards = [Card(value, colour)
                      for value in list(Value)
                      for colour in list(Colour)]
