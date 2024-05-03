## creates a file with gasoline prices
import random
days_months = {'january': 31, 'february': 28, 'march': 31, 'april' : 30, 'may': 31, 'june': 30, 'jule': 31, 'august': 31, 'september': 30, 'october': 31, 'nowember': 30, 'december': 31}
start_year = 1993
end_year = 2013

def main(months, start_year, end_year):
    infile = open('prices.txt', 'w')
    for year in range(start_year, end_year+1):
        for month in months:
            for day in range(months[month]):
                #date = ()
                price = random.uniform(1, 2)
                infile.write(f'{day+1}-{month}-{year}:{price:.3f}\n')
    infile.close()


main(days_months, start_year, end_year)


