from Player import Player
from Deck import Deck
from Hand import Hand
class Dealer(Player):
	"""This will encapuslate the dealer class"""
	
	def __init__(self):
		super(Dealer, self).__init__(10000)
		self.__deck = Deck()
		self.__all_bets = []
	
	def set_winner(players):
		"""Set the winner"""
		

	def start_new_hand(self):
		"""restart the game"""
		black_jack()

	def give_card_to_player(self, player):
		"""Take a card off the deck.
			This will also check to see if we need to change one of the dealers
			cards to face down.
		"""
		if(player.__class__.__name__ == 'Dealer'):
			if(player.get_hand().get_number_of_cards() == 1):
			#check to see if player is actually the dealer!
				c1 = self.__deck.deal_card()
				c1.set_face_down(True)
				player.recieve_new_card(c1)
			else:
				player.recieve_new_card(self.__deck.deal_card())
		else:
			player.recieve_new_card(self.__deck.deal_card())

	def shuffle_deck(self):
		"""make the deck random again"""
		self.__deck = Deck()

	def get_all_bets(self, player):
		"""get all the bets from the players"""
		self.__bet = 25
		self.__money = 999999
		self.__all_bets.append(self.__bet)
		player.betting()
		self.__all_bets.append(player.get_bet())

	def want_card(self):
		"""This will provide all the logic for wether a dealer should hit or stay"""
		pass

def black_jack():
	"""This will be the driver for the game. we only have a single player vs the dealer"""
	dealer = Dealer()
	player1 = Player(input("How much money does the player have?"))

	
	
	#this should be the black_jack hand, while the begging should be setting up a new game
	dealer.get_all_bets(player1)
	##deal two cards each, one to the dealer should be set to face down
	for x in xrange(1,3):
		dealer.give_card_to_player(player1)
		dealer.give_card_to_player(dealer)

	###Now the game is ready to start showing the hands of the dealer and the player should be done
	print "Dealer's Hand"
	dealer.get_hand().showHand()
	print "Player's Hand"
	player1.get_hand().showHand()
	while(player1.want_card()):
		dealer.give_card_to_player(player1)
		print "Players Hand"
		player1.get_hand().showHand()

	while(dealer.want_card()):
		dealer.give_card_to_player(dealer)
		print "Dealers Hand"
		dealer.get_hand().showHand()

	
	