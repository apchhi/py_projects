# # For the teacher. Average student score
# get the number of students
num_student = int(input("How many students do you have?" ))
num_scores = int(input("How many grades per student?"))

# student GPA
for student in range(num_student):
  # grade accumulator
  total = 0.0
  # student number
  print(f"Student number ", student + 1)
  print("--------------------")
  # get grades for labs
  for test_num in range(num_scores):
    print(f"Lab number = {test_num + 1}", end = '')
    score = float(input(": "))
    total += score
  #Student GPA
  average = total / num_scores
  print(f"Student GPA N.{student+1} = {average:.1f}")
  print