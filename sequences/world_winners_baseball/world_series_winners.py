dict_date = dict()
dict_win_count = dict()
infile = open('WorldSeriesWinners.txt', 'r')
for line in infile:
    #list_file = line.readline()
    list_line = line.rstrip('\n').split(' - ')
    if list_line[1] in dict_win_count:
        dict_win_count[list_line[1]] += 1
    else:
        dict_win_count[list_line[1]] = 1
    dict_date[int(list_line[0])] = list_line[1]
infile.close()
print('Date dictionary: ')
print(dict_date)
input()
print('Win dictionary: ')
print(dict_win_count)

