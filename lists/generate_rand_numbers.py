'''
Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную комбинацию лотерейных чисел. Программа должна сгенерировать семь случайных чисел, каждое в диапазоне от 0 до 9, и присвоить каждое число элементу списка. (Случайные числа рассматривались в главе 5.) 
Затем напишите еще один цикл, который показывает содержимое списка.
'''
import random

def main():
    AMOUNT_NUMBERS = 7
    RAND_START = 0
    RAND_END = 9
    game_list = []

    for num in range(AMOUNT_NUMBERS):
        game_list.append(random.randint(RAND_START,RAND_END))

    print([num for num in game_list])



main()
