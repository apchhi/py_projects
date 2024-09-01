## Класс содержит данные о работнике

class Employee:
    def __init__(self, name, ident_num, department, position):
        self.__name = name
        self.__ident_num = ident_num
        self.__department = department
        self.__position = position
## Мутаторы
    def set_name(self, name):
        self.__name = name
    def set_ident_name(self, ident_num):
        self.__ident_num = ident_num
    def set_department(self, department):
        self.__department = department
    def set_position(self, position):
        self.__position
## Получатели
    def get_name(self):
        return self.__name
    def get_ident_num(self):
        return self.__ident_num
    def get_department(self):
        return self.__department
    def get_position(self):
        return self.__position
