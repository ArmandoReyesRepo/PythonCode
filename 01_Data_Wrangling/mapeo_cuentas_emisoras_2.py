# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:32:32 2019

@author: arman
"""

import pandas as pd


import os
os.getcwd()

os.chdir('C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python')

#s = pd.Series([1,3,4,5,8,11,16,17,18,19,20,21,24,25,26,27,28,29,32,33,34,36,38,39,40,41,42,43,44,46,47,48,49,60,62,66,67,69,79,80,81,83,84,85,86,87,88,89,93,94,95,96,97,111,112,113,114,115,116,117,121,122,127,130,131,135,136,137,139,144,148,155,156,159,160,162,163,164,169,170,178,180,181,182,184,185,187,188,189,190,192,193,196,197,198,202,204,205,206,208,209,230,232,235,239,241,247,258,259,295,298,299,302,317,321,327,331,333,334,335,340,341,342,343,345,361,369,374,378,380,392,405,406,418,422,423,433,434,435,436,437,439,441,443,445,447,448,449,450,451,458,477,478,480,481,485,489,490,491,492,493,494,495,507,515,522,523,588  ])



ref = pd.read_csv('00_168.csv')

ref

df = pd.read_csv('AA1CK - 3015.csv')

df

mapeo = ref.merge(df, on='concepto', how='outer')

#export_csv = df.to_csv (r'C:\Users\Ron\Desktop\export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

export_csv = mapeo.to_csv(r'C:\\Users\\arman\\Desktop\\Proyectos Manuel Sarmiento\\02 Algoritmos\\Python\\mapeo_dataframe.csv', index=None, header=True)

##############   Another example

## https://stackoverflow.com/questions/28174752/pandas-merge-dataframe-with-nan-or-unknown-for-missing-values

names = pd.DataFrame({'names':['bob','frank','bob','bob','bob', 'james','tim','ricardo','mike','mark','joan','joe'], 
                      'position':['dev','dev','dev','dev','dev','dev', 'sys','sys','sys','sup','sup','sup']})

info = pd.DataFrame({'names':['joe','mark','tim','frank','joe','bill'],
                     'classification':['thief','thief','good','thief','good','thief']})

what = pd.merge(names, info, how="outer")

what.fillna('unknown', inplace=True)



