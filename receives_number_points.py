## This program receives a number of points from the user and shows the corresponding letter level of knowledge.

A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60


print("This this program receives a number of points from the user and shows the corresponding letter level of knowledge.\n")
score = int(input("Enter your a number of point from (1 - 100): "))
#years_job = float(input("Enter how many years have you been working: "))

if score >= A_SCORE:
    print("Your level is - A")
elif score >= B_SCORE:
    print("Your level is - B")
elif score >= C_SCORE:
    print("Your level is - C")
elif score >= D_SCORE:
    print("Your level is - D")
else:
    print("Your level is - F")


"""
if score >= A_SCORE:
    print("Your level is - A")
else:
    if score >= B_SCORE:
        print("Your level is - B")
    else:
        if score >= C_SCORE:
            print("Your level is - C")
        else:
            if score >= D_SCORE:
                print("Your level is - D")
            else:
                print("Your level is - F")
"""







