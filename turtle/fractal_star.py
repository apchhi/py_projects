import turtle

screen = turtle.Screen()
screen.setup(600,600)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

length = 150
angle = 135
quantity = 8

t.penup()
t.goto(-50, 50)
t.pendown()

for count in range(quantity):
  t.right(angle)
  t.forward(length)

turtle.done()