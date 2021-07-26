# You're given a dataset of searches for properties on Airbnb. For simplicity, let's say 
# that each search result (i.e., each row) represents a unique host. Find the city with 
# the most amenities across all their host's properties. Output the name of the city.

# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details
df['amenities'] = df['amenities'].str.replace('{', '').str.replace('}', '')
df['num_amenities'] = df['amenities'].apply(lambda x: len(x.split(',')))
df = df[['city','num_amenities']]
df.groupby('city', as_index=False)['num_amenities'].sum().nlargest(1, 'num_amenities')['city']
