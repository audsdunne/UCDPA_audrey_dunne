# Import external libraries required
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

# Import data files
apple_stock = pd.read_csv("Datasets/AAPL_daily_update.csv")
print(apple_stock)

# Sort data based on volume
apple_stock_sorted = apple_stock.sort_values(["Adj Close"])
print(apple_stock_sorted.head(10))


