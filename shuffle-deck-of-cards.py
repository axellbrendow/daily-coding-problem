import random

def rand(k):
	return random.randint(1, k)

def shuffle_deck_of_cards(deck):
	for i in range(len(deck) - 1, 0, -1):
		swap_index = rand(i + 1) - 1
		deck[i], deck[swap_index] = deck[swap_index], deck[i]

def build_deck():
    ranks = ['A', *range(2, 10), 'J', 'Q', 'K']
    suits = ['♠','♦','♣','♥']
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append(f'{rank}{suit}')
    return deck

deck = build_deck()
print('Before shuffle:', deck)
shuffle_deck_of_cards(deck)
print()
print('After shuffle:', deck)
