# Classify each Olympics as 'European' or  'NonEuropean' based on the city it was hosted. 
# Output all details along with the corresponding city classification.

# European cities are Athina, Berlin, London, Paris, and Lillehammer.

# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events
e_cities = ["Athina", "Berlin", "London", "Paris", "Lillehammer"]
df['classification'] = df['city'].apply\
    (lambda x: 'European' if x in e_cities else 'NonEuropean')
df
