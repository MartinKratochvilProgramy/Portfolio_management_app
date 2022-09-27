import yfinance as yf
from func.stocks import STOCKS
from func.stock_functions import get_total_invested_value

#WRITES DIVIDEND YIELD FOR EACH STOCK

TOTAL_DIVIDEND_YIELD = 0

def print_stock_name(stock):
    if len(stock.ticker) > 6:
        print(stock.ticker, "\t\t", end="")
    else:
        print(stock.ticker, "\t\t\t", end="")

def print_div_rates(stock, ticker):
    global TOTAL_DIVIDEND_YIELD
    if ticker.info['dividendYield'] is not None:
        #HANDLE STOCK WITH DIVIDEND PAYOUTS
        print(round(ticker.info['dividendYield']*100, 4), "%", end="")

        stock.get_stock_info()
        dividend_yield = round(ticker.info['dividendYield'] * stock.total_price, 3)
        TOTAL_DIVIDEND_YIELD += dividend_yield
        print("\t ", dividend_yield)
    
    elif (stock.ticker == "TABAK.PR"):
        #HANDLE PM
        TOTAL_DIVIDEND_YIELD += 1113
        stock.get_stock_info()
        print(round(1113/stock.total_price * 100, 2), "%","\t ", 1113 * stock.amount)

    else:
        #HANDLE STOCK WITHOUT DIVIDEND PAYOUTS
        print("-", "%")

print("NAME", "\t\t\t", "YIELD", "\t", "TOTAL")
print("-------------------------------------------")

for stock in STOCKS:
    ticker = yf.Ticker(stock.ticker)
    print_stock_name(stock)

    print_div_rates(stock, ticker)


print("-------------------------------------------")
print("TOTAL:", "\t\t\t", round(TOTAL_DIVIDEND_YIELD / get_total_invested_value()*100, 2), "%", " ", round(TOTAL_DIVIDEND_YIELD, 2))



