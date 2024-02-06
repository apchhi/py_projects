from chart import diagram
#import matplotlib.pyplot as plt

'''
 Expenses items:
1. Rental of property
2. Petrol
3. Products
4. Clothes
5. Pays for auto
6. Other pays
'''

def main():
    NAME_FILE = 'Expenses.txt'
    expenses = {
            'rental':None,
            'petrol':None,
            'products':None,
            'clothes':None,
            'auto':None,
            'other':None,
            }
    # populating the dictionary with values
    expenses = populating(NAME_FILE, expenses)
    coord_diagram = []
    for value in expenses.values():
        coord_diagram.append(value)
    #print(coord_diagram)
    diagram(coord_diagram)

def populating(name_f, expenses):
    infile = open(name_f, 'r')
    numbers = infile.readlines()
    infile.close()
    for count, key in enumerate(expenses.keys()):
        expenses[key] = int(numbers[count].rstrip('\n'))
    return expenses


main()










