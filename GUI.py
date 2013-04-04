from Tkinter import *
import tkMessageBox
from tkSimpleDialog import *
from tkFileDialog import *
from Player import Player
from Dealer import Dealer
from Deck import Deck
from Hand import Hand

class image_object(object):
    def __init__(self):
  self.im_cards = []
	self.cards = []
	self.im_dict = dict()
	self.lbl = []

    def lbl_add(self,lbl):
	self.lbl.append(lbl)

    def lbl_rmv(self):
	for lbl in self.lbl:
	    lbl.grid_forget()
	    lbl.destroy()
	self.lbl = []

    def pop_dict(self):
	values = ['2','3','4','5','6','7','8','9','10']
	suits = ["Spades","Clubs","Hearts","Diamonds"]
	faces = ["Jack of ","Queen of ","King of ","Ace of "]
	of = " of "
	im_vals = ['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
	im_suits = ['s','c','h','d']
	im_loc = "Cards/"
	im_ext = ".gif"

	for suit in suits:
    	    for value in values:
		self.cards.append(value+of+suit)
    	    for face in faces:
		self.cards.append(face+suit)
	self.cards.append('Face Down')

	for suit in im_suits:
    	    for val in im_vals:
		self.im_cards.append(PhotoImage(file=(im_loc+val+suit+im_ext)))
	self.im_cards.append(PhotoImage(file=('Cards/back.gif')))

	self.im_dict = dict(zip(self.cards,self.im_cards))

    def is_in(self,var):
	return self.im_dict[var]

class Game(object):
    def __init__(self):
	self.dealer = Dealer()
	self.dealer.set_money(999999)
	self.dealer.set_bet(1)
	self.players = []

    def spawn_players(self):
	lbl_player('Dealer',2)
	txt = 'How many players?'
	num_player = int(askstring('Players', txt ))
	ask_name = 'What is the players name?'
	ask_purse = 'How much money will you start with?'
	for i in range(num_player):
	    player = Player()
	    name = askstring('Name', ask_name )
	    money = float(askstring(name, ask_purse ))
	    player.set_money(money)
	    self.players.append([player,name,i+3])
	    lbl_player(name,i+5)

    def place_bets(self):
	self.cur_dealer = self.dealer
	ask_bet = 'Please enter a bet'
	for player in self.players:
	    bet = float(askstring(player[1], ask_bet ))
	    player[0].set_bet(bet)

    def give_two(self):
	for player in self.players:
	    self.cur_dealer.give_card(player[0])
	self.cur_dealer.give_card(self.cur_dealer)
	for player in self.players:
	    self.cur_dealer.give_card(player[0])
	self.cur_dealer.give_card(self.cur_dealer)
	
    def show_hands(self):
	print "Dealer's Hand"
	d1 = self.cur_dealer.get_hand().get_cards()
	draw_cards(d1,0)
	for player in self.players:
	    print player[1],"'s Hand"
    	    d1 = player[0].get_hand().get_cards()
	    draw_cards(d1,player[2])

    def hit_stay(self):
	ask_card = 'Would you like to hit?'
	hit = False
	for player in self.players:
	    value = player[0].get_valuehand()
	    if value<21:
	    	hit = bool(askstring(player[1], ask_card ))
	    if(hit):
		self.cur_dealer.give_card(player[0])
		print player[1],"'s Hand"
		d1 = player[0].get_hand().get_cards()
		draw_cards(d1,player[2])

    def hit_dealer(self):
	self.cur_dealer.get_hand().flip_card()
	print "Dealer's Hand"
	d1 = self.cur_dealer.get_hand().get_cards()
	draw_cards(d1,0)
	value = self.cur_dealer.get_valuehand()
	while(value<17):
	    self.cur_dealer.give_card(self.cur_dealer)
	    print "Dealer's Hand"
	    d1 = self.cur_dealer.get_hand().get_cards()
	    draw_cards(d1,0)
	    value = self.cur_dealer.get_valuehand()

    def pick_winner(self):
	for player in self.players:
	    value = player[0].get_valuehand()
	    print player[1],": ",value
	value = self.cur_dealer.get_valuehand()
	print "Dealer: ",value

def draw_cards(d1,p):
    im = []
    for card in d1:
	im.append(im_c.is_in(card.show_card()))
    cnt = 2
    for photo in im:
	label = Label(image=photo)
	label.image = photo
	label.grid(row=p+2, column=cnt, pady=5, sticky=NS)
	im_c.lbl_add(label)
	cnt+=1

def start_game():
    im_c.lbl_rmv()
    game = Game()
    game.spawn_players()
    game.place_bets()
    game.give_two()
    game.show_hands()
    game.hit_stay()
    game.hit_dealer()
    game.pick_winner()

def lbl_player(name,rw):
    player = Label(text=name)
    player.grid(row=rw, column=1)

def btn_start(root):
    StartGame = Button(root, text="Start Game", \
                        command=start_game)
    StartGame.config(width=10)
    StartGame.grid(row=1, column=1, pady=5, sticky=NS)

root = Tk()
root.title('BlackJack')
root.geometry("800x600")
im_c = image_object()
im_c.pop_dict()
btn_start(root)


root.mainloop()
