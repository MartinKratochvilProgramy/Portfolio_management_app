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
