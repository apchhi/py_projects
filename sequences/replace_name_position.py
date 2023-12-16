# # Found and replace a name position
def main():
    prod_code = ['Pizza', 'Burger', 'Fri', 'Cola']
    print('Positions:', prod_code)
    item = input('Enter name position: ')
    try:
        item_index = prod_code.index(item)
        new_item = input('Enter name a new position: ')
        prod_code[item_index] = new_item
    except ValueError:
        print('Item not found.')
    
    print(prod_code)

main()


