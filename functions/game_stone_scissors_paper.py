# # Python
import random


def main():
  print('This game - "Stone, scissors, paper" with a computer')
  computer_attribute = generate_computer_attribute()
  #print(computer_attribute)
  user_attribute = input('Please, select "stone", "scissors", "paper": ')
  print(computer_attribute)
  while computer_attribute == user_attribute:
    print('no one won')
    computer_attribute = generate_computer_attribute()
    #print(computer_attribute)
    user_attribute = input('Please, select "stone", "scissors", "paper": ')
  comparison = comparison_attributes(user_attribute, computer_attribute)
  print(comparison)

  
def generate_computer_attribute():
  number = random.randint(1, 3)
  if number == 1:
    attribute = 'stone'
  elif number == 2:
    attribute = 'scissors'
  elif number == 3:
    attribute = 'paper'
  return attribute

def comparison_attributes(user, pc):
  #while user != pc:
  if (user == 'stone' or pc == 'stone') and (user == 'scissors' or pc == 'scissors'):
    return 'stone breaks scissors'
  elif (user == 'scissors' or pc == 'scissors') and (user == 'paper' or pc == 'paper'):
    return 'scissors cutting paper'
  elif (user == 'paper' or pc == 'paper') and (user == 'stone' or pc == 'stone'):
    return 'paper wraps the stone'
  


main()