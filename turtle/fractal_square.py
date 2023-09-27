import turtle

screen = turtle.Screen()
screen.setup(600,600)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

length = 10
next_length = 5
quantity = 50

for number in range(quantity):
  for angle in range(4):
    t.left(90)
    t.forward(length)
  length += next_length
  
turtle.done()