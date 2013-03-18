

class Card():
	#face value is the number that the card will use zero will be the intial
	face_value = 0
	#Should be false unless otherwised specified
	face_down = False
	#Name is the name of the card IE King, Queen
	name = ""
	def __init__(self, face_value, name, face_down):
		"""Constructs the Card using the input from the callee"""
		self.face_value = face_value
		self.name = name
		self.face_down = face_down

	def 