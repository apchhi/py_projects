# # python
'''
Черепашья графика: шахматная доска. Напишите программу 
с использованием черепашьей графики, в которой применяется  
функция square вместе с циклом (или циклами) для создания 
шахматного узора.
'''

import turtle

NUMBER_FIELDS = 64
SIZE = 10
ANGLE = 90
COLOR = 'black'

def main():
  screen = turtle.Screen()
  screen.setup(500, 600)  
  turtle.speed(0)
  drawing_square()
  turtle.done()

def drawing_square():
  turtle.goto(0,0)

  count_fields = int(NUMBER_FIELDS ** 0.5)
  
  all_size = count_fields * SIZE
  for y in range(0, all_size, SIZE):
    for x in range(0, all_size, SIZE):
      turtle.penup()
      turtle.goto(x, y)
      turtle.pendown()
      if ((x + y) // SIZE) % 2 == 0:
        square_color()
    

def square_color():
      turtle.fillcolor(COLOR)
      turtle.begin_fill()
      square()
      turtle.end_fill()

def square():
  for _ in range(4):
    turtle.forward(SIZE)
    turtle.left(ANGLE)

main()