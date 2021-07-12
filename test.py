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


