## roulette wheel colors

print('Roulette pocket color display program.')
# number pocket
num = int(input('Enter pocket number: '))
# color pocket
color = ''

#pockets 0 - 36
if num >= 0 and num <= 36:
    if num == 0:
        color = 'green'
    elif num >= 1 and num <= 10:
        if num % 2 != 0:
            color = 'red'
        elif num % 2 == 0:
            color = 'black'
    elif num >= 11 and num <= 18:
        if num % 2 != 0:
            color = 'black'
        elif num % 2 == 0:
            color = 'red'
    elif num >= 19 and num <= 28:
        if num % 2 != 0:
            color = 'red'
        elif num % 2 == 0:
            color = 'black'
    elif num >= 29 and num <= 36:
        if num % 2 != 0:
            color = 'red'
        elif num % 2 == 0:
            color = 'black'
elif num < 0 or num > 36:
    print('Error! The entered value is less than 0 or greater than 36.')
else:
    print('Error! Value is not number. Repeat.')

print(f'The color of the entered number {num} on the roulette wheel = {color}')




