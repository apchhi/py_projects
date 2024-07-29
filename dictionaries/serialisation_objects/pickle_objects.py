## conservation object
import pickle

def main():
    again = 'y'
    output_file = open('info.dat', 'wb')
    while again.lower() == 'y':
        save_data(output_file)
        again = input('Would you like more data? (y/n): ')

def save_data(file):
    person = {}
    print('Enter data a person')
    person['name'] = input('name: ')
    person['age'] = int(input('age: '))
    person['mass'] = float(input('mass: '))
    pickle.dump(person, file)

if __name__ in '__main__':
    main()

