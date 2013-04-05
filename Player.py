from Hand import Hand
class Player(object):
	
    def __init__(self):
        self.__money = 0
        self.__bet = 0
        self.__hand = Hand()
        self.__want_card = True
        self.__name = "Test"
        self.__pixel = 0

    def set_money(self, money):
        self.__money = money

    def set_bet(self, bet):
        if bet > self.__money:
            return False
        else:
            self.__bet = bet
            return True

    def get_bet(self):
        return self.__bet

    def get_money(self):
        return self.__money

    def get_hand(self):
        return self.__hand

    def get_valuehand(self):
        return self.__hand.get_value_of_hand()

    def get_numcards(self):
        return self.__hand.get_number_of_cards()

    def receive_card(self, card):	
        self.__hand.add_card(card)

    def clear_hand(self):
        self.__hand = Hand()

    def get_want_card(self):
        return self.__want_card

    def set_want_card(self, plychoice):
        self.__want_card = plychoice

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_pixel(self, pixel):
        self.__pixel = pixel

    def get_pixel(self):
        return self.__pixel