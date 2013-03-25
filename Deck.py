

class Deck():
    """Initialize new deck and shuffle"""
    #deck is list which represents the deck of cards
    deck = []
    #number of cards initialized to 0. Will be equal to length of deck list
    num_of_cards = 0
    def __init__(self):
        deck.append(Card(2, "2 of Spades", False))
        deck.append(Card(2, "2 of Hearts", False))
        deck.append(Card(2, "2 of Diamonds", False))
        deck.append(Card(2, "2 of Clubs", False))
        deck.append(Card(3, "3 of Spades", False))
        deck.append(Card(3, "3 of Hearts", False))
        deck.append(Card(3, "3 of Diamonds", False))
        deck.append(Card(3, "3 of Clubs", False))
        deck.append(Card(4, "4 of Spades", False))
        deck.append(Card(4, "4 of Hearts", False))
        deck.append(Card(4, "4 of Diamonds", False))
        deck.append(Card(4, "4 of Clubs", False))
        deck.append(Card(5, "5 of Spades", False))
        deck.append(Card(5, "5 of Hearts", False))
        deck.append(Card(5, "5 of Diamonds", False))
        deck.append(Card(5, "5 of Clubs", False))
        deck.append(Card(6, "6 of Spades", False))
        deck.append(Card(6, "6 of Hearts", False))
        deck.append(Card(6, "6 of Diamonds", False))
        deck.append(Card(6, "6 of Clubs", False))
        deck.append(Card(7, "7 of Spades", False))
        deck.append(Card(7, "7 of Hearts", False))
        deck.append(Card(7, "7 of Diamonds", False))
        deck.append(Card(7, "7 of Clubs", False))
        deck.append(Card(8, "8 of Spades", False))
        deck.append(Card(8, "8 of Hearts", False))
        deck.append(Card(8, "8 of Diamonds", False))
        deck.append(Card(8, "8 of Clubs", False))
        deck.append(Card(9, "9 of Spades", False))
        deck.append(Card(9, "9 of Hearts", False))
        deck.append(Card(9, "9 of Diamonds", False))
        deck.append(Card(9, "9 of Clubs", False))
        deck.append(Card(10, "10 of Spades", False))
        deck.append(Card(10, "10 of Hearts", False))
        deck.append(Card(10, "10 of Diamonds", False))
        deck.append(Card(10, "10 of Clubs", False))
        deck.append(Card(10, "Jack of Spades", False))
        deck.append(Card(10, "Jack of Hearts", False))
        deck.append(Card(10, "Jack of Diamonds", False))
        deck.append(Card(10, "Jack of Clubs", False))
        deck.append(Card(10, "Queen of Spades", False))
        deck.append(Card(10, "Queen of Hearts", False))
        deck.append(Card(10, "Queen of Diamonds", False))
        deck.append(Card(10, "Queen of Clubs", False))
        deck.append(Card(10, "King of Spades", False))
        deck.append(Card(10, "King of Hearts", False))
        deck.append(Card(10, "King of Diamonds", False))
        deck.append(Card(10, "King of Clubs", False))
        deck.append(Card(11, "Ace of Spades", False))
        deck.append(Card(11, "Ace of Hearts", False))
        deck.append(Card(11, "Ace of Diamonds", False))
        deck.append(Card(11, "Ace of Clubs", False))

        deck.shuffle()
        num_of_cards = len(deck)

    def dealCard(self):
        """Give a card off top of deck"""
        card = deck.pop()
        num_of_cards = len(deck)
        return card
