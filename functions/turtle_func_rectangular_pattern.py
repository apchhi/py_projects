# # Python
'''
Черепашья графика: прямоугольный узор. В программе напишите 
функцию drawPattern, которая использует библиотеку черепашьей 
графики, чтобы нарисовать прямоугольный узор. 
Функция drawPattern должна принимать два аргумента: 
один из них задает ширину узора, другой — его высоту. 
Узор будет выглядеть, когда ширина и высота одинаковые. 
Когда программа выполняется, она должна запросить у 
пользователя ширину и высоту узора и затем передать эти 
значения в качестве аргументов в функцию drawPattern.

'''

import turtle

def main():
    width = int(input('Enter width of the pattern: '))
    height = int(input('Enter height of the pattern: '))
    while width != height:
      print('No correct value! Enter value width = value height')
      width = int(input('Enter width of the pattern: '))
      height = int(input('Enter height of the pattern: '))
    drawPattern(width, height)

def drawPattern(width, height):
    coord_list = []
    line = width // 2
    start_x = width
    start_y = width
    multiplier = 0.25
    
    screen = turtle.Screen()
    screen.setup(400, 500)
    t = turtle.Turtle()
  
    for i in range(3):
      if i != 0:
        start_x += (width/i * multiplier)
        print(start_x)
      else:
        start_x = 0
        print(start_x)
      start_y = start_x
        
      t.penup()
      t.goto(start_x, start_y)
      print(t.pos())
      t.pendown()
      if i == 2:
        t.fillcolor('black')
        t.begin_fill()
        for j in range(4):
          coord_list.append(t.pos())
          t.forward(line)   
          coord_list.append(t.pos())
          t.forward(line)
          t.left(90)
        line *= 0.5
        t.end_fill()
      else:
        for j in range(4):
          coord_list.append(t.pos())
          t.forward(line)   
          coord_list.append(t.pos())
          t.forward(line)
          t.left(90)
        line *= 0.5

      
    for i in range(8):
      t.penup()
      t.goto(coord_list[i])
      t.pendown()
      for j in range(4, 9, 4):
        t.goto(coord_list[i+j])
      

    turtle.done()

main()


'''
      for i in range(3):
        if i == 0:
          start_x = 50
        elif i == 1:
          start_x = 50 + (50 * multiplier)
        elif i == 2:
          start_x = 62.5 + (25 * multiplier)
'''
