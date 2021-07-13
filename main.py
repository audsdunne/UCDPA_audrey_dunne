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

# Check for missing or N/A values
print(apple_stock.isnull())
print(apple_stock.isnull().sum())




# Stop

print(apple_stock.shape)
print(apple_stock.info())
print(apple_stock.describe().transpose)
print(apple_stock.head(10))
print(apple_stock.tail(10))

# Check for missing or N/A values
print(apple_stock.isnull())
print(apple_stock.isnull().sum())
