# reading file number_list.txt
def main():
	total = 0
	infile = open('number_list.txt', 'r')
	for number in infile:
		number = int(number.rstrip('\n')) 
		print(number)
		total += number
	infile.close()
	print()
	print('Read file "number_list.txt" successfully.')
	print(f'Is sum all numbers = {total}')

#if __name__ == "__main__":
main()