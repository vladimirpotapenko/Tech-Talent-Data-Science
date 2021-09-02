#1

import numpy as np
import pandas as pd

#2/3

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv'

baby_names = pd.read_csv(url)

#4

print(baby_names.head(10),'\n')

#5

baby_names.drop(columns=['Unnamed: 0','Id'],inplace=True)
print(baby_names.columns,'\n')

#6

print(baby_names.groupby('Gender').count().T.iloc[0],'\n','There are more FEMALES',
      '\n')

#7

names = baby_names.drop('Year',axis=1)
names = names.groupby('Name').sum()

#8

print(names.index.nunique(),'\n')

#9

print(names.idxmax(), '\n')

#10

names.sort_values(by='Count',inplace=True)

print(len([x for x in names['Count'] if (x == names.iloc[0,0])]),'\n')

#11

print(names.Count.median(),'\n')

#12

print(names.std(),'\n')

#13

print(names.describe(),'\n')
