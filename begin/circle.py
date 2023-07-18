import turtle

screen = turtle.Screen()
screen.setup(400, 600)

t = turtle.Turtle()
radius = turtle.numinput('Введите значение', 'Каков радиус окружности?')
#print(radius)
t.circle(radius)

turtle.done()
