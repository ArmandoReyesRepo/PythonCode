# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:40:21 2019

@author: arman
"""

import pandas as pd
df = pd.read_csv('sales.csv', index_col ='month')
df
df['salt']['Jan']
df.eggs['Mar']

df.loc['May','spam']

df.iloc[4,2]

df_new = df[['salt','eggs']]

df_new

df['eggs']

type(df['eggs'])

df['eggs'][1:4]

df['eggs'][4]


df.loc[:,'eggs':'salt']

df.loc['Jan':'Apr',:]

df.loc['Mar':'May', 'salt':'spam']

df.iloc[2:5,1:]


df.loc['Jan':'May',['eggs','spam']]


df.salt>60

df1 = df[df.salt>60]

df1



export_csv = df1.to_csv('test.csv',header=True) 



df[(df.salt>=50)&(df.eggs<200) ]


df2 = df.copy()

df2

df2['bacon']= [0,0,50,60,70,80]

df2.loc[:, df2.all()]


df2.loc[:,df2.any()]

df2.loc[:,df2.isnull().any()]

df.loc[:,df2.notnull().all()]

df


df.dropna(how='any')

df.eggs[df.salt>55]


df

df.floordiv(12)

import numpy as np

np.floor_divide(df,12)
       
       

def dozens(n):
    return n//12

df.apply(lambda n: n//12)

df['dozens_of_eggs'] = df.eggs.floordiv(12)

df.index

df.index = df.index.str.upper()

df.index = df.index.map(str.lower)

df['salty_eggs'] = df.salt + df.dozens_of_eggs
