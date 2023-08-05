import turtle

## создаем экран для рисования
screen = turtle.Screen()
screen.setup(500, 600)
## создаем черепашку
t = turtle.Turtle()

t.penup()
t.pensize(1)
t.hideturtle()
t.pencolor('#ffffff')
t.color('#ffffff')
t.screen.bgcolor('#000000')

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200
RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180
LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20
MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0
RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20
LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180
RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# shoulder
t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
t.write('Betelgeyser')
t.dot(8)
#
t.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
t.write('Hatisa')
t.dot(8)
#
# beltstar
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.write('Alnitac')
t.dot(8)
#
t.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
t.write('Alnilam')
t.dot(8)
#
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.write('Mintaka')
t.dot(8)
#
# knee
t.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
t.write('Saif')
t.dot(8)
#
t.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
t.write('Rigel')
t.dot(8)
#

#lines
#
t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
t.pendown()
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.penup()
#
t.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
t.pendown()
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.penup()
#
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.pendown()
t.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.penup()
#
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.pendown()
t.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
t.penup()
#
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.pendown()
t.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
t.penup()
#

screen.exitonclick()
#turtle.done()
