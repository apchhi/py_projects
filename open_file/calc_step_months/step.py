# #
'''
Среднее количество шагов. 
Браслет для занятий спортом —  это носимое устройство, которое отслеживает вашу физическую активность, количество сожженных калорий, сердечный ритм, модели сна и т. д. Одним из самых распространенных видов физиче­ ский активности, который отслеживает большинство таких устройств, является количество шагов, которые вы делаете каждый день. Среди исходного кода файл steps.txt. Этот файл содержит количество шагов, которые человек делал каждый день в течение года. В файле 365 строк, и каждая строка содержит количество шагов, сделанных в течение дня. (Первая строка —  это число шагов, сделанных 1 января, вторая строка —  число шагов, сделанных 2 января, и т. д. Напишите программу, которая читает файл и затем выводит среднее количество шагов, сделанных в течение каждого месяца. (Данные были записаны в год, который не был високосным, и поэтому февраль имеет 28 дней.
'''

def main():
    months = 12
    list_days_months = {
        'january' : 31,
        'february' : 28,
        'march' : 31,
        'april' : 30,
        'may' : 31,
        'june' : 30,
        'july' : 31,
        'august' : 31,
        'september' : 30,
        'october' : 31,
        'november' : 30,
        'december' : 31,
    }

    outfile = open('step.txt', 'r')
    
    for month, days in list_days_months.items():
        calc = 0
        print()
        print('--------------------------')
        print(f'Month: {month}\n')
        print('--------------------------')
        print('Days    |    Steps')
        print()
        
        for count in range(days):
            step = int(outfile.readline())
            print(f' {count+1}           {step}')
            calc += step
        print()
        average = int(calc / days)
        print(f'Average steps in {month} = {average};')
        print()
        
        
main()
    
