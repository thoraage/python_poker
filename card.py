from enum import IntEnum

class Colour(IntEnum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

class Value(IntEnum):
    V2 = 2
    V3 = 3
    V4 = 4
    V5 = 5
    V6 = 6
    V7 = 7
    V8 = 8
    V9 = 9
    V10 = 10
    KN = 11
    Q = 12
    K = 13
    ACE = 14

class Card:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Value: " + str(self.value) + ", colour: " + str(self.colour)

    def __eq__(self, other):
        return self.value == other.value and self.colour == other.colour

    def __lt__(self, other):
        return self.value < other.value or (self.value == other.value and self.colour < other.colour)
