## Класс представляет пройденную пациентом процедуру
class Procedure:
    def __init__(self, procedure_name, date, doctor_name, procedure_cost):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__doctor_name = doctor_name
        self.__procedure_cost = procedure_cost

        ## Мутаторы
        def set_procedure_name(self, procedure_name):
            self.__procedure_name = procedure_name
        def set_date(self, date):
            self.__date = date
        def set_doctor_name(self, doctor_name):
            self.__doctor_name = doctor_name
        def set_procedure_cost(self, procedure_cost):
            self.__procedure_cost = procedure_cost

        ## Получатели
        def get_procedure_name(self):
            return self.__procedure_name
        def get_date(self):
            return self.__date
        def get_doctor_name(self):
            return self.__doctor_name
        def get_procedure_cost(self):
            return self.__procedure_cost
