import turtle

screen = turtle.Screen()
screen.setup(500, 600)
t = turtle.Turtle()
#t.hideturtle()

START_X = -200
START_Y = 0
NUM_LINES = 36
LINE_LENGTH = 400
ANGLE = 170
t.speed(10)
t.penup()
t.goto(START_X, START_Y)
t.pendown()

for count in range(NUM_LINES):
  t.forward(LINE_LENGTH)  
  t.left(ANGLE)

turtle.done()