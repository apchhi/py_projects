## Общий объем продаж

prices = []
all_sum = 0.0
tax_percent = 0.07

for i in range(5):
    price = float(input(f'Enter sale product {i+1}: '))
    prices.append(price)
    
for i in prices:
    all_sum += i
    
tax_money = all_sum * tax_percent
final_sum = all_sum - tax_money

print(f'All prices sum = {all_sum:.2f}$')
print(f'Tax money all price = {tax_money:.2f}$')
print(f'All final sum = {final_sum:.2f}$')








