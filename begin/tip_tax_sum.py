## Чаевые, налог и общая сумма

"""
-> Вычисляет общую стоимость блюд
- Попросить юзера ввести стоимость еды
- Вычислить размер 18% чаевых
- Вычислить 7% налога с продаж
- Показать все стоимости
- Показать итоговую сумму
"""

coast_list = []
tip = 0
tax = 0

print('\nProgram for calculating the cost, tip and taxes.\n')
print('Enter value the coast dash or "stop" for counting.')

while True:
    num = input('Enter value: ')
    if num == 'stop':
        break
    # check on Error
    try:
        num_list = float(num)
        coast_list.append(num_list) # To add a value in list
    except ValueError as e:
        print(f'Error: {e}. Enter num value or word "stop" for counting')

sum_coast = sum(coast_list)
tip = sum_coast / 100 * 18
tax = sum_coast / 100 * 7
total_sum = sum_coast - tax + tip

#print('List value', coast_list)
print('\nTotal:')
print(f'Sum coast = {sum_coast:.2f}$')
print(f'Tip = {tip:.2f}$')
print(f'Tax = {tax:.2f}$')
print(f'Total sum (profit with tip and tax) = {total_sum:.2f}$')
