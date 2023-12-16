# add player in "golf.txt"
import os

def main():
	found = False
	get_name = input('Enter name a player for found: ')
	get_points = int(input('Enter new points a player: '))
	infile = open('golf.txt', 'r')
	temp_file = open('temp.txt', 'w')
	line_name = infile.readline()
	line_name = line_name.rstrip('\n')
	while line_name != '':
		line_points = infile.readline()
		line_points = line_points.rstrip('\n')
		if get_name != line_name:
			temp_file.write(f'{line_name}\n')
			temp_file.write(f'{line_points}\n')
		else:
			temp_file.write(f'{get_name}\n')
			temp_file.write(f'{get_points}\n')
			found = True
			
	if found:
		print(f'Player {get_name} points correct.')
	else:
		print('Player {get_name} not found.')
		answer_user = input('You have create new players(Y/N): ')
		while answer_user != 'Y' or answer_user != 'N':
			answer_user = input('Enter value is not correct. Enter "Y" - yes, or "N" - no, to create or not a user: ')
		if answer_user == 'Y':
			temp_file.write(f'{get_name}\n')
			temp_file.write(f'{get_points}\n')
			print('New player is created.')
		elif answer_user == 'N':
			print('New user has not been created.')
	
	infile.close()
	temp_file.close()
	os.remove('golf.txt')
	os.rename('temp.txt', 'golf.txt')
	print('Exit the program.')
	
#if __name__ == '__main__':
main()