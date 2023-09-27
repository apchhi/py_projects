## picnic hot dog calculator

sausages_per_pack = int(input("Enter the number of sausages in one pack: "))
buns_per_pack = int(input("Enter the number of buns in one pack: "))

participants = int(input("Enter the number of picnic participants: "))
hot_dogs_per_participant = int(input("Enter the number of hot dogs per participant: "))

sausages_needed = buns_needed= participants * hot_dogs_per_participant
#buns_needed = participants * hot_dogs_per_participant

sausages_packs = (sausages_needed + sausages_per_pack - 1) // sausages_per_pack
buns_packs = (buns_needed + buns_per_pack - 1) // buns_per_pack

sausages_leftover = (sausages_packs * sausages_per_pack) - sausages_needed
buns_leftover = (buns_packs * buns_per_pack) - buns_needed

print("Minimum number of sausage packs needed:", sausages_packs)
print("Minimum number of bun packs needed:", buns_packs)
print("Number of leftover sausages:", sausages_leftover)
print("Number of leftover buns:", buns_leftover)



'''
sausages_all_bags = 0
baguettes_all_bags = 0

## in one bag
sausages_bag = int(input('Enter the number of sausages: '))
baguettes_bag = int(input('Enter the number of bagets: '))
# all persons
participants = int(input('Enter the number of picnic participants: '))
hot_dogs_per_participant = int(input('Enter the number of hot dogs per 1 participants: '))

# one hot dog = 1 sausage + 1 baget

## one participant 
# sausages and bagets per one participant
sausages_participant = baguettes_participant = hot_dogs_per_participant 

# all sausages
sausages_all = sausages_participant * participants
baguettes_all = baguettes_participant * participants


if (sausages_all % sausages_bag != 0) and (baguettes_all % baguettes_bag != 0):
    sausages_all_bags = sausages_all // sausages_bag + 1
    baguettes_all_bags = baguettes_all // baguettes_bag + 1
elif (sausages_all % sausages_bag != 0) or (baguettes_all % baguettes_bag != 0):
    if (sausages_all % sausages_bag != 0):
        sausages_all_bags = sausages_all // sausages_bag
        baguettes_all_bags = baguettes_all // baguettes_bag + 1
    elif (baguettes_all % baguettes_bag != 0):
        sausages_all_bags = sausages_all // sausages_bag + 1
        baguettes_all_bags = baguettes_all // baguettes_bag


sausages_leftover = sausages_all_bags % sausages_bag
baguettes_leftover = baguettes_all_bags % baguettes_bag

print('All bags of sausages:', sausages_all_bags)
print('All bags of baguettes:', baguettes_all_bags)
print('Sausages leftover:', sausages_leftover)
print('Baguettes leftover:', baguettes_leftover)
'''


