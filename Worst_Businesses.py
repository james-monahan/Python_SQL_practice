# For every year, find the worst business in the dataset. 
# The worst business has the most violations during the year. 
# You should output the year, business name, and number of violations.

# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations
df['year'] = df['inspection_date'].dt.year
df = df.groupby(['business_name', 'year'])['violation_id'].count().reset_index()
df['rank'] = df.groupby('year')['violation_id'].rank(method='dense', ascending=False)
df[df['rank']==1].drop('rank', axis=1)
