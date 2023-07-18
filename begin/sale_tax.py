## Налог с продаж
"""
Plan:
- запросить пользователя ввести величину покупки
- вычислить федератьный и региональный налоги с продаж
- показать:
    =показать сумму покупки
    =федеральный налог с продаж
    =региональный налог с продаж
    =общий налог с продаж
    =общую сумму продажи(сумма покупки + общий налог с продаж)
"""

purchase_list = []

## Tax
FEDERAL_TAX_PERCENT = 0.05
REGION_TAX_PERCENT = 0.025

sum_amoutn = 0

print('\nYou need enter a purchase amounts or "stop" for stop input and output result.\n')

while True:
    user_input = input('Enter your value: ')
    
    if user_input.lower() == 'stop':
        break
    
    try:
        purchase_list.append(float(user_input))
    except ValueError:
        print('The entered value is not correct. Try again:.')
    
       


#print(purchase_list)

for num in purchase_list:
    sum_amoutn += num


federal_tax_money = sum_amoutn * FEDERAL_TAX_PERCENT
region_tax_money = sum_amoutn * REGION_TAX_PERCENT
general_tax = federal_tax_money + region_tax_money
sum_sale = sum_amoutn - general_tax

print('\nCalculated date:\n')
print(f'All sum purchase amount = {sum_amoutn:,.2f}$')
print(f'Federal tax in amount = {federal_tax_money:,.2f}$')
print(f'Region tax in amount = {region_tax_money:,.2f}$')
print(f'General tax in amount = {general_tax:,.2f}$')
print(f'Sum sale minus tax = {sum_sale:,.2f}$')




