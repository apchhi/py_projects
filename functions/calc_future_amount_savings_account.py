# # Python
'''
Будущая стоимость. Предположим, что на вашем сберегательном 
счете есть определенная сумма денег, и счет приносит составной
ежемесячный процентный доход. Вы хотите вычислить сумму, 
которую будете иметь после определенного количества месяцев. 
Формула приведена ниже: 
F  = P * (1 + i)^t, 
где F —  будущая сумма на счете после указанного периода 
времени; Р —  текущая сумма на счете; i — ежемесячная 
процентная ставка; t —  количество месяцев. 
Напишите программу, которая предлагает пользователю ввести 
текущую сумму на счете, ежемесячную процентную ставку и 
количество месяцев, в течение которых деньги будут находиться 
на счете. Программа должна передать эти значения в функцию, 
которая возвращает будущую сумму на счете после заданного 
количества месяцев. Программа должна показать будущую сумму 
на счете.
'''

def main():
  current_amount = float(input('Enter the current account amount($): '))
  monthly_rate = float(input('Enter the monthly interest rate(%): '))
  number_months = int(input('Enter the number of months during which the money will be in the account: '))
  future_amount_period = calc_current_amoutn(current_amount, monthly_rate, number_months)
  account_all_amoutn = future_amount_period + current_amount
  print(f'Future amount in account = {account_all_amoutn:,.2f}$')

def calc_current_amoutn(p, i, t):
  f  = p * (1 + (i/100))**t
  return f

main()