##blackjack game on two players
import random
from cards_value import deck, count_num, suit_list

#count_num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
#suit_list = ['spades', 'worms', 'diamonds', 'crosses']
def main():
    card_deck = create_deck()
    stage = 0
    while len(card_deck) != 0:
        answer_player1 = 'y'
        answer_player2 = 'y'
        counter_player1 = 0
        counter_player2 = 0
        stage += 1
        print('Stage', stage)
        print('-------')

        while answer_player1 == 'y' or answer_player2 == 'y' or counter_player1 <= 21 or counter_player2 <= 21:
            
            
            print()
            if counter_player1 == 21:
                 break
            elif counter_player1 < 21:
                print('Player 1')
                answer_player1 = input('Player 1, you need 1 card?(y/n): ')
                counter_player1 = give_card(card_deck, counter_player1)
            if counter_player2 == 21:
                break
            elif counter_player2 < 21:
                print('Player 2')
                answer_player2 = input('Player 2, you need 1 more card?(y/n): ')
                counter_player2 = give_card(card_deck, counter_player2)
            print('Player 1', counter_player1, 'points')
            print('Player 2', counter_player2, 'points')
            
            print()

        if counter_player1 == 21 and counter_player2 == 21:
            print('Draw.')
        elif counter_player1 > counter_player2 or counter_player2 > 21:
            print('Player 1 win.')
        elif counter_player1 < counter_player2 or counter_player1 > 21:
            print('Player 2 win.')
        

              
def give_card(card_deck, counter):
            card_player = random.choice(list(card_deck))
            value_card = card_deck[card_player]
            if card_player[0] == 'tuz':
                if counter + value_card[1] <= 21:
                    value_card = value_card[1]
                else:
                    value_card = value_card[0]
            counter += value_card
            print(card_player, '-', value_card, '=>', counter, 'points')
            return counter
            

def create_deck():
    card_deck = dict()
    for suit in suit_list:
        for key, val in deck.items():        
            card_deck[(key, suit)] = val
    return card_deck


if __name__ in '__main__':
    main()
