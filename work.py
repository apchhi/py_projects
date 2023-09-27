num = float(input("Enter randon number: "))
product = num

while product < 100:
  product = num * 10
  print("product = ", product)
  num = float(input("Repeat enter random number: "))
  
print("product > 100. Exit!")