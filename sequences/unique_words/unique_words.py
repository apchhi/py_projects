# unique words

def main():
    infile = open('words.txt', 'r')
    lines_words = infile.readline()
    infile.close()
    list_words = lines_words.split()
    unique_words = set(list_words)
    print(unique_words)
    
if __name__ in '__main__':
    main()
