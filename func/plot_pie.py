import matplotlib.pyplot as plt

def plot_pie(STOCKS, total_value):
    names = []
    fractions = []
    
    for stock in STOCKS:
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


