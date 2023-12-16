# # Python
'''
Напишите программу, которая позволяет проводить простые
математические тесты. Она должна показать два случайных числа, 
которые должны быть просуммированы вот так: 
247 
+ 129 
Эта программа должна давать обучаемому возможность вводить 
ответ. Если ответ правильный, то должно быть показано 
поздравительное сообщение. Если ответ неправильный, то должно 
быть показано сообщение с правильным ответом.
'''
import random

def main():
  num_1 = generate_num()
  num_2 =generate_num()
  print(' ', num_1)
  print('+', num_2)
  answer_user = int(input('Enter the result of the expression: '))  
  answer_comparison(num_1, num_2, answer_user)

def generate_num():
  return random.randrange(1000)

def answer_comparison(num_1, num_2, answer):
  if answer == num_1 + num_2:
    print(f'Your answer {answer} is true')
  else:
    print(f'Your answer {answer} is false')

main()