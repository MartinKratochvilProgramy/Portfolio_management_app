from functions.show_stocks import show_stocks
from functions.add_stock import add_stock
from functions.remove_stock import remove_stock
from functions.update_stocks import update_stocks
from functions.print_help import print_help

def main():
    # ask for user input
    print_help()

    while True:
        print("-------------------------------------------------------")
        action = input()
        if (action == 'show'):
            show_stocks()
        elif (action == 'add'):
            add_stock()
            show_stocks()
        elif (action == 'remove'):
            remove_stock()
            show_stocks()
        elif (action == 'update'):
            update_stocks()
        elif (action == 'help'):
            print_help()
        elif(action == 'quit'):
            break
        else:
            print('Invalid input')
            print("-------------------------------------------------------")
            print_help()

if __name__ == '__main__':
    main()