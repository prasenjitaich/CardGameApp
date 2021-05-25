import random
from django.core.mail import send_mail
from CardGameApp import settings
import constants


def send_email(subject, recipient, body, message=None):
    sender = settings.EMAIL_HOST_USER
    send_mail(
        subject=subject,
        message=message,
        from_email=sender,
        recipient_list=recipient,
        html_message=body,
    )


class Card:
    """
    Represents a standard playing card.
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        """Compares this card to other, first by suit, then rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return (t1 > t2) - (t1 < t2)


class Deck:
    """Represents a deck of cards.
    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        self.cards = []
        self.hands = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ','.join(res)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def move_cards(self, num):
        """Moves the given number of cards from the deck into the Hand.
        num: integer number of cards to move
        """
        self.hands.clear()
        for i in range(num):
            self.hands.append(str(self.pop_card()))

    def hand_cards(self):
        """Hands Cards."""
        return self.hands

    def count_left_cards(self):
        """Count of left cards in this deck."""
        return len(self.cards)

    def count_dealt_cards(self):
        """Count of dealt cards from this deck."""
        return constants.TOTAL_CARD - len(self.cards)

    def result(self):
        if self.cards:
            for card in self.cards:
                if 'Ace' in str(card):
                    return True
                continue
