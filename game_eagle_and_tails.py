# # game eagle and tails

import random
EAGLE = "eagle"
TAILS = "tails"

def main():
  answer = question()
  while answer == "yes" or answer == "Yes":
    setter = random.randint(1,2)
    if setter == 1:
      print(EAGLE)
    else:
      print(TAILS)
    answer = question()
  
def question():
  print("Enter 'yes' for play game or 'no' for stop game:")
  answer = input()
  return answer
  

main()
