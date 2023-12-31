# # Python
'''
Кинетическая энергия. Из физики известно, что движущееся тело 
имеет кинетическую энергию. Приведенная ниже формула может 
использоваться для определения кинетической энергии движущегося 
тела:
Кe = 1/2mv^2, 
где Кe; —  это кинетическая энергия; 
m —  масса тела, кг; 
v —  скорость тела, м/с. 
Напишите функцию kinetic energy, которая в качестве аргументов 
принимает массу тела (в килограммах) и его скорость
(в метрах в секунду). Данная функция должна вернуть величину
кинетической энергии этого тела. Напишите программу, которая
просит пользователя ввести значения массы и скорости, а затем
вызывает функцию kinetic energy, чтобы получить кинетическую 
энергию тела.
'''
def main():
  print('Enter the mass of the object(kg):')
  mass = float(input())
  print('Enter the speed of the object(m/sec)')
  speed = float(input())
  Ke = kinetic_energy(mass, speed)
  print(f'The kinetic energy of the object = {Ke}')

def kinetic_energy(m, v):
  return 1/2 * m * v**2
  
main()

    
  
  
  
  