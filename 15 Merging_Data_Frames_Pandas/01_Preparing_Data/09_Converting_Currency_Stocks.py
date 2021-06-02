import pandas as pd
import os

path = "C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data"

os.chdir(path)
os.getcwd()
os.listdir(path)

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('sp500.csv', index_col='Date', parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('exchange.csv', index_col='Date', parse_dates=True)

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500.loc[:,['Open','Close']]

# Print the head of dollars
print(dollars.head())

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

# Print the head of pounds
print(pounds.head())