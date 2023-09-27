# # distance traveled by train


print("Distance traveled by train.")

#distance = speed * time

get_speed = float(input("What is the speed of the train?"))
get_time = float(input("How many hours did the trip take?"))

speed = get_speed
value = int(get_time)

print("Hours\tDistance")
print("------------------------------------")
for count in range(value):
  time = count + 1
  distance = int(speed * time)
  print(time, "\t\t", distance)