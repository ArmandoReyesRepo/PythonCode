import pandas as pd
import os

path = "C:\\Users\\arman\\OneDrive\\Desktop\\2020\DataCamp\\15 Merging_Data_Frames_Pandas\\01_Preparing_Data\\Baby names"

os.chdir(path)
os.getcwd()
os.listdir(path)

names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)