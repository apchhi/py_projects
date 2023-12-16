# # Python
'''
Счетчик четных/нечетных чисел. В этой главе вы увидели пример 
написания алгоритма, который определяет четность или 
нечетность числа. Напишите программу, которая генерирует 100 
случайных чисел и подсчитывает количество четных и нечетных 
случайных чисел.
'''
import random

def main():
  numbers_list = generate_numbers()
  event_count, odd_count = is_even(numbers_list)
  print(numbers_list)
  print('Event numbers: ', event_count)
  print('Odd numbers: ', odd_count)
  
def generate_numbers():
  numbers_list = []
  for i in range(100):
    numbers_list.append(random.randint(1,1000))
  return numbers_list

def is_even(numbers_list):
  event_count = 0
  odd_count = 0
  for value in numbers_list:
    if value % 2 == 0:
      event_count += 1
    elif value % 2 != 0:
      odd_count += 1
  return event_count, odd_count

main()