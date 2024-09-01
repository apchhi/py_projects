## Программа создает 3 экземпляра класса о разных юзерах
from information import Information 

COUNT_PEOPLES = 3
def main():
    peoples = dict()
    for person in range(COUNT_PEOPLES):
        print()
        print(f'Enter the details of {person+1} person')
        name = input('name: ')
        address = input('address: ')
        age = input('age: ')
        phone_number = input('phone number: ')
        el_dict = Information(name, address, age, phone_number)
        peoples[name] = el_dict
        
    ## Проверка
    print()
    search_name = input('Enter search name: ')
    print(f'age: {peoples[search_name].get_age()} || ',
          f'address: {peoples[search_name].get_address()} || ',
          f'phone number: {peoples[search_name].get_phone_number()}')
    
if __name__ == '__main__':
    main()
