import turtle

screen = turtle.Screen()
screen.setup(500, 600)
t = turtle.Turtle()

square_width = -100 // 2
square_height = -100 // 2

circle_width = 0 // 2
circle_height = -160 // 2

go_square = [square_width, square_height]
go_circle = [circle_width, circle_height]

t.fillcolor('red')

t.penup()
t.goto((go_square[0]), (go_square[1]))
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto((go_circle[0]), (go_circle[1]))
t.pendown()

t.begin_fill()
t.circle(80)
t.end_fill()

t.hideturtle()

screen.exitonclick()
