def main():
	inline = open('data.txt', 'r')
	
	for line in inline:
		line = line.rstrip('\n')
		print(line)
		
	inline.close()
	print('Operation sucseccful.')

#if __name__ == '__main':
main()
	