from random_word import Wordnik 

W= Wordnik()

START_YEAR = 1903
END_YESR = 2009
YEARS_NOT_GAME = [1904, 1994]

def main():
    infile = open('WorldSeriesWinners.txt', 'w')
    period_generation = END_YESR - (START_YEAR + len(YEARS_NOT_GAME)) 
    for _ in range(period_generation):
        team = str(W.get_random_word())
        print(team)
        write_team_file = team.title()
        infile.write(write_team_file + '\n')
    infile.close()
    print('write to file successful')

main()







