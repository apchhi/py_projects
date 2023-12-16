# # Python
'''
Один фут равняется 12 дюймам. Напишите функцию feet to inches, 
которая в качестве аргумента принимает количество футов и 
возвращает количество дюймов в этом количестве футов. 
Примените эту функцию в программе, которая предлагает 
пользователю ввести количество футов и затем показывает 
количество дюймов в этом количестве футов. QI дюймы"
'''
ONE_FOOT = 12 #inch

def main():
  number_feet = float(input('Enter number of feet'))
  number_inches = feet_to_inches(number_feet)
  print(f'At {number_feet} feet {number_inches:,.2f} inches')
  
def feet_to_inches(number_feet):
  return number_feet * ONE_FOOT

main()
