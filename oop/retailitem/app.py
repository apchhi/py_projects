##  Программа выводит данные по товарам на складе
from retailitem import RetailItem
product_data = {'Товар 1':['Пиджак', 12, 59.95], 'Товар 2':['Дизайнерские джинсы', 40, 34.95], 'Товар 3':['Рубашка', 20, 24.95]}


def main():
    product_objects = dict()
    for el in product_data:
        product_desc = product_data[el][0]
        quantity = product_data[el][1]
        price = product_data[el][2]
        product_objects[el] = RetailItem(product_desc, quantity, price)
    #print(product_objects)
    show_data(product_objects)

def show_data(objects):
    print('---------------------------------------------')
    print('******** / Описание / Количество / Цена')
    print('---------------------------------------------')
    for el in objects:
        print(f'{el} / {objects[el].get_product_desc()} / {objects[el].get_quantity()} / {objects[el].get_price()}')
        print('---------------------------------------------')
    #print(product_data['Товар 1'][2])

if __name__ == '__main__':
    main()
