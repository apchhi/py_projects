## storing names and birthdays
DICT_BOUND = 2
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
def main():
    data_users = {}
    user_answer = 0
    print("Hello! This is peoples data program. Enter the data of the first person in database.")
    print('Create the first peoples in dictionary')
    for _ in range(DICT_BOUND):
        add(data_users, username())
    while user_answer != QUIT:
        user_answer = get_menu_choice(data_users)
    # show dictionary
    for key, value in data_users.items():
        print(key, ' - ', value)

def get_menu_choice(dict_users):
    print()
    print('---------------------------------')
    print('MAIN')
    print('-----')
    print('1. Find date of birth.')
    print('2. Add new person.')
    print('3. Change a person.')
    print('4. Remove person.')
    print('5. Exit for program.')
    print('---------------------------------')
    number_menu = int(input('What to do. Enter the menu item number: '))
    while number_menu < LOOK_UP or number_menu > QUIT:
        number_menu = int(input('Value is not correct. Enter the menu item number: '))
    if number_menu == LOOK_UP:
        look_up(dict_users, username())
    elif number_menu == ADD:
        add(dict_users, username())
    elif number_menu == CHANGE:
        change(dict_users, username())
    elif number_menu == DELETE:
        delete(dict_users, username())
    return number_menu

def username():
    return input('Enter user name: ')

def user_in_data(data, name):
    flag = True
    while flag:
        if name in data:
            print('Name is found.')
            flag = False
        else:
            name = input('Name not found. Try again.')
    return name

def look_up(data, name):
    value = data.get(name, 'not found.')
    print('Name:', name, ' - ', value)

def add(data, name): 
    if name is not data:
        user_date = input('Person date (in format - 01.01.1950): ')
        data[name] = user_date
        print('Entry added.')
    else:
        print('This entry already exists.')

def change(data, name):
    if name in data:
        user_date = input('Enter the person date (in format - 01.01.1950): ')
        data[name] = user_date
        print('Entry changed.')
    else:
        print('Name not found.')

def delete(data, name):
    if name in data: 
        del data[name]
        print('Entry deleted.')
    else:
        print('Name not found.')



if __name__ == 'main':
    main()
