## days in february

print('This program calculates the days in the month of february, determining if it is a leap year or not leap year.\n')
year = int(input('Enter year (format YYYY): '))

if (year % 100 == 0) and (year % 400 == 0):
    print(f'Leap year of february {year} has 29 days')
elif (year % 100 != 0) and (year % 4 == 0):
    print(f'Leap year of february {year} has 29 days')
else:
    print(f'Not leap year of february {year} has 28 days')


