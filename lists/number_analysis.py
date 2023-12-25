'''
Программа анализа чисел. Разработайте программу, которая просит 
пользователя ввести ряд из 20 чисел. Программа должна сохранить числа
в списке и затем показать при­ веденные ниже данные: 
• наименьшее число в списке; 
• наибольшее число в списке; 
• сумму чисел в списке; 
• среднее арифметическое значение чисел в списке.
'''
COUNT_NUMBERS = 4   # default 20
def main():
    numbers_list = create_numbers()
    #print(numbers_list)
    min_number, max_number, sum_numbers, average_number = calc_numbers(numbers_list)
    print('Number minimal = ',min_number, ', maximal = ', max_number, ', sum = ', sum_numbers, ', average = ', average_number)

def create_numbers():
    numbers = []
    print(f'Enter {COUNT_NUMBERS} random numbers: ')
    for count in range(COUNT_NUMBERS):
        number = float(input(f'{count+1} number: '))
        numbers.append(number)
    return numbers
    #print(numbers)

def calc_numbers(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    sum_num = sum(numbers)
    average_num = sum_num / len(numbers)
    return min_num, max_num, sum_num, average_num
    
main()
