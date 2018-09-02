import random

class RandomAIPlayer:
    def __init__(self, name):
        self.name = name

    def set_hand(self, hand):
        self.hand = hand

    def keep_cards(self):
        cards = self.hand.cards[:]
        random.shuffle(cards)
        return cards[0:random.randrange(len(cards))]

    def bet_or_fold(self):
        pass

    def compare_key(self):
        return self.hand.get_combination()