## Rising tuition fees

price_semester = 145000      # 1 student
percent = 0.03     #up price / 1 year
time = 5        #up price over all years
semesters_year = 2     # number semesters in 1 year
percent_year = 0        # count variable
price_year = price_semester * semesters_year


print('Year \t\t Price')
print('---------------------------')
for year in range(time):
    percent_year += percent
    price = price_year + (percent_year * price_year)
    print(f'{year+1} \t\t {price:.2f} rub')
