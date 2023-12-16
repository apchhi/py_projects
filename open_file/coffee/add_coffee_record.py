# # this program adds entries for coffee shops

def main():
	answer_user = 'y'

	coffee_file = open('coffee.txt', 'a')
	
	while answer_user == 'y' or answer_user == 'Y':
		print('Enter next date about a coffee')
		name = input('Enter coffee name: ')
		count = float(input(f'Enter count {name} coffee in pounts(kg): '))
		
		coffee_file.write(f'{name}\n')
		coffee_file.write(f'{count:.3f}\n')
		
		answer_user = input('Do you want add another entry(y / n)? ')
		
	coffee_file.close()
	print('Date entry in file coffee.txt')
	
#if __name__ == '__main__':
main()