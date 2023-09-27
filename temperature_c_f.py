# #  temperature C -> F
# fahrenheit
# celsius

temp_list = []
print("Temperature to table conversion program.")
get_temp_min = int(input("Enter minimum temperature: "))
get_temp_max = int(input("Enter maximum of temperature: "))

for temp in range(get_temp_min, get_temp_max):
  celsius = int(temp + 1)
  fahrenheit = float(9 / 5 * celsius + 32)
  temp_list.append((celsius, fahrenheit))
print("  Celsius", "\t\t", "Fahrenheit")

for count in range(get_temp_min, get_temp_max):
  print("--------------------------------------------------")  
  print(f"\t {temp_list[count][0]}\t\t || \t\t{temp_list[count][1]:.1f}\t")

# fahrenheit temperature
#f = float(9 / 5 * c + 32)