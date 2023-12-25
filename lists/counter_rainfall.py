'''
Статистика дождевых осадков. Разработайте программу, которая позволяет пользователю занести в список общее количество дождевых осадков за каждый из 12 месяцев. Программа должна вычислить и показать суммарное количество дождевых осадков за год, среднее ежемесячное количество дождевых осадков и месяцы с самым высоким и самым низким количеством дождевых осадков.
'''
def main():
    YEAR = 12   # months
    rainfall = [
        ['January'],
        ['February'],
        ['March'],
        ['April'],
        ['May'],
        ['June'],
        ['July'],
        ['August'],
        ['September'],
        ['October'],
        ['November'],
        ['December']]
    
    print('Enter rainfall for ...')
    for month in range(len(rainfall)):
        rainfall[month].append(int(input(f'{rainfall[month]}: ')))
    #print(rainfall)
    months_numbers = (number for name, number in rainfall)
    list_months_numbers = list(months_numbers)
    sum_months = sum(list_months_numbers)
    average = sum_months / YEAR   #average quantity rainfall
    min_number = min(list_months_numbers)
    #min_month = [name for name, number in rainfall if number == min_number]
    max_number = max(list_months_numbers)
    #max_month = [name for name, number in rainfall if number == max_number]
    min_month, max_month = min_max_month(rainfall, min_number, max_number) 
    print(f'Sum months rainfall = {sum_months:,.1f} mm')
    print(f'Average quantity fainfall = {average:,.1f} mm')
    print(f'Min rainfall {min_month}({min_number:,.1f} mm)')
    print(f'Max rainfall {max_month}({max_number:,.1f} mm)')

def min_max_month(rainfall, min_number, max_number):
    for name, number in rainfall:
        if number == min_number:
            min_month = name
        if number == max_number:
            max_month = name
    return min_month, max_month
    
    
main()
