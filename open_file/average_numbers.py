# average and except 
def main():
	total = 0
	count_line = 0
	try:
		infile = open('numbers.txt', 'r')
		for line in infile:
			line = float(line.rstrip('\n'))
			print(line)
			total += line
			count_line += 1
		average = total / count_line
	
		infile.close()
		print('File "numbers.txt" close.')
		print()
		print(f'Average = {average:,.2f}')
	except IOError:
		print('Error reading file.')
	except ValueError:
		print('Error converted a value in number.')
	except:
		print('An error has occurred.')
	
main()