import random
def deal_cards(deck, number):
    hand_value = 0
    if number > len(deck):
        number = len(deck)
    for count in range(number):
        card = random.choice(list(deck))
        print(card)
        hand_value += deck[card]
    return hand_value
