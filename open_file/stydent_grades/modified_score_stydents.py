# modified a stydent's score
import os
def main():
	found = False
	search = input('Enter name of stydent: ')
	new_score = int(input('Enter new score a stydent: '))
	stydents_file = open('stydents.txt', 'r')
	temp_file = open('temp.txt', 'w')
	desc = stydents_file.readline()
	
	while desc != '':
		qty = stydents_file.readline()
		desc = desc.rstrip('\n')
		if search != desc:
			temp_file.write(f'{desc}\n')
			temp_file.write(qty)
		else:
			temp_file.write(f'{desc}\n')
			temp_file.write(f'{new_score}\n')
			found = True
			
	stydent_file.close()
	temp_file.close()
	os.remove('stydents.txt')
	os.rename('temp.txt', 'stydents.txt')
	
	if found:
		print('Record successfully modified.')
	else:
		print('Record not modided.')
	
#if __name__ == "__main__":
main()