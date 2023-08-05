## Compound percent at a rate 

# a - все деньги на счете после t лет
# p - певоначальный вклад 
# r - процентная ставка в год 
# n - частота начисления процентного дохода в год
# t - польное количество лет 

# показать сумму на счете после заданного количества лет

print("The program for calculating the receipt of income from the contribution. Enter data to calculate your income.\n")
P = float(input("Initial deposit amount: "))
r = float(input("Percent rate per year: "))
n = float(input('Frequency accrual of percent of income per year. \nEnter "1" if monthly or "2" if quarterly interest: '))
while n != 1 and n != 2:
    n = int(input("The value is not corrected. Repeat on more time: "))
t = float(input("Number of years to deposit: "))

r /= 100

if n == 1:
    n = 1 / 12
elif n == 2:
    n = 4

A = P * (1 + r/n) ** (n*t)
# p * (int(1 + r / n) ^ int(n * t))

print(f"Total on the account for all {t} years will be the amount of {A:,.2f}$")




