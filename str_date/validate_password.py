
def main():
    password = input('Enter your password: ')
    while not valid_password(password):
        password = input('Enter password is not correct. Return enter the password: ')
    print(f'Password {password} is correct. Thenx!')

def valid_password(password):
    #is_valid = False
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) >= 7:
        correct_length = True
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True

    if correct_length and has_uppercase and \
            has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    
    return is_valid


if __name__ == '__main__':
    main()
