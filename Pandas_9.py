# Investor: Flow of Funds

# 1

import numpy as np
import pandas as pd

# 2/3

investor_data = pd.read_csv("https://raw.githubusercontent.com/datasets/investor-flow-of-funds-us/master/data/weekly.csv")

# 4

print(investor_data.Date.head(), '\n')
print('Weekly', '\n')

# 5

investor_data.set_index('Date',inplace=True)

# 6

print(type(investor_data.index), '\n')

# 7

datetime = investor_data.index.to_numpy()

dti = pd.DatetimeIndex(datetime)
investor_data.set_index(dti,inplace=True)
print(type(investor_data.index))

# 8

monthly = investor_data.resample('M').sum()

# 9

monthly = monthly.replace(0,np.nan)

monthly.dropna(inplace=True)

# 10 

yearly = monthly.resample('Y').sum()
