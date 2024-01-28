def main():
    print('Enter an integer number greater than 1: ', end='')
    number = check_correct_number()
    list_integer_numbers = created_list_numbers(number)
    # go through the list and show natural prime numbers
    print(f'Natural prime numbers up to {number}: ')
    for element_list in list_integer_numbers:
        generator(element_list)

def generator(element_list):
    for i in range(2, element_list):
        if (element_list % i) == 0:
            break 
    else:
        print(element_list)

def check_correct_number():
    while True:
        number = input()
        try:
            number = int(number)
            if number <= 1:
                raise ValueError
            print('Thanx! Enter a number is correct.')
            break
        except ValueError:
            print('Enter value is not correct. Repeat your input.')
    return number

def created_list_numbers(number):
    list_numbers = []
    for index in range(2, number + 1):
        list_numbers.append(index)
    return list_numbers

main()
