# Find the history of each sport by finding the first year, last year, and the total number of years that sport played in the Olympics.
# Output the sport name along with the first year, last year, and the total years.
# Order records by the first year in descending order

# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
df = df.groupby('sport')['year'].agg({'first':'min', 'last':'max', 'total':'nunique'}).reset_index()
df.sort_values('first', ascending=False)
