from func.show_stocks import show_stocks
from func.add_stock import add_stock
from func.remove_stock import remove_stock
from func.update_stocks import update_stocks
from func.print_help import print_help

def main():
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
        elif(action == 'q'):
            break

if __name__ == '__main__':
    main()