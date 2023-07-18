# вычисляет стоимость товара со скидкой

def discount (cost, percent):
    disc = cost * (percent / 100)
    remains = cost - disc
    return remains

cost = float(input('Enter cost: '))
percent = float(input('Enter discount percent: '))

print('You need pay per product ', discount(cost, percent), '$')
