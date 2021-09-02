# SCORES

#1

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#2

df_dict = {'first_name': ['Jason','Molly','Tina','Jake','Amy'],
           'last_name': ['Miller','Jacobson','Ali','Milner','Cooze'],
           'age': [42,52,36,24,73],
           'female': [0,1,1,0,1],
           'preTestScore': [4,24,31,2,3],
           'postTestScore': [25,94,57,62,70]
           }

score_df = pd.DataFrame.from_dict(df_dict)

#3

score_df.plot.scatter(x='preTestScore',
                      y='postTestScore',
                      s='age',
                      title='pre x post')

#4

new_df = score_df.copy()
new_df['adj_size'] = score_df['postTestScore']*4

new_df.plot.scatter(x='preTestScore',
                    y='postTestScore',
                    s='adj_size',
                    c='female',
                    colormap='viridis',
                    title = 'pre x post',
                    xlabel = 'preTestScore')

#or doing it this way

plt.scatter(x=new_df.preTestScore,
            y=new_df.postTestScore,
            s=new_df.postTestScore*4,
            c=new_df.female
            )

plt.title("pre x post")
plt.xlabel('preTestScore')
plt.ylabel('preTestScore')