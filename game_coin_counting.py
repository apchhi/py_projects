## coin counting game
print('Game of counting coins. Enter the number of coins and if the total amount is equal to 1 ruble, then you will win.')

# coins
five = int(input('Enter the number of coins 5 kopecks: '))
ten = int(input('Enter the number of coins 10 kopecks '))
fifty = int(input('Enter the number of coins 50 kopecks: '))

sum_kop = 5 * five + 10 * ten + 50 * fifty
sum_rub = sum_kop / 100

if sum_rub == 1:
    print('Congratulations. You won! Your amount of kopecks is equal to 1 ruble.')
else:
    print('You loose! Sum of kopecks is not equal to 1 ruble.')

