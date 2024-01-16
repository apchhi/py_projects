## weight and mass

def weight_calc(mass):
    weight = mass * 9.8
    return weight

mass = float(input("Enter the mass of the object: "))

if weight_calc(mass) > 500:
    print('Object is too heavy')
elif weight_calc(mass) < 100:
    print('Object is too light')
else:
    print(f'Weight of the object = {weight_calc(mass)} N')
