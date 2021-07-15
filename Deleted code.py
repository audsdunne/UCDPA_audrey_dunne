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

print(volume)

# Check for duplicates
contains_duplicates = any(date.count(element))
print(contains_duplicates)



# Import data files
apple_stock_monthly = pd.read_csv("Datasets/AAPL_Montly_updates.csv")
apple_stock_weekly = pd.read_csv("Datasets/AAPL_weekly_update.csv")
apple_stock_daily = pd.read_csv("Datasets/AAPL_daily_update.csv")


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


# Check for duplicates
contains_duplicates = any(date.count(element))
print(contains_duplicates)

apple_stock_final = list(set(date))
print(apple_stock_final)

# Understand different attributes of the dataset
print(apple_stock.shape)
print(apple_stock.info())
print(apple_stock.describe().transpose)
print(apple_stock.head(10))
print(apple_stock.tail(10))
