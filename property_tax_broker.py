# # property tax
# property value
TAX_FACTOR = 0.0065   #coef
all_tax = 0

# enter lot value
print('Enter lot number or 0 to complete.')
lot = int(input('Enter lot: '))

while lot != 0:
  #get value property
  property_value = float(input('Enter property value: '))
  #calculate tax property
  property_tax = property_value * TAX_FACTOR
  all_tax += property_tax
  print(f'Troperty tax = ${property_tax:.2f}')
  
  # enter next lot value
  print('Enter lot number or 0 to complete.')
  lot = int(input('Enter lot: '))
  
print(f'Your all tax = ${all_tax}')

