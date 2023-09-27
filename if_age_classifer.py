## age classifier

print('This program output age class a people.')
age = float(input('Enter is age a people (age.months = 0.0): ')) 

if age >= 0 and age <= 1:
    print('~ Person - baby.')
elif age > 1 and age < 13:
    print('~ Person - child.')
elif age >= 13 and age <= 20:
    print('~ Person - teenager.')
elif age > 20:
    print('~ Person - adult.')
else:
    print('Error. Age value is not correct. Try entering again.')








