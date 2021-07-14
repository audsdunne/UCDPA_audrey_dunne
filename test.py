# Import external libraries required
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

# Import data files
apple_stock_monthly = pd.read_csv("AAPL_Montly_updates.csv")
apple_stock_weekly = pd.read_csv("AAPL_weekly_update.csv")
apple_stock_daily = pd.read_csv("AAPL_daily_update.csv")

# Understand different attributes of the dataset
print(apple_stock.shape)
print(apple_stock.info())
print(apple_stock.describe().transpose)
print(apple_stock.head(10))
print(apple_stock.tail(10))

# Check for missing or N/A values
print(apple_stock.isnull())
print(apple_stock.isnull().sum())


# Gain valuable insights

# Identify Minimum Closing Stock Value
closing_price = (apple_stock["Adj Close"])
print(closing_price)

min_closing_price = min(closing_price)
print(min_closing_price)

# Identify min closing stock value index
min_index = closing_price.index(min_closing_price)
print(min_index)

# Identify the month with the minimum closing stock value
months = (apple_stock["Date"])
min_month = months[min_index]
print(min_month)

# Calculate the average closing stock value
average_closing_price = statistics.mean(closing_price)
print(average_closing_price)

# Check for duplicates
contains_duplicates = any(date.count(element))
print(contains_duplicates)

apple_stock_final = list(set(date))
print(apple_stock_final)
