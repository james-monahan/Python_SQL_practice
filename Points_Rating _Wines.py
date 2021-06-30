# Find the average points difference between each and previous years starting from 
# the year 2000. Output the year, average points, previous average points, and the 
# difference between them. If you're unable to calculate the average points 
# rating for a specific year, use an 87 average points rating for that year 
# (which is the average of all wines starting from 2000).


# Import your libraries
import pandas as pd

# Start writing code^
winemag_p2['year'] = winemag_p2['title'].str.extract('(2\d\d\d)')
df = winemag_p2[['points', 'year']].dropna()
df = df.groupby('year', as_index=False)['points'].mean().sort_values('year')
df['prior'] = df['points'].shift(1).fillna(87)
df['difference'] = df['points'] - df['prior']
df
