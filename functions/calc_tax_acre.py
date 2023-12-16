# # Python
'''
Муниципальный округ собирает налоги на недвижимое 
имущество на основе оценочной стоимости имущества, 
составляющей 60% его фактической стоимости. Например, 
если акр земли оценен в 10 000 долларов, то его оценочная
стоимость составит 6000 долларов. В этом случае налог на 
имущество составит 72 цента за каждые 100 долларов оценочной 
стоимости. Налог на акр, оцененный в 6000 долларов, составит 
43.20 доллара. Напишите программу, которая запрашивает 
фактическую стоимость недвижимого имущества и показывает 
оценочную стоимость и налог на имущество.
'''
EVALUATION_PERCENT = 0.6
# tax ... cents
TAX_ON_100_DOL = 72

def main():
  coast_acre = float(input('Enter the coast of your estate per a acre: '))
  coast_estate = calc_evaluation(coast_acre)
  tax = calc_tax(coast_estate)
  print(f'Assessed value = {coast_estate:,.2f}$ and property tax = {tax:,.2f}$')
  
# assessed value
def calc_evaluation(coast):
  return coast * EVALUATION_PERCENT
  
# property tax
def calc_tax(coast):
  tax_dollar = TAX_ON_100_DOL / 100 / 100
  return tax_dollar * coast 

main()



