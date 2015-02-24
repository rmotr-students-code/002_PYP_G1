# slot machine game
#player wagers tokens and recieves a payout based on
#whether 2 or 3 numbers match, in conjunction with some bonus based on their multiplyer score
#multipliyer is increased by hitting 2 or 3 in a row, and decreased whenever no numbers match.
# ex payout of hitting 2 of a kind would be larger if you hit 2 of a kind in the previous
# spin because the multiplyer value would be higher.
from random import randrange
from numbergraphic import *


class Player:
    def __init__(self, name):
        self.name = name
        self.tokens = 0
        self.luck = 0

    def add_tokens(self, numtokens):
        self.tokens += numtokens

    def add_luck(self):
        self.luck += 1


class Slot_machine:
    def __init__(self):
        self.numbers = []
        self.multiplyer = 1

    def spin(self):
        self.numbers = [randrange(1, 11) for x in range(3)]

    def up_multi(self):
        if self.multiplyer < 3:
            self.multiplyer += 1
        else:
            pass

    def down_multi(self):
        if self.multipliyer > 1:
            self.multiplyer -= 1
        else:
            pass

    def rep_numbers(self):
        mylist = []
        for x in self.numbers:
            mylist.append(num_list[x-1])  #Trying to get these to print out on one line instead of vertically
        print mylist

#each object in num_list from numbergraphic corresponds to a number image
#num_list = [one, two, three, four, five, six,
#			seven, eight, nine, ten]

##Test

def test():
    slot = Slot_machine()

    slot.spin()
    slot.rep_numbers()
    print "create slot instance, print numbers attribute after spinning: "
    print slot.numbers, "\n"
'''
    print "**Create player instance, print amt of tokens(0): "
    player1 = Player('Alan')
    print player1.tokens, "\n"

    print "**add_tokens(10), print player tokens(10): "
    player1.add_tokens(10)
    print player1.tokens, "\n"

    print dir(player1)
'''

test()