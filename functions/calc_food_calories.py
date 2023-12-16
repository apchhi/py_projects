# # Python
'''
Диетолог работает в спортивном клубе и дает рекомендации 
клиентам в отношении диеты. В рамках своих рекомендаций 
он запрашивает у клиентов количество граммов жиров и углеводов, 
которые они употребили за день. Затем на основе приведенной 
ниже формулы он вычисляет количество калорий, которые 
получаются в результате употребления жиров: 
калории от жиров = граммы жиров х 9. 
Затем на основе еще одной формулы он вычисляет 
количество калорий, которые получаются в результате 
употребления углеводов: 
калории от углеводов = граммы углеводов х 4. 
Диетолог просит вас написать программу, которая выполнит 
эти расчеты.
'''

def main():
  print('This program - calculator calories')
  fats, carbohydrates = request_food()
  fat_calories, carbohydrates_calories = calculator(fats, carbohydrates)
  print(f'Your fat calories - {fat_calories:,.2f} & carbohydrates calories - {carbohydrates_calories:,.2f} for day')
  
# send a request gram fats and carbohydrates
def request_food():
  fats = float(input('Enter amount of fat consumed per day(gram): '))
  carbohydrates = float(input('Enter amount of carbohydrates consumed per day(gram): '))
  return fats, carbohydrates
  
# calories counting
def calculator(fats, carbohydrates):
  fat_calories = fats * 9
  carbohydrates_calories = carbohydrates * 4
  return fat_calories, carbohydrates_calories
  
  
main()