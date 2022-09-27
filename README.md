# Portfolio_management_app
Manage your net worth with the Yahoo finance API

# How to run
Program requires python to be installed on your machine. Install required packages by running:
```
pip install -r requirements.txt
```
After starting the program by running:
```
python main.py
```
write actions into the console.
![image](https://user-images.githubusercontent.com/94861828/192496793-3c091ac7-da54-46ba-b16e-981bff569573.png)
Show stocks - lists all stocks in users portfolio
Add stock - add stock to the portfolio, stock ticker has to be valid for the Yahoo finance API - go to finance.yahoo.com and search for stock tickers (eg. Apple = 'AAPL'), also specify the currency in which the stock is listed
Remove stock - remove stock from the porfolio
Update stock prices - connects to the API and for each stock in the portfolio finds the current value

# Outputs
After running the code program outputs several figures in the main folder.
## Account value in time
Blue line shows total net worth in time, orange shows invested amount.
![image](https://user-images.githubusercontent.com/94861828/192497986-04ee22c2-dfd8-4fd3-8e29-2112d9b5dbfb.png)
## Relative change
Percent change in portfolio value since it's creation.
![image](https://user-images.githubusercontent.com/94861828/192498302-9d1a27e4-8d9a-4995-a137-3aea4cef50f5.png)
## Pie
Pie chart of percentage amount of each individual stock
![image](https://user-images.githubusercontent.com/94861828/192498866-46aedc34-3277-4d5c-ba64-66379d985f76.png)

