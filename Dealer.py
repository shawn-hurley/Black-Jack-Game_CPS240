from Player import Player
from Deck import Deck
from Hand import Hand
class Dealer(Player):
    
    def __init__(self):
        super(Dealer, self).__init__()
        self.__deck = Deck()
        self.__bets = []

    def new_deck(self):
        self.__deck = Deck()   

    def give_card(self, player):
        if(player.__class__.__name__ == 'Dealer'):
            if(player.get_hand().get_number_of_cards() == 1):
                c1 = self.__deck.get_card()
                c1.set_face_down(True)
                player.receive_card(c1)
            else:
                player.receive_card(self.__deck.get_card())
        else:
            player.receive_card(self.__deck.get_card())
    
