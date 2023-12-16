# # Python
'''
Список простых чисел. Это упражнение предполагает, что вы уже 
написали функцию is prime в упражнении 17. Напишите еще одну 
программу, которая показывает все простые числа от 1 до 100. 
В программе должен быть цикл, который вызывает 
функцию is_prime.
'''

def main():
  for count in range(1, 100+1):
    if is_prime(count):
      print(count)

def is_prime(number):
  if number < 2:
    return False
  # checking to the square edge of a number
  for i in range(2, int(number**0.5)+1):
    if number % i == 0:
      return False
      break
    return True

main()