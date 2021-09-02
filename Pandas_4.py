#1/2/3

import numpy as np
import pandas as pd

site=('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv')

df = pd.read_csv(site)

#4 

df_slice = df.loc[:,'school':'guardian']

#5/6/8

str_func = lambda x: x.capitalize()

df['Mjob'], df['Fjob'] = (df['Mjob'].apply(str_func),
                          df['Fjob'].apply(str_func))

#7

print(df.tail(3))

#9

def majority(_df_):
    if _df_ >= 17:
        return True
    else:
        return False
    
df['legal_drinker'] = df['age'].apply(majority)

#10

def mult_10(_df_):
    if type(_df_) == int:
        return _df_*10
    else:
        return _df_

df_10 = df.applymap(mult_10)

print(df_10.head(10))


    
    



