# Calculate the running total (i.e., cumulative sum) energy consumption of the 
# Facebook data centers in all 3 continents by the date. Output the date, 
# running total energy consumption, and running total percentage rounded 
# to the nearest whole number.

# Import your libraries
import pandas as pd

# Start writing code
df = pd.concat([fb_eu_energy, fb_na_energy, fb_asia_energy])
df = df.groupby('date', as_index=False)['consumption'].sum()
df['date'] = df['date'].dt.date
df['cumsum'] = df['consumption'].cumsum()
df['cumsum_pct'] = round((df['cumsum']/df['consumption'].sum())*100)
df[['date','cumsum','cumsum_pct']]
