from Hand import Hand
class Player(object):
	
    def __init__(self):
	self.__money = 0
	self.__bet = 0
	self.__hand = Hand()

    def set_money(self, money):
	self.__money = money

    def set_bet(self, bet):
	self.__bet = bet

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
