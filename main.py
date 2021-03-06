# Import external libraries required
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import requests

# Import data files
apple_stock = pd.read_csv("Datasets/AAPL_daily_update.csv")
print(apple_stock.head(5))


# Insert new column called Stock Name
apple_stock['Name'] = "APPL"

# Count missing values in each column
missing_values_count = apple_stock.isnull().sum
print(missing_values_count)

# Drop duplicate rows based on column date
drop_duplicates = apple_stock.drop_duplicates(subset=['Date'])
print(apple_stock.shape, drop_duplicates.shape)

# Create a new column with month of date
apple_stock['month'] = pd.DatetimeIndex(apple_stock['Date']).month
# Create a new column with year of date
apple_stock['year'] = pd.DatetimeIndex(apple_stock['Date']).year
# Create a new column with month and year of date
apple_stock['month_year'] = pd.to_datetime(apple_stock['Date']).dt.to_period('M')
print(apple_stock.tail(10))

# Understand different attributes of the dataset
print(apple_stock.shape)
print(apple_stock.info())
print(apple_stock.describe().transpose)
print(apple_stock.values)
print(apple_stock.columns)
print(apple_stock.index)

# Sort data based on volume
apple_stock_sorted = apple_stock.sort_values(["Adj Close"], ascending=False)
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

# Create an array from H1 Data
h120_apple = np.array(h12020_apple)
print(h120_apple)
print(type(h120_apple))

# Retrieve data from online API
url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=aapl&apikey==XCHDP0ZBLSGMS7HD'
r = requests.get(url)
apple_earnings = r.json()
print(apple_earnings)

# Gain valuable insights
# Calculate the average closing stock value for H1 2020
average_closing_price = statistics.mean(h12020_apple['Close'])
print(average_closing_price)

# Identify Minimum closing stock value for H1 2020
closing_price = (h12020_apple["Close"])
min_closing_price = min(closing_price)
print(min_closing_price)

# Identify maximum closing stock value for H1 2020
max_closing_price = max(closing_price)
print(max_closing_price)

# Identify the day which had the highest close in H1 2020
max_day = (h12020_apple[h12020_apple.Close == h12020_apple.Close.max()])
print(max_day)

# Identify the day which had the lowest close in H1 2020
min_day = (h12020_apple[h12020_apple.Close == h12020_apple.Close.min()])
print(min_day)

# Create a chart showing the history of Apple closing stock price  over H12020
x = h12020_apple['Date']
y = h12020_apple["Close"]
plt.plot(x, y, marker="s", linestyle="--", color="cyan")
plt.xlabel("Date")
plt.ylabel("Closing Stock ???")
plt.title("H1 2020 Apple Closing Stock Value")
plt.show()

# Create a chart showing June 2020 data only
month_year = h12020_apple["month_year"]
start_date = "2020-06"
end_date = "2020-06"
after_start_date = month_year >= start_date
before_end_date = month_year <= end_date
between_two_dates = after_start_date & before_end_date
Jun20_apple = h12020_apple.loc[between_two_dates]
x = Jun20_apple['Date']
y1 = Jun20_apple["High"]
y2 = Jun20_apple["Low"]
plt.plot(x, y1, marker="^", linestyle=":", color="hotpink")
plt.plot(x, y2, marker="P", linestyle="--", color="cyan")
plt.xlabel("Date")
plt.ylabel("High Stock Value ??? / Low Stock Value ???")
plt.title("June 2020 Apple Stock Value")
plt.show()

# Import Samsung dataset and create H1 2020 data only (as per Apple)
samsung_stock = pd.read_csv("Datasets/samsung.csv")
samsung_stock['Name'] = "SAMS"
samsung_stock['month'] = pd.DatetimeIndex(samsung_stock['Date']).month
samsung_stock['year'] = pd.DatetimeIndex(samsung_stock['Date']).year
samsung_stock['month_year'] = pd.to_datetime(samsung_stock['Date']).dt.to_period('M')
month_year = samsung_stock["month_year"]
start_date = "01/01/2020"
end_date = "30/06/2020"
after_start_date = month_year >= start_date
before_end_date = month_year <= end_date
between_two_dates = after_start_date & before_end_date
h12020_samsung = samsung_stock.loc[between_two_dates]
print(h12020_samsung.tail(10))

# Merge Apple and Samsung Dataframes
telecoms_stock = pd.concat([h12020_apple, h12020_samsung], axis=0)
print(telecoms_stock.head(5))
print(telecoms_stock.tail(5))

# Using looping and iterrows on dataframe
for index, row in telecoms_stock.iterrows():
    print(row["Date"], row["Close"])
