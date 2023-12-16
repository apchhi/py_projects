# # Python
'''
Черепашья графика: модульный снеговик. Напишите программу, 
которая использует черепашью графику для изображения снеговика.
Помимо главной функции программа также должна иметь 
перечисленные ниже функции: 
• drawBase —  функция должна нарисовать основу снеговика, 
т. е. большой снежный ком внизу; 
• drawMidSection —  функция должна нарисовать средний 
снежный ком; 
• drawArms —  функция должна нарисовать руки снеговика; 
• drawHead —  функция должна нарисовать голову снеговика, 
глаза, рот и другие черты лица по вашему усмотрению; 
• drawHat —  эта функция должна нарисовать шляпу снеговика.

'''
import turtle

def main():
  coord_circles = [-200, 0, 120]
  angle_fing = 20 
  radius = 100
  screen = turtle.Screen()
  screen.setup(400, 500)
  t = turtle.Turtle()
  '''
  # ПО ЗАДАНИЮ 
  drawBase(radius, t)
  drawMidSection(radius, t)
  drawHead(radius, t)
  '''
  drawBody(coord_circles, radius, t)
  drawHead(coord_circles, radius, t)
  drawArms(radius, angle_fing, t)
  drawHat(coord_circles, radius, t)
  turtle.done()

def drawBody(coords, radius, t):
  for coord in coords:
    t.penup()
    t.goto(0, coord)
    t.pendown()
    t.circle(radius)
    t.penup()
    radius *= 0.6

def drawHead(coords, radius, t):
  base_line = coords[2] + radius
  t.penup()
  t.goto(-coords[2]*0.1, base_line*0.73)
  t.pendown()
  t.dot(8)
  t.penup()
  t.goto(coords[2]*0.1, base_line*0.73)
  t.pendown()
  t.dot(8)
  t.penup()
  #
  t.goto(-coords[2]*0.12, base_line*0.65)
  t.pendown()
  t.pensize(3)
  t.goto(coords[2]*0.12, base_line*0.65)
  t.pensize(1)
  t.penup
    
def drawHat(coords, radius, t):
  base_line = coords[2]
  
  t.penup()
  t.goto(-base_line*0.5, base_line+radius/2)
  t.pendown()
  t.fillcolor("black")
  t.begin_fill()
  t.setheading(0)
  t.forward(base_line)
  t.left(90)
  t.forward(base_line*0.33)
  t.left(90)
  t.forward(base_line*0.15)
  #
  t.right(90)
  t.forward(base_line*0.11)
  t.left(90)
  t.forward(base_line*0.7)
  t.left(90)
  t.forward(base_line*0.11)
  t.right(90)
  #
  t.forward(base_line*0.15)
  t.left(90)
  t.forward(base_line*0.33)
  t.pendown()
  t.end_fill()
  
'''
# ПО ЗАДАНИЮ
def drawBase(radius, t):
    t.penup()
    t.goto(0, -radius*2)
    t.pendown()
    t.circle(radius)
    t.penup()

def drawMidSection(radius, t):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(radius*0.5)
    t.penup()

def drawHead(radius,t):
  t.penup()
  t.goto(0, radius)
  t.pendown()
  t.circle(radius*0.25)
  t.penup()
'''

def drawArms(radius, angle_fing, t):
  for i in range(2):  
    
    if i == 0:
      determ = -radius
      angle = 160
    else:
      determ = radius
      angle = 20
      
    # arm
    t.penup()
    t.goto(determ//2, radius//2)
    t.pendown()
    t.setheading(angle)
    t.forward(radius//2)
    t.left(40)
    t.forward(radius//2)
    # fingers
    coord = t.pos()
    t.right(angle_fing)
    t.forward(radius//3)
    t.penup()
    t.goto(coord)
    t.pendown()
    t.left(angle_fing*2)
    t.forward(radius//3)
    t.penup()

  
main()
