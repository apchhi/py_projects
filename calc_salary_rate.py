# salary calculating and rate

clock = None
EDGE_HOURS = 40
OT_MULTIPLIER = 1.5

print("This is the program for calculating the salary of an employee with overtime. \n")

hours_worked = int(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))


def base_payroll():
    salary = hours_worked * hourly_rate
    return salary

def rate_payroll():
    owertime_hours = hours_worked - EDGE_HOURS
    rate_salary = owertime_hours * hourly_rate * OT_MULTIPLIER
    salary = rate_salary + EDGE_HOURS * hourly_rate
    return salary    


if hours_worked > 40:
    print("Salary basic + rate = ", rate_payroll(), "$")

else:
    print("Basic salary = ", base_payroll(), "$")






