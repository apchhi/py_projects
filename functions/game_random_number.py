# # Python
'''
Игра в угадывание случайного числа. Напишите программу, которая 
генерирует случайное число в диапазоне от 1 до 100 и просит 
пользователя угадать это число. Если догадка пользователя 
больше случайного числа, то программа должна вывести сообщение
"Слишком много, попробуйте еще раз". Если догадка меньше 
случайного числа, то программа должна вывести сообщение
"Слишком мало, попробуйте еще раз". Если пользователь число 
угадывает, то приложение должно поздравить пользователя и 
сгенерировать новое случайное число, чтобы возобновить игру.
'''
import random

def main():
  answer_agry= input('You have play in this game?(yes/no) ')
  while answer_agry.lower() == 'yes':
    number = generate_number()
    сomparison_answer(number)
    answer_agry = input('You have play in this game?(yes/no) ')
        #number = generate_number()
        
#def start_game():
#  number = generate_number()
#  answer_user = int(input('Enter any integer number from 1 to 100: '))

def сomparison_answer(number):
  answer_user = int(input('Enter any integer number from 1 to 100: '))
  while answer_user != number:
    if answer_user > number:
      answer_user = int(input('Very more, reload enter of number less:'))
    elif answer_user < number:
      answer_user = int(input('Very less, reload enter of number more:'))
  else:
    print('Congratulations! The number is equal to the answer.')
    
def generate_number():
  return random.randint(1,100)

main()