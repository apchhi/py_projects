## Black triangle

import turtle

screen = turtle.Screen()
screen.setup(400, 500)
t = turtle.Turtle()

t.goto(50, 100)
t.goto(100, 0)
t.goto(0, 0)

t.fillcolor('black')
t.begin_fill()

t.hideturtle()
t.goto(50, 50)
t.goto(100, 0)
t.goto(0, 0)

t.end_fill()
turtle.exitonclick()



