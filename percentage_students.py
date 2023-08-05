## Percentage of female and male student 

print('This program finds is pecrentage of male and female students\n')

male = int(input('Enter the number of male persons: '))
female = int(input('Enter the number of female persons: '))

all_persons = male + female
# okruglenye - round
male_percent = int((male / all_persons) * 100)
female_percent = int((female / all_persons) * 100)

print(f'Percentage of male student = {male_percent}% from group')
print(f'Percentage of female student = {female_percent}% from group')



   
