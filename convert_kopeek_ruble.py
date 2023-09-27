# # # # small money salary
#kopeyka / penny
#ruble
salary_list = []
#one ruble = kopeek
rubl = 60
kopeek = 0

days = int(input("Enter the number of days for which the salary will be issued: "))

for count in range(days):
  kopeek = (count + 1) * 2
  ruble = kopeek / 100
  salary_list.append(ruble)

# enter all salary  
print("DAYS\t\tSALARY")
print("--------------------------------")
for count in range(days):
  print(count+1, "\t\t\t", salary_list[count], "rub")
  
#print(salary_list)

