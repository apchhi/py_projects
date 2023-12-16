# deleted record a stydent's
import os

def main():
	found = False
	search = input('Enter name of stydent: ')	# John Perc

	stydents = open('stydents.txt', 'r')
	temp_file = open('temp.txt', 'w')
	descr = stydents.readline()
	
	while descr != '':
		qty = int(stydents.readline())
		descr = descr.rstrip('\n')
		if search != descr:
			temp_file.write(f'{descr}\n')
			temp_file.write(f'{qty}\n')
		else:
			found = True
		descr = stydents.readline()
		
	stydents.close()
	temp_file.close()
	os.remove('stydents.txt')
	os.rename('temp.txt', 'stydents.txt')
	
	if found:
		print(f'{search} record has been deleted.')
	else:
		print(f'{search} record not found.')
	
#if __name__ == "__main__":
main()