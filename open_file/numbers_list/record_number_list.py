# created secuences from 1 to 100
def main():
	infile = open('number_list.txt', 'w')
	for count in range(1, 101):
		infile.write(f'{count}\n')
	infile.close()
	print()
	print('Numbers recorded.')
#if __name__ == '__main__':
main()