from Card import Card

class Hand(object):

    def __init__(self):
        #Constructor
        self.__number_cards = 0
        self.__value = 0
        self.__cards = []

    def showHand(self):
        #Parse list of cards, asks card to show value
        for card in self.__cards:
            card.show_card()

    def add_card(self, card):
        #Takes Card from player, updates total value and card count, adds card to hand
        self.__number_cards +=1
        self.__value += card.get_face_value()
        self.__cards.append(card)

    def useCard(self):
        #Do Something
        pass

    def get_value_of_hand(self):
        #Get hand value
        return self.__value

    def get_number_of_cards(self):
        #Get number of cards
        return self.__number_cards
        
