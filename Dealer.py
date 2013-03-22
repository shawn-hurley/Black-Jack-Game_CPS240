from Player import Player
from Deck import Deck
class Dealer(Player):
	"""This will encapuslate the dealer class"""
	deck = Deck()
	allbets = []

	def __init__(self):
		super(Dealer, self).__init__()
	
	def set_winner(players):
		"""Set the winner"""
		

	def start_new_hand():
		"""restart the game"""
		black_jack()

	def give_card_to_player():
		"""Take a card off the deck."""
		return deck.deal_card()

	def shuffle_deck():
		"""make the deck random again"""
		self.deck = Deck()

	def get_all_bets(self, player):
		"""get all the bets from the players"""
		self.bet = 25
		self.money = 999999
		allbets[1] = self.bet
		allbets[2] = player.bet

	def want_card(self):
		"""This will provide all the logic for wether a dealer should hit or stay"""
		pass

def black_jack():
	"""This will be the driver for the game. we only have a single player vs the dealer"""
	dealer = Dealer()
	player1 = Player()
	dealer.get_all_bets()
	print dealer.allbets
	##deal two cards each, one to the dealer should be set to face down
	for x in xrange(1,3):
		player.recieve_new_card(dealer.give_card_to_player())

	dealer.recieve_new_card(dealer.give_card_to_player().set_face_down(True))
	dealer.recieve_new_card(dealer.give_card_to_player())
	###Now the game is ready to start showing the hands of the dealer and the player should be done
	dealer.hand.showHand()
	player.showHand()
	while(player.want_card()):
		player.recieve_new_card(dealer.give_card_to_player())

	
	