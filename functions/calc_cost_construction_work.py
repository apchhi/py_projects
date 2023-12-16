# # Python
'''
Малярная компания установила, что на каждые 10 квадратных
метров поверхности стены требуется 5 литров краски и 8 часов 
работы. Компания взимает за работу 2000 руб. в час. 
Напишите программу, которая просит пользователя ввести площадь 
поверхности окрашиваемой стены и цену 5-литровой емкости краски. 
Программа должна показать следующие данные: 
• количество требуемых емкостей краски: 
• количество затраченных рабочих часов; 
• стоимость краски; 
• стоимость работы; 
• общая стоимость малярных работ.
'''
import math

# need work
BASE_AREA = 10 #kv/m:
BASE_VOLUME = 5 #l paint container 
BASE_HOURS = 8 #hours work
# cost work
COST_HOUR = 2000  #R/h


def main():
  area = float(input('Enter the surface area of the wall to be painted(kv/m): '))
  #one container
  cost_5l_paint = float(input('Enter price of 5 liter paint container(rub): '))
  paint_container = int(quantity_container_calc(area))

  hours_work = hours_calc(area)
  #print(hours_work)

  cost_all_containers = (cost_containers_calc(paint_container,cost_5l_paint))
  #print(cost_all_containers)

  cost_work = cost_hours_calc(hours_work)
  
  all_coast = all_coast_calc(cost_all_containers, cost_work)
  
  print(f'\n- number of paint containers: {paint_container}',
f'\n- number of working hours: {hours_work}',
f'\n- paint cost: {cost_all_containers:,}rub',
f'\n- cost of work: {cost_work:,}rub',
f'\n- total cost of materials and work: {all_coast:,}rub')

  
def quantity_container_calc(area):
  count_container_paint = 0
  if area <= BASE_AREA:
    count_container_paint = 1
  else:
      count_container_paint = math.ceil(area / BASE_AREA)
  return count_container_paint
  
def hours_calc(area):
  return math.ceil(BASE_HOURS / BASE_AREA * area)

def cost_containers_calc(container, cost):
  return round((container * cost), 2)
  
def cost_hours_calc(hours):
  return round((hours * COST_HOUR), 2)

def all_coast_calc(container, work):  
  return (container + work)
  
main()