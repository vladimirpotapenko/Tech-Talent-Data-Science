#HOUSING DATA

#1

import numpy as np
from numpy import random as rd
import pandas as pd

#2

s1 = pd.Series(rd.randint(1, 5, size=100),name='s1')
s2 = pd.Series(rd.randint(1, 4, size=100),name='s2')
s3 = pd.Series(rd.randint(10000, 40001, size=100), name='s3')

#3

series_group = [s1,s2,s3]

df = pd.concat(series_group, axis = 1)

#4

df.columns = [' bedrs', 'bathrs', 'price_sqr_meter']

#5

bigcolumn = pd.DataFrame(pd.concat(series_group,ignore_index=True))

bigcolumn.columns = ['Number']

#6

if bigcolumn.iloc[250].any():
    print('It goes past 99')
else:
    print("It doesn't go past 99")
    
#7 It already does! So I will mult by 10

bigcolumn.index = [x*10 for x in range(300)]