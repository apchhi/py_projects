##  magic date

def magic(day, month):
    procreation = day * month
    return procreation


print('This progam print the magic date (day * month = year)')
day = int(input('Enter day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: 19'))


if magic(day, month) == year:
    print(f'The entered date and month are magic - {day}.{month}.19{year}')
else:
    print('No! Reload!')
