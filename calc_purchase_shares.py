## Calculation of purchase of the shares  (akcii)
"""
Sum in $:
- покупки акций
- продажи акций
- комиссии покупки
- комиссии продажи
- прибыли / убытка ( + or - )
"""

# shares
purchase_shares = 2000
joe_shares = 0
sale_shares = 2000
# one shares
purchase_rat = 40
sale_rat = 42.75
# broker's
purchase_comission_percent = 0.03
sale_comission_percent = 0.03

days = 14

# Money shares
purchase_money = purchase_shares * purchase_rat
sale_money = sale_shares * sale_rat
# Comission
purchase_comission_money = purchase_money * purchase_comission_percent
sale_comission_money = sale_money * sale_comission_percent
# Profit
profit = (-purchase_money - purchase_comission_money) + (sale_money - sale_comission_money)
#sale_comission_money - purchase_comission_money

print("The program evaluates the gains and losses of financial transactions.\n")
print(f"The price for the purchase of shares = {purchase_money:,.2f}$")
print(f"The price for the sale of shares = {sale_money:,.2f}$")
print(f"The price of the commission for the purchase = {purchase_comission_money:,.2f}$")
print(f"The price of the commission for the sale = {sale_comission_money:,.2f}$")

if profit > 0:
    print(f"Arrive made profit up  = {profit:,.2f}$")
elif profit < 0:
    print(f"The loss amounted to = {profit:,.2f}$")
else:
    print(f"The transaction brought neither profit nor loss = {int(profit)}$")









   
