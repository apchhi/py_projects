# # calorie calc on treadmill 
#number calories / one minute
minute_calories = 4.2
print("Treadmill Calorie Burn Calculator.")
answer = input('You want to count the number of calories? ')

while answer != 'no':
  time = int(input("Enter the number of minutes on the treadmill: "))  
  calories = time * minute_calories
  print(f"Summ calories = -{calories:.1f}")
  answer = input('You want to count the number of calories? ')
  
print("Program exit. Bye.")
