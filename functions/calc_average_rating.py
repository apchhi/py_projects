# # Python
'''
Средний балл и его уровень. Напишите программу, которая 
просит пользователя ввсти пять экзаменационных оценок (баллов). 
Программа должна показать буквенный уровень для каждой оценки 
и средний балл. Предусмотрите в программе функции:
- calc average —  функция должна принимать в качестве 
аргументов пять балльных оценок и возвращать средний балл; 
- determine grade —  функция должна принимать в качестве 
аргумента балльную оценку и возвращать буквенный уровень 
оценки, опираясь на приведенную в табл:
90 и выше А 
80-89 В 
70-79 С 
60-69 D 
Ниже 60 F
'''

def main():
  list_rating = []
  print('Table character rating:\n', 
    'A: 90 and more', 
    'B: 80-89\n', 
    'C: 70-79\n',
    'D: 60-69\n',
    'F: less 60\n')
  print('Enter five rating to calculate your average score')
  for count in range(5):
    list_rating.append(int(input(f'{count+1} rating: ')))
  number_rating = calc_average(sum(list_rating))
  character_rating = determine_grade(number_rating)
  print(f'Your average rating = {number_rating:.1f} - {character_rating}')

def calc_average(summ_rating):
  return (summ_rating / 5) * (100 / 5)
    
def determine_grade(number):
  if number >= 90:
    return 'A'
  elif number >= 80 and number <= 89:
    return 'B'
  elif number >= 70 and number <= 79:
    return 'C'
  elif number >= 60 and number <= 69:
    return 'D'
  elif number < 60:
    return 'F'
    
main()