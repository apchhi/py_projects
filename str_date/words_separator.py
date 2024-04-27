## words separator

string = 'LoremIpsumDolorSitAmet,ConsecteturAdipiscingElit.EtiamDapibusLoremEgetNislGravidaEfficitur!NullaEgetOdioTincidunt,EleifendOrciNon,InterdumEros.NamEfficiturDapibusMassa,PosuerePharetraSemVestibulumEt?SedVestibulum,LoremSitAmetInterdumTristique,LectusJustoIaculisQuam,AElementumNislSemNecOdio.'

def main(string):
    new_string = ''
    index = 0
    while index < len(string):
        if index == 0:
            new_string += string[index]
        elif (string[index-1] == '.') or (string[index-1] =='!') or (string[index-1] =='?'):
            new_string += ' ' + string[index]
        elif string[index].isupper():
            new_string += ' ' + string[index].lower()
        else:
            new_string += string[index]
        index += 1
    print(new_string)




main(string)
