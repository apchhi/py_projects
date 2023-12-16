# # Python
'''
При падении тела под действием силы тяжести для определения 
расстояния, которое тело пролетит за определенное время, 
применяется формула: 
d = 1/2gt^2 
где d  —  расстояние, м; 
g = 9.8, м/с2; 
t —  время падения тела, с. 
Напишите функцию falling distance, которая в качестве 
аргумента принимает время падения тела (в секундах). 
Функция должна вернуть расстояние в метрах, которое тело 
пролетело в течение этого времени. Напишите программу, 
которая вызывает эту функцию в цикле, передает значения от 
1 до 10 в качестве аргументов и показывает возвращаемое 
значение.
'''
GRAVITY = 9.8 #m/s

def main():
  print('Enter your answer "start", that you hawe calc distance or "stop" that to stop program: ')
  answer = input()

  while answer != 'stop':
    time = int(input('Enter time falling in seconds: '))
    distance = falling_distance(time)
    print(f'{distance:,.2f} meters')
    answer = input('Enter "stop" to stop program or another value to continue thr program: ')
  
def falling_distance(time):
  return 1/2 * GRAVITY * time**2
   
main()