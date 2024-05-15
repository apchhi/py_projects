## storing names and birthdays
DICT_BOUND = 2
def main():
    data_users = {}
    user_answer = 0
    print("Hello! This is peoples data program. Enter the data of the first person in database.")
    print('Create the first peoples in dictionary')
    for _ in range(DICT_BOUND):
        add(data_users, username())
    #user_name = check_correct_input(data_users)
    while user_answer != 5:
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
    if number_menu == 1:
        look_up(dict_users, username())
    elif number_menu == 2:
        add(dict_users, username())
    elif number_menu == 3:
        change(dict_users, username())
    elif number_menu == 4:
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
    user_date = input('Person date (in format - 01.01.1950): ')
    data[name] = user_date
    print('Entry added.')

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



#if __name__ == 'main':
main()
