def main():
    square_lo_shu = [[4,9,2],[3,5,7],[8,1,6]]
    set_list = [[1,9,2],[3,5,7],[8,1,6]]
    answer_func = check_list(square_lo_shu, set_list)
    print(answer_func)

def check_list(lo_shu, set_list):
    for row_count in range(len(lo_shu)):
        #row_lo_shu = lo_shu[row_count]
        #row_set_list = set_list[row_count]
        #print(row_lo_shu, end=' --- ')
        #print(row_set_list)
        for col_count in range(len(lo_shu[0])):
            if lo_shu[row_count][col_count] != set_list[row_count][col_count]:
                return('Value the square Lo-Shu not is equal the check list.')
                break
    return('Value the square Lo-Shu is equal the check list.')

main()
