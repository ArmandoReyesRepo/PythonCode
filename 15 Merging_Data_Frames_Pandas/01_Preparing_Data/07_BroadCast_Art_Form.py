import pandas as pd
import os

path = "C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data"

os.chdir(path)
os.getcwd()
os.listdir(path)

weather = pd.read_csv('pittsburgh2013.csv', index_col='Date', parse_dates=True)

# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather.loc[:, ['Min TemperatureF','Mean TemperatureF','Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace('F','C')

# Print first 5 rows of temps_c
print(temps_c.head())