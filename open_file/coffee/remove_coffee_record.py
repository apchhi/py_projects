# remove records in data coffee
import os
def main():
	found = False
	search = input('Do you want to deleted of brand? ')
	coffee_file = open('coffee.txt', 'r')
	temp_file = open('temp.txt', 'w')
	descr = coffee_file.readline()
	while descr != '':
		qty = float(coffee_file.readline())
		descr = descr.rstrip('\n')
		if descr != search:
			temp_file.write(f'{descr}\n')
			temp_file.write(f'{qty}\n')
		else:
			found = True
					
		descr = coffee_file.readline()
		
	coffee_file.close()
	temp_file.close()
	os.remove('coffee.txt')
	os.rename('temp.txt', 'coffee.txt')
	if found:
		print('Record deleted.')
	else:
		print('This record in file "coffee.txt" is not found.')		
		
#if __name__ = '__main__':
main()
	