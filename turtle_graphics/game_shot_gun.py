## Game: Shot gun

import turtle

# Name constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100    # left bottom X target
TARGET_LLEFT_Y = 250    # right bottom Y target
TARGET_WIDTH = 35
FORCE_FACTOR = 30       # random force
PROJECTILE_SPEED = 1    # speed animation
NORTH = 90              # direction corner ...
SOUTH = 270
EAST = 0
WEST = 180              #

t = turtle.Turtle()

# customize window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# draw a target
t.hideturtle()
t.speed(0)
t.penup()
t.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
t.pendown()
t.setheading(EAST)
t.forward(TARGET_WIDTH)
t.setheading(NORTH)
t.forward(TARGET_WIDTH)
t.setheading(WEST)
t.forward(TARGET_WIDTH)
t.setheading(SOUTH)
t.forward(TARGET_WIDTH)
t.penup()

# center turtle
t.goto(0, 0)
t.setheading(EAST)
t.showturtle()
t.speed(PROJECTILE_SPEED)

# get the angle and force of shot from the user
angle = float(input("Enter the angle of the projectile: "))
force = float(input("Enter the force of the projectile: "))

distance = force * FORCE_FACTOR

# direction
t.setheading(angle)

# projectile launch
t.pendown()
t.forward(distance)

# how launch hit the target
if (t.xcor() >= TARGET_LLEFT_X and
    t.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    t.ycor() >= TARGET_LLEFT_Y and
    t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("Taret hit!")
else:
    print("Target not hit!")
