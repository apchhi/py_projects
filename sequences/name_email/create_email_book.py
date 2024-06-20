#create email_book 
import pickle
def main():
    dict_email = dict()
    flag = 'y'
    while flag == 'y':
        name = input('Enter user name: ')
        email = input('Enter user email: ')
        dict_email[name] = email
        flag = input('Do you wang to continue(y/n): ')
    outfile = open('email_book.dat', 'wb')
    pickle.dump(dict_email, outfile)
    outfile.close()
    print(dict_email)
    print('Successfully')

if __name__ in '__main__':
    main()
