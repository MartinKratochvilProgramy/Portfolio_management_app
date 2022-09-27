from datetime import datetime
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt

def plot_relative_change_in_time():
#vývoj portfolia v čase - částky jsou v souboru acct_value_in_time.csv
    dates = []
    values = []
    rel_df = pd.read_csv('relative_change.csv')

    for i in range(len(rel_df)):
        dates.append(rel_df.loc[i].iat[0])
        values.append(rel_df.loc[i].iat[1])

    rel_x = [datetime.strptime(d, '%Y/%m/%d').date() for d in dates]
    rel_y = values

    plt.figure(figsize=(8.8, 6.6),dpi=160)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())    #značky na ose x měsíčně

    relative_change = round(rel_df.iloc[-1].iat[1] * 100 - 100, 2)

    if relative_change >= 0:
        plt.title(f'Relative change: +{round(rel_df.iloc[-1].iat[1] * 100 - 100, 2)}%')
    else:
        plt.title(f'Relative change: {round(rel_df.iloc[-1].iat[1] * 100 - 100, 2)}%')
    plt.plot(rel_x, rel_y, color="green")
    plt.grid()
    plt.gcf().autofmt_xdate()
    plt.savefig('relative_change_in_time.png')
    plt.clf()

if __name__ == '__main__':
    plot_relative_change_in_time()
