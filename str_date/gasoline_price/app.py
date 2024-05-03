## average prices per year
def main():
    prices = read_file()
    calc_price(prices)

def read_file():
    text_file = open('prices.txt', 'r')
    lines = text_file.readlines()
    text_file.close()
    for index in range(len(lines)):
        element_list = lines[index].split(':')
        element_list[0] = element_list[0].split('-')
        element_list[1] = float(element_list[1])
        lines[index] = element_list
    return lines       

def calc_price(prices):
    answer_years = [False, False, False]
    print('To calculate the average price from the specified year.')
    answer_period = int(input('Do you want to calculate for one year or a period years? (Write "1" for one / write "2" for period): '))
    if answer_period == 1:
        answer_years[0] = int(input(f'Enter year from {prices[0][0][2]} to {prices[-1][0][2]}: '))
        user_consent_month = input('Do you want to calculate the average price for a specific month ("y" or "n")? ')
        if user_consent_month == 'y':
            answer_years[2] = input('Enter month: ')
    else:
        answer_years[0] = int(input(f'Enter year from {prices[0][0][2]} to {prices[-1][0][2]}: '))
        answer_years[1] = int(input(f'Enter year from {answer_years[0]+1} to {prices[-1][0][2]}: '))
    slice_years = search_elements(answer_years, prices)
    calc_average_prices(slice_years)  #1 summ all elemenst slice

def search_elements(years, prices):
    slice_years = []
    if years[1]:
        slice_years = [item for item in prices if str(years[0]) <= item[0][2] <= str(years[1])]
    else:
        if years[2]:
            slice_years = [item for item in prices if str(years[0]) == item[0][2] and str(years[2]) == item[0][1]]
        else:
            slice_years = [item for item in prices if str(years[0]) == item[0][2]]
    return slice_years


def calc_average_prices(slice_years):
    print('\nPer period\n')
    #average
    prices_period = [price[1] for price in slice_years]
    average = sum(prices_period) / len(prices_period)
    print('Average price = {average:.2f}')
    print()

    #max price
    name_func = 'Max price'
    res_func_max = max(prices_period)
    print('Max price =', print_result_min_max(name_func, res_func_max, slice_years, prices_period))
    print()

    #min price
    name_func = 'Min price'
    res_funct_min = min(prices_period)
    print('Min price =', print_result_min_max(name_func, res_funct_min, slice_years, prices_period))
    print()

    #prices ascending
    ascending_sort = sorted(prices_period)
    print('Ascending price in period:')
    displaying_values(ascending_sort, prices_period, slice_years)
    
    #prices descending
    descending_sort = sorted(prices_period, reverse=True)
    print('Descending price in period:')
    displaying_values(descending_sort, prices_period, slice_years)


def displaying_values(sorted_list, prices, slice_years):
    list_values = [y for x in sorted_list if (y := order_value(x, prices, slice_years))]
    #print_asc_desc(list_ascending)
    for item in list_values:
        print(f'price: {item[1]} / date: {item[0][0]} {item[0][1]} {item[0][2]}')
    print()

def print_result_min_max(name_func, result, slice_years, prices):
    index_max_price = prices.index(result)
    return (f'{name_func} = {result} day: {slice_years[index_max_price][0][0]} month: {slice_years[index_max_price][0][1]} year: {slice_years[index_max_price][0][2]}')


def order_value(base_value, prices, slice_years):
    index_price = prices.index(base_value)
    return slice_years[index_price]



main()
