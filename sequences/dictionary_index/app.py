## create to dictionary word from text file
import re
N_INFILE = 'Kenneby.txt'
N_OUTFILE = 'index.txt'

def main():
    lines_file = read_file_txt()
    dict_words = create_dict(lines_file)
    create_file_dict(dict_words)
        
def read_file_txt():
    infile = open(N_INFILE, 'r')
    lines_file = infile.readlines()
    infile.close()
    return lines_file

def create_dict(lines_file):
    dict_words = dict()
    for i, line in enumerate(lines_file, start=1):
        list_words = [word.lower() for word in re.findall(r'\w+', line)]        
        for word in list_words:
            if word in dict_words:
                dict_words[word].add(i)
            else:
                dict_words[word] = {i}  
    return dict_words

def create_file_dict(dict_words):
    outfile = open(N_OUTFILE, 'w')
    for key, set_values in dict_words.items():
        string = str(key) + ':'
        for value in set_values:
            string += ' ' + str(value)
        string += '\n'
        outfile.write(string)

if __name__ in '__main__':
    main()
