# Portfolio_management_app
Manage your net worth with the Yahoo finance API.

# How to run
Program requires python to be installed on your machine. Install required packages by running:
```
pip install -r requirements.txt
```
Start the program by running:
```
python main.py
```
Write actions into the console, following commands are available:

![image](https://user-images.githubusercontent.com/94861828/192496793-3c091ac7-da54-46ba-b16e-981bff569573.png)

Show stocks - lists all stocks in users portfolio

Add stock - add stock to the portfolio, stock ticker has to be valid for the Yahoo finance API - go to http://finance.yahoo.com and search for stock tickers (eg. Apple = 'AAPL'), also specify the currency in which the stock is listed

Remove stock - remove stock from the porfolio

Update stock prices - connects to the API and for each stock in the portfolio finds the current value, also calculates the total net worth of the portfolio, stores the values and outputs the charts described in the next chapter

# Outputs
After running the code program outputs several figures in the main folder. IMPORTANT: in order to create data for the time-dependent chart program should be run preferable every day, unsless the program is run the figures will not be updated.
## Account value in time
Blue line shows total net worth in time, orange shows invested amount.

![image](https://user-images.githubusercontent.com/94861828/192497986-04ee22c2-dfd8-4fd3-8e29-2112d9b5dbfb.png)
## Relative change
Percent change in portfolio value since it's creation.

![image](https://user-images.githubusercontent.com/94861828/192499672-5a653a9d-aff3-40ad-95e5-e19092b74e4b.png)
## Pie
Pie chart of percentage amount of each individual stock

![image](https://user-images.githubusercontent.com/94861828/192498866-46aedc34-3277-4d5c-ba64-66379d985f76.png)

# Future work
If somebody cares I will write a GUI, maybe transform the project into a web app using flask/django.

