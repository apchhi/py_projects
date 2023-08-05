#вычисляем сумму вноса                  
# провентная ставка должна быть в сотых (0.12) годовых от общей суммы(1)00%

future_value = float(input('Enter all have money: '))
rate = (float(input('Enter percent in year: '))) /100  #interest rate
years = float(input('Enter years all: '))
percent_value = future_value / (1.0 + rate) ** years    #insert money/ years

#print(rate)
print('You need insert ', percent_value)
