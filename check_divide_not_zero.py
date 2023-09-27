# # check value is not zero
num1 = int(input('Enter num 1: '))
num2 = int(input('Enter num 2: '))

def divide(num1,num2):
  if num2 == 0:
    result = None
  else:
    result = num1 / num2
  return result

quotient = divide(num1,num2)

if quotient is None:
  print(' Num : 0 - NO!')
else:
  print(f'{num1} : {num2} = {quotient}')