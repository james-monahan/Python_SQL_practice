#Estimate the growth of Airbnb each year using the number of hosts registered as the growth metric. 
# The rate of growth is calculated by taking ((number of hosts registered in the current year - number 
# of hosts registered in the previous year) / the number of hosts registered in the previous year) * 100.
# Output the year, number of hosts in the current year, number of hosts in the previous year, and the 
# rate of growth. Round the rate of growth to the nearest percent and order the result in the ascending 
# order based on the year.
# Assume that the dataset consists only of unique hosts, meaning there are no duplicate hosts listed.


# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details
df['year'] = df.host_since.dt.year
df = df[['id', 'year']]
df = df.groupby('year', as_index=False)['id'].count()
df['prior_year'] = df.id.shift(1)
df['growth_rate'] = round(((df['id'] - df['prior_year'])/df['prior_year'])*100)
df
