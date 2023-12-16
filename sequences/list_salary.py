# # list salary
NUM_EMPLOYEES=6
list_salary = [0] * NUM_EMPLOYEES
list_time = [0] * NUM_EMPLOYEES
pay_rat = int(input('Enter salary in hour($): '))
for emp in range(NUM_EMPLOYEES):
    time=float(input(f"Enter time employee {emp+1}: "))
    list_time[emp]=time
    salary=pay_rat*time
    list_salary[emp]=salary

print('$:', list_salary)
print('time:', list_time)
