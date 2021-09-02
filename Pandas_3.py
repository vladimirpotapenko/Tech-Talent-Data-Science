#1/2/3

import numpy as np
import pandas as pd

site = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'

drinks = pd.read_csv(site)

#4

beers_data = (drinks['beer_servings'].groupby(drinks['continent'])
              .agg("mean"))
max_beers = beers_data.idxmax()

#5

wine_data = drinks.groupby('continent').wine_servings.agg('describe').T

#6/7

alc_data = (drinks.groupby('continent').agg(['mean','median']).round(2))

#8

spirit_data = drinks.groupby('continent').agg(['min','mean','max']).T