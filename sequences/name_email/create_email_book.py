#create email_book 
import pickle
def main():
    dict_email = dict()
    flag = 'y'
    while flag == 'y':
        name = input('Enter name: ')
        email = input('Enter email: ')
        dict_email[name] = email
    print(dict_email)
    outfile = open('email_book.dat', 'wb')
    pickle.dump(dict_email, outfile)
    outfile.close()
    print('Successfully')

if __name__ in '__main':
    main()
