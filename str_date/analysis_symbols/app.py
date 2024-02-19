NAME_FILE = 'text.txt'

def main():
    infile = open(NAME_FILE, 'r')
    list_file = infile.readlines()
    infile.close()
    upper_case_count = 0
    lower_case_count = 0
    number_count = 0
    space_count = 0
    index = 0

    while index < len(list_file):
        list_file[index] = list_file[index].rstrip('\n')
        index += 1

    for elem in list_file:
        for ch in elem:
            if ch.isupper():
                upper_case_count += 1
            if ch.islower():
                lower_case_count += 1
            if ch.isdigit():
                number_count += 1
            if ch.isspace():
                space_count += 1

    print(f'"{NAME_FILE}" file contains: \n{upper_case_count} - upper case \n{lower_case_count} - lower case \n{number_count} - number symbols \n{space_count} - space, new line & tabulation symbols')



main()
