## Класс создает объекты данных о товаре
class RetailItem:
    def __init__(self, product_desc, quantity, price):
        self.__product_desc = product_desc
        self.__quantity = quantity
        self.__price = price

    ## Методы мутаторы
    def set_product_desc(self, product_desc):
        self.__product_desc = product_desc
    def set_quantity(self, quantity):
        self.__quantity = quantity
    def set_price(self, price):
        self.__price = price

    ## Методы получатели
    def get_product_desc(self):
        return self.__product_desc
    def get_quantity(self):
        return self.__quantity
    def get_price(self):
        return self.__price
    
