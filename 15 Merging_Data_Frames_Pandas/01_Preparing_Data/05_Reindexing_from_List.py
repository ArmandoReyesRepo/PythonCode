import pandas as pd
import os

os.chdir("C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data")
os.getcwd()
os.listdir("C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data")

## Read Weather data Quarterly
weather1 = pd.read_csv('weather1.csv',index_col='Month')

weather2 = pd.read_csv('monthly_max_temp.csv', index_col='Month')

##  Months year list / months is the index
year= weather2.index.tolist()

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)