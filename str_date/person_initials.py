## person initials
def main():
    user_input = input('Enter full name a person(firstname, lastname, surname): ')
    user_list = user_input.split()
    firstname = user_list[0][0]
    lastname = user_list[1][0]
    surname = user_list[2][0]
    print(firstname + '.' + lastname + '.' + surname + '.')


main()
