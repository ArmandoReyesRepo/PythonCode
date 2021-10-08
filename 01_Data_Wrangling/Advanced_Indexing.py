# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:03:25 2019

@author: arman
"""

import pandas as pd
import os
os.getcwd()

os.chdir('C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python')



prices = [10.7,10.86,10.74,10.71,10.79]

shares = pd.Series(prices)

print(shares)


days = ['Mon','Tue','Wed','Thur','Fri']

shares = pd.Series(prices, index = days)

print(shares)

print(shares.index)

print( shares.index[2])

print( shares.index[:2])

print( shares.index[-2:])

print(shares.index.name)

shares.index.name = 'weekday'

print(shares)


shares.index[2] = "Wednesday"

shares.index[:4] = ['Monday','Tuesday','Wednesday','Thursday']

shares.index = ['Monday','Tuesday','Wednesday','Thursday','Friday']

print(shares)

elections = pd.read_csv('pennsylvania2012_turnout.csv')

elections.head()

elections.info()

elections.index = elections['county']

elections.head()

del elections['county']

elections.head(3)

print (elections.index)

print(type(elections.index))

print(elections.columns)



users = pd.read_csv('users.csv')

users
visitors_pivot = users.pivot(index='weekday', columns ='city', values = 'visitors')

print(visitors_pivot)






#  move to code for chapter 3

###  titanic = pd.read_csv('titanic.csv')

### by_class = titanic.groupby('pclass')

### by_class

### count_by_class = by_class['survived'].count()

### print(count_by_class)




