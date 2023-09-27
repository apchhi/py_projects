import turtle

screen = turtle.Screen()
screen.setup(500, 600)
t = turtle.Turtle()
#t.hideturtle()
NUM_CIRCLE = 20
OFFSET = 10
STARTING_RADIUS = 20
radius = STARTING_RADIUS

for count in range(NUM_CIRCLE):
  t.circle(radius)
  x = t.xcor()
  y = t.ycor() - OFFSET
  radius = radius + OFFSET
  t.penup()
  t.goto(x, y)
  t.pendown()
  #t.right(45)

turtle.done()