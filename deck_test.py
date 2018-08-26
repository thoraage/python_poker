import unittest
from deck import Deck

class DeckTestCase(unittest.TestCase):

    def test_init_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

if __name__ == '__main__':
    unittest.main()
