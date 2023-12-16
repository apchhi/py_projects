# # read all duration clip in file
def main():
	total_duration = 0
	count = 1
	
	duration = open('clips.txt', 'r')
	
	for line in duration:
		amount = float(line)
		print(f'{count} clip duration = {amount:.2f} sec')
		total_duration += amount
		count += 1
	
	duration.close()	
	print('Operation sucessfull')
	
	print(f'All duration clips = {total_duration:.2f} sec')
	
main()