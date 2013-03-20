#!/usr/bin/python

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


	def get_face_value(self):
		"""Get the face value"""
		return self.face_value


	def get_name(self):
		"""Get the name of the card"""
		return self.name


	def set_face_value(self, face_value):
		"""Set the face value to the given value"""
		self.face_value = face_value

	def set_face_down(self, face_down):
		"""Set the face down Boolean to specified Value"""
		self.face_down = face_down


	def show_card(self):
		if (self.face_down):
			print "Face Down\n"
		else:
			print "*****Card****\nName: %s\nFace Value:  %d\n" % (self.name, self.face_value)


