# build a graph
import matplotlib.pyplot as plt 

def main():
    file = '1994_Weekly_Gas_Averages.txt'
    x_coord, y_coord = readfile(file)
    #print(x_coord, y_coord)
    build_graph(x_coord, y_coord)

def readfile(file):
    rfile = open(file, 'r')
    price = [float(item.rstrip('\n')) for item in rfile.readlines()]
    rfile.close()
    num_sale = [item+1 for item in range(len(price))]
    return num_sale, price

def build_graph(x, y):
    plt.plot(x, y)
    plt.title('Gasoline price chart in 1994 year')
    plt.xlabel('Weeks')
    plt.ylabel('U.S. Dollars for liter')
    plt.grid(True)
    plt.show()

main()
