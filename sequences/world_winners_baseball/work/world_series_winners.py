def main():
    name_file = 'WorldSeriesWinners.txt'
    date_winners, win_count = create_dicts(name_file)
    print('Date dictionary: ')
    print(date_winners)
    input()
    print('Win dictionary: ')
    print(win_count)
    print('Enter the year from 1903 to 2009')
    year = int(input())
    team = date_winners.get(year, 'Enter year is not found')
    print(f'In {year} year champion: {team}')

def create_dicts(nfile):
    dict_date = dict()
    dict_win_count = dict()

    infile = open(nfile, 'r')
    for line in infile:
        list_line = line.rstrip('\n').split(' - ')
        if list_line[1] in dict_win_count:
            dict_win_count[list_line[1]] += 1
        else:
            dict_win_count[list_line[1]] = 1
        dict_date[int(list_line[0])] = list_line[1]
    infile.close()
    return dict_date, dict_win_count

if __name__ in "__main__":
    main()
