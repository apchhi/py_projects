## Reading date from a file and copy this date in list
def main():
    #names = []
    infile = open('text.txt', 'r')
    numbers1 = infile.readlines()
    infile.close()
    #print(len(names))

    for index in range(len(numbers1)):
        numbers1[index] = int(numbers1[index].rstrip('\n'))

    numbers2 = [item for item in numbers1]
    print(numbers2)
    
main()

