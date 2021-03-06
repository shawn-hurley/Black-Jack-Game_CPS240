from Player import Player
from Deck import Deck
from Hand import Hand
class Dealer(Player):
    """This will encapuslate the dealer class"""
    
    def __init__(self):
        super(Dealer, self).__init__(10000)
        self.__deck = Deck()
        self.__all_bets = []    
    
    def set_winner(self, player):
        """Set the winner Dealer will always win in a tie"""
        if player.get_value_of_hand() > 21:
            print "Player busted and you lose"
            player.set_money((player.get_money()-player.get_bet()))

        elif player.get_value_of_hand() > self.get_value_of_hand():
            print "YOU WIN!"
            player.set_money((player.get_money()+player.get_bet()))
            
        elif self.get_value_of_hand() > 21:
            print "YOU WIN!"
            player.set_money((player.get_money()+player.get_bet()))
        else:
            print "You lose"
            player.set_money((player.get_money()-player.get_bet()))
        
        print "You have %d left to play with" % player.get_money()
        

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
        """make the deck random again, also the dealer should recieve a new hand"""
        self.__deck = Deck()


    def get_all_bets(self, player):
        """get all the bets from the players"""
        self.__bet = 25
        self.__money = 999999
        self.__all_bets.append(self.__bet)
        player.betting()
        self.__all_bets.append(player.get_bet())

    def want_card(self):
        """This will provide all the logic for whether a dealer should hit or stay
            As of right now we have the dealer standing on all 17's which is the most
            conseritive.
        """

        choice = True
        if self.get_hand().get_value_of_hand() >= 17:
            choice = False
        else:
            choice = True
        return choice

    def flip_card_over(self):
        """flip the card over because other wise that makes no sense"""
        self.get_hand().flip_card_over()


def black_jack():
    """This will be the driver for the game. we only have a single player vs the dealer"""
    dealer = Dealer()
    player1 = Player(input("How much money does the player have?"))
    want_to_play = 1
    while(want_to_play == 1):
        dealer.shuffle_deck()
        dealer.ready_for_next_hand()
        player1.ready_for_next_hand()

        black_jack_hand(player1, dealer)
        want_to_play = input("Would you like to play another hand? Select 1 for Yes and 0 for no")
    
def black_jack_hand(player1, dealer):
    """This will be the code for a single hand. it should just exit and return back to the calle
        which will be black_jack game
    """ 
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

    
    dealer.flip_card_over()
    while(dealer.want_card()):
        dealer.give_card_to_player(dealer)
        
    print "Dealers Hand"
    dealer.get_hand().showHand()

    dealer.set_winner(player1)

    
    