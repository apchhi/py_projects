# # python
'''
Черепашья графика: городской силуэт. Напишите программу с 
черепашьей графикой, которая рисует городской силуэт. 
Конечная задача программы состоит в том, чтобы нарисовать 
контуры нескольких городских зданий на фоне ночного неба. 
Подразделите программу на модули, написав функции, 
которые выполняют приведенные ниже задачи: 
• рисование контуров зданий; 
• рисование нескольких окон в зданиях; 
• использование случайно разбросанных звезд в виде точек 
  (убедитесь, что звезды появляются на небе, а не на зданиях).
'''

import turtle
import random


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
X_START = -250
Y_START = -300
START_STAR = 5
END_STAR = 5
CITY_START_STAR = 10
STAR_SIZE_START = 2
STAR_SIZE_END =  5
STAR_SIZE_STEP = 10
COLOR_BUILDING = "gray"
STAR_COLOR = "white"
COLOR_BASE = "black"
COLOR_WINDOW = "yellow"

FROM_RAND_X_GENERATE = 50
BEFORE_RAND_X_GENERATE = 151
RAND_STEP_GENERATE = 50
STEP_START_FROM_RAND_Y = 50
STEP_STOP_BEFORE_RAND_Y = 99

size_foot = (50, 100, 150)
line = (1, 2, 3)

size_height = (50, 100, 150, 200, 250, 300, 350, 400, 450, 500)

stars_value = (5, 10, 15)
windows_value = (0, 2, 4, 8, 12, 16)

bool_value = (True, False)


def main():
  date_building = {
  "all_height_building" : [],
  "all_coord_width_building" : [],
  "all_width_foot" : [],
  "all_cut_foot" : [],
  "all_windows_line" : []
  }
  screen = turtle.Screen()
  screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
  screen.bgcolor('black')
  drawing_outlines_buildings(date_building)
  turtle.done()


def drawing_outlines_buildings(date_building):
  coord_width_building = X_START
  height_building = Y_START
  from_rand_y = int(Y_START + STEP_START_FROM_RAND_Y)
  before_rand_y = int(Y_START + (SCREEN_HEIGHT - STEP_STOP_BEFORE_RAND_Y))
  
  turtle.penup()
  turtle.goto(X_START, Y_START)
  turtle.pendown()
  
  turtle.fillcolor(COLOR_BUILDING)
  turtle.begin_fill()

  while coord_width_building < X_START + SCREEN_WIDTH:
    height_building = random.randrange(from_rand_y, before_rand_y, RAND_STEP_GENERATE)
    turtle.goto(coord_width_building, height_building)

    width_foot = random.randrange(size_foot[0], size_foot[2]+1, RAND_STEP_GENERATE)
    coord_width_building += width_foot

    if coord_width_building < X_START + SCREEN_WIDTH:
      turtle.goto(coord_width_building, height_building)
    elif coord_width_building >= X_START + SCREEN_WIDTH:
      coord_width_building = X_START + SCREEN_WIDTH
      turtle.goto(coord_width_building, height_building)
      turtle.goto(coord_width_building, Y_START)
      turtle.goto(X_START, Y_START)
    
    ## check
    print('Coord_width: ', coord_width_building)
    date_building["all_coord_width_building"].append(coord_width_building)
    print('Height_building: ', height_building)
    date_building["all_height_building"].append(height_building)
    print('Width_foot: ', width_foot)
    date_building["all_width_foot"].append(width_foot)

    windows_line, cut_foot = calculate_line(width_foot)
    date_building["all_cut_foot"].append(cut_foot)
    print('Cut_foot:', cut_foot)
    date_building["all_windows_line"].append(windows_line)
    print('Windows_line: ', windows_line)
    print('--------------------')
    
  turtle.end_fill()
  ## check
  drawing_windows_and_stars(date_building)
  print(date_building)

def calculate_line(width_foot):
    windows_line = 0
    cut_foot = 0
    
    if width_foot == size_foot[0]:
      windows_line = size_foot[0]
      cut_foot = width_foot // 2
    elif width_foot == size_foot[1]:
      windows_line = size_foot[1]
      cut_foot = width_foot // 3
    elif width_foot == size_foot[2]:
      windows_line = size_foot[2]
      cut_foot = width_foot // 4
      
    return windows_line, cut_foot


