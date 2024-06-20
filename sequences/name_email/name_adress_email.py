import pickle

def main():
    dict_users = dict()
    input_file = open('email_book.dat', 'rb')
    object_file = pickle.load(input_file)
    input_file.close()
    
    flag = 'y'
    while flag == 'y':
        menu(dict_users)
        flag = input('Do you want to continue?(y/n): ')
    print(dict_users)
        
def menu(users):
    print('MENU')
    print('-----------')
    print('1. Search to e-mail a user')
    print('2. Add a new user')
    print('3. Change existing e-mail')
    print('4. Delete extsting a user')
    print('5. Exit')
    print()
    answer_menu = int()
    while type(answer_menu) == int:
        try:
            answer_menu = int(input('Select a menu item: '))
            break
        except ValueError:
            print('Enter value type is not correct')
        
    if answer_menu == 1:
        search_user(users)
    elif answer_menu == 2:
        add_user(users)
    elif answer_menu == 3:
        change_email(users)
    elif answer_menu == 4:
        delete_user(users)

def search_user(users):
    name = ('Enter name user: ')
    #if name in users:
    email = users.get(name, 'not found')
    #else:
    #    print('User not found.')
    print(name, ':', email)

def add_user(users):
    name = input('Enter name a user: ')
    if name not in users:
        email = input('Enter email a user: ')
        users[name] = email
        print('Successfull')
    else:
        print('The user is already in the database')

def change_email(users):
    name = input('Enter a user name: ')
    if name in users:
        email = input('Enter new email: ')
        users[name] = email
        print('Successfull')
    else:
        print('User not found')

def delete_user(users):
    name = input('Enter a user name: ')
    if name in users:
        del users[name]
        print('Successfull')
    else:
        print('User not found')

if __name__ in '__main__':
    main()
