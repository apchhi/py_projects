# # write in file duration clips
def main():
	duration = open('clips.txt', 'w')
	
	count_clips = int(input('Enter count all clips: '))
	
	for count in range(1, count_clips+1):
		clip_duration = str(input(f'Enter clip {count} duration: '))
		duration.write(f'{clip_duration}\n')	
	
	duration.close()

main()