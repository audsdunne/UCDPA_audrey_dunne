# Import external libraries required
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Import data files
apple_stock = pd.read_csv("AAPL_Montly_updates.csv")

# Understand different attributes of the dataset
print(apple_stock.shape)
print(apple_stock.info())
print(apple_stock.describe().transpose)
print(apple_stock.head(10))
print(apple_stock.tail(10))

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