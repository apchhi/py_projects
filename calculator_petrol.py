## Расход бензина на пройденный путь

print('\nHello! You need to enter of value for search all expenditure\n')
track = float(input('Enter all distance(km): \n'))
liter = float(input('Enter consumption of beznin in liters per 100 km: \n'))

liter_km = liter / 100.0

consumption = track * liter_km

print(f'Full consumption of beznin = {consumption:.1f} liters')



