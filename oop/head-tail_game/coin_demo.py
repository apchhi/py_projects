import random

## класс Coin имитирует монету, которую можно подбрасывать
class Coin:

    ## метод __init__ инициализирует атрибут данных sideup значением "Орел"
    ## атрибут __sideup делается приватным. Его нельзя изменить из вне
    def __init__(self):
        self.__sideup = 'Орел'

    ## метод toss генерирует случайное число от 0 до 1
    ## если случайное число == 0, то sideup = 'Орел', иначе sideup == 'Решка'
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    ## метод get_sideup возвращает значение, на которое ссылается sideup
    def get_sideup(self):
        return self.__sideup


