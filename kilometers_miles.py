# # kilometers per hour to miles per hour

START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSION_FACTOR = 0.6214

print('Kilometers\t\tMiles')
print('-----------------------------')

for kph in range(START_SPEED, END_SPEED, INCREMENT):
  mph = int(kph * 0.6214)
  print(f'{kph}km\t\t{mph:}ml')
  