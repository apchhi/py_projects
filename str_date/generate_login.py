## creating login

def main():
    first_name, last_name, id_number = get_date()
    #print(first_name, last_name, id_number)
    login = create_login_name(first_name, last_name, id_number)
    print('Your login: ', login)

def get_date():
    print('Enter date a stydent')
    first_name = input('First name: ')
    last_name = input('Last name: ')
    while first_name.isdigit() or last_name.isdigit():
        print('Enter value name is not correct.')
        first_name = input('Repeat first name: ')
        last_name = input('Repeat last name: ')
    id_number = input('Input ID a stydent: ')
    while id_number.isdigit() is not True:
        print('Enter value ID is not correct.')
        id_number = input('Repeat ID: ')
    return first_name, last_name, id_number

def create_login_name(first, last, id_n):
    set1 = first[:3]
    set2 = last[:3]
    set3 = id_n[-3:]
    return set1 + set2 + set3

if __name__ == '__main__':
    main()
