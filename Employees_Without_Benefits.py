# Find the ratio between the number of employees without benefits to total employees. 
# Output the job title, number of employees without benefits, total employees relevant 
# to that job title, and the corresponding ratio. Order records based on the ratio in ascending order.


# Import your libraries
import pandas as pd

# Start writing code
df = sf_public_salaries[['jobtitle','benefits']]
df['benefits'].fillna(0, inplace=True)
df['benefits'] = df['benefits'].apply(lambda x: 0 if x != 0 else 1)
df = df.groupby('jobtitle').agg({'count', 'sum'}).reset_index()
df['ratio'] = df[('benefits', 'sum')]/df[('benefits', 'count')]
df.sort_values('ratio')
