from Hand import Hand
class Player():
	"""Player will represent the behavior and data of a player"""
	#These will be the class variables.
	hand = Hand()
	money = 0
	bet = 0

	def __init__(self, money):
		self.money = money


	def get_hand(self):
		"""Return the entire hand"""
		return self.hand

	def get_value_of_hand(self):
		"""Return the value of the hand"""
		return self.hand.get_value_of_hand()

	def get_number_of_cards(self):
		"""Return the number of cards"""
		return self.hand.get_number_of_cards()

	def set_bet(self, bet):
		"""Set the bet for this player"""
		self.bet = bet

	def get_bet(self):
		"""Get the bet for this player"""
		return self.bet

	def get_money(self):
		"""Get the Money for this player"""
		return self.money

	def recieve_new_card(self, card):
		"""Should take the new Card and add it to the hand"""
		self.hand.add_card(card)

	def want_card(self):
		"""Ask this player if they would like to get another card"""
		choice = raw_input("Would you like another card? (Please Enter True or False\n")
		return bool(choice)
		