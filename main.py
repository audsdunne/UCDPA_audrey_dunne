# Import external libraries required
import statistics

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Import data files
apple_stock = pd.read_csv("AAPL_Montly_updates.csv")

# Check for missing or N/A values
print(apple_stock.isnull())
print(apple_stock.isnull().sum())


# Gain valuable insights

# Identify Minimum Closing Stock Value
closing_price = (apple_stock["Adj Close"])
print(closing_price)

min_closing_price = min(closing_price)
print(min_closing_price)

# Calculate the average closing stock value
average_closing_price = statistics.mean(closing_price)
print(average_closing_price)