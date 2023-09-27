# #average rainfall thickness

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_in_year = 12
rainfall_counter = 0
get_age = int(input("Enter number of years: "))
month_counter = 0

for age in range(get_age):
  for month in range(len(month_list)):
    rainfall = int(input(f"Enter rainfall for {month_list[month]} (mm): "))
    rainfall_counter += rainfall
    month_counter += 1 

average_rainfall_month = rainfall_counter / month_counter
  
print(f"Total month in {get_age} years = {month_counter}.")
print(f"Total rainfall for 3 years = {rainfall_counter} mm.")
print(f"The average rainfall over {get_age} year is {average_rainfall_month:.1f} mm per month.")