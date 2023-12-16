import module1
import turtle
X1 = 0
Y1 = 0
X2 = 100
Y2 = 0
X3 = 50
Y3 = 100
LENGTH = 100
RADIUS = 20

def main():
# square
	module1.square(X1,Y1,LENGTH,'red')
# circle
	module1.circle(X1,Y1,RADIUS,'grey')
	module1.circle(X2,Y2,RADIUS,'grey')
	module1.circle(X3,Y3,RADIUS,'grey')
# triangle
	module1.line(X1,Y1,X2,Y2,'yellow')
	module1.line(X2,Y2,X3,Y3,'yellow')
	module1.line(X3,Y3,X1,Y1,'yellow')


screen = turtle.Screen()
screen.setup(500,600)
main()
screen.exitonclick()