# Wine

# 1

import numpy as np
import pandas as pd
from numpy import random as rd

# 2/3

wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data')

# 4
 
wine.drop(wine.columns[[0,3,6,8,10,12,13]], axis=1, inplace=True)

# 5

wine.columns = ['alcohol','malic_acid','alcalinity_of_ash','magnesium','flavanoids',
                'proanthocyanins','hue']

# 6

wine.alcohol.iloc[:3] = np.nan

# 7

wine.magnesium.iloc[[2,3]] = np.nan

# 8

wine.alcohol.fillna(value=10, inplace=True)

wine.magnesium.fillna(value=100, inplace=True)

# 9 

number_na = wine.isnull().sum().sum()

print(number_na)

# 10

rand_nums = rd.randint(0,11,size=10)

# 11

wine.alcohol[rand_nums] = np.nan

# 12

print(wine.isnull().sum())

# 13

wine = wine.dropna(axis=0)

# 14

print(wine.alcohol)

# 15

wine.reset_index(drop=True,inplace=True)