## Quadrangular prism

import turtle

def create_dict():
    """
    Создает пустой словарь с ключами для координат углов квадрата.
    """
    return {
        "one_square": {"x": [], "y": []},
        "two_square": {"x": [], "y": []}
    }

def draw_square(sq_name, x, y, size):
    """
    Рисует квадрат с координатами (x, y) и размером size, и добавляет значения x и y в словарь sq_name.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(4):
        t.left(90)
        t.forward(size)
        value_x, value_y = t.pos()
        my_dict[sq_name]["x"].append(value_x)
        my_dict[sq_name]["y"].append(value_y)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(400, 500)

    t = turtle.Turtle()
    #t.hideturtle()

    my_dict = create_dict()

    for sq_name in my_dict:
        draw_square(sq_name, 0 if sq_name == "one_square" else 100, 0 if sq_name == "one_square" else -100, 100)

    # Рисуем линии между противоположными углами квадратов
    t.penup()

    for x1, y1, x2, y2 in zip(my_dict["one_square"]["x"], my_dict["one_square"]["y"], my_dict["two_square"]["x"], my_dict["two_square"]["y"]):
        t.goto(x1, y1)    	
        t.pendown()
        t.goto(x2, y2)
        t.penup()

turtle.done()





