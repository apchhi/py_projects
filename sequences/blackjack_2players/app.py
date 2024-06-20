##blackjack game on two players
#import random
from cards_value import deck
count_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suit_list = ['spades', 'worms', 'diamonds', 'crosses']
def main(count_num, suit_list):
    create_deck(count_num, suit_list)
    
    suit_card = random.choice(suit_list)

def create_deck(nums, suits):
    card_deck = dict()
    for suit in suits:
        for num in nums:
            value = cards_value.get(num)
            card_deck[(num, suit)] = deck[num]
    print(card_deck)
    
if __name__ in '__main__':
    main(count_num, suit_list)