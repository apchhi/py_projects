## print date

def main():
    months_list = ['January','February','March','April','May','June','July','August','September','October','November','December']  
    day, month, year = get_date()
    while day > 31 or day <= 0 or month <= 0 or month > 12 or year <= 0:
        print('Enter date is not correct.')
        day, month, year = get_date()
    print(f'{day} {months_list[month-1]} {year}')


def get_date():
    #user_input = input('Enter a date in format DD/MM/YYYY : ')
    input_list = input('Enter a date in format DD/MM/YYYY : ').split('/')
    return int(input_list[0]), int(input_list[1]), int(input_list[2])



main()
