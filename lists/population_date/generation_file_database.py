import random
START_YEAR = 1950
END_YEAR = 1990
POPULATION_GROWTH_START = 148281550 #next year = 150598452
#POPULATION_GROWTH_END = 248083732
RANDOM_POPULATION_GROWTH_START = 2000000
RANDOM_POPULATION_GROWTH_END = 2800000

def main():
    infile = open('population_database.txt', 'w')
    pop_year = POPULATION_GROWTH_START
    for _ in range(START_YEAR, END_YEAR+1):
        pop_growth_year = random.randint(RANDOM_POPULATION_GROWTH_START, RANDOM_POPULATION_GROWTH_END)
        pop_year += pop_growth_year
        infile.write(str(pop_year) + '\n')

main()



