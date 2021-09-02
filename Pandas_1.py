#Chipotle Data

#1

import pandas as pd
import numpy as np

#2/3

chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep=
                    '\t') 

#4

print(chipo.head(10).to_string(), '\n')

#5/6

chipo_shape = chipo.shape
print(f'''The number of observations: {chipo_shape[0]}
The number of columns: {chipo_shape[1]}''', '\n')

#7

for name in chipo.columns:
    print(name)
    
#8

print('\n')
print(chipo.index)

#9/10

print('\n')
items = chipo.item_name
items_grouped = chipo.groupby(['item_name']).sum()
items_grouped.sort_values(['quantity'], ascending = False, inplace=True)
print(items_grouped.iloc[0])

#11

print('\n')
ch_descr = chipo.groupby(['choice_description']).sum()
ch_descr = ch_descr.sort_values(['quantity'], ascending=False)
print(ch_descr.iloc[0])

#12/17

print('\n')
print(f'The number of unique items ordered is: {len(items.unique())}')
print('\n')
print(f'''The number of items ordered is {chipo['quantity'].sum()}''')

#13

print('\n')
print(chipo.item_price.dtype)
float_func = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.map(float_func)
print('\n')
print(chipo.item_price.dtype)

#14

chipo['revenue'] = chipo.item_price * chipo.quantity
print('\n')
print(chipo.revenue.sum())

#15

print('\n')
print(len(chipo.order_id.unique()))

#16

print('\n')
print(f'Average Revenue per Order: {chipo.revenue.sum()/((chipo.order_id.nunique())):.2f}')



