# # Python
def main():
  print('This progran - expense calculator on car in month and year')
  service, insurance, petrol, credit, oil, maintenance, tires = user_answer()
  output_month, output_year = calculator(service, insurance, petrol, credit, oil, maintenance, tires)
  #get_year = calt_year(get_month)
  #calculator(user_answer(service, insurance, petrol, credit, oil, maintenance, tires))
  print(f'Expense in month: {output_month:,.2f}$ & expense in year: {output_year:,.2f}$')

def user_answer():
  print('Enter value coast expense on car in month($)')
  ser = float(input('service: '))
  ins = float(input('insurance: '))
  pet = float(input('petrol: '))
  cre = float(input('credit: '))
  oil = float(input('oil: '))
  mai = float(input('maintenance: '))
  tir = float(input('tires: '))
  return ser, ins, pet, cre, oil, mai, tir
  
def calculator(ser, ins, pet, cre, oil, mai, tir):
  month = ser+ins+pet+cre+oil+mai+tir
  year = month * 12
  return month, year
  
main()


