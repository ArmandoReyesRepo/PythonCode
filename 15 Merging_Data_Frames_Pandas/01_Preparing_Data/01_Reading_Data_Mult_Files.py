import pandas as pd
import os

os.chdir("C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data\\Summer Olympic medals")
os.getcwd()
os.listdir("C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data\\Summer Olympic medals")

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())