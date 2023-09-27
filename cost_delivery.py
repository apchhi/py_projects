## cost of delivery

print('The program calculates the cost of delivery depending on the weight of the cargo.\n')
weight = float(input('Enter the weight of the cargo (kg): '))

sale = 0

if weight > 0 and weight <= 200:
    sale = 150
elif weight > 200 and weight <= 600:
    sale = 300
elif weight > 600 and weight <= 1000:
    sale = 400
elif weight > 1000:
    sale = 475

print(f'Shiping cost = {sale}$')



