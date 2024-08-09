## Программа консервирует объект CellPhone
import pickle
import cellphone

FILENAME = 'cellphone.dat'

def main():
    ## Переменная для управления циклом
    again = 'y'
    
    ## Открыть файл
    output_file = open(FILENAME, 'wb')

    ## Получить данные от пользователя
    while again.lower() == 'y':
        ## Получить данные о сотовом телефоне
        man = input('Введите производителя: ')
        mod = input('Введите модель: ')
        retail = float(input('Введите розничную стоимость: '))
        ## Создать объект CellPhone
        phone = cellphone.CellPhone(man, mod, retail)

        ## Законсервировать объект и записать его 
        pickle.dump(phone, output_file)

        ## Получить еще один элемент данных
        again = input('Записать еще один элемент данных? (y/n): ')

    ## Закрыть файл
    output_file.close()

    print('Данные записаны в файл', FILENAME)

if __name__ == '__main__':
    main()
