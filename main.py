from func.init_stocks import init_stocks
from func.add_stock import add_stock
from func.show_stocks import show_stocks
from func.remove_stock import remove_stock
from func.write_get_functions import write_total_value, get_total_value, get_total_invested_value, get_daily_change
from func.plot_portfolio_in_time import plot_portfolio_in_time
from func.plot_pie import plot_pie
from func.plot_relative_change import plot_relative_change_in_time
from datetime import datetime
import time
import os

def main():
    #clear console
    # os.system('cls' if os.name=='nt' else 'clear')

    print("*********************************************************")
    print(f"Initializing stock prices at day {datetime.today().strftime('%d/%m/%Y')}...")
    
    STOCKS = init_stocks()
    write_total_value(STOCKS)

    total_account_value = get_total_value()
    total_invested_value = get_total_invested_value()

    print('\n')
    print(f"Total account value: {total_account_value:_} kč")
    print(f"Total invested value: {total_invested_value:_} kč")

    print('\n')
    print(f"Today's change: {get_daily_change()} %")
    print(f"Total change: {round((total_account_value/total_invested_value - 1)*100, 2)}%")

    plot_portfolio_in_time()
    plot_relative_change_in_time()
    plot_pie(STOCKS)


if __name__ == '__main__':
    while True:
        print("Select action:")
        print("Show stocks          -    \'show\'")
        print("Add stock            -    \'add\'")
        print("Remove stock         -    \'remove\'")
        print("Update stock prices  -    \'update\'")
        print("Quit                 -    \'q\'")

        action = input()

        if (action == 'show'):
            show_stocks()
        elif (action == 'add'):
            add_stock()
        elif (action == 'remove'):
            remove_stock()
        elif (action == 'update'):
            main()
        elif(action == 'q'):
            break
    