## correct mystics of wifi

print('Программа для исправления ошибок при прдключении к маршрутизатору wi-fi.\n')
#print('Перезагрузите компьютер и попробуйте подключиться.')
#ansver = input('Не работает подключение к маршрутизатору и Вам нужна помощь?: ')

list_question = [
        'Перезагрузите ПК и попробуйте подключиться.',
        'Перезагрузите маршрутизатор и попробуйте подключиться.',
        'Убедитесь, что кабель между маршрутизатором и ПК почно присоединены.',
        'Переместите маршрутизатор на новое место.',
        ]

for i in list_question:
    print(i)
    ansver = input('Вы исправили проблемму? (Да/Yes): ')
    if ansver == 'Да' or ansver == 'Yes':
        print('Проблема решена. Спасибо за обращение.')
        break
    else:
        print('Купите новый маршрутизатор. \nВсего доброго!')

#        ansver = input('Вы исправили проблемму?: ')
#        print(i)

#    print('Спасибо за обращение. Всего добрго!')
#    break


