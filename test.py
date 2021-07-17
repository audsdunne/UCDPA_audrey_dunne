# Import external libraries required
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

# Import data files
apple = pd.read_csv("Datasets/AAPL_daily_update.csv")
apple_stock = np.array(apple)


print(apple_stock)