'''
Получить оценки студента. 
Вычислить сумму оценок.
Найти минимальную оценку. 
Вычесть минимальную оценку из суммы оценок. 
Это дает скорректированную сумму. 
Разделить скорректированную сумму на количество оценок минус 1. 
Это средняя оценка. 
Показать среднюю оценку.

'''

def main():
    scores = get_scores()
    total = get_total(scores)
    
    lowest = min(scores)
    total -= lowest

    #correct_sum = int(sum_values - min_value)
    #count_list_point = len(values_stydent) - 1
    average = total / (len(scores) - 1)         
    print('Average score = ', average)
    
def get_scores():
    list_scores = []
    again = 'y'
    while again == 'y':
        num = int(input('Enter point a stydent: '))
        list_scores.append(num)
        again = input('You want enter a next point? (y/n): ')
    return list_scores

def get_total(value_list):
    return sum(value_list)

main()
