## Building histogram

import matplotlib.pyplot as plt

def main():
    x_coords=[0,10,20,30,40]
    y_coords=[100,200,300,400,500]
    bar_width = 5
    plt.bar(x_coords,y_coords, bar_width, color=('r','g','b','m','k'))      # func building
    plt.savefig('histogram.png')    

main()
