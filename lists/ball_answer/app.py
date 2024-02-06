import random

def main():
    infile = open('8_ball_responses.txt', 'r')
    responses = [item.rstrip('\n') for item in infile]
    infile.close()
    agreement = input('This is responses to the question. Do you want to ask a question? (yes / no): ')
    while agreement != 'no':
        input('Ask a simple question whose answer is "yes" or "no": ')
        print(f'{generator_response(responses)}')
        print()
        agreement = input('Do you want to ask another question? (yes / no): ')
    print('Bye!')

def generator_response(responses):
    index = random.randrange(0, len(responses))
    return responses[index]

main()

