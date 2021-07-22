# Calculate the share of new and existing users. Output the month, share of new users, and share of existing users as a ratio.
# New users are defined as users who started using services in the current month. Existing users are users who started using 
# services in current month and used services in any previous month. 
# Assume that the dates are all from the year 2020.

# Import your libraries
import pandas as pd

# Start writing code
fact_events['month'] = fact_events.time_id.dt.month
fact_events['min_month'] = fact_events.groupby('user_id')['month'].transform('min')
fact_events['is_min_month'] = (fact_events['month']==fact_events['min_month']).astype('int')
fact_events = fact_events.drop_duplicates(subset=['user_id', 'month'])

table = fact_events.groupby(['month'])['is_min_month'].agg(['sum','count']).reset_index()
table['ratio_new'] = table['sum']/table['count']
table['ratio_existing'] = 1-table['ratio_new']
table[['month', 'ratio_new', 'ratio_existing']]
