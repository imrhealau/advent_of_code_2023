from helper import get_day, get_test_data
from enum import Enum
import functools

data = get_day(7)

# data = ['32T3K 765',
#         'T55J5 684',
#         'KK677 28',
#         'KTJJT 220',
#         'QQQJA 483']

hands = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

class HandType(Enum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7

def hand_strength(cards):
    # hand_type == "Five of a kind":
    if len(set(cards)) == 1:
        return HandType.FiveOfAKind, cards

    elif len(set(cards)) == 2 :
        for card in set(cards):
            # hand_type == "Four of a kind":
            if cards.count(card) == 4:
                return HandType.FourOfAKind, cards
            
            # hand_type == "Full house":
            if cards.count(card) == 3:
                remaining_cards = set(cards) - {card}
                return HandType.FullHouse, cards

    elif len(set(cards)) == 3: 
        for card in set(cards):  
            # hand_type == "Three of a kind":         
            if cards.count(card) == 3:
                return HandType.ThreeOfAKind, cards
            # hand_type == "Two pair":
            if cards.count(card) == 2:
                return HandType.TwoPair, cards
                
    # hand_type == "One pair":
    elif len(set(cards)) == 4: 
        return HandType.OnePair, cards
    # hand_type == "High card":
    return HandType.HighCard, cards


def sort_cards(card1, card2):
    if card1[0][0] != card2[0][0]:
        return card1[0][0].value - card2[0][0].value
    for i in range(5):
        if card1[0][1][i]!= card2[0][1][i]:
            return hands.index(card2[0][1][i]) - hands.index(card1[0][1][i])
        

cards_bids = [(hand_strength(card[0:5]), card[6:]) for card in data]
cards_bids  = sorted(cards_bids,key=functools.cmp_to_key(sort_cards))

q1_sum = 0
for i in range(len(cards_bids)):
    q1_sum += int(cards_bids[i][1]) * (i+1)

print(q1_sum)

#---------
# Part 2
#---------
hands = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def new_handtype(card,bid):
    strength = card[0]
    hand = card[1]

    if 'J' in hand:
        for c in set(hand):
            if c != 'J':
                hand2 = hand.replace('J',c)
                if hand_strength(hand2)[0].value > strength.value:
                    strength = hand_strength(hand2)[0]

    return ((strength,hand),bid)
    
cards_bids2 = [new_handtype((hand_strength(card[0:5])), card[6:]) for card in data]
cards_bids2  = sorted(cards_bids2,key=functools.cmp_to_key(sort_cards))

q2_sum = 0
for i in range(len(cards_bids2)):
    q2_sum += int(cards_bids2[i][1]) * (i+1)

print(q2_sum)