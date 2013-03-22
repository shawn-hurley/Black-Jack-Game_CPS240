#Sean Mead

#game plays until the deck is gone.
#Each player is dealt two cards at the beginning
#Aces are seen as 11 points but will be reduced automatically if the player goes over 21

import select
import random
import time


print 'The Game of Black Jack'
print
deck = {'Ace of Diamonds':11, 'Two of Diamonds':2, 'Three of Diamonds':3, 'Four of Diamonds':4,'Five of Diamonds':5,'Six of Diamonds':6,'Seven of Diamonds':7,'Eight of Diamonds':8,'Nine of Diamonds':9,'Ten of Diamonds':10,'Jack of Diamonds':10,'Queen of Diamonds':10,'King of Diamonds':10,'Ace of Hearts':11, 'Two of Hearts':2, 'Three of Hearts':3, 'Four of Hearts':4,'Five of Hearts':5,'Six of Hearts':6,'Seven of Hearts':7,'Eight of Hearts':8,'Nine of Hearts':9,'Ten of Hearts':10,'Jack of Hearts':10,'Queen of Hearts':10,'King of Hearts':10,'Ace of Clubs':11, 'Two of Clubs':2, 'Three of Clubs':3, 'Four of Clubs':4,'Five of Clubs':5,'Six of Clubs':6,'Seven of Clubs':7,'Eight of Clubs':8,'Nine of Clubs':9,'Ten of Clubs':10,'Jack of Clubs':10,'Queen of Clubs':10,'King of Clubs':10, 'Ace of Spades':11, 'Two of Spades':2, 'Three of Spades':3, 'Four of Spades':4,'Five of Spades':5,'Six of Spades':6,'Seven of Spades':7,'Eight of Spades':8,'Nine of Spades':9,'Ten of Spades':10,'Jack of Spades':10,'Queen of Spades':10,'King of Spades':10}

def cardpick (haveAce, totalp1):
    cardp1 = random.choice(deck.items())
    deck.pop(cardp1[0])

    if cardp1[1] == 11:
        haveAce = haveAce + 1
    else:
        haveAce = haveAce
    totalp1 = totalp1 + cardp1[1]
    return haveAce, totalp1, cardp1[0]

def figure (totalp1,haveAce,dec,bust):
    if totalp1>21:
        if haveAce > 0:
            haveAce = haveAce - 1
            totalp1 = totalp1 - 10
            dec = 0
        else:
            bust = 1
    elif totalp1 == 21:
        bust = 1
        dec = 1
    else:
        dec = 0
    return totalp1, haveAce, dec, bust

def playerchoose(dec,totalp1,bust):
    while dec == 0:
        print 'hit or stay: '
        time.sleep(1)
        print 'hit'
        choice = 'hit'
        choice = raw_input('hit or stay: ')
        if choice == 'stay':
            dec = 1
            bust = 1
        elif choice == 'hit':
            dec = 1
        else:
            dec = 0
    return dec, bust

def rungame():
    totalp1 = 0
    totalp2 = 0
    bust1 = 0
    bust2 = 0
    haveAce1 = 0
    haveAce2 = 0
    haveAced = 0
    dec1 = 0
    dec2 = 0
    cardp1 =''
    cardp2 = ''
    stay1 = 0
    stay2 = 0

    haveAce1, totalp1, cardp1 = cardpick(haveAce1, totalp1)
    print cardp1, 'for player', name1
    print

    haveAce2, totalp2, cardp2 = cardpick(haveAce2, totalp2)

    print cardp2, 'for player', name2
    print

    while bust1 & bust2 ==0:

        if bust1 == 0:
            haveAce1, totalp1, cardp1 = cardpick(haveAce1, totalp1)
            print cardp1, 'for player',name1
            totalp1, haveAce1, dec1, bust1 = figure(totalp1,haveAce1,dec1,bust1)
            if totalp1>21:
                stay1 = 0
                print name1, 'busted.'
                print
            else:
                stay1 = 1
                print
        else:
            print name1, 'passes.'
            print

        if bust2 == 0:
            haveAce2, totalp2, cardp2 = cardpick(haveAce2, totalp2)
            print cardp2, 'for player',name2
            totalp2, haveAce2, dec2, bust2 = figure(totalp2,haveAce2,dec2,bust2)
            if totalp2>21:
                stay2 = 0
                print name2, 'busted.'
                print
            else:
                stay2 = 1
                print
        else:
            print name2, 'passes.'
            print


        if bust1 == 0:
            print name1, 'your total is', totalp1
            dec1, bust1 = playerchoose(dec1,totalp1,bust1)
            print
        else:
            print

        if bust2 == 0:
            print name2, 'your total is', totalp2
            dec2, bust2 = playerchoose(dec2,totalp2,bust2)
            print
        else:
            print


    print
    print
    print 'Final Score'

    print name1, totalp1
    print name2, totalp2

    if totalp1>21:
        totalp1=0
    else:
        totalp1
    if totalp2>21:
        totalp2=0
    else:
        totalp2

    if totalp1>totalp2:
        print name1, 'wins!'
    else:
        print name1, 'busts'
    
    if totalp2>totalp1:
        print name2, 'wins!'
    else:
        print name2, 'busts'

    if totalp2==totalp1:
        print name1, 'and', name2, 'tie.'
    else:
        print
    

run = 1
name1 = raw_input('Enter your name player 1: ')
name2 = raw_input('Enter your name player 2: ')
while run == 1:
    try:
        rungame()
    except IndexError:
        run = 0
        print 'Out of Cards'





