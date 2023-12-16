# reading points gamer
def main():
	count = 0
	infile = open('golf.txt', 'r')
	name = infile.readline()
	name = name.rstrip()
	print('Players:')
	while name != '':
		count += 1
		points = infile.readline()
		points = points.rstrip('\n')
		print(f'{count}. {name}, points: {points}.')
		name = infile.readline()
		name = name.rstrip()
		
	infile.close()
	print()
	print('File "golf.txt" closed.')
	
#if __name__ == "__main__":
main()