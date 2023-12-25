'''
Проверка допустимости номера расходного счета.
Файл с номерами. Каждый номер счета представляет собой семизначное число, в частности 5658845. 
Напишите программу, которая считывает содержимое файла в список. 
Затем она должна попросить пользователя ввести номер расходного 
счета. 
Программа должна определить, что номер является допустимым, путем 
его поиска в списке. Если число в списке имеется, то программа 
должна вывести сообщение, указывающее на то, что номер допустимый. 
Если числа в списке нет, то программа должна вывести сообщение, 
указывающее на то, что номер недопустимый.
'''
# value 1450825
import math

def main():
    infile = open('numbers.txt', 'r')
    list_numbers = [int(number.rstrip('\n')) for number in infile]
    # 1450825
    get_number, flag = user_input_processing()
    if flag:
        if found_number(list_numbers, get_number):
            print('The number found in the database.')
        else:
            print('The number not found in the database.')
    
def user_input_processing():
    flag = True
    while True:
        try:
            get_number = input('Enter your a seven-diling number: ')
            get_number = int(get_number)
            len_number = math.floor(math.log10(get_number)) + 1
            if len_number != 7:
                raise ValueError
            break
        except ValueError:
            print('Error! Type value is not integer or not have seven-diling.')
    print('Enter value is correct.')    
    return get_number, flag   

def found_number(list_numbers, get_number):
    try:
        list_numbers.index(get_number)
        return True
    except ValueError:
        return False
    
main()
