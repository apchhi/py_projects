## conservation object
import pickle

def main():
    end_of_file = False
    input_file = open('info.dat', 'rb')
    while not end_of_file:
        try:
            person = pickle.load(input_file)
            #print(person)
            display_data(person)
        except EOFError:
            end_of_file = True
    input_file.close()

def display_data(person):
    print()
    print('Name: ',person['name'])
    print('Age: ', person['age'])
    print('Mass: ', person['mass'])

if __name__ in '__main__':
    main()

