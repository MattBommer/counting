import sys

"""
This list is basic strategy for hitting and staying on hard hands (hands without aces) in blackjack.
The row is equal to the players hand value and the column is the dealers hand. 
The following elements may occur and their values are: H = hit, S = stay, D = double down.
Eqn for calculating ROW indices into the list: row = total - 8; if less than 8 then always hit
Eqn for calculating COLUMN indices into the list: col = upcard - 2;
These lists model the basic strategies found on https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
"""
hard_totals = [["H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
               ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
               ["D", "D", "D", "D", "D", "D", "D", "D", "H", "H"],
               ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
               ["H", "H", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "H", "H", "H", "H", "H"],
               ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]]


"""
This list is basic strategy for hitting and staying on soft hands (hands containing an ace) in blackjack.
The row is equal to the players hand value and the column is the dealers hand. 
The following elements may occur and their values are: H = hit, S = stay, D = double down.
Eqn for calculating ROW indices into the list: row = non_ace_card - 2;
Eqn for calculating COLUMN indices into the list: col = upcard - 2;
These lists model the basic strategies found on https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
"""
soft_totals = [["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
               ["H", "H", "H", "D", "D", "H", "H", "H", "H", "H"],
               ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
               ["H", "H", "D", "D", "D", "H", "H", "H", "H", "H"],
               ["H", "D", "D", "D", "D", "H", "H", "H", "H", "H"],
               ["D", "D", "D", "D", "D", "S", "S", "H", "H", "H"],
               ["S", "S", "S", "S", "D", "S", "S", "S", "S", "S"],
               ["S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]]

"""
This list is basic strategy for splitting pairs in blackjack.
The row is equal to the players hand value and the column is the dealers hand. 
The following elements may occur and their values are: Y = split, N = don't split, Y/N = split if you can double down after spliting.
Eqn for calculating ROW indices into the list: row = one_of_the_pair - 2;
Eqn for calculating COLUMN indices into the list: col = upcard - 2;
These lists model the basic strategies found on https://www.blackjackapprenticeship.com/blackjack-strategy-charts/
"""
pair_splitting = [["Y/N", "Y/N", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
                  ["Y/N", "Y/N", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
                  ["N", "N", "N", "Y/N", "Y/N", "N", "N", "N", "N", "N"],
                  ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
                  ["Y/N", "Y", "Y", "Y", "Y", "N", "N", "N", "N", "N"],
                  ["Y", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N"],
                  ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
                  ["Y", "Y", "Y", "Y", "Y", "N", "Y", "Y", "N", "N"],
                  ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N"],
                  ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"]]


interpretation  = {"H" : "hit", "S" : "stay", "D" : "double down", "Y" : "split the pair", "N" : "DON'T split the pair", "Y/N" : "split only if you can double down after"}

#Args: 
#   0 : The number of decks being used for the shoe (usually 6 or 8), 
#   1 : The number of players at the table besides yourself
#   2 : Potentially the pre-existing count but will add later
def main(args):
    try:
        deck_num = int(args[0])
        player_num = int(args[1])
        player_position = int(args[2])
    except ValueError:
        print("One or more arguements is not of type int")
        sys.exit()
    cc = Count(deck_num)
    cc.add_players(player_num)
    cc.place_the_player(player_position)
    while True:
        cc.run_round()
        cc.running_count()
        #This returns the true count.
        tc = cc.true_count()
        ev = tc * .5
        print("The true count is: " + tc)
        print("The expected value is " + ev)
        if ev > 0:
            print("The player has the advantage!")
        else:
            print("The house has the advantage!")
        bet = (tc - 1)/2
        print("You should bet " + bet + " units")
        cc.reset()
        l = input("What players (by positions) left?")
        for x in l.split():
            try:
                cc.remove_player(int(x))
            except ValueError:
                print("Input is not a number")
        j = input("What players (by positions) joined?")
        for x in j.split():
            try:
                cc.insert_player(int(x))
            except ValueError:
                print("Input is not a number")



class Count:

    def __init__(self, deck_num, card_num=0, card_count=0):
        self.run_count = card_count
        self.card_num = card_num
        self.deck_num = deck_num
        self.dealer = Player()
        self.the_player = Player(True)
        self.players = []

    def place_the_player(self, pos):
        self.players.insert(pos, self.the_player)

    def add_players(self, num):
        for _ in range(num):
            self.players.append(Player())

    def insert_player(self, idx):
        self.players.insert(idx)

    def remove_player(self, pos):
        self.players.pop(pos)

    def running_count(self):
        for x in self.players:
            hand = x.get_hand()
            self.run_count += hand.ret_count()
            self.card_num += hand.num_cards()
            self.update_deck()
    

	#come back too, I would like it to be so that the deck number is rounded to the nearest half
    def update_deck(self):
        if self.card_num >= 26:
            self.card_num -= 26
            self.deck_num -= .5

    #round to the nearest int
    def true_count(self):
        return self.run_count // self.deck_num

    def run_round(self):
        for l in range(2):
            for x in self.players:
                val = None
                if x.is_the_player:
                    val = input("Your card: ").strip().replace(" ","")
                else:
                    val = input("Player card: ").strip().replace(" ","")
                x.hand_dealt(val)
            if l < 1:
                self.dealer.hand_dealt(input("Dealers upcard: ").strip().replace(" ",""))
        upidx = self.dealer.get_hand().hand_value() - 2
        for i,p in enumerate(self.players):
            curr_hand = p.get_hand()
            total = curr_hand.hand_value()
            stay = True
            skip = True
            print("Player " + i + " turn.")
            while (total < 21 and stay):
                if p.is_the_player:
                    self.basic_strategy(curr_hand, total, upidx)
                if skip and p.get_hand().is_pair():
                    inp = input("Did the player split? (y for yes, n for no)")
                    if inp == 'y':
                        stay = self.run_split(p)
                    else: 
                        skip = False
                else:
                    val = input("Next card (use s to indicate the player is staying): ").strip().replace(" ","")
                    stay = False if val.lower() == "s" else True
                    if stay:
                        curr_hand.hand_dealt(val)
                        total = curr_hand.hand_value()
        self.run_dealer()
        

    #finish this
    def run_split(self, player):
        h1 = player.get_hand()
        h2 = player.get_hand(True)
        h2.add_cards(h1.get_card(1).get_card_str())
        h1.remove_card(1)
        hands = [h1, h2]
        for i,h in enumerate(hands):
            stay = True
            total = h.hand_value()
            while (total < 21 and stay):
                val = input("Next card of split " + i + " (use s to indicate the player is staying): ").strip().replace(" ","")
                stay = False if val.lower() == "s" else True
                if stay:
                    h.hand_dealt(val)
                    total = h.hand_value()	
        return False

    def run_dealer(self):
        dealer = self.dealer.get_hand()
        total = dealer.hand_value()
        while(total < 17):
            val = input("Next card from dealer: ")
            self.dealer.hand_dealt(val)
            total = dealer.hand_value()

    def basic_strategy(self, curr_hand, total, upidx):
        print("It\'s your turn now!")
        if curr_hand.is_pair:
            print(interpretation[pair_splitting[curr_hand.get_card(0).get_value() - 2][upidx]])
            #Implement splitting option where player has more than one hand
        elif curr_hand.ace():
            print(interpretation[soft_totals[total - 13][upidx]])
        else:
            if total > 17:
                print("stay")
            elif total < 8:
                print("hit")
            else:
                print(interpretation[hard_totals[total - 8][upidx]])

    def reset(self):
        for p in self.players:
            p.flush_player_hand()
        self.dealer.flush_player_hand()

class Player:
    def __init__ (self, the_player=False):
        self.hand = Hand()
        self.split = Hand()
        self.the_player = the_player
    
    def flush_player_hand(self):
        self.hand = Hand()
        self.split = Hand()

    def hand_dealt(self, card, split=False):
        self.split.add_cards(card) if split else self.hand.add_cards(card) 

    def get_hand(self, split=False):
        return self.split if split else self.hand

    def is_the_player(self):
        return self.the_player


#This class is for the "hands" (or cards received from the dealer) of a player/dealer
class Hand:

    def __init__(self, cards=[]):
        self.cards = []
        self.value = 0
        self.has_ace = False
        self.pair = False
        self.hand_count = 0
        self.idx = 0
        self.add_cards(cards)
        self.update_hand()

    def flush_hand(self):
        self.value = 0
        self.has_ace = False
        self.pair = False
        self.hand_count = 0
        self.idx = 0

    def add_cards(self, card):
        self.cards.append(Card(card))
        self.update_hand()

    def remove_card(self, num):
        self.cards.pop(num)
        self.flush_hand()
        self.update_hand()

    def ret_count(self):
        return self.hand_count

    def update_hand(self):
        if self.idx < len(self.cards):
            for x in self.cards[self.idx:]:
                self.hand_count += x.get_count()
                self.value += x.get_value()
                if not self.has_ace:
                    self.has_ace = x.is_ace()
            if self.idx < 2:
                self.pair = self.cards[0].is_pair(self.cards[1])
            self.idx = len(self.cards)
        if self.value > 21 and self.has_ace:
            for x in self.cards:
                if x.is_ace and x.get_value != 1:
                    x.set_ace()
                    break

    def get_card(self, idx):
        return self.cards[idx]

    def ace(self):
        return self.has_ace

    def is_pair(self):
        return self.pair

    def hand_value(self):
        return self.value

    def num_cards(self):
    	return len(self.cards)

class Card:

    card = {'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11 }

    def __init__ (self, val):
        self.card_num = str(val)
        self.card_val = 0
        try:
            self.card_val += int(val)
        except ValueError:
            self.card_val += self.card[val.upper()]

        if self.card_val >= 10:
            self.count_val = 1
        elif self.card_val <= 6:
            self.count_val = -1
        else:
            self.count_val = 0

    def is_ace (self):
        return 'A' == self.card_num.upper()

    def get_count (self):
        return self.count_val

    def set_ace(self):
        self.card_val = 1

    def get_value(self):
        return self.card_val

    def get_card_str(self):
        return self.card_num

    def is_pair(self, other_card):
        return self.card_num == other_card.get_card_str()
        

if __name__ == "__main__":
    main(sys.argv[1:])