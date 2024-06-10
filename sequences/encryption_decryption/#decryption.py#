#decryption of files
def main():
    codes =  {'a':'229', 'b':'234', 'c':'178', 'd':'123',
         'e':'789', 'f':'678', 'g':'543', 'h':'321',
         'i':'987', 'j':'567', 'k':'123', 'l':'789',
         'm':'654','n': '543', 'o': '321', 'p':'987',
         'q':'567', 'r':'123', 's':'789', 
         't':'654',  'u':'543',  'v':'321','w':'987',
         'x':'567', 'y':'891','z':'982', '0':'1723', 
         '1':'1456', '2':'1987', '3':'1145', '4':'1567', 
         '5':'1892', '6':'1234', '7':'1765', '8':'1345',
         '9':'1999', ' ':'444', '.':'443', ',':'442', '\n':'441',
        }	
    input_file = open('encrypt_text.txt', 'r')
    lines = input_file.readlines()
    input_file.close()
    list_word = lines[0].split(':')
    for code_word in list_word:
        for key, value in codes.items():
            if code_word == value:
                print(key, end='')
                
    print('Successfully.')
 
if __name__ in '__main__':
    main()
