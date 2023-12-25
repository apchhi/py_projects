import matplotlib.pyplot as plt

def main():
    values = [100,400,300,600]
    slice_labels = ['I quarter','II quarter','III quarter','IV quarter']
    ## Doli and their markers /\
    plt.pie(values, labels=slice_labels)
    plt.savefig('pie_chart.png')
    plt.title('Sales by quarters')

main()
