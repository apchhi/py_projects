def main():
	num_emp = int(input('How many employee records do you want to create? '))
	emp_file = open('employees.txt', 'w')
	
	for count in range(1, num_emp+1):
		print(f'Enter date about the employee N {count}')
		name = input('Name: ')
		id_num = input('ID: ')
		dept = input('Department: ')
		
		emp_file.write(f'{name}\n')
		emp_file.write(f'{id_num}\n')
		emp_file.write(f'{dept}\n')
		
		print()
		
	emp_file.close()
	print('Recorded in employess.txt')
	
main()