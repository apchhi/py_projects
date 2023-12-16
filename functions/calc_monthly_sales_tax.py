# # Pyton
'''
Розничная компания должна зарегистрировать отчет о месячном
налоге с продаж с указанием общего налога с продаж за месяц
и взимаемых сумм муниципального и федерального налогов с 
продаж. Федеральный налог с продаж составляет 5%, муниципальный 
налог с продаж — 2,5%. Напишите программу, которая просит 
пользователя ввести общий объем продаж за месяц. Из этого 
значения приложение должно рассчитать и показать: 
• сумму муниципального налога с продаж; 
• сумму федерального налога с продаж; 
• общий налог с продаж (муниципальный плюс федеральный).
'''
FEDERAL_TAX = 5 #%
MUNICIPAL_TAX = 2.5 #%

def main():
  total_sales_volume = float(input('Enter total sales volume: '))
  federal = federal_tax_calc(total_sales_volume)
  municipal = municipal_tax_calc(total_sales_volume)
  general = general_tax_calc(federal, municipal)
  print(f'Federal tax = {federal:,.2f}$, municipal tax = {municipal:,.2f}$, general tax = {general:,.2f}$')

#federal 
def federal_tax_calc(volume):
  return FEDERAL_TAX / 100 * volume

#municipal 
def municipal_tax_calc(volume):
  return MUNICIPAL_TAX / 100 * volume

#general
def general_tax_calc(federal, municipal):
  return federal + municipal
  
main()



