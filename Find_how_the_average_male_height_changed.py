# Find how the average male height changed between each Olympics from 1896 to 2016.
# Output the Olympics year, average height, previous average height, and the corresponding average height difference.
# Order records by the year in ascending order.

# If avg height is not found, assume that the average height of an athlete is 172.73.


# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
df = df[df['year'].between(1896,2016)]
df = df[df['sex']=='M'].dropna(subset=['height'])
df = df.groupby('year')['height'].mean().reset_index()
df['prior'] = df['height'].shift(1).fillna(172.23)
df['difference'] = df['height'] - df['prior']
df
