import pickle

def main():
    #deconservation
    input_file = open('email_book.dat', 'rb')
    dict_users = pickle.load(input_file)
    input_file.close()

    flag = 'y'
    while flag == 'y':
        menu(dict_users)
        flag = input('Do you want to continue?(y/n): ')
<<<<<<< HEAD
    print('Bye!')
    
    print(dict_users)
=======

    #conservation
    output_file = open('email_book.dat', 'wb')
    pickle.dump(dict_users, output_file)
    output_file.close()
    print('Successfully')
>>>>>>> 7a28ba943a40099161179de1bb6522aad0b4fc0d
        
def menu(users):
    print('MENU')
    print('-----------')
    print('1. Search to e-mail a user')
    print('2. Add a new user')
    print('3. Change existing e-mail')
    print('4. Delete extsting a user')
<<<<<<< HEAD
    #print('5. Exit')
=======
    print('5. Show all users name and their e-mails.')
    #print('6. Exit')
>>>>>>> 7a28ba943a40099161179de1bb6522aad0b4fc0d
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
    elif answer_menu == 5:
        show_users(users)

def search_user(users):
<<<<<<< HEAD
    name = input('Enter name user: ')
    #if name in users:
=======
    name = input('Enter name user: ')
>>>>>>> 7a28ba943a40099161179de1bb6522aad0b4fc0d
    email = users.get(name, 'not found')
<<<<<<< HEAD
    #else:
    #    print('User not found.')
    print(name, email)
=======
    print(name, ':', email)
>>>>>>> 7a28ba943a40099161179de1bb6522aad0b4fc0d

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

def show_users(users):
    for key, value in users.items():
        print(f'User: "{key}", e-mail: "{value}"')


if __name__ in '__main__':
    main()
