# Chipotle Data

#1 

import pandas as pd
import numpy as np

#2/3

chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t')
float_func = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.map(float_func)


#4
#### NOTE: I am considering each combination of add-ons and main dish as one product.
####       thus various combinations of steak burritos, for example, can be counted
####       as unique items 

items = chipo[chipo.quantity.isin([1])]
items = items.drop_duplicates(['item_name','choice_description'])
items_g10 = items[items.item_price > 10]
print(items_g10.shape[0])

#### If only concerned with what items led to a price greater than $10, we can
#### do the following:
    
print('\n')
print(items_g10.item_name.nunique())

#5

items_prc = (items.loc[:,['item_name','item_price']]
            .drop_duplicates(['item_name','item_price'],
            ignore_index=True)
            .sort_values(['item_price']))

print(items_prc.to_string())

#6

print('\n')
chipo.sort_values(by=['item_name'],inplace=True)
print(chipo.item_name)

#7

# I looked at the Zach Hall answer and like mine better since the question
# asks for the most expensive 'item' and the chips as an'item' are relatively
# cheap, so I do not consider it a valid answer

print('\n')
chipo.sort_values(['item_price'],ascending=False,inplace=True)
chipo_dropped = (chipo[chipo.quantity ==  1]
                 .drop_duplicates(['item_name','item_price']))
chipo_dropped = (chipo_dropped[chipo_dropped.item_price == chipo_dropped
                 .item_price.max()])
print(chipo_dropped[['item_name','quantity','item_price']])

#8

print('\n')
veg_salad = chipo[chipo.item_name == 'Veggie Salad Bowl']
print(f'The number of Veggie Salad Bowls is: {veg_salad.shape[0]}')

#9

print('\n')
canned_soda_2plus = chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]
print(f'''The number of Canned Soda orders of two or more is: {canned_soda_2plus.shape[0]}''')



