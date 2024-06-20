# words frequency

def main():
    infile = open('words.txt', 'r')
    words = infile.read().split()
    infile.close()
    
    dict_count_words = dict()
    
    for word in words:
        if word in dict_count_words:
            dict_count_words[word] += 1
        else:
            dict_count_words[word] = 1

    for key, value in dict_count_words.items():
        print(f'Word {key} count: {value}')


if __name__ in '__main__':
    main()
