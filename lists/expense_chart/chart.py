import matplotlib.pyplot as plt

def diagram(coords_list):
    #print(coords_list)
    coords_label = ['Rental', 'Petrol', 'Products', 'Clothes', 'Auto', 'Other']
    plt.pie(coords_list, labels=coords_label)
    plt.show()



