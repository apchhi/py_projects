## choice of restaurants on the menu

#list of restaurants

restaurants = {
        "Joe's Gourmet Burgers":[False, False, False],
        "Central pizzeria":[True, False, True],
        "Dishes around the corner":[True, True, True],
        "Italian mom's coffee":[True, False, False],
        "Chef's Kitchen":[True, True, True],
        }
# vegetarian, vegan, gluten free diet
# True / False


print('Enter your food preferences to select the restaurant you need.')
vegetarian = input('Need a vegetarian menu? Enter( + or - ): ')
vegan = input('Need a vegan menu? Enter( + or - ): ')
gluten = input('Need a gluten free menu? Enter( + or - ): ')

#vegetarian_check = None
#vegan_check = None
#gluten_check = None

if vegetarian == '+':
    vegetarian_check = True
else:
    vegetarian_check = False
if vegan == '+':
    vegan_check = True
else:
    vegan_check = False
if gluten == '+':
    gluten_check = True
else:
    gluten_check = False


found_key = []

print('Found restaurants for your request: ')
for key, value in restaurants.items():
    if value == [vegetarian_check, vegan_check, gluten_check]:
        print(key)
        found_key.append(key)

if len(found_key) == 0:
    print('Found not result.')

#else:
#    vegetarian_check = False
#    vegan_check = False
#    gluten_check = False

#print(f'The following restaurants are for you: ')
#print(vegetarian_check, ' ', vegan_check, ' ', gluten_check)








