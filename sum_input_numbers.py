# # the program calculates the sum of the entered positive numbers
print("Enter a series of positive numbers and one negative \nto complete the series and further calculation by the program:")

get_number = float(input())
sum_number = 0

while get_number > 0:
  sum_number += get_number
  get_number = float(input())
  
print("Sum input numbers =", sum_number)
 
 
 
 
 
 