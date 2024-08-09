## Программа расконсервирует объект CellPhone

import pickle
import cellphone

FILENAME = 'cellphone.dat'

def main():
    ## Переменная для управления циклом
    end_of_file = False
    
    ## Открыть файл
    input_file = open(FILENAME, 'rb')

    ## Получить данные от пользователя
    while not end_of_file:
        try:
            ## Расконсервировать объект 
            phone = pickle.load(input_file)
            
            ## Показать данные о сотовом телефоне
            display_data(phone)
        
        except EOFError:
            ## Установить флаг показывающий,
            ## что был достигнут конец файла
            end_of_file = True

    ## Закрыть файл
    input_file.close()

## Функция display_data показывает данные 
## из объекта CellPhone, преданного 
## в качестве аргумента
def display_data(phone):
    print(f'Производитель: {phone.get_manufact()}')
    print(f'Модель: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():,.2f}')
    print()

if __name__ == '__main__':
    main()
