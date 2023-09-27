## area of rectangles

print('This prog output area of larger a rectangle. (cm)')
length_one = float(input('Enter length a FIRST rectangle: ')) 
width_one = float(input('Enter wigth a FIRST rectangle: '))
length_two = float(input('Enter length a SECOND rectangle: ')) 
width_two = float(input('Enter wigth a SECOND rectangle: '))

area_one = length_one * width_one
area_two = length_two * width_two

if area_one > area_two:
    print(f'the area of the first rectangle is greater than the area of the second rectangle and = {area_one} cm')
elif area_one < area_two:
    print(f'the area of the second rectangle is greater than the area of the first rectangle and = {area_two} cm')
elif area_one == area_two:
    print(f'the area of the first rectangle are equal the area of the second rectangle and = {area_one} cm')
else:
    print('Error. Try entering again.')








