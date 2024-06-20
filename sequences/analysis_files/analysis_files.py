## alalysis to files

def main():
    name_file1 = 'words1.txt'
    name_file2 = 'words2.txt'
    set_file1 = set(read_file(name_file1))
    set_file2 = set(read_file(name_file2))
    
    unique_words_files = set_file1.union(set_file2)
    intersection_files = set_file1.intersection(set_file2)
    difference_file1 = set_file1.difference(set_file2)
    difference_file2 = set_file2.difference(set_file1)
    symmetric_difference_files = set_file1.symmetric_difference(set_file2)
    
    print(f'Unique words in files {name_file1} and {name_file2}: ')
    print(unique_words_files)
    input()
    print(f'Intersection words in files {name_file1} {name_file2}: ')
    print(intersection_files)
    input()
    print(f'Difference of {name_file1} and {name_file2}: ')
    print(difference_file1)
    input()
    print(f'Difference of {name_file2} and {name_file1}: ')
    print(difference_file2)
    input()
    print(f'Symmeric difference words of {name_file1} and {name_file2}: ')
    print(symmetric_difference_files)

def read_file(name_file):
    infile = open(name_file, 'r')
    read_file = infile.read().split()
    infile.close()
    return read_file

if __name__ in '__main__':
    main()
