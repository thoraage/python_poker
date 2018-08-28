from card import *

class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.cards.sort(key = lambda c: (c.value, c.colour))

    def get_combination(self):
        for fn in [self.is_straight, self.is_flush, self.is_card]:
            value = fn()
            if value != None:
                return value

    def is_card(self):
        return (Combination.CARD, self.cards[-1])

    def is_straight(self):
        if all(map(lambda pair: pair[0].value + 1 == pair[1].value, window(self.cards, 2))):
            return (Combination.STRAIGHT, self.cards[-1])
        return None

    def is_flush(self):
        dict = group_by(self.cards, lambda card: card.colour).values()
        if (len(dict) == 1):
            return (Combination.FLUSH, self.cards[-1])
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

def group_by(elems, fn):
    dict = {}
    def add(elem):
        key = fn(elem)
        cat = dict.get(key, [])
        cat.append(elem)
        dict[key] = cat
    for elem in elems:
        add(elem)
    return dict