def main():
    FIRST_LIST_YEAR = 1950
    LAST_LIST_YEAR = 1990
    YEARS_FILE = 'population_database.txt'
    population_list = read_file(YEARS_FILE, FIRST_LIST_YEAR, LAST_LIST_YEAR)
    print('Average annual population change during the period ')
    get_start_period, get_end_period = check_correct_enter_value(population_list)
    change_population, min_population_year, max_population_year = calc_population_period(get_start_period, get_end_period, population_list)
    print()
    print(change_population)
    print()
    print(max_population_year)
    print()
    print(min_population_year)
    
def read_file(file_name, first_year, last_year):
    infile = open(file_name, 'r')
    years = infile.readlines()
    infile.close()
    new_years = {}
    for key, num in enumerate(years, start=first_year):
        new_num = int(num.rstrip('\n'))
        new_years[key] = new_num 
    return new_years

def calc_population_period(start_period, end_period, population):
    start_persons = population[start_period]    # 173 999 222
    end_persons = population[end_period]    # 197 343 753
    years_difference = (end_period - start_period)  # 10
    
    persons_difference = end_persons - start_persons
    average_population = int(persons_difference / years_difference)
    average_annual_population_change = out_average(start_period,end_period,persons_difference,average_population,)
    year_min_population, year_max_population = out_max_population(start_period,end_period,population)
    return average_annual_population_change, year_min_population, year_max_population

def out_average(start_period,end_period,persons_difference,average_population):
    answer = (f'Population from {start_period} to {end_period} years')    
    average_answer = ('\nAverage annual population change for period')
    if persons_difference > 0:
        answer += (f' increased in {persons_difference:,} persons.') + average_answer + (f' {average_population:,} persons in year.')
    elif persons_difference < 0:
        answer += (f' decreased in {persons_difference:,} persons.') + average_answer + (f' {average_population:,} persons in year.')
    elif persons_difference == 0:
        answer += (f' not changed.')
    return answer

def out_max_population(start_period,end_period,population):
    #max_year = start_period
    max_persons_year = (start_period, population[start_period])
    min_persons_year = (start_period, population[start_period])
    for index in range(start_period, end_period+1):
        persons = population[index]
        if population[index] > max_persons_year[1]:
            max_persons_year = (index, population[index])
        elif population[index] < min_persons_year[1]:
            min_persons_year = (index, population[index])
    max = (f"Year with maximum population in period form {start_period} to {end_period} years it's {max_persons_year[0]} with the population = {max_persons_year[1]:,} persons.")
    min = (f"Year with minimum population in period form {start_period} to {end_period} years it's {min_persons_year[0]} with the population = {min_persons_year[1]:,} persons.")
    return min, max

def check_correct_enter_value(population):
    while True:
        start_period = input('Enter the starting year: ')
        end_period = input('Enter the ending year: ')
        try:
            start_period = int(start_period)
            end_period = int(end_period)
            population[start_period]
            population[end_period]
            return start_period, end_period
        except KeyError:
            print("Error. Enter value it's not hawe in database. Try again. ", end=' ')
        except ValueError:
            print('Error. Enter value is not correct. Try again. ', end=' ')


if __name__ == "__main__":
    main()

