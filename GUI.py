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
        self.play = 0

    def spawn_players(self):
        lbl_player('Dealer',2)
        txt = 'How many players?'
        num_player = int(askstring('Players', txt ))
        self.play = num_player
        ask_name = 'What is the players name?'
        ask_purse = 'How much money will you start with?'
        hit = True #What is this?
        for i in range(num_player):
            player = Player()
            name = askstring('Name', ask_name )
            money = float(askstring(name, ask_purse ))
            player.set_money(money)
            player.set_name(name)
            player.set_pixel(i+3)
            self.players.append(player)
            lbl_player(name,i+5)

    def place_bets(self):
        self.dealer.clear_hand()
        ask_bet = 'Please enter a bet'
        for player in self.players:
            bet = float(askstring(player.get_name(), ask_bet ))
            while (not player.set_bet(bet)):
                bet = float(askstring(player.get_name(), "Bet was greater than total"+ask_bet))
            player.clear_hand()
            player.set_want_card(True)
            self.play+=1

    def give_card(self):
        for player in self.players:
            self.dealer.give_card(player)
        self.dealer.give_card(self.dealer)
	
    def show_hands(self):
        print "Dealer's Hand"
        d1 = self.dealer.get_hand().get_cards()
        draw_cards(d1,0)
        for player in self.players:
            print player.get_name(),"'s Hand"
            d1 = player.get_hand().get_cards()
            draw_cards(d1,player.get_pixel())

    def hit_player(self):
        ask_card = 'Would you like to hit?'
        for player in self.players:
            #value = player.get_valuehand()
            if player.get_valuehand()<21 and player.get_want_card() is True:
                player.set_want_card(tkMessageBox.askyesno(player.get_name(), (ask_card+" Total: "+str(player.get_valuehand()))))
            else:
                self.play-=1
                player.set_want_card(False)
                #player[3] = False
            if(player.get_want_card()):
                self.dealer.give_card(player)
                print player.get_name(),"'s Hand"
                d1 = player.get_hand().get_cards()
                draw_cards(d1,player.get_pixel())

    def hit_dealer(self):
        self.dealer.get_hand().flip_card()
        print "Dealer's Hand"
        d1 = self.dealer.get_hand().get_cards()
        draw_cards(d1,0)
        value = self.dealer.get_valuehand()
        while(value<17):
            self.dealer.give_card(self.dealer)
            print "Dealer's Hand"
            d1 = self.dealer.get_hand().get_cards()
            draw_cards(d1,0)
            value = self.dealer.get_valuehand()

    def pick_winner(self):
        mes = "Winner! Won: "
        mes2 = "Tie"
        mes3 = "Dealer Wins Total: "
        d_val = self.dealer.get_valuehand()
        print "Dealer: ",d_val
        for player in self.players:
            p_val = player.get_valuehand()
            print player.get_name(),": ",p_val
            money = player.get_money()
            bet = player.get_bet()
            if (d_val<p_val<=21) or (d_val>21 and p_val<=21):
                winnings = bet*2
                money+=(winnings)
                player.set_money(money)
                var = mes+str(winnings)+" Total: "+str(money)
                tkMessageBox.showwarning(player.get_name(),var)
            elif d_val==p_val:
                tkMessageBox.showwarning(player.get_name(),mes2)
            else:
                money-=bet
                player.set_money(money)
                var = mes3+str(money)
                tkMessageBox.showwarning(player.get_name(),var)
                

    def loop(self):
        mes = "Play another hand?"
        new_hand = True
        while(new_hand):
            self.place_bets()
            self.give_card()
            self.give_card()
            self.show_hands()
            while(self.play>0):
                self.hit_player()
            self.hit_dealer()
            self.pick_winner()
            new_hand = tkMessageBox.askyesno("Game",mes)
            im_c.lbl_rmv()

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
    game.loop()

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
