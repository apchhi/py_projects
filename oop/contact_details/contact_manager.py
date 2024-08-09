## Эта программа управляет контактами

import contact
import pickle

## Глоальные константы для пунктов меню
LOOK_UP = 1
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
        ## Получить ыбранный пользователем пункт меню
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
    pass

def get_menu_choice():
    pass

def look_up(mycontacts):
    pass

def add(mycontacts):
    pass

def change(mycontacts):
    pass

def delete(mycontacts):
    pass

def save_contacts(mycontacts):
    pass
    
