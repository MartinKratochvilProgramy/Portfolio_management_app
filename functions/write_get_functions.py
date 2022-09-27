import csv
import pandas as pd
import os.path
import pandas as pd
from datetime import datetime

def write_total_value(STOCKS):
    #write current portfolio value to file
    if os.path.isfile("acct_value_in_time.csv"):
        #if file exists
        with open("acct_value_in_time.csv", 'a') as vals:
            total_value = 0
            for stock in STOCKS:
                total_value += stock.total_price

            today = datetime.today().strftime('%Y/%m/%d')
            vals.write('\n')
            vals.write(today)
            vals.write(', ')
            vals.write(str(round(total_value)))
    else:
        with open("acct_value_in_time.csv", 'w') as vals:
            total_value = 0
            for stock in STOCKS:
                total_value += stock.total_price

            today = datetime.today().strftime('%Y/%m/%d')
            vals.write(today)
            vals.write(', ')
            vals.write(str(round(total_value)))


def get_total_value():
    #returns latest portfolio value
    if not os.path.isfile('acct_value_in_time.csv'):
        write_total_value()

    df = pd.read_csv('acct_value_in_time.csv')

    if len(df) > 0:
        data = df.iloc[-1].iat[1]
    else: 
        with open('acct_value_in_time.csv') as file:
            df = csv.reader(file, delimiter=' ')
            for row in df:
                data = row[1]
    return round(float(data))


def get_total_invested_value():
    #returns total amount invested into portfolio
    if os.path.isfile('money_invested.csv'):
        df = pd.read_csv('money_invested.csv')
        invested_value = 0
        if len(df) > 0:
            for i in range(len(df)):
                invested_value += df.loc[i].iat[1]
        else:
            with open('money_invested.csv') as file:
                spamreader = csv.reader(file, delimiter=' ')
                for row in spamreader:
                    invested_value = float(row[1])

        return round(invested_value)
    else:
        with open("money_invested.csv", 'w') as vals:
            vals.write(datetime.today().strftime('%Y/%m/%d'))
            vals.write(', ')
            vals.write(str(get_total_value()))
        return (get_total_value())

def get_daily_change():
    #returns change in portfolio value from previous day in %

    if not os.path.isfile('relative_change.csv'):
        with open("relative_change.csv", 'w') as vals:
            today = datetime.today().strftime('%Y/%m/%d')
            vals.write(today)
            vals.write(', ')
            vals.write(str(1))
            vals.write('\n')
            vals.write(today)
            vals.write(', ')
            vals.write(str(1))

    df = pd.read_csv('acct_value_in_time.csv')
    rdf = pd.read_csv('relative_change.csv')
    inv_df = pd.read_csv('money_invested.csv')

    #if file is populated enough
    if len(df) > 1:
        #get percentual change
        if (datetime.today().day == datetime.strptime(inv_df.iloc[-1].iat[0], '%Y/%m/%d').day):
            #if money was invested today. do not include in percent change because invested value would skew the % change
            percent_change = (df.iloc[-1].iat[1] - inv_df.iloc[-1].iat[1]) / df.iloc[-2].iat[1] * 100 - 100    #%
        else:
            percent_change = df.iloc[-1].iat[1] / df.iloc[-2].iat[1] * 100 - 100    #%
        last_relative_percentage = rdf.iloc[-1].iat[1]
        current_relative_percentage = last_relative_percentage * ((100 + percent_change) / 100)

        #force display + with positive vals
        if percent_change >= 0:
            percent_change = "+" + str(round(percent_change, 2))
        else:
            percent_change = str(round(percent_change, 2))
        
        #write relative percent change to file
        with open("relative_change.csv", 'a') as vals:
            today = datetime.today().strftime('%Y/%m/%d')
            vals.write('\n')
            vals.write(today)
            vals.write(', ')
            vals.write(str(current_relative_percentage))


        return percent_change

    else:
        return 0