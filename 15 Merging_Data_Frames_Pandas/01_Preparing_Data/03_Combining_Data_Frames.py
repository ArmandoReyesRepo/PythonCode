import pandas as pd
import os

os.chdir("C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data\\Summer Olympic medals")
os.getcwd()
os.listdir("C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data\\Summer Olympic medals")


# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())