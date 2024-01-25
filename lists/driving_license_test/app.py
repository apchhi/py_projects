def main():
    COUNT_ANSWERS=20
    START=0
    COUNT_STEP=1
    PASSING_SCORE = 15
    FILE_STUDENT_ANSWERS = 'student_answer.txt'
    FILE_TEST_ANSWERS = 'test_answers.txt'
    FILE_QUESTIONS = 'questions.txt'
    list_questions = reading_file(FILE_QUESTIONS,START,COUNT_STEP)
    get_answer_user(FILE_QUESTIONS,COUNT_ANSWERS)
    list_get = reading_file(FILE_STUDENT_ANSWERS,START,COUNT_STEP)
    list_test = reading_file(FILE_TEST_ANSWERS,START,COUNT_STEP)
    comparison_answers(list_get,list_test,COUNT_ANSWERS,START,COUNT_STEP,PASSING_SCORE)

def get_answer_user(questions,count):
    infile = open('student_answers.txt','w')
    print('Enter your answers to questions(A-D)')
    for i in range(count):
        question = questions[i].rstrip('\n')
        answer = input(f'{question}: ')
        answer = correct_answer(answer,i)
        infile.write(f'{answer}\n')
        infile.close()

def reading_file(file_name,index,step):
    infile = open(file_name,'r')
    answers = infile.readlines()
    infile.close()
    while index<len(answers):
        answers[index] = answers[index].rstrip('\n')
        index+=step
        return answers

def comparison_answers(get_user,list_test,count,start,step,passing_score):
    true_answers = start
    false_answers = start
    numbers_false_answers = []
    for i in range(count):
        if get_user[i] == list_test[i]:
            true_answers += step
        else:
            false_answers += step
            numbers_false_answers.append(i+1)
            if true_answers >= passing_score:
                print('The student passed the exam.')
            else:
                print('The student failed the exam.')
                print(f'Numbers of correct answers = {true_answers}')
                print(f'Numbers of incorrect answers = {false_answers}')
                print('Numbers of questions whose answers were incorrect: ', end=' ')
                for number in numbers_false_answers:
                    print(number, end=' ')
                    print()


def correct_answer(answer,i):
    flag = False
    while flag == False:
        if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
            flag = True
        else:
            flag = False
            answer = input(f'Your answer is not correct. Repeat enter {i+1} question(A-D): ')
            return answer


main()
