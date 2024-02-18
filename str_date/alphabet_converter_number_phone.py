## converter a phone number like 555-GET-FOOD to 555-438-3663

DICT_LETTERS = {
            2: ('A','B','C'),
            3: ('D','E','F'),
            4: ('G','H','I'),
            5: ('J','K','L'),
            6: ('M','N','O'),
            7: ('P','Q','R','S'),
            8: ('T','U','V'),
            9: ('W','X','Y','Z')
            }


def main(list_letters):
    print('# 555-GET-FOOD')  
    tel_number = input('Please, enter phone number consisting of 10 characters of the form XXX-XXX-XXXX: ') 
    print(f'The new a number: {concatenation(list_letters, tel_number)}')


def concatenation(list_letters, tel_number):
    first_word = tel_number[:3]
    second_word = tel_number[4:]
    new_number = first_word + '-'

    for ch in second_word:
        if ch.isalpha():
            number = check_list(list_letters, ch)
            new_number += number
        else:
            new_number += '-'
    return new_number


def check_list(list_letters, ch):
    data_items = list_letters.items() 
    for key, value in data_items: 
        if ch in value:
            return str(key)


if __name__ == '__main__':
    main(DICT_LETTERS)
