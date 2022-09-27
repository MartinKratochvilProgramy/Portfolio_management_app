import sqlite3

def show_stocks():
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