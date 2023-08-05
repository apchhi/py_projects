## draw a compass
import turtle

screen = turtle.Screen()
screen.setup(700, 800)
t = turtle.Turtle()
t.hideturtle()
radius = 50
x_coord = [-200, 0]
y_coord = [0, -200]
direction = ['west', 'east', 'south', 'north']
length_line = 400
corner = 90

# circle
t.penup()
t.goto(0, -50)
t.pendown()
t.circle(radius)

t.penup()

# line 1
def lines(x, y, dir1, dir2):
    t.goto(x, y)
    t.write(dir1)
    t.pendown()
    t.forward(length_line)
    t.write(dir2)
    t.penup()
    t.backward(length_line)
    t.left(corner)

for x, y, dir1, dir2 in zip(x_coord, y_coord, direction[:2], direction[2:]):
    lines(x, y, dir1, dir2)


turtle.done()
