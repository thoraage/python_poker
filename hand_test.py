import unittest
from hand import *
from card import *

class HandTestCase(unittest.TestCase):

    def test_is_straight_flush(self):
        hand = decode_hand("V2,HEARTS;V4,HEARTS;V3,HEARTS;V6,HEARTS;V5,HEARTS")
        self.assertEqual(hand.get_combination(), (Combination.STRAIGHT_FLUSH, Card(Value.V6, Colour.HEARTS)))

    def test_is_four_equal(self):
        hand = decode_hand("V2,SPADES;V2,HEARTS;K,HEARTS;V2,CLUBS;V2,DIAMONDS")
        self.assertEqual(hand.get_combination(), (Combination.FOUR_EQUAL, Card(Value.V2, Colour.SPADES)))

    def test_is_full_house(self):
        hand = decode_hand("K,SPADES;V2,HEARTS;K,HEARTS;V2,CLUBS;V2,DIAMONDS")
        self.assertEqual(hand.get_combination(), (Combination.FULL_HOUSE, Card(Value.K, Colour.SPADES)))

    def test_is_straight(self):
        hand = decode_hand("V2,SPADES;V4,HEARTS;V3,HEARTS;V6,HEARTS;V5,HEARTS")
        self.assertEqual(hand.get_combination(), (Combination.STRAIGHT, Card(Value.V6, Colour.HEARTS)))

    def test_is_flush(self):
        hand = decode_hand("V2,HEARTS;V4,HEARTS;V3,HEARTS;KN,HEARTS;V5,HEARTS")
        self.assertEqual(hand.get_combination(), (Combination.FLUSH, Card(Value.KN, Colour.HEARTS)))

    def test_is_three_equal(self):
        hand = decode_hand("Q,SPADES;V2,HEARTS;K,HEARTS;V2,CLUBS;V2,DIAMONDS")
        self.assertEqual(hand.get_combination(), (Combination.THREE_EQUAL, Card(Value.V2, Colour.HEARTS)))

    def test_is_card(self):
        hand = decode_hand("V2,SPADES;V4,HEARTS;V3,HEARTS;KN,HEARTS;V5,HEARTS")
        self.assertEqual(hand.get_combination(), (Combination.CARD, Card(Value.KN, Colour.HEARTS)))

    def test_window(self):
        self.assertEqual(window([1,2,3], 2), [[1,2], [2,3]])

    def test_group_by(self):
        actual = group_by(decode_hand("V2,SPADES;V4,HEARTS;V3,HEARTS").cards, lambda card: card.colour)
        expected = { Colour.SPADES: [ decode_card("V2,SPADES") ], Colour.HEARTS: [ decode_card("V3,HEARTS"), decode_card("V4,HEARTS") ] }
        self.assertEqual(actual, expected)

    def test_dict_equal(self):
        self.assertEqual({'Name': 'Zara', 'Age': 7}, {'Age': 7, 'Name': 'Zara' })

def decode_card(s):
    attrs = s.split(",")
    return Card(Value[attrs[0]], Colour[attrs[1]])

def decode_hand(s):
    return Hand(list(map(decode_card, s.split(";"))))

if __name__ == '__main__':
    unittest.main()
