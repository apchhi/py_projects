## person body mass index
print('The program calculates the body mass index of a person and shows the norm or deviation from the norm.\n')
#rost
height = float(input('Enter your height(meters.santimeter): '))
while height > 2.5 or height <= 0:
    height = float(input('Input valut is not correct. Enter your height(meters.santimeter): '))
#ves
mass = float(input('Enter your mass(kg): '))
while mass <= 0 or mass > 300:
    mass = float(input('Input value is not correct. Enter your mass(kg): '))

value_ip = ''

index_person = mass // pow(height, 2) 

if index_person < 18.5:
    value_ip =  'less than normal. Need to eat more'
elif index_person > 25:
    value_ip = 'more than normal. Need to exercise and eat less'
else:
    value_ip = 'normal'

print(f'Your body index mass = {index_person}. This is {value_ip}.')
