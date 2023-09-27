import turtle

screen = turtle.Screen()
screen.setup(500, 600)
t = turtle.Turtle()
#t.hideturtle()
t.speed(8)


RADIUS = 50
ANGLE = 10
#counter
angle = 0

while angle < 360:
  t.left(ANGLE)
  t.circle(RADIUS)
  angle += ANGLE

turtle.done()