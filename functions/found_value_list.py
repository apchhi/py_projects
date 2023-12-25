## Reading date from a file and copy this date in list
def main():
    names = ['Python','C','PHP','Ruby','C++','CSS']
    found_value = 'Ruby'

    if search_name(names, found_value):
        print(f'Hello {found_value}!')
    else:
        print('Value {found_value} not found!')

def search_name(n_list, value):
    if value in n_list:
        return True
    else:
        return False

main()
