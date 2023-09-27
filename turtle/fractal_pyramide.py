import turtle

screen = turtle.Screen()
screen.setup(600,600)
t = turtle.Turtle()
t.hideturtle()
#t.speed(0)

length = 10
angle = 90
quantity = 80

for count in range(quantity):
  t.forward(length)
  t.right(angle)
  length += 5
  
turtle.done()