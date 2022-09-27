import pandas as pd
import math
import sqlite3
from datetime import datetime
import os
import yfinance as yf
from currency_converter import CurrencyConverter
# from func.stock_class import Stock

def add_stock():
    ''' 
        Create user prompt in terminal and ask user to input values for new stock
        Values are:
        Ticker
        Amount (how much of new was bought)
        Currency (currency in which stock is traded on yfinance)
        Add stock to the existing SQL database
    '''
    c = CurrencyConverter()
    dollar = c.convert(1, 'USD', 'CZK')
    euro = c.convert(1, 'EUR', 'CZK')
    koruna = 1

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS stocks (
                ticker text,
                amount integer,
                currency text
                )""")

    currencies = ["dollar", "euro", "koruna"]

    # get user inputs
    if (input("Add new stock? [y/n] ") == "y"):
        # add ticker
        ticker = input("Ticker: ")
        ticker.strip()
        stock_data = yf.download(ticker, group_by="Ticker", period='7d', progress=False)
        if (len(stock_data) == 0):
            print("Incorrect ticker!")
            add_stock()

        # add amount
        amount = input("Amount: ")
        amount.strip()
        if not amount.isdigit():
            print("Amount not an int!")
            add_stock()
        amount = int(amount)
        if (amount <= 0):
            print("Negative amount!")
            add_stock()

        # add currency
        currency = input("Currency [dollar, euro, koruna]:")
        currency.strip()
        if currency not in currencies:
            print("Currency not in ")
            print(currencies)
            add_stock()
        
        #find if stock of this ticker already exists
        cursor.execute("SELECT * FROM stocks WHERE ticker=(?)", (ticker, ))
        conn.commit()
        existing_stock = cursor.fetchall()
        if (len(existing_stock) > 0):
            # if ticker already exists, add new_amount to it
            new_amount = int(existing_stock[0][1]) + amount
            cursor.execute("UPDATE stocks SET amount=(?) WHERE ticker=(?)", (new_amount, ticker))
            conn.commit()
            print(f"Added new stock! Ticker: {ticker} Amount: {amount} Currency: {currency}\n")
        else:
            # else add new column
            cursor.execute("INSERT INTO stocks VALUES (?, ?, ?)", (ticker, amount, currency))
            print(f"Added new stock! Ticker: {ticker} Amount: {amount} Currency: {currency}\n")
            conn.commit()
        
        conn.close()

        #find how much money was invested
        df_list = list()
        df_list.append(stock_data)
        df = pd.concat(df_list)
        for value in df['Close'].values.tolist():
            if not math.isnan(value):
                previous_close_price = value
        if (currency == 'dollar'):
            total_value = previous_close_price * amount * dollar
        if (currency == 'euro'):
            total_value = previous_close_price * amount * euro
        if (currency == 'koruna'):
            total_value = previous_close_price * amount * koruna

        # write invested value into money_invested.csv
        if os.path.isfile("money_invested.csv"):
            #if file exists
            with open("money_invested.csv", 'a') as vals:
                today = datetime.today().strftime('%Y/%m/%d')
                vals.write('\n')
                vals.write(today)
                vals.write(', ')
                vals.write(str(round(total_value)))
        else:
            #if file does not exist, create new
            with open("money_invested.csv", 'w') as vals:
                today = datetime.today().strftime('%Y/%m/%d')
                vals.write(today)
                vals.write(', ')
                vals.write(str(round(total_value)))
        return 
    else: 
        conn.close()
        return

if __name__ == '__main__':
    add_stock()
