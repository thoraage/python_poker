import unittest
from deck import Deck

class DeckTestCase(unittest.TestCase):
    def test_init_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_get_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.get_cards(10)), 10)
        self.assertEqual(len(deck.cards), 42)

if __name__ == '__main__':
    unittest.main()
