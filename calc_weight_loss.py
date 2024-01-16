# # weight loss

#calories
print("The program calculates body weight during weight loss.")
print("You need to cut your calorie intake by 500.")
weight = float(input("Enter your weight(kg): "))

period = 6      #month
loss_month = 1.5        #kg / month

print("Year \t\t Weight")
print("---------------------------------")
for month in range(period):
    weight -= loss_month
    print("{} \t\t {:.1f}".format(month+1, weight))
