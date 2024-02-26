## words separator

string = 'LoremIpsumDolorSitAmet,ConsecteturAdipiscingElit.EtiamDapibusLoremEgetNislGravidaEfficitur!NullaEgetOdioTincidunt,EleifendOrciNon,InterdumEros.NamEfficiturDapibusMassa,PosuerePharetraSemVestibulumEt?SedVestibulum,LoremSitAmetInterdumTristique,LectusJustoIaculisQuam,AElementumNislSemNecOdio.'

def main(string):
    start_word = 0
    end_word = 1
    new_string = ''
    len_str = len(string)
    print(string)
    print('--------------')
    '''
    for index in range(1,len_str):
        if string[index].isupper() and string[index] != 1:
            end_word = index
            #print('end word:', end_word)
            new_string += string[start_word:end_word] + ' '
            start_word = index
    '''
    for ch in string:
        if ch == '.' or ch=='!' or ch=='?':
            new_string += ch + ' '
        elif ch.isupper():
            new_string += ' ' + ch
        else:
            new_string += ch


            #print('start word:', start_word)
            #print('-------------')
        #if (not string[0]) or string[index] != '.':
        #    new_string += string.lower()
        #if string[index].isupper:
        #    if (string[index-1] == '.' or string[index-1] == '!' or string[index-1] == '?'):
            #end_word = string[index-1]
        #        new_string += ' ' + string[index]
        #    else:
        #        new_string += ' ' + string[index].lower()
        
            #start_word = string[index]
            #print(string[index], string[index-1])
        #    if (not string[0]) or (not string[index-1]) == '.' or (not string[index-1]) == '!' or (not string[index-1]) == '?' :
            #end_word = index
            #new_string += string[start_word:end_word].title()
        #if string[index].isupper():
                       #else:
            #    new_string += ' ' + string[start_word:end_word].lower()
                #start_word = index

                #print(string[index])
                #print(string[index-1])
                #print()
    print(new_string)




main(string)
