## what is the angle of the turtle
import turtle


screen = turtle.Screen()
screen.setup(800, 600)
t = turtle.Turtle()
t.pencolor('black')
t.pensize(1)

#RECTANGLE
LEFT_BUTTOM_X = 100
LEFT_BUTTOM_Y = 100
RIGHT_TOP_X = 200
RIGHT_TOP_Y = 200

RECTANGLE_WIDTH = int(RIGHT_TOP_X) - int(LEFT_BUTTOM_X)
#PROJECTILE_SPEED = 1
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


# draw a rectangle
t.hideturtle()
t.speed(0)
t.penup()
t.goto(LEFT_BUTTOM_X, LEFT_BUTTOM_Y)
t.pendown()
t.setheading(EAST)
t.forward(RECTANGLE_WIDTH)
t.setheading(NORTH)
t.forward(RECTANGLE_WIDTH)
t.setheading(WEST)
t.forward(RECTANGLE_WIDTH)
t.setheading(SOUTH)
t.forward(RECTANGLE_WIDTH)

t.setheading(45)
t.penup()
t.goto(0, 0)
t.showturtle()

print('Enter coordinates turtle in x and y')
position_x = int(input('Enter "x": '))
position_y = int(input('Enter "y": '))

t.goto(position_x, position_y)
t.pendown()


if (t.xcor() >= LEFT_BUTTOM_X and
    t.xcor() <= RIGHT_TOP_X and
    t.ycor() >= LEFT_BUTTOM_Y and
    t.ycor() <= RIGHT_TOP_Y):
    t.hideturtle()
    t.pencolor('red')
    t.dot(10)
    print('Hit!')
else:
    print('No hit!')




screen.exitonclick()
