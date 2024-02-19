## more a symbol

def main():
    string = input('Enter any a text: ').lower()
    comparison(string) 

def comparison(string):
    ch_more = ''
    count_prew = 0
    count_next = 0
    for i in string:
        for y in string:
            if i == y:
                count_next += 1
        if count_next > count_prew:
            ch_more = i
        count_prew = count_next
        count_next = 0
    print(ch_more)


main()
