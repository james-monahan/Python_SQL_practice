# Find the cheapest and the most expensive variety in each region. 
# Output the region along with the corresponding most expensive and the cheapest variety.

import pandas as pd

df1 = winemag_p1[['region_1', 'price', 'variety']].rename(columns={'region_1':'region'})

df2 = winemag_p1[['region_2', 'price', 'variety']].rename(columns={'region_2':'region'})

winemag_p1 = pd.concat([df1, df2], ignore_index=True)

winemag_p1['min_price'] = winemag_p1.groupby('region')['price'].transform('min')
winemag_p1['max_price'] = winemag_p1.groupby('region')['price'].transform('max')

wine_low = winemag_p1[(winemag_p1['price'] == winemag_p1['min_price'])][['region', 'variety']]
                    
wine_high = winemag_p1[(winemag_p1['price'] == winemag_p1['max_price'])][['region', 'variety']]


wine_high.columns = ['region', 'variety_high']
wine_low.columns = ['region', 'variety_low']

wine_high.merge(wine_low, on='region').sort_values('region').drop_duplicates()
