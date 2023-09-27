## day of the week
print('This prog output is day of the week')
day = int(input('Enter number(1-7) of the week: '))

try:
    if day == 1:
        print('Monday')
    elif day == 2:
        print('Truesday')
    elif day == 3:
        print('Wednesday')
    elif day == 4:
        print('Thursday')
    elif day == 5:
        print('Friday')
    elif day == 6:
        print('Saturday')
    elif day == 7:
        print('Sunday')
    else:
        print('~ An error! You entered invalid value!\n' +
              'You need to enter a value from 1 - 7')
except Exception as e:
    print(f'An error has occured: {e}')
    












