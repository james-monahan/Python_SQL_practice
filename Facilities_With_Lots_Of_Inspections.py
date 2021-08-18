# Find the facility that got the highest number of inspections in 2017 compared to other years. 
# Compare the number of inspections per year and output only facilities that had the number of inspections greater in 2017 than in any other year.
# Each row in the dataset represents an inspection. Base your solution on the facility name and activity date fields.

# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections
df['year'] = df['activity_date'].dt.year
df = df.groupby(['facility_name', 'year'], as_index=False)['score'].count()
df = df.pivot(index='facility_name', columns='year', values='score')
df[df.idxmax(axis=1, skipna=True)==2017].reset_index()['facility_name']
