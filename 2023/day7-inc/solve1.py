# credit: 0xdf

from typing_extensions import Self
from enum import IntEnum

with open('input.txt','r') as f:
    input = [i.strip() for i in f.readlines()]


class HANDTYPE(IntEnum):
    HIGHCARD = 1
    PAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7

#weakest to strongest mapping
card_map = {'T':'A', 'J':'B', 'Q':'C', 'K':'D', 'A':'E'}

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type =  self.get_hand_type()

    def __repr__(self):
        return f"<HAND {self.hand}: {self.type}>"


    def __eq__(self, other: Self) -> bool:
        return self.hand == other.hand
     

    def __gt__(self, other: Self) -> bool:
        if self.type == other.type:
            selfcards = [card_map.get(i,i) for i in self.hand]
            othercards = [card_map.get(i,i) for i in other.hand]
            
            return selfcards > othercards
        return self.type > other.type

    def get_hand_type(self) -> HANDTYPE:
        counts = [self.hand.count(c) for c in self.hand]
        if 5 in counts:
            return HANDTYPE.FIVEOFAKIND
        if 4 in counts:
            return HANDTYPE.FOUROFAKIND
        if 3 in counts:
            if 2 in counts:
                return HANDTYPE.FULLHOUSE
            return HANDTYPE.THREEOFAKIND

        if counts.count(2) == 4:
            return HANDTYPE.TWOPAIR
        if 2 in counts:
            return HANDTYPE.PAIR

        return HANDTYPE.HIGHCARD




hands = [i.split()[0] for i in input]
bids = [i.split()[1] for i in input]

sorted_hands = sorted([Hand(i,j) for i,j in zip(hands,bids)])
final_sum = 0
for rank, hand in enumerate(sorted_hands, 1):
    final_sum += rank * hand.bid

print(final_sum)

