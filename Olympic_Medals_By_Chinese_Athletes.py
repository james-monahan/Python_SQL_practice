# Find the number of medals earned in each category by Chinese athletes from the 
# 2000 to 2016 summer Olympics. For each medal category, calculate the number of 
# medals for each olympic games along with the total number of medals across all years. 
# Sort records by total medals in descending order.

# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
df = df[(df['year'].between(2000,2016)) & (df['season']=='Summer') & (df['team']=='China')]

df = df.groupby(['year', 'medal'])['season'].size().reset_index()
df = df.pivot(index='medal', columns='year', values='season')
df['total'] = df.sum(axis=1)
df.reset_index()
