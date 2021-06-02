import pandas as pd
import os

path = "C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data\\Baby names"

os.chdir(path)
os.getcwd()
os.listdir(path)

names_1881 = pd.read_csv('names1881.csv', header=None)
names_1981 = pd.read_csv('names1981.csv', header=None)

# Renames col names names_1881
names_1881.columns=['name','gender','count','year']

# Renames col names names_1981
names_1981.columns=['name','gender','count','year']


# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981

# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names =  names_1881.append(names_1981,ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name']=='Morgan'])