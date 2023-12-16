# integet numbers
def main():
	name_file = input('Enter name file: ')	# numbers.txt
	infile = open(name_file, 'r')
	
	#for count, line in enumerate(infile):
	for count in range(5):
		line = infile.readline()
		if line != '':
			line = line.rstrip('\n')
			print(f'{count+1}: {line}')
			
	infile.close()
	print()
	print('File "numbers.txt" close.')

main()
