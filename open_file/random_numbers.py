# range from 1 to 500
import random

def main():
	count_num = int(input('Enter the count of random numbers: '))
	infile = open('rand_numbers.txt', 'w')
	for i in range(count_num):
		number = random.randint(1, 501)
		infile.write(f'{number}\n')
		
	infile.close()
	print('File "rand_numbers.txt" successfully created.')
	
#if __name__ == "__main__":
main()