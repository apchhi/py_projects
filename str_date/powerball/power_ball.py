## game PowerBall
import random

SIMPLY_NUM_RANGE = [1,69]
POWER_BALL_NUM_RANGE = [1,26]
COUNT_СYCLE = 6

def main():
    powerball_sum = 600000
    other_sum = 400000
    gen_nums_str = generator_numbers() 
    user_nums_str = get_user_num().split()
    print(result(powerball_sum, other_sum, gen_nums_str, user_nums_str))

def result(powerball_sum, other_sum, gen_nums_str, user_nums_str):
    power_ball_flag = False
    counter = 0
    answer = ''
    for count in range(len(gen_nums_str)):
        try:
            if gen_nums_str[count] == gen_nums_str[-1]:
                gen_nums_str.index(int(user_nums_str[count]))
                power_ball_flag = True
            else:
                gen_nums_str.index(int(user_nums_str[count]))
                counter += 1
        except ValueError:
            pass
    if counter == 5 and power_ball_flag:
        winning_sum = other_sum + powerball_sum
        answer += ('Bingo! PowerBall!')
    else:
        winning_sum = other_sum / (len(gen_nums_str)-1) * counter
    answer += (f'Your winning amount = {winning_sum:.2f}$')
    return answer


def generator_numbers():
    return random.sample(range(SIMPLY_NUM_RANGE[0], SIMPLY_NUM_RANGE[1]+1), COUNT_СYCLE)
    

def get_user_num():
    user_nums = ''
    print('Enter 5 random numbers from 1 to 69')
    for count in range(COUNT_СYCLE-1):
        user_nums += str(input(f'{count+1} number: ')) + ' '
    user_power_ball_num = str(input('Enter num PowerBall form 1 to 26: '))
    user_nums += user_power_ball_num
    return user_nums

main()
