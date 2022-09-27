from currency_converter import CurrencyConverter
import sqlite3
from functions.stock_class import Stock

def init_stocks():
    # for each stock in db finds current converted price in CZK and returns
    # array of Stock objects
    c = CurrencyConverter()
    dollar = c.convert(1, 'USD', 'CZK')
    euro = c.convert(1, 'EUR', 'CZK')
    koruna = 1

    # load stocks from db into stocks array
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
    conn.close()
    #get current stock info (price) for each stock from yfinance
    for stock in STOCKS:
        stock.get_stock_info()
        print(f"{stock.ticker} current price: {round(stock.previous_close_price, 2)} amount: {stock.amount} total price in czk: {round(stock.currency * stock.amount * stock.previous_close_price, 2)},-")

    return STOCKS