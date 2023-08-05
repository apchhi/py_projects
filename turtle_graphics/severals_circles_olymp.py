## Severals circles
import turtle

screen = turtle.Screen()
screen.setup(400, 500)
t = turtle.Turtle()
radius = 60
t.penup()

#one variant
x_coord = [-100, 0, 100, -50, 50]
y_coord = [0, 0, 0, -75, -75]

def draw_circle(x, y):
	t.goto(x, y)
	t.pendown()
	t.circle(radius)
	t.penup()
	
for x, y in zip(x_coord, y_coord):
	draw_circle(x, y)

turtle.done()


"""
## two variant
x = -100
y = 0

while x <= 100:
	t.goto(x, y)
	t.pendown()
	t.circle(radius)
	t.penup()
	x += 100

x = -50
y = -75
while x <= 50: 		
	t.goto(x, y)
	t.pendown()
	t.circle(radius)
	t.penup()
	x += 100

turtle.done()
"""


