# # Python
'''
Простые числа. Простое число —  это число, которое делится 
без остатка на само себя и 1. Например, число 5 является 
простым, потому что оно делится без остатка только на 1 и 5. 
Однако число 6 не является простым, потому что оно делится без 
остатка на 1, 2, 3 и 6. Напишите булеву функцию is prime, 
которая в качестве аргумента принимает целое число и возвращает 
истину, если аргумент является простым числом, либо ложь в 
противном случае. Примените функцию в программе, которая 
предлагает пользователю ввести число и затем выводит 
сообщение с указанием, является ли это число простым.
'''
def main():
  number = int(input('Enter number: '))
  ansver_program = is_even(number)
  print_ansver_program(ansver_program)
  
def is_even(number):
  ansver_program = None
  for i in range(2, number):
    if number % i == 0:
      #print('This number odd')
      ansver_program = True
      break
    else:
      ansver_program = False
  return ansver_program

def print_ansver_program(ansver_program):
  if ansver_program == False:
    print('This number: prime')
  else:
    print('This number: not prime')

main()