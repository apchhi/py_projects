def main():
	emp_file = open('employees.txt', 'r')
	name = emp_file.readline()
	count = 1
	
	while name != '':
		id_num = emp_file.readline()
		dept = emp_file.readline()
		
		name = name.rstrip('\n')
		id_num = id_num.rstrip('\n')
		dept = dept.rstrip('\n')
		
		print(f'The employees N{count}')
		print(f'Name: {name}')
		print(f'ID: {id_num}')
		print(f'Department: {dept}')
			
		print()
		
		name = emp_file.readline()
		count += 1
		
	emp_file.close()
	print('Reading from employess.txt')
	
main()