import turtle

screen = turtle.Screen()
screen.setup(600,600)
t = turtle.Turtle()
t.hideturtle()
#t.speed(0)

length = 50
angle = 45
quantity = 8

t.write("STOP")

t.penup()
t.goto(-15, -50)
t.pendown()

for count in range(quantity):
  t.forward(length)
  t.left(angle)

turtle.done()

