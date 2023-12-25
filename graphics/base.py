import matplotlib.pyplot as plt
##Data for x-axis
x = [0, 1, 2, 3, 4]
# Data for y-axis
y = [0, 3, 1, 5, 2]

## Create a line plot and marker in points
plt.plot(x, y, marker='o')

## Title
plt.title('My date')

## Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

## Size X-axis and Y-axis
plt.xlim(xmin = -1, xmax = 10)
plt.ylim(ymin = -1, ymax = 10)

## Grid(setka)
plt.grid(True)

## Ticks marks(metki deleniy)
plt.xticks([0,1,2,3,4],[2016,2017,2018,2019,2020])
plt.yticks([0,1,2,3,4,5],["$0m","$1m","$2m","$3m","$4m","$5m"])

## Display the plot
#plt.show()

## Save PNG pictures
plt.savefig('plot.png')
