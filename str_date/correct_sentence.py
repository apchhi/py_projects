## correct capitalize a sentence

def main():
    symbols_end_sent = ['.', '!', '?']
    sentence = input('Enter eny a few suggestions in lower case: ')
    # hello! my name is Joe. how are you name?
    # hello!
    # my name is joe.
    # how are you name?
    new_sentence = correct(sentence, symbols_end_sent)
    print(new_sentence)


def correct(sentence, symbol_end):
    new_value = ''
    for char in sentence:
        for symbol in symbol_end:
            if char == symbol:
                index_ch = sentence.index(char)
                new_value += sentence[:index_ch+1].capitalize() + ' '
                sentence = sentence[index_ch+2:]
                #list_words = sentence.split(symbol)
    return new_value





main()
