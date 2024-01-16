## speed normal or danger
speed = int(input('Enter speed your a car: '))
if speed >= 24 and speed <= 56:
    print('Speed is normal')
elif speed < 24:
    print('Speed is small')
else:
    print('Speed is danger')
