## time calculate
#one variant

import datetime

print('The program calculates days, hours, minutes and seconds from the seconds it receives.\n')
seconds = int(input("Enter number of seconds: "))

time_delta = datetime.timedelta(seconds=seconds)
formatted_time = str(time_delta)

print(f"Time: {formatted_time}")


"""
#two variant

seconds = int(input('Please enter the number of seconds you need to count: '))

if seconds >= 86400:    # days
    days = seconds // 86400
    seconds %= 86400
else:
    days = 0

if seconds >= 3600:   # hours
    hours = seconds // 3600
    seconds %= 3600
else:
    hours = 0

if seconds >= 60:   # minutes
    minutes = seconds // 60
    seconds %= 60
else:
    minutes =0

print(f'In seconds received by the program {days} day : {hours} hour : {minutes} minute : {seconds} second')
"""




