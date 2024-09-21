from employee import Employee
## имя / id / отдел / должность
emp_list = [['Сьюзан Мейерс', 47899, 'Бухгалтерия', 'Вице-президент'], ['Марк Джоунс', 39119, 'IT', 'Программист'], ['Джой Роджерс', 81774, 'Производственнй', 'Инженер']]


def main():
    emp_objcts = list()
    for el in emp_list:
        emp_objcts.append(Employee(el[0], el[1], el[2], el[3]))
    
    print(emp_objcts)

    
    print('---------------------------------------------------')
    print('   ИМЯ      /   ID     /     ОТДЕЛ   /     ДОЛЖНОСТЬ')
    print('---------------------------------------------------')
    for el in emp_objcts:    
        #print(el)
        print(f'{el.get_name()} / {el.get_ident_num()} / {el.get_department()} / {el.get_position()}')
        print('---------------------------------------------------')

if __name__ == '__main__':
    main()
    
