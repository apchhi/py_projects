## программа теста класса CellPhone

import cellphone

def main():
    ## получить данные телефона
    man = input('Введите производителя: ')
    mod = input('Введите модель: ')
    retail = float(input('Введите розничную цену: '))

    phone = cellphone.CellPhone(man, mod, retail)

    print(f'Производитель: {phone.get_manufact()}')
    print(f'Модель: {phone.get_model()}')
    print(f'Цена: ${phone.get_retail_price():,.2f}')

if __name__ == '__main__':
    main()
    
