from Player import Player

class Dealer(Player):
	"""This will encapuslate the dealer class"""
	
	def __init__(self, arg):
		super(Dealer, self).__init__()
		self.arg = arg
	
	