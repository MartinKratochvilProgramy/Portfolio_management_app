from functions.init_stocks import init_stocks
from functions.write_get_functions import write_total_value, get_total_value, get_total_invested_value, get_daily_change
from functions.plot_portfolio_in_time import plot_portfolio_in_time
from functions.plot_pie import plot_pie
from functions.plot_relative_change import plot_relative_change_in_time
from datetime import datetime

def update_stocks():

    print("*********************************************************")
    print(f"Initializing stock prices at day {datetime.today().strftime('%d/%m/%Y')}...")

    # get individual stocks with updated prices into an array    
    STOCKS = init_stocks()
    # write updated total portfolio value into acct_value_in_time.csv
    write_total_value(STOCKS)

    # get total last portfolio value
    total_account_value = get_total_value()
    # get total value invested into portfolio
    total_invested_value = get_total_invested_value()

    print('\n')
    print(f"Total account value: {total_account_value:_} kč")
    print(f"Total invested value: {total_invested_value:_} kč")

    print('\n')
    print(f"Today's change: {get_daily_change()} %")
    print(f"Total change: {round((total_account_value/total_invested_value - 1)*100, 2)}%")

    # plot portfolio value in time into portfolio_in_time.png
    plot_portfolio_in_time()
    # plot relative change in time into relative_change_in_time.png
    plot_relative_change_in_time()
    # plot pie chart of all stocks into pie.png
    plot_pie(STOCKS, total_account_value)

if __name__ == '__main__':
    update_stocks()