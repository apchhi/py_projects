## Game: Shot gun

import turtle
import math

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

# coordinates x and y
x = t.xcor()
y = t.ycor()

# angles
target_left_button_angle = math.degrees(math.atan2(TARGET_LLEFT_Y, TARGET_LLEFT_X))
target_right_button_angle = math.degrees(math.atan2(TARGET_LLEFT_Y, TARGET_LLEFT_X + TARGET_WIDTH))
target_left_top_angle = math.degrees(math.atan2(TARGET_LLEFT_Y + TARGET_WIDTH, TARGET_LLEFT_X))
# point of impact angle
point_angle = math.degrees(math.atan2(y, x))

print("Left top: ", target_left_top_angle)
print("Left button: ", target_left_button_angle)
print("Right button: ", target_right_button_angle)

# how launch hit the target
if (x >= TARGET_LLEFT_X and
    x <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    y >= TARGET_LLEFT_Y and
    y <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("Taret hit!")
else:
    print("Target not hit!")

# force
if (x < TARGET_LLEFT_X and
    y < TARGET_LLEFT_Y):
    print("Decrease the force.")
elif (x > (TARGET_LLEFT_X + TARGET_WIDTH) and
      y > (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("Increase the force.")
else:
    print("Normal the force!")

## angle
if point_angle > target_left_top_angle:
    print("Increase the angle.")
elif point_angle < target_right_button_angle:
    print("Decrease the angle.")
else:
    print("Normal the angle!")
    ## force and angle
    #if (t.cor() > (TARGET_LLEFT_X + TARGET_WIDTH) and
    #    t.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH)):
    #    print("Decrease the force.")
    #
    #if (point_angle < target_right_button_angle and
    #    point_angle > target_left_button_angle):
    #    print("If you want, you can slightly increase the angle(optional).")
    #elif (point_angle > target_right_button_angle and
    #      point_angle < target_left_button_angle):
    #    print("If you want, you can slightly decrease the angle(optional).")

#if point_angle > target_left_button_angle and point_angle < target_left_top_angle:
#    print("If you want, you can slightly decrease the angle(optional).")
#    else:
#        print("Decrease the angle.")
#elif point_angle < target_left_button_angle and point_angle > target_right_button_angle:
#    print("If you want, you can slightly increase the angle(optional).")
#    else:
#        print("Increase the angle.")
t.down()
