# # search need data 
def main():
	found = False
	search = input('Enter name of coffee: ')
	
	coffee_file = open('coffee.txt', 'r')
	
	descr = coffee_file.readline()
	
	while descr != '':
		qty = float(coffee_file.readline())
		descr = descr.rstrip('\n')
		
		if descr == search:
		 	print('Found sucсessful')
		 	print(f'Description: {descr}, count: {qty:.3f}kg')
		 	found = True
		
		descr = coffee_file.readline()
		 	 	
	coffee_file.close()
		 
	if not found:
		 	print('Found not successful')
		 	print('Searching value not found!')
		 
#if __name__ == '__main__':
main()	
		 	 	
		 	 	 	 	