from Hand import Hand
class Player(object):
	"""Player will represent the behavior and data of a player"""
	#These will be the class variables.

	def __init__(self, money):
		self.__money = money
		self.__hand = Hand()
		self__bet = 0

	def get_hand(self):
		"""Return the entire hand"""
		return self.__hand

	def get_value_of_hand(self):
		"""Return the value of the hand"""
		return self.__hand.get_value_of_hand()

	def get_number_of_cards(self):
		"""Return the number of cards"""
		return self.__hand.get_number_of_cards()

	def set_bet(self, bet):
		"""Set the bet for this player"""
		self.__bet = bet

	def get_bet(self):
		"""Get the bet for this player"""
		return self.__bet

	def get_money(self):
		"""Get the Money for this player"""
		return self.__money

	def set_money(self, money):
		"""set the amount of money the player should have"""
		self.__money = money
	def recieve_new_card(self, card):
		"""Should take the new Card and add it to the hand"""	
		self.__hand.add_card(card)

	def want_card(self):
		"""Ask this player if they would like to get another card
			Also check to see if the player has busted, because if they have
			they can not recieve any new cards.
		"""		
		#print self.__hand.get_value_of_hand()
		if self.__hand.get_value_of_hand() > 21:
			print "You have busted"
			choice = False
			
		
		else:
			choice = raw_input("Would you like another card? (Please Enter True or False\n")
			if choice == 'True':
				choice = True
			else:
				choice = False

		return bool(choice)

	def betting(self):
		self.__bet = input("What is the players bet\n")

	def ready_for_next_hand(self):
		"""Get the Player ready for the next hand."""
		self.__hand = Hand()
		self.__bet = 0
		