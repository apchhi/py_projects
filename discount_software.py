## sale of software
print('This program - discount on the number of program packages.\n')
quantity_packages = int(input('Enter the number of packages to be purchased: '))

sale_package = 99   #dollars
discount = 0

#discount - %
if quantity_packages >= 10 and quantity_packages <= 19:
    discount = 10
elif quantity_packages >= 20 and quantity_packages <= 49:
    discount = 20
if quantity_packages >= 50 and quantity_packages <= 99:
    discount = 30
if quantity_packages >= 100:
    discount = 40

discount_money = float(quantity_packages * sale_package / discount)
amount_due = float(quantity_packages * sale_package - discount_money)

print(f'Total discount amount = {discount_money:.2f}')
print(f'Total payable including discount = {amount_due:.2f}')








