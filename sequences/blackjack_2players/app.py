##blackjack game on two players
import random
from cards_value import deck, count_num, suit_list

#count_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
#suit_list = ['spades', 'worms', 'diamonds', 'crosses']
def main():
    card_deck = create_deck()

    while len(card_deck) != 0:
        answer_player1 = 'y'
        answer_player2 = 'y'
        counter_player1 = 0
        counter_player2 = 0
        while answer_player1 == 'y' or answer_player2 == 'y' or counter_player1 <= 21 or counter_player2 <= 21:
            card_player1 = random.choice(list(card_deck))
            value_card_player1 = card_deck[card_player1]
            if card_player1[0] == 'tuz':
                if counter_player1 + value_card_player1[1] <= 21:
                    value_card_player1 = value_card_player1[1]
                else:
                    value_card_player1 = value_card_player1[0]
            counter_player1 += value_card_player1
            print(card_player1, '-', value_card_player1, '=>', counter_player1)
            answer_player1 = input('1 more card?(y/n): ')
        
        if answer_player1 != 'y' or answer_player2 != 'y':
            
        print('Answer player - stop')


        
def create_deck():
    card_deck = dict()
    for suit in suit_list:
        for key, val in deck.items():        
            card_deck[(key, suit)] = val
    return card_deck



if __name__ in '__main__':
    main()
