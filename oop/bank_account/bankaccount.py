## класс BankAccount имитирует банковский счет
class BankAccount:

    ## Метод __init__ принимает аргумент с остатком на счете
    ## Он присваивается атрибуту __balance
    def __init__(self, bal):    ## bal - начальный остаток на счете
        self.__balance = bal

    ## Метод deposit вносит на счет вклад
    def deposit(self, amount):  ## amount - вносимая сумма
        self.__balance += amount

    ## Метод withdraw снимает сумму со счета
    def withdraw(self, amount): # amount - снимаемая с банковского счета сумма
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Ошибка: недостаточно средств')

    ## Метод get_balance возвращает остаток средств на счете
    def get_balance(self):
        return self.__balance

    ## Метод __str__ возвращает строковое значение  сообщает о состоянии объекта
    def __str__(self):
        return f'${self.__balance:,.2f}'
