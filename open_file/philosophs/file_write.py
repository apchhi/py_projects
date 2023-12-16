def main():
	print('Enter name in tree friends.')
	name1 = input('Name # 1: ')
	name2 = input('Name # 2: ')
	name3 = input('Name # 3: ')

	outfile = open('friends.txt', 'w')

	outfile.write(name1 + '\n')
	outfile.write(name2 + '\n')
	outfile.write(name3 + '\n')

	outfile.close()
	print('Operation sucsessfull.')

#if __name__ == '__main':
main()
	