# Name: Miguel Viloria
# Date Created: November 13, 2026

import random


class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [
        None,
        'Ace',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'Jack',
        'Queen',
        'King',
    ]

    def __init__(self, suit=0, rank=2):
        """Initializes the card with suit and rank."""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a string representation of the card."""
        return f'{self.rank_names[self.rank]} of {self.suit_names[self.suit]}'


class Deck:
    """Represents a deck of 52 playing cards."""

    def __init__(self):
        """Initializes a full deck of cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        """Shuffles the deck randomly."""
        random.shuffle(self.cards)

    def pop_card(self):
        """Removes and returns the top card from the deck."""
        return self.cards.pop()


def deal_poker_hand(deck, num_cards=5):
    """Deals a specified number of cards from the deck to form a hand."""
    hand = []

    # Loop through the range to draw five cards for the initial hand
    for i in range(num_cards):
        card = deck.pop_card()
        hand.append(card)

    return hand


def draw_phase(deck, hand):
    """Prompts the user to replace selected cards and draws new ones."""
    print('\nYour current hand:')
    for index, card in enumerate(hand, start=1):
        print(f'{index}: {card}')

    # Prompt user to enter card positions to replace separated by commas
    user_input = input(
        '\nEnter the numbers of the cards you want to replace (e.g., 1, 3, 5), '
        'or press Enter to keep all: '
    )

    # Check if the user pressed Enter without input to keep all cards
    if user_input.strip() == '':
        print('\nNo cards were replaced.')
        return hand

    # Convert the user input string into a list of integers for indexing
    indices = [int(item.strip()) for item in user_input.split(',')]

    # Iterate through selected positions to substitute with new cards
    for pos in indices:
        if 1 <= pos <= len(hand):
            new_card = deck.pop_card()
            hand[pos - 1] = new_card

    print('\nYour final hand after the draw:')
    for index, card in enumerate(hand, start=1):
        print(f'{index}: {card}')

    return hand


def main():
    """Main function to run the poker draw game program."""
    # Instantiate and shuffle the deck to randomize card order
    deck = Deck()
    deck.shuffle()

    # Deal an initial hand of five cards to the player
    hand = deal_poker_hand(deck, 5)

    # Execute the draw phase to allow card replacements
    draw_phase(deck, hand)


if __name__ == '__main__':
    main()