import sqlite3

def remove_stock():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    # get user inputs
    if (input("Remove stock? [y/n] ") == "y"):
        # get ticker
        ticker = input("Ticker: ")
        ticker.strip()
        cursor.execute("SELECT * FROM stocks WHERE ticker=(?)", (ticker, ))
        existing_stock = cursor.fetchall()
        conn.commit()
        if (len(existing_stock) == 0):
            print("Stock not found")
            remove_stock()
        
        # get remove amount
        amount = input("Amount to remove: ")
        amount.strip()
        if not amount.isdigit():
            print("Amount not an int!")
            remove_stock()
        amount = int(amount)
        if (amount <= 0):
            print("Negative amount!")
            remove_stock()

        # find what the new amount will be
        # if 0 then remove stock from db
        new_amount = existing_stock[0][1] - amount
        if new_amount == 0:
            cursor.execute("DELETE from stocks WHERE ticker=(?)", (ticker, ))
            conn.commit()
        else:
            cursor.execute("UPDATE stocks SET amount=(?) WHERE ticker=(?)", (new_amount, ticker))
            conn.commit()
        
        conn.close()
        return

    else:
        conn.close()
        return

if __name__ == '__main__':
    remove_stock()