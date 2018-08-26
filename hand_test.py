import unittest
from hand import *
from card import *

class HandTestCase(unittest.TestCase):

    def test_is_straight(self):
        hand = decode_hand("V2,SPADES;V4,HEARTS;V3,HEARTS;V6,HEARTS;V5,HEARTS")
        self.assertEqual(hand.get_combination(), (Combination.STRAIGHT, Card(Value.V6, Colour.HEARTS)))
        hand.cards[4].value = Value.KN
        self.assertEqual(hand.get_combination(), (Combination.CARD, Card(Value.KN, Colour.HEARTS)))

#    def test_is_flush(self):

    def test_window(self):
        self.assertEqual(window([1,2,3], 2), [[1,2], [2,3]])

def decode_card(s):
    attrs = s.split(",")
    return Card(Value[attrs[0]], Colour[attrs[1]])

def decode_hand(s):
    return Hand(list(map(decode_card, s.split(";"))))

if __name__ == '__main__':
    unittest.main()
