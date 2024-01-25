def main():
    FILE_WOMAN_NAMES = 'GirlNames.txt'
    FILE_MEN_NAMES = 'BoyNames.txt'
    name_sex = ''
    sex = input('Enter of sex person("m" if man or "g" if woman) : ')
    while sex != 'm' and sex != 'g':
        sex = input('Your enter value is not correct. Enter sex person: ')
    #print(sex)
    if sex == 'm':
        name_sex = FILE_MEN_NAMES
    elif sex == 'g':
        name_sex = FILE_WOMAN_NAMES
    #print(name_sex)
    name_list = read_file(name_sex)
    #print(name_list)
    print('Enter full a name person(Антонов Родион Абрамович) for found it ')
    name_search = input(': ')
    if search_name(name_search, name_list):
        print(f'"{name_search}" found in database.')
    else:
        print(f'"{name_search}" not found in database.')

def read_file(sex):
    infile = open(sex, 'r')
    names = infile.readlines()
    infile.close()
    index = 0
    while index < len(names):
        names[index] = names[index].rstrip('\n')
        index += 1
    return names

def search_name(name_search, name_list):
    try:
        name_list.index(name_search)
        return True
    except ValueError:
        return False


main()



