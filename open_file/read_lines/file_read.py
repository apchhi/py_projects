def main():
	inline = open('data.txt', 'r')
	line = inline.readline()
	line = line.rstrip('\n')
	
	while line != '':
		
		print(line)
		line = inline.readline()
		line = line.rstrip('\n') 
	
	inline.close()
	print('Operation sucseccful.')

#if __name__ == '__main':
main()
	