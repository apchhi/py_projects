import random
years = 365
step_start = 580
step_end = 5000

def main():
    outfile = open('step.txt', 'w')
    for line in range(years):
        number_step = random.randint(step_start, step_end)
        outfile.write(f'{number_step}\n')
    outfile.close()

main()
    
