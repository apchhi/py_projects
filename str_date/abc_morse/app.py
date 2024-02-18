## ABC Morse 

def main():
    infile = open('alphabet.txt', 'r')
    list_alphabet = infile.readlines()
    infile.close()
    #print(list_alphabet)
    delimiter = '|'
    dict_alphabet = created_dict_alphabet(list_alphabet, delimiter)
    #print(dict_alphabet)
    
    string = ''
    print('The program converts your text into Morse code. Use only symbols A-B, А-Б, 0-9')
    user_answer = input('Enter text: ').upper()
    for ch in user_answer:
        string += dict_alphabet.get(ch) + ' '
    print(string)

    #for ch in dict_alphabet:
    #    #print(f'>>>{ch}<<<')
    #    if ' ' == ch:
    #        print(True)
        #print(dict_alphabet[ch])

def created_dict_alphabet(list_alphabet, delimiter):
    dict_alphabet = {}
    for line in list_alphabet:
        line = line.rstrip('\n')
        #list_alphabet[index] = list_alphabet[index].rstrip('\n')
        #print(line)
        data = [x for x in line.split(delimiter)] 
        #print(data) 
        dict_alphabet[data[0]] = data[1]
        #print(dict_alphabet)
    #print(dict_alphabet)
    return dict_alphabet
    
    


        #print(data)
        #if data[0] == ' ':
        #    print('1', True)
        #elif data[1] == ' ':
        #    print('2', True)
        #else:
        #    print(False)
    #for line in list_alphabet:
    #    #line = line.rstrip('\n')
    #    tokens = line.split('|')
    #    print(tokens)

main()
