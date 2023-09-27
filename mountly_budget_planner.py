# # monthly budget planner

sum_expense = 0
name_items = []
expense_sums = []

print("Monthly expense calculator.")

answer = input("Enter answer (yes / no) if you want or no calculate of monthly budget planner: ")

if answer == "yes":
  budget = float(input("Enter your monthly budget: "))
  
while answer != "no":
  item = input("Enter the name of the expense item: ")
  amount_expense = float(input("Enter the amount of the expense: "))
  name_items.append(item)
  expense_sums.append(amount_expense)
  
  sum_expense += amount_expense
  answer = input("Enter answer (yes / no) if you want repeat enter yor expense: ")
  
total = budget - sum_expense


if total < 0:
  print("Your expenses will exceed the budget =", total)
else:
  print("The balance of all expenses will be =", total)
  





