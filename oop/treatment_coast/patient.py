## Класс созает объекты для данных пациентов
class Patient:
    def __init__(self, first_name, last_name, patronymic,
                 city, region, postal_code,
                 phone_number_person,
                 contact_name, contact_phone_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
        #self.__address = address
        self.__city = city
        self.__rerion = region
        self.__postal_code = postal_code
        self.__phone_number_person = phone_number_person
        self.__contact_name = contact_name
        self.__contact_phone_number = contact_phone_number
    ## Мутаторы
    def set_name(self, first_name, last_name, patronymic):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__patronymic = patronymic
    def set_address(self, city, region, postal_code):
        #self.__address = address
        self.__city = city
        self.__rerion = region
        self.__postal_code = postal_code
    def set_phone_number_person(self, phone_number_person):
        self.__phone_number_person = phone_number_person
    def set_contact(self, contact_name, contact_phone_number):
        self.__contact_name = contact_name
        self.__contact_phone_number = contact_phone_number
    ## Получатели
    def get_name(self):
        return self.__first_name, self.__last_name, self.__patronymic
    def get_address(self):
        return self.__city, self.__rerion, self.__postal_code
    def get_phone_number_person(self):
        return self.__phone_number_person
    def get_contact(self):
        return self.__contact_name, self.__contact_phone_number
