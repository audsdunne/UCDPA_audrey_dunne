# Import external libraries required
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import requests

# Import data files
apple_stock = pd.read_csv("Datasets/AAPL_daily_update.csv")
print(apple_stock.head(5))

# Create a new column with month of date
apple_stock['month'] = pd.DatetimeIndex(apple_stock['Date']).month
# Create a new column with year of date
apple_stock['year'] = pd.DatetimeIndex(apple_stock['Date']).year
# Create a new column with month and year of date
apple_stock['month_year'] = pd.to_datetime(apple_stock['Date']).dt.to_period('M')
print(apple_stock.tail(10))

# Sort data based on volume
apple_stock_sorted = apple_stock.sort_values(["Adj Close"],ascending=False)
print(apple_stock_sorted.head(10))

# Group by Month_Year
apple_stock.groupby("month_year")
print(apple_stock.groupby("month_year").groups)

# Filter dataset by H1 2020 only
month_year = apple_stock["month_year"]
start_date = "2020-01"
end_date = "2020-06"
after_start_date = month_year >= start_date
before_end_date = month_year <= end_date
between_two_dates = after_start_date & before_end_date
h12020_apple = apple_stock.loc[between_two_dates]
print(h12020_apple.head(10))

# Check for missing or N/A values
print(h12020_apple.isnull())
print(h12020_apple.isnull().sum())

# Retrieve data from online API
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=aapl&apikey==XCHDP0ZBLSGMS7HD'
r = requests.get(url)
apple_earnings = r.json()
print(apple_earnings)

# Gain valuable insights
# Calculate the average closing stock value
average_closing_price = statistics.mean(h12020_apple['Close'])
print(average_closing_price)





