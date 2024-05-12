## Game "Black Jack"
#import random
from create import create_deck
from deal import deal_cards

def main():
    deck = create_deck()
    num_cards = int(input('Enter the quantity of cards: '))
    points = deal_cards(deck, num_cards)
    print('Your points:', points)
    
if __name__ == "__main__":
    main()
