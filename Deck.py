from random import shuffle
from Card import Card

class Deck():

    def __init__(self):
        values = [2,3,4,5,6,7,8,9,10]
        suits = ["Spades","Hearts","Diamonds","Clubs"]
        faces = ["Jack of ","Queen of ","King of "]
        ace = "Ace of "
        of = " of "
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(value,(str(value)+of+suit),False))
            for face in faces:
                self.deck.append(Card(10,(face+suit),False))
            self.deck.append(Card(11,(ace+suit),False))

        shuffle(self.deck)
        self.num_cards = len(self.deck)

    def get_card(self):
        card = self.deck.pop()
        self.num_cards-=1
        return card
