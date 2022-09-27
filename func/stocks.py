from currency_converter import CurrencyConverter
import sqlite3
import math
import pandas as pd
import yfinance as yf

class Stock:
    def __init__(self, ticker, amount, currency):
        self.ticker = ticker
        self.amount = amount
        self.currency = currency

    def get_stock_info(self):
        df_list = list()

        data = yf.download(self.ticker, group_by="Ticker", period='7d', progress=False)
        # print(f"{self.ticker} data: {data}")
        df_list.append(data)

        df = pd.concat(df_list)

        for value in df['Close'].values.tolist():
            if not math.isnan(value):
                self.previous_close_price = value

        self.total_price = self.previous_close_price * self.amount * self.currency

c = CurrencyConverter()
dollar = c.convert(1, 'USD', 'CZK')
euro = c.convert(1, 'EUR', 'CZK')
koruna = 1


conn = sqlite3.connect('stocks.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM stocks")
stocks = cursor.fetchall()

STOCKS = []
for stock in stocks:
    if stock[2] == 'koruna':
        STOCKS.append(Stock(stock[0], stock[1], koruna))
    if stock[2] == 'dollar':
        STOCKS.append(Stock(stock[0], stock[1], dollar))
    if stock[2] == 'euro':
        STOCKS.append(Stock(stock[0], stock[1], euro))

