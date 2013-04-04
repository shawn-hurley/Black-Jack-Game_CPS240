class Card():
    """This is the card class, will represent a single card"""
    #face value is the number that the card will use zero will be the intial
    #Should be false unless otherwised specified
    #Name is the name of the card IE King, Queen
    def __init__(self, face_value, name, face_down):
        """Constructs the Card using the input from the callee"""
        self.__face_value = face_value
        self.__name = name
        self.__face_down = face_down

    def get_face_value(self):
        """Get the face value"""
        return self.__face_value

    def get_name(self):
        """Get the name of the card"""
        return self.__name

    def get_face_down(self):
        return self.__face_down

    def set_face_value(self, face_value):
        """Set the face value to the given value"""
        self.__face_value = face_value

    def set_face_down(self, face_down):
        """Set the face down Boolean to specified Value"""
        self.__face_down = face_down

    def show_card(self):
    card = "Face Down"
        if (self.__face_down):
            pass
        else:
            card = self.__name
	return card
