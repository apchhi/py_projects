## Эта программа управляет контактами

import contact
import pickle

## Глоальные константы для пунктов меню
LOOK_UP = 1 #искать
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

## Глобал константа для имени файла
FILENAME = 'constant.dat'

def main():
    ## Загрузить существующий словарь контактов 
    ## и присвоить его переменной
    mycontacts = load_contacts()
    ## Инициализировать переменную 
    ## для выбора пользователя
    choice = 0
    ## Обрабатывать вбранные пользоателем 
    ## пункты меню, пока он не захочет выйти
    while choice != QUIT:
        ## Получить выбранный пользователем пункт меню
        choice = get_menu_choice()
        ## Обработать выбранный авриант
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    ## Сохранить словарь в файле
    save_contacts(mycontacts)

def load_contacts():
    try:
        ## Открыть файл contact.dat
        input_file = open(FILENAME, 'rb')
        ## Расконсервировать словарь
        contact_dct = pickle.load(input_file)
        ## Закрыть файл
        input_file.close()
    except IOError:
        ## Не получилось открыть файл
        ## создаем пустой словарь
        contact_dct = dict()
    ## Вернуть словарь
    return contact_dct

## Ф-ция выводит меню и получает проверенный 
## на допустимость выбранный пользователем пункт меню
def get_menu_choice():
    print()
    print('Меню')
    print('---------------------------------')
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()
    ## Получить выбранный пользователем пунк меню 
    choice = int(input('Введите пунк меню: '))
    ## Проверить пункт меню на допустимость
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Повторите свой выбор: '))
    ## Вернуть выбранный пользователем пункт меню
    return choice

## Ф-ция отыскивает элемент в словаре
def look_up(mycontacts):
    ## Получить искомое имя
    name = input('Введите имя: ')
    ## Отыскать его в словаре
    print(mycontacts.get(name, 'Имя не найдено.'))

## Ф-ция добавляет новую запись в словарь
def add(mycontacts):
    name = input('Введите имя: ')
    phone = input('Ведите телефон: ')
    email = input('Введите e-mail: ')
    ## Создать именованную запись объекта Contact
    entry = contact.Contact(name, phone, email) 
    ## Если имя в слваре не существует,
    ## то добавить его в качестве ключа со связанным
    ## с ним значением в виде объекта
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена.')
    else:
        print('Имя уже существует.')

## Ф-ция изменяет существующую запись в словаре
def change(mycontacts):
    ## Получить искомое имя
    name = input('Введите имя: ')
    if name in mycontacts:
        ## Получить новый телефон и e-mail
        phone = input('Введите телефон: ')
        email = input('Введите e-mail: ')
        ## Создать именованную запись с объектом Contact
        entry = contact.Contact(name, phone, email)
        ## Обновить запись
        mycontacts[name] = entry
        print('Запись обновлена.')
    else:
        print('Это имя не найдено.')

## Ф-ция удаляет запись из словаря
def delete(mycontacts):
    ## Получить искомое имя
    name = input('Введите имя: ')
    ## Если имя есть, удалить его 
    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print('Запись не найдена.')
    
## Ф-ция консервирует указанный объект и
## сохраняет его в файле
def save_contacts(mycontacts):
    ## Открыть файл для запись
    output_file = open(FILENAME, 'wb')
    ## Законсервировать словарь и сохранить его
    pickle.dump(mycontacts, output_file)
    ## Закрыть файл
    output_file.close()

if __name__ == '__main__':
    main()
    