def drawing_windows_and_stars(date_building):
  for i in range(len(date_building["all_coord_width_building"])):
    coutn_stars = count_generate_stars(date_building["all_height_building"][i])
    count_windows = count_generate_windows(date_building["all_height_building"][i])
    drawing_windows(
      date_building["all_coord_width_building"][i],
      date_building["all_height_building"][i],
      date_building["all_windows_line"][i],
      date_building["all_cut_foot"][i],
      count_windows)
    drawing_stars(date_building["all_height_building"][i], 
    date_building["all_coord_width_building"][i], 
    date_building["all_width_foot"][i], 
    coutn_stars)


def drawing_stars(height_building, coord_width, width_foot, count_stars):
  for _ in range(count_stars):
    x = random.randint(coord_width - width_foot + START_STAR, coord_width - END_STAR)
    y = random.randint(height_building + CITY_START_STAR, SCREEN_HEIGHT - END_STAR)
    star_size = random.randrange(STAR_SIZE_START, STAR_SIZE_END, STAR_SIZE_STEP)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(STAR_COLOR)
    turtle.dot(star_size)
    turtle.penup()
    turtle.pencolor(COLOR_BASE)


def drawing_windows(coord_width, coord_height, windows_line, cut_foot, count_windows):
  coord_count_width = coord_width
  for _ in range(windows_line):
    coord_count_width -= cut_foot
    turtle.penup()
    turtle.goto(coord_count_width,coord_height)
  drawing_line_windows(count_windows)


def drawing_line_windows(count_windows):
  for _ in range(count_windows):
    off_on = random.choice(bool_value)
    if off_on == True:
      turtle.penup()
      turtle.setheading(270)
      turtle.forward(5)
      turtle.pendown()
      turtle.fillcolor(COLOR_WINDOW)
      turtle.begin_fill()
      for _ in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(90)
      turtle.end_fill()
    else:
      pass


def count_generate_stars(height_building):
  count_stars = 0
  if (height_building >= Y_START + size_height[0]) and (height_building <= Y_START + size_height[2]):
    count_stars= random.randint(1, stars_value[2])
  elif (height_building >= Y_START + size_height[3]) and (height_building <= Y_START + size_height[6]):
    count_stars= random.randint(1, stars_value[1])
  elif (height_building >= Y_START + size_height[7]) and (height_building <= Y_START + size_height[9]):
    count_stars= random.randint(1, stars_value[0])
  return count_stars


def count_generate_windows(heigth_building):
  if (heigth_building >= size_height[0]) and (heigth_building < size_height[1]):
    return windows_value[1]
  elif (heigth_building >= size_height[1]) and (heigth_building < size_height[3]):
    return windows_value[2]
  elif (heigth_building >= size_height[3]) and (heigth_building < size_height[5]):
    return windows_value[3]
  elif (heigth_building >= size_height[5]) and (heigth_building < size_height[7]):
    return windows_value[4]
  elif (heigth_building >= size_height[7]) and (heigth_building < size_height[9]):
    return windows_value[5]
  else:
    return windows_value[0]
  
'''
size_height = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
windows_value = [0, 2, 4, 8, 12, 16]
def count_generate_windows(heigth_building):
  count_windows = windows_value[0]
  if (heigth_building >= size_height[0]) and (heigth_building < size_height[1]):
    count_windows = windows_value[1]
  elif (heigth_building >= size_height[1]) and (heigth_building < size_height[3]):
    count_windows = windows_value[2]
  elif (heigth_building >= size_height[3]) and (heigth_building < size_height[5]):
    count_windows = windows_value[3]
  elif (heigth_building >= size_height[5]) and (heigth_building < size_height[7]):
    count_windows = windows_value[4]
  elif (heigth_building >= size_height[7]) and (heigth_building < size_height[9]):
    count_windows = windows_value[5]
  return count_windows


'''
main()


