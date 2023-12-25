'''
Больше числа п. В программе напишите функцию, которая принимает два 
аргумента: список и число п. Допустим, что список содержит числа. 
Функция должна показать все числа в списке, которые больше п.
'''
import math
def main():
    list_number = [465,4674,1,4,2,3,7,1656,777,0]
    number_pi= math.pi
    more_pi(list_number,number_pi)

def more_pi(numbers,pi):
    list_more=[number for number in numbers if number > pi]
    print(list_more)
    
main()
