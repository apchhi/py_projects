import circle
import rectangle

# main
AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5


def display_menu():
  print('The program allows you to make calculations between geometric shapes')
  print()
  print(' MAIN')
  print('1. Area of circle')
  print('2. Circumference of circle')
  print('3. Area rectangle')
  print('4. Perimeter rectangle')
  print('5. Quit')

def main():
  # contains user selection
  choice = 0
  
  while choice != QUIT_CHOICE:
    display_menu()
    choice = int(input('Enter option: '))
    
    if choice == AREA_CIRCLE_CHOICE:
      radius = float(input('Enter radius a circle: '))
      print('Area circle = ', circle.area(radius))
    elif choice == CIRCUMFERENCE_CHOICE:
      radius = float(input('Enter radius of circle: '))
      print('Circumference of circle = ', circle.circumference(radius))
    elif choice == AREA_RECTANGLE_CHOICE:
      width = float(input('Enter width of rectangle: '))
      length = float(input('Enter width of rectangle: '))
      print('Area of rectangle = ', rectangle.area(width, length))
    elif choice == PERIMETER_RECTANGLE_CHOICE:
      width = float(input('Enter width of rectangle: '))
      length = float(input('Enter width of rectangle: '))
      print('Perimeter of rectangle = ', rectangle.perimeter(width, length))
    elif choice == QUIT_CHOICE:
      print('Quit from program.')
    else:
      print('Error. Invalid value. Reload enter.')
      
main()
      
      
      