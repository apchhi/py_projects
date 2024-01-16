# # reproduction of a population of organisms
print("Enter the starting number of organisms:")
number = int(input())
print("Enter the average daily population increase(percente):")
percente = int(input()) / 100
print("Enter the number of days for breeding:")
days = int(input())

count_population= 0

print("Day \t\t Population")
print("---------------------------------")
for count in range(days):
    number_day = number + (number * percente)
    count_population += (number_day)
    print("{} \t\t\t {:.0f}".format(count+1, count_population))

 #print(number, percente, days)
