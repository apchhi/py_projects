## info about studies courses
def main():
    courses_number = []
    answer = 'y'
    while answer.lower() == 'y':
        input_user = input('Enter number a course: ')
        courses_number.append(input_user)
        answer = input('Want to add another course? (y/n): ')
    audiences_numb = input_audiens_numb(courses_number)
    teachers = input_teacher(courses_number)
    dates = input_date(courses_number)
    
    print('Number course  :  number audience')
    print(audiences_numb)
    print()

    print('Number course  :  teacher')
    print(teachers)
    print()


    print('Number course  :  time')
    print(dates)
    print()

def input_audiens_numb(courses_number):
    audiences_number = dict()
    for course in courses_number:
        print('Enter the number audience of the course ')
        audience = input(f'N{course}: ')
        audiences_number[course] = audience
    return audiences_number

def input_teacher(courses_number):
    teachers = dict()
    for course in courses_number:
        print('Enter the name a teacher of the course ')
        teacher = input(f'N{course}: ')
        teachers[course] = teacher
    return teachers

def input_date(courses_number):
    dates = dict()
    for course in courses_number:
        print('Enter the time of the course(00:00) ')
        date = input(f'N{course}: ')
        dates[course] = date
    return dates

if __name__ in "__main__":
    main()




