# # calculation of payments to sellers

#commission_rate_list = (10, 12, 14, 16, 18)
commission_rate_list = {
  10: (0, 9999), 
  12: (10000, 14999), 
  14: (15000, 17999), 
  16: (18000, 21999), 
  18: (22000, 100000)
  }

#payments = []

def main():
  print("Hello! This is program - calculation of payments to sellers. Enter your values and set the result.")
  payments = payment_calculation()
  if payments < 0:
    print(f"You must reimburse the company {abs(payments):.2f}$")
  else:
    print(f"Your payout = {payments:.2f}$")
  
def payment_calculation():
  sales_amount = get_sales_amount()
  prepaid_expense = get_prepaid_expense()
  commission_rate = calculate_commission_rate(sales_amount) / 100
  return (sales_amount * commission_rate - prepaid_expense)
  
def get_sales_amount():
  print("Enter the seller's monthly sales amount in dollars:")
  return float(input())
  
def get_prepaid_expense():
  print("Enter the seller's monthly prepaid expense in dollars from 0$ to 2000$:")
  expense = float(input())
  while expense < 0 or expense > 2000:
    print("Reload your enter from 0$ to 2000$ !!!")
    expense = float(input())
  return expense

def calculate_commission_rate(sales):
  for key, value in commission_rate_list.items():
    if sales >= value[0] and sales <=value[1]:
      for key_list in commission_rate_list.keys():
        if commission_rate_list[key_list] == value:
          return key_list

'''
def calculate_commission_rate(sales_amount):
  # < 9 999
  if (sales_amount < commission_rate_list[10]):
    return list(commission_rate_list.keys())[0]
  # >10000  & <14999
  elif (sales_amount >= commission_rate_list[12][0]) and (sales_amount <= commission_rate_list[12][1]):
    return list(commission_rate_list.keys())[1]
  # >15000 & <17999
  elif (sales_amount >= commission_rate_list[14][0]) and (sales_amount <= commission_rate_list[14][1]):
    return list(commission_rate_list.keys())[2]
  # >18000 & <21999
  elif (sales_amount >=commission_rate_list[16][0]) and (sales_amount <= commission_rate_list[16][1]):
    return list(commission_rate_list.keys())[3]
  # >22000
  elif (sales_amount > commission_rate_list[18]):
    return list(commission_rate_list.keys())[4]
'''

main()
