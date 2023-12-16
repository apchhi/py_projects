# # Python
'''
Черепашья графика: функция рисования треугольника. 
Напишите функцию triangle, которая использует библиотеку 
черепашьей графики для рисования треугольника. 
Функция должна принимать в качестве аргументов 
координаты X  и Y сторон треугольника и цвет, которым 
треугольник должен быть заполнен. Продемонстрируйте эту 
функцию в программе.
'''
import turtle


def main():
  triangle_coord = {
    "x_coord" : [], 
    "y_coord" : []
  }
  
  triangle_color = input('Enter any color of the triangle: ')
  for i in range(3):
    triangle_coord["x_coord"].append(float(input(f'Enter the X coordinate of {i+1} point: ')))
    triangle_coord["y_coord"].append(float(input(f'Enter the Y coordinate of {i+1} point: ')))
  
  triangle(
    triangle_coord["x_coord"][0], triangle_coord["y_coord"][0], 
    triangle_coord["x_coord"][1], triangle_coord["y_coord"][1], 
    triangle_coord["x_coord"][2], triangle_coord["y_coord"][2],
    triangle_color
    )
  
  
def triangle(x1, y1, x2, y2, x3, y3, color):
  screen = turtle.Screen()
  screen.setup(400,500)
  t = turtle.Turtle()
  t.hideturtle()
  t.fillcolor(color)
  t.begin_fill()
  t.penup()
  t.goto(x1,y1)
  t.pendown()
  t.goto(x2,y2)
  t.goto(x3,y3)
  t.goto(x1,y1)
  t.end_fill()
  turtle.done()
  

main()