import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

SUIT_VALUES = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()


# __len__
# Get the deck length using len()
print(f'Deck length is : {len(deck)}')

# __getitem__
# Get specific card
print(f"First card of the deck is: {deck[0]}")

# Pick a random card
print(f"Random card: {choice(deck)}")

# Slicing
print(f"First three cards: {deck[:3]}")

# Pick only the Aces
print(f"Aces: {deck[12::13]}")


# Sorting
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(SUIT_VALUES) + SUIT_VALUES[card.suit]


print(f"Sorted deck: {sorted(deck, key=spades_high)}")
