import unittest
from hand import *
from card import *

class HandTestCase(unittest.TestCase):

    def test_is_straight(self):
        hand = Hand([Card(Value.V2, Colour.SPADES), Card(Value.V4, Colour.HEARTS), Card(Value.V3, Colour.HEARTS), Card(Value.V6, Colour.HEARTS), Card(Value.V5, Colour.HEARTS)])
        self.assertEquals(hand.get_combination(), (Combination.STRAIGHT, Card(Value.V6, Colour.HEARTS)))
        hand.cards[4].value = Value.KN
        self.assertEqual(hand.get_combination(), (Combination.CARD, Card(Value.KN, Colour.HEARTS)))

    def test_window(self):
        self.assertEqual(window([1,2,3], 2), [[1,2], [2,3]])

if __name__ == '__main__':
    unittest.main()
