# reading names in file 
def main():
	infile = open('my_name.txt', 'r')
	for line in infile:
		line = line.rstrip('\n')
		print(line)
	infile.close()
	print()
	print('All entries are read.')
#if __name__ == '__main__':
main()