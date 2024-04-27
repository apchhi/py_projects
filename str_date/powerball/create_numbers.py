## create file with numbers
import random

def main():
    infile = open('pbnumbers.txt', 'w')
    count = 0
    number = ''
    while count < 654:
        for index in range(6):
            if index == 5:
                number += (str(random.randint(1,26+1)) + '\n')
            else:
                number += str(random.randint(1, 69+1)) + ' '
        infile.write(number)
        count += 1
    infile.close()
    
main()



