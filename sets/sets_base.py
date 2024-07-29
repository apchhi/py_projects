## teams basketball and baseball
baseball = set(['Jonny', 'Karmen', 'Aida', 'Alice'])
basketball = set(['Eva', 'Karmen', 'Alice', 'Sara'])

def main():
    in_both = baseball.intersection(basketball)
    all_students = baseball.union(basketball)
    only_baseball = baseball.difference(basketball)
    only_basketball = basketball - baseball
    only_one_team = basketball.symmetric_difference(baseball)

    print('In both', in_both)
    print('All students', all_students)
    print('Only baseball', only_baseball)
    print('Only basketball', only_basketball)
    print('Only one team', only_one_team)

if __name__ in '__main__':
    main()
