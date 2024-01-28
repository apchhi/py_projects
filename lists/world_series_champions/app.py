def main():
    infile = open('WorldSeriesWinners.txt', 'r')
    list_teams = infile.readlines()
    infile.close()
    list_teams = reading_file(list_teams)
    name_team = input('Enter team name(Toccer): ')
    search_team(name_team, list_teams)

def reading_file(list_teams):
    for index in range(len(list_teams)):
        list_teams[index] = list_teams[index].rstrip('\n')    
    
    return(list_teams)

def search_team(name_team, list_teams):
    counter = 0
    for list_name in list_teams:
        if name_team == list_name:
            counter += 1
    print(f'The {name_team} have won the championship {counter} times.')


main()
