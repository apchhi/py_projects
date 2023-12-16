def main():
	sales_file = open('sales.txt', 'r')
	line = sales_file.readline()
	all_sum = 0
	
	while line != '':
		all_sum += float(line)
		line = sales_file.readline()
		
	print(f'All sum sales = {line:.2f}$')	
	sales_file.close()
	print('Operation sucseccful.')

#if __name__ == '__main':
main()
	