## words separator

string = 'SLEPT ALMOST ALL NIGHT'

def main(string):
    end_word = 'KI'
    list_string = string.split()
    for index in range(len(list_string)):
        #new_string[index]
        print(list_string[index][0])
        new_word = list_string[index][1:] + list_string[index][0] + end_word
        list_string[index] = new_word
    print(list_string)




main(string)
