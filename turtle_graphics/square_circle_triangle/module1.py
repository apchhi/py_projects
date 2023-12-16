import turtle

t = turtle.Turtle()
t.hideturtle()

def square(x,y,width,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.fillcolor(color)
	t.begin_fill()
	for i in range(4):
		t.forward(width)
		t.left(90)
	t.end_fill()
	
def circle(x,y,radius,color):
	t.penup()
	t.goto(x,y-radius)
	t.pendown()
	t.fillcolor(color)
	t.begin_fill()
	t.circle(radius)
	t.end_fill()

def line(start_x, start_y, end_x, end_y, color):
	t.penup()
	t.goto(start_x, start_y)
	t.pendown()
	t.pencolor(color)
	t.goto(end_x, end_y)