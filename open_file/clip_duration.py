def main():
	count_clips = int(input('Enter count all clips: '))
	
	duration = open('clips.txt', 'w')
	
	for count in range(1, count_clips+1):
		clip_duration = str(input(f'Enter clip {count} duration: '))
		duration.write(f'{clip_duration}\n')	
	
	duration.close()

main()