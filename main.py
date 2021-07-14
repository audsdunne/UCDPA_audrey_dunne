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

# Combine 3 apple stock datasets and merge to one dataset
apple_stock = pd.concat([apple_stock_daily, apple_stock_weekly, apple_stock_monthly], axis = 0)

# Assign values to lists in dataset
date = apple_stock["Date"]
open = apple_stock["Open"]
high = apple_stock["High"]
low = apple_stock["Low"]
close = apple_stock["Close"]
adj_Close = apple_stock["Adj Close"]
volume = apple_stock["Volume"]

# Sort values by closing stock by ascending
sorted_closing_stock = apple_stock_daily["Adj Close"].sort()
print(sorted_closing_stock)

# Check for missing or N/A values
print(apple_stock.isnull())
print(apple_stock.isnull().sum())


