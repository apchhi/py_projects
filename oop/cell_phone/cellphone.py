## класс CellPhone содержит данные о сотовом телефоне

class CellPhone:
    ## метод __init__ инициализирует атрибуты
    def __init__(self, manufact, model, price) -> None:
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    ## метод set_manufact принимает аргумент для произвозителя телефона
    def set_manufact(self, manufact):
        self.__manufact = manufact

    ## метод set_model принимает аргумент для произвозителя телефона
    def set_model(self, model):
        self.__model = model

    ## метод set_retail_price принимает аргумент для цены телефона
    def set_retail_price(self, price):
        self.__retail_price = price
    
    ## методы возврата ...
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

