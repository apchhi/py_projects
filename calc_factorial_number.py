# # Calculating the factorial of a number

print("This program - Calculating the factorial of a number.")
print("Please enter a non-negative integer:")
number = int(input())
factorial = 1

for count in range(number):
    factorial *= count + 1

print(f"{number}! = {factorial}")
