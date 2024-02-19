NAME_FILE = 'text.txt'

def main():
    infile = open(NAME_FILE, 'r')
    list_file = infile.readlines()
    infile.close()
    count_words = 0
    index = 0

    while index < len(list_file):
        list_file[index] = list_file[index].rstrip('\n')
        index += 1

    for elem in list_file:
        line_list = elem.split()
        count_words += len(line_list)

    print(f'All words in file "{NAME_FILE}" = {count_words}')



main()
