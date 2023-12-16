def main():
    prod_code = ['V450', 'L351', 'T301', 'F110']
    search = input('Enter number a model: ')
    if search in prod_code:
        print('Model found in list')
    else:
        print('Model not found in list')

main()


