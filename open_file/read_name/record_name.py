def main():
	name = input('Enter name: ')
	infile = open('my_name.txt', 'a')
	infile.write(f'{name}\n')
	infile.close()
	print('Recording in file "my_name.txt".')
#if __name__ == '__main__':
main()