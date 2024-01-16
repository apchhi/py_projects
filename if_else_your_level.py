## your level if-else
A_scope = 95
B_scope = 85
C_scope = 75
D_scope = 65

scope = int(input('Enter your is number: '))

if scope >= A_scope:
    print('Your level - A.')
else:
    if scope >= B_scope:
        print('Your level is - B.')
    else:
        if scope >= C_scope:
            print('Your level is - C.')
        else:
            if scope >= D_scope:
                print('Your level is - D.')
            else:
                print('Your level is - F.')
