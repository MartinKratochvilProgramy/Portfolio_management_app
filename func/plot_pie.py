import matplotlib.pyplot as plt
from func.write_get_functions import get_total_value

def plot_pie(STOCKS):
    names = []
    fractions = []
    
    for stock in STOCKS:
        total_value = get_total_value()

        names.append(stock.ticker)
        fractions.append(stock.total_price / total_value)

    
    colors = ['lightcyan' for _ in range(len(fractions))]

    fig = plt.figure(figsize=(10.8, 8.6),dpi=160)

    plt.pie(fractions, labels = names, autopct='%1.1f%%', colors=colors, wedgeprops={"edgecolor":"dodgerblue",'linewidth': 1, 'antialiased': True})
    plt.title("Stocks")
    plt.savefig('pie.png')
    plt.clf()

if __name__ == '__main__':
    plot_pie()


