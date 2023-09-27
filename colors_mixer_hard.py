## colors mixer

# base color
my_list = ['red', 'green', 'blue']

# В словаре пара кей-велью кортежа
color_mapping = {
    ('red', 'blue'): 'New color - violet',
    ('red', 'yellow'): 'New color - orange',
    ('blue', 'yellow'): 'New color - green',
        }

# функция в которой ищем и сопоставляем эл-ты 
def mix_color(color1, color2):
    if color1 in my_list and color2 in my_list: # ищем эл-ты в my-list
        for colors, result in color_mapping.items():   # перебираем эл-то кортежа из color_mapping 
            if color1 in colors and color2 in colors:   # сравниваем их и введенные пользователем значения
                return result   # выводм значение того или иного ключа с парой элементов
        return 'Input value is not correct! Repeat.'    # если нет подходящих - ошибка


print('This program is a color mixer. It makes a new color.')
print('Enter "red" or "green" or "blue".')

color1 = str(input('Enter first color: '))
color2 = str(input('Enter second color: '))

print(mix_color(color1, color2))


