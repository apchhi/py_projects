# # Python
'''
На стадионе имеется три категории сидячих мест. 
Места класса А стоят 20 долларов, 
места класса В —  15 долларов, 
места класса С —  10 доллоров. 
Напишите программу, которая запрашивает, сколько билетов 
каждого класса было продано, и затем выводит сумму дохода, 
полученного от продажи билетов.
'''
# plase class
A = 20  # dollars
B = 15
C = 10

def main():
  print('This program - calculator ...')
  a_coast, b_coast, c_coast = question_user()
  sum_tickets = calculation_profit(a_coast, b_coast, c_coast)
  print('All sum coast of tickets = ', sum_tickets, '$')

def question_user():
  print('Enter numbers of ticket sold')
  a_coast = int(input('class "A": '))
  b_coast = int(input('class "B": '))
  c_coast = int(input('class "C": '))
  return a_coast, b_coast, c_coast
  
def calculation_profit(a_coast, b_coast, c_coast):
  a_sum = a_coast * A
  b_sum = b_coast * B
  c_sum = c_coast * C
  return a_sum + b_sum + c_sum
  
main()