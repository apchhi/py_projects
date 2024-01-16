## what is the angle of the turtle
import turtle


screen = turtle.Screen()
screen.setup(300, 300)
t = turtle.Turtle()

t.hideturtle()
color = input('Enter color of the pen: \n   / red, green, blue, orange, yellow, pink, black, white / \n')
t.pencolor(color)

what_pencolor = t.pencolor()
if  what_pencolor == 'red' or what_pencolor == 'blue':
    t.pensize(5)

t.pendown()
t.dot()

screen.exitonclick()
