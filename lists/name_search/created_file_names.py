from faker import Faker
fake = Faker('ru_RU')
def main():
    infile_female = open('GirlNames.txt', 'w')
    for i in range(200):
        name_female = str(fake.name_female())+'\n'
        infile_female.write(name_female)
    infile_female.close()

    infile_male = open('BoyNames.txt', 'w')
    for i in range(200):
        name_male = str(fake.name_male())+'\n'
        infile_male.write(name_male)
    infile_male.close()

main()
#address = fake.address()
#text = fake.text()



#print(name)
#print(name1)
#print(address)
#print(text)

#def main():

#    infile_girl_name = open('GirlNames.txt', 'w')
