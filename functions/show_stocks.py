import sqlite3
import os

def show_stocks():
    if not os.path.isfile('stocks.db'):
        print("Add stocks first!")
        return

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stocks")
    stocks = cursor.fetchall()
    # TODO make printing pretty
    print('(TICKER, amount, currency)')
    for stock in stocks:
        print(stock)


if __name__ == '__main__':
    show_stocks()