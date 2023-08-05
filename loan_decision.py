## Loan Decision Program

MIN_SALARY = 30000
MIN_JOB = 2

print("This is program loan decision. Pleas ...")
salary = float(input("Enter your salary in a one year: "))
years_job = float(input("Enter how many years have you been working: "))


## alternatuve variant
if salary >= MIN_SALARY and years_job >= MIN_JOB:
    print("Your loan is approved")
else:
    print("Your loan is not approved")


"""
if salary >= MIN_SALARY:
    if years_job >= MIN_JOB:
        print("Your loan is approved.")
    else:
        print(f"You must have worked for at least {MIN_JOB} years to be approved.")
else:
    print(f"You must earn at least ${MIN_SALARY:.2f} to be approved")
"""

