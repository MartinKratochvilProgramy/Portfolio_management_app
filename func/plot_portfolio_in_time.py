from datetime import datetime
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt

def plot_portfolio_in_time():
#vývoj portfolia v čase - částky jsou v souboru acct_value_in_time.csv
    dates = []
    values = []
    df = pd.read_csv('acct_value_in_time.csv')

    for i in range(len(df)):
        dates.append(df.loc[i].iat[0])
        values.append(df.loc[i].iat[1])

    x = [datetime.strptime(d, '%Y/%m/%d').date() for d in dates]
    y = values

#vykreslí investované peníze - částky jsou v souboru money_invested.csv
    invested_dates = []
    invested_values = []
    df = pd.read_csv('money_invested.csv')

    for i in range(len(df)):
        invested_dates.append(df.loc[i].iat[0])
        if i > 0:
            invested = 0
            for j in range(i + 1):
                invested += df.loc[j].iat[1]
            invested_values.append(invested)
        else:
            invested_values.append(df.loc[i].iat[1])

    x_inv = [datetime.strptime(d, '%Y/%m/%d').date() for d in invested_dates]
    y_inv = invested_values

    plt.figure(figsize=(8.8, 6.6),dpi=160)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())    #značky na ose x měsíčně

    plt.title('Account value in time')
    plt.plot(x, y)
    plt.grid()
    plt.scatter(x_inv, y_inv, color='tab:orange')
    plt.plot(x_inv, y_inv, color='tab:orange', linestyle='--')
    plt.gcf().autofmt_xdate()
    plt.savefig('vyvoj.png')
    plt.clf()