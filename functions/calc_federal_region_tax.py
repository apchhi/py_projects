print('This program calculates federal and state sales taxes.')
# %
REGION_TAX_PERCENT = 2.5
FEDERAL_TAX_PERCENT = 5

def main():
	# input
	buy = float(input('Enter purchase amoutn: '))
	# output
	region_tax_money,federal_tax_money,all_tax_money = tax_money(buy,REGION_TAX_PERCENT,FEDERAL_TAX_PERCENT)
	profit = profit_sale(buy,region_tax_money,federal_tax_money) 	

	print(f'Regional sales tax: {region_tax_money:,.2f}')
	print(f'Federal sales tax: {federal_tax_money:,.2f}')
	print(f'All sales tax: {all_tax_money:,.2f}')

	print(f'Your sales income: {profit:,.2f}')


def tax_money(buy, reg_per, fed_per):
	region = buy * reg_per / 100
	federal = buy * fed_per / 100
	all = region + federal
	return region, federal, all

def profit_sale(buy, reg_money, fed_money):
	profit = buy - (reg_money + fed_money)
	return profit

main()