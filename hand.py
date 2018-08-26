from card import *

class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.cards.sort(key = lambda c: (c.value, c.colour))

    def get_combination(self):
        for fn in [lambda me: me.is_straight(), lambda me: me.is_card()]:
            value = fn(self)
            if value != None:
                return value

    def is_card(self):
        return (Combination.CARD, self.cards[-1])

    def is_straight(self):
        if all(map(lambda pair: pair[0].value + 1 == pair[1].value, window(self.cards, 2))):
            return (Combination.STRAIGHT, self.cards[-1])
        else:
            return None

class Combination(IntEnum):
    CARD = 1,
    PAIR = 2,
    TWO_PAIRS = 3,
    THREE_EQUAL = 4,
    STRAIGHT = 5,
    FLUSH = 6,
    FULL_HOUSE = 7,
    FOUR_EQUAL = 8,
    STRAIGHT_FLUSH = 9

def window(elems, n):
    return [elems[x:x + n] for x in range(len(elems) - n + 1 )]
