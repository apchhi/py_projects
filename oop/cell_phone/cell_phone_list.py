## Программа теста класса CellPhone

import cellphone

def main():
    ## Получить список объеков CellPhone
    phones = make_list()
    print('Вот веденные вами данные: ')
    display_list(phones)

## Ф-ция make_list получает от пользователя данные 
## о пяти телефонах, а затем возвращает список 
## объектов CellPhone, содержащих эти данные
def make_list():
    phone_list = list()
    ## Добавить пять объектов CellPhone в список
    print('Введите данные о пяти телефонах.')
    for count in range(1, 6):
        
        ## Получить данные телефона
        print(f'Телефон №{str(count)}.')
        man = input('Введите производителя: ')
        mod = input('Введите модель: ')
        retail = float(input('Введите розничную цену: '))
        print()

        ## Создать новый объект 
        ## и присвоить его переменной phone
        phone = cellphone.CellPhone(man, mod, retail)
        
        ## Добавить объект в список
        phone_list.append(phone)
        
    return phone_list

## Ф-ция display_list принимает список с объектами 
## CellPhone в качестве аргумента и показывает
## хранящиеся в каждом объекте данные
def display_list(phone_list):
    for item in phone_list:
        print('Телефон №', int(phone_list.index(item))+1)
        print(f'Производитель: {item.get_manufact()}')
        print(f'Модель: {item.get_model()}')
        print(f'Цена: ${item.get_retail_price():,.2f}')
        print()


if __name__ == '__main__':
    main()
    
