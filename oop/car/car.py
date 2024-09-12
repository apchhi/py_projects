START_SPEED = 0
NEXT_SPEED = 5


class Car:
# Атрибуты данных
    def __init__(self, model, make):
        # Модель указанного года
        self.__year_model = model
        # Фирма - изготовитель
        self.__make = make
        # Текущая скорость авто
        self.__speed = START_SPEED
# Методы
    # Увеличить скорость
    def accelerate(self):
        self.__speed += NEXT_SPEED
    # Уменьшить скорость
    def breake(self):
        self.__speed -= NEXT_SPEED
    # Вернуть текущую скорость
    def get_speed(self):
        return self.__speed


