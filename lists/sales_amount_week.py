'''
Общий объем продаж. Разработайте программу, которая просит пользователя ввести продажи магазина за каждый день недели. Суммы должны быть сохранены в списке. Примените цикл, чтобы вычислить общий объем продаж за неделю и показать результат.
'''
def main():
    DAYS = 7    # WEEK
    sales = []
    total = 0
    print('Enter sales amount for ... ')
    for day in range(DAYS):
        sale = float(input(f'{day+1} day: '))
        total += sale
        sales.append(sale)
    print(f'All sales in week = {total:,.2f}$')


main()
