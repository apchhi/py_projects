# reading numbers from file "rand_numbers.txt", outputting their number and sum
def main():
	infile = open('rand_numbers.txt', 'r')
	count = 0
	total_num = 0
	for number in infile:
		number = float(number.rstrip('\n'))
		count += 1
		total_num += number
		
	infile.close()
	print('File "rand_numbers.txt" closed.')
	print()
	print(f'Sum is random numbers in file "rand_numbers.txt" = {total_num}.')
	print(f'Count numbers = {count}.')
	
main()