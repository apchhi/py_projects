## what is the angle of the turtle
import turtle


screen = turtle.Screen()
screen.setup(300, 300)
t = turtle.Turtle()


angle = int(input('Enter degree angle: '))
t.pendown()
t.setheading(angle)


if int(t.heading()) >= 0 and t.heading() <= 45:
    t.penup()

print ('Turtle angle = ', t.heading(), 'and Pen Up - ', not(t.isdown()))

screen.exitonclick()
