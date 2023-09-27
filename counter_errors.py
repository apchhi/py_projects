# # counter of mistake
days = int(input("Enter the number of days all: "))
count = 0

print("The program for calculating the sum of the number of errors for a user-specified period of time.")

for i in range(days):
  mistake = int(input(f"Enter the number of errors per {i+1} day: "))
  count += mistake

print(f"All the number of errors per {days} days = {count}")