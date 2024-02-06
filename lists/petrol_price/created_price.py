# price for petrol in 1994 for each week
import random
WEEKS = 48      #in year

def main():
    infile = open('1994_Weekly_Gas_Averages.txt', 'w')
    for price in range(WEEKS):
        price = random.uniform(0.52, 1.37)  # U.S. Dollar
        infile.write(str(price) + '\n')
    infile.close()
    print('Successfully')
main()
