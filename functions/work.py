import turtle
import random


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
X_START = -250
Y_START = -300


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
  from_rand_y = int(Y_START + 50)
  befor_rand_y = int(Y_START + (SCREEN_HEIGHT - 99))
  from_rand_x = 50
  befor_rand_x = 151
  rand_step = 50
  turtle.penup()
  turtle.goto(X_START, Y_START)
  turtle.pendown()
  turtle.fillcolor('gray')
  turtle.begin_fill()

  while coord_width_building < X_START + SCREEN_WIDTH:
    height_building = random.randrange(from_rand_y, befor_rand_y, rand_step)
    turtle.goto(coord_width_building, height_building)

    width_foot = random.randrange(from_rand_x, befor_rand_x, rand_step)
    coord_width_building += width_foot

    if coord_width_building < X_START + SCREEN_WIDTH:
      turtle.goto(coord_width_building, height_building)
    elif coord_width_building >= X_START + SCREEN_WIDTH:
      coord_width_building = X_START + SCREEN_WIDTH
      turtle.goto(coord_width_building, height_building)
      turtle.goto(coord_width_building, Y_START)
      turtle.goto(X_START, Y_START)

    print('Coord_width: ', coord_width_building)
    date_building["all_coord_width_building"].append(coord_width_building)
    print('Height_building: ', height_building)
    date_building["all_height_building"].append(height_building)
    print('Width_foot: ', width_foot)
    date_building["all_width_foot"].append(width_foot)
    print('--------------------')
    
    drawing_windows(width_foot, coord_width_building, height_building, date_building)

  print(date_building)  
  turtle.end_fill()


def drawing_windows(width_foot, coord_width_building, height_building, date_building):
    count_coord_foot = coord_width_building
    windows_line = 0
    cut_foot = 0
    if width_foot == 50:
        windows_line = 1
        cut_foot = width_foot // 2
    elif width_foot == 100:
        windows_line = 2
        cut_foot = width_foot // 3
    elif width_foot == 150:
        windows_line = 3
        cut_foot = width_foot // 4
        
	date_building["all_windows_line"].append(windows_line)
	date_building["all_cut_foot"].append(cut_foot)

    #print("Count_coord_foot: ", count_coord_foot)
    #print('With_foot: ', width_foot)
    #print('Windows_line: ', windows_line)
    #print('Cut_foot: ', cut_foot)


'''
    for _ in range(windows_line):
      count_coord_foot += cut_foot
      turtle.penup()
      turtle.goto(count_coord_foot, height_building)

      drawing_windows_count(height_building)

def drawing_windows_count(height):
  count_windows = 0
  if (height >= 50) and (height < 100):
    count_windows = random.randint(0, 2)
  elif (height >= 100) and (height < 200):
    count_windows = random.randint(0, 4)
  elif (height >= 200) and (height < 300):
    count_windows = random.randint(0, 8)
  elif (height >= 300) and (height < 400):
    count_windows = random.randint(0, 12)
  elif (height >= 400) and (height < 500):
    count_windows = random.randint(0, 16)

  for _ in range(count_windows):
    draw_one_window()


def draw_one_window():
  turtle.penup()
  turtle.setheading(270)
  turtle.forward(5)
  turtle.pendown()
  for _ in range(2):
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(90)
'''
main()


drawing_windows(
date_building["all_coord_width_building"][i],
date_building["all_height_building"][i],
date_building["all_windows_line"][i],
date_building["all_cut_foot"][i],
count_windows)