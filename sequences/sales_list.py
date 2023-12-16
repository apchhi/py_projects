NUM_DAYS = 5    #count days sale

def main():
    list_sales = [0] * 5    #created list with 5 elements. value 0 - default
    print('Enter sales for all days.')
    for index in range(len(list_sales)):
        list_sales[index] = float(input(f'Day N{index+1}: '))
    print()
    print('Values that were entered: ')
    for value in list_sales:
        print(value, '$')

#if __name__ == "__main__":
main()
