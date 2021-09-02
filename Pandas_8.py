#1

import pandas as pd
import numpy as np

#2

poke_dict = {
             'evolution':['Ivysaur','Charmeleon','Wartortle','Metapod'],
             'hp': [45,39,44,45],
             'name':['Bulbasaur','Charmander','Squirtle','Caterpie'],
             'pokedex':['yes','no','yes','no'],
             'type':['grass','fire','water','bug']
            }

#3

pokemon = pd.DataFrame.from_dict(poke_dict)

 #Place the order of the columns as name, type, hp, evolution, pokedex
 
#4

#pokemon = pokemon[['name','type','hp','evolution','pokedex']]

pokemon = pokemon.reindex(columns=['name','type','hp','evolution','pokedex'])

#5

pokemon['place'] = ['forest','air','sea','ground']

#6

print(pokemon.dtypes)